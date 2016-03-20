#!/usr/bin/env python3
import os
import json
import random
import requests

from flask import Flask
from flask import request
from flask import send_from_directory
from flask import jsonify

# import from the 21 Developer Library
from two1.lib.wallet import Wallet
from two1.lib.bitserv.flask import Payment

app = Flask(__name__)
wallet = Wallet()
payment = Payment(app, wallet)

# machine-payable endpoint that returns selected file if payment made
@app.route('/gitmoney')
@payment.required(1000)
def gitmoney():
    gitmoney = []
    r = requests.get("https://api.github.com/repos/21hackers/git-money/issues?state=open&labels=git%20money")
    for x in r.json():
        title = x['title']
        body = x['body']
        html_url = x['html_url']
        payload = {'title': title, 'description': body, 'url': html_url}
        
        gitmoney.append(payload)
        return jsonify(results=gitmoney)
    
if __name__ == '__main__':
    app.run(host='0.0.0.0')
                                                            
