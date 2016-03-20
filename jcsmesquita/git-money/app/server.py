#!/usr/bin/env python
import io
import os
import re
import sys
import json
import hashlib
import subprocess
import requests
import ipaddress
import hmac
from app.github import github
from hashlib import sha1
from app.multisig_wallet import multisig_wallet
from app.twitter import twitter
from PIL import Image, ImageFont, ImageDraw
from flask import Flask, request, abort, send_file
from commonregex import CommonRegex

"""
Conditionally import ProxyFix from werkzeug if the USE_PROXYFIX environment
variable is set to true.  If you intend to import this as a module in your own
code, use os.environ to set the environment variable before importing this as a
module.

.. code:: python

    os.environ['USE_PROXYFIX'] = 'true'
    import flask-github-webhook-handler.index as handler

"""
config_path = os.path.dirname(os.path.realpath(__file__)) + '/../config/config.json'
repository = json.loads(io.open(config_path, 'r').read())
repository_path = repository['path']

DEFAULT_WALLET_PATH = os.path.join(os.path.expanduser('~'),
                                   ".two1",
                                   "wallet",
                                   "multisig_wallet.json")

if os.environ.get('USE_PROXYFIX', None) == 'true':
    from werkzeug.contrib.fixers import ProxyFix

app = Flask(__name__)
app.debug = os.environ.get('DEBUG') == 'true'

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return 'OK'
    elif request.method == 'POST':
    # Store the IP address of the requester
        request_ip = ipaddress.ip_address(u'{0}'.format(request.remote_addr))

        # If GHE_ADDRESS is specified, use it as the hook_blocks.
        if os.environ.get('GHE_ADDRESS', None):
            hook_blocks = [os.environ.get('GHE_ADDRESS')]
        # Otherwise get the hook address blocks from the API.
        else:
            hook_blocks = requests.get('https://api.github.com/meta').json()['hooks']

        if request.headers.get('X-GitHub-Event') == "ping":
            return json.dumps({'msg': 'Hi!'})

        if request.headers.get('X-GitHub-Event') == 'pull_request':
            if (request.json['pull_request']['user']['site_admin'] == 'false'):
                return json.dumps({'message': 'Pull request not submitted by site admin'})
            merge_state = request.json['pull_request']['state']
            merge_body = request.json['pull_request']['body']
            if (merge_state == 'closed'):
                print('Merge state closed')
                print('Merge Body: ' + merge_body)
                parsed_bounty_issue = re.findall(r"#(\w+)", merge_body)[0]
                addresses = CommonRegex(merge_body).btc_addresses[0]
                bounty_address = github.get_address_from_issue(parsed_bounty_issue)
                amount = multisig_wallet.get_address_balance(bounty_address)
                try:
                # use username to look up wallet Id
                    with open(DEFAULT_WALLET_PATH, 'r') as wallet:
                        data = json.loads(wallet.read())
                    for user in data:
                        try:
                            if (user['issue_number'] == int(parsed_bounty_issue)):
                                print('Wallet found')
                                wallet_name = user['wallet_name']
                                walletId = user[wallet_name]['walletId']
                        except:
                            print('Loading wallet..')        

                except:
                    print('Wallet not found, creating new user...')

                # Set up sending of the bounty
                
                issue_title = wallet_name
                repository_path_encode = repository_path.encode('utf-8')
                issue_title_encode = issue_title.encode('utf-8')
                passphrase = hashlib.sha256(repository_path_encode + issue_title_encode).hexdigest()
                multisig_wallet.send_bitcoin_simple(walletId, str(addresses), amount, passphrase)

                # Set up sending of the tweet
                
                usd_per_btc = requests.get(
                    'https://bitpay.com/api/rates/usd').json()['rate']
                bounty_in_btc = round((int(bounty_in_satoshi) / 10**8), 3)
                bounty_in_usd = round(bounty_in_btc * usd_per_btc, 2)
                url = 'https://github.com/21hackers/git-money/issues/'+ parsed_bounty_issue
                twitter.send('Bounty Granted (' + amount + ' bits ~ $' + bounty_in_usd + '): ' + issue_title + ' ' + url)

                return json.dumps({'message': 'Pull request received'})
            return json.dumps({'message': 'Pull request payout failed'})

        if request.headers.get('X-GitHub-Event') == 'issue_comment':            
            comment_data = {
                'url': request.json['comment']['issue_url'],
                'payout_address': request.json['issue']['labels'][0]['name'],
                'payout_amount': request.json['issue']['labels'][1]['name'],
                'body': request.json['comment']['body']
            }
            print(comment_data)
            return json.dumps({'message': 'Issue comment received'})


@app.route('/badge/<path:path>')
def bounty_badge(path):

# Get values to draw on image
    usd_per_btc = requests.get(
        'https://bitpay.com/api/rates/usd').json()['rate']
    bounty_in_satoshi = requests.get(
        'https://blockchain.info/q/addressbalance/{0}'.format(path)).text
    bounty_in_btc = round((int(bounty_in_satoshi) / 10**8), 3)
    bounty_in_usd = round(bounty_in_btc * usd_per_btc, 2)

    # load up background image and fonts
    badge = Image.open('app/assets/bounty-bg.jpg')
    font_bounty = ImageFont.truetype('app/assets/western.ttf', 60)
    font_btc = ImageFont.truetype('app/assets/western.ttf', 50)
    font_usd = ImageFont.truetype('app/assets/western.ttf', 25)

    # draw on background
    draw = ImageDraw.Draw(badge)
    draw.text((10, 30), 'BOUNTY', fill='black', font=font_bounty)
    draw.text((20, 200), '{0} BTC'.format(
        bounty_in_btc), fill='black', font=font_btc)
    draw.text((55, 260), '({0} USD)'.format(bounty_in_usd),
            fill='black', font=font_usd)

    def serve_pil_image(pil_img):
        img_io = io.BytesIO()
        pil_img.save(img_io, 'JPEG', quality=70)
        img_io.seek(0)
        return send_file(img_io, mimetype='image/jpeg')

    return serve_pil_image(badge)



class server(object):
    def run():
        if os.environ.get('USE_PROXYFIX', None) == 'true':
            app.wsgi_app = ProxyFix(app.wsgi_app)
        app.run(host='0.0.0.0', port='21336')
