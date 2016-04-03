#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import logging
import psutil
import subprocess
import os
import sys
import yaml

from flask import Flask
from flask import request

from two1.lib.wallet.two1_wallet import Wallet
from two1.lib.bitserv.flask import Payment

from nyt_movie_reviews21 import reviews21

app = Flask(__name__)

# setup wallet
wallet = Wallet()
payment = Payment(app, wallet)


# hide logging
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)


@app.route('/manifest')
def manifest():
    """Provide the app manifest to the 21 crawler.
    """
    with open('./manifest.yaml', 'r') as f:
        manifest = yaml.load(f)
    return json.dumps(manifest)


@app.route('/')
@payment.required(2500)
def reviews():
    try:
        query = request.args['keyword']
    except KeyError:
        return 'HTTP Status 400: URI keyword parameter is missing from your request.', 400

    try:
        data = reviews21(query)
        response = json.dumps(data, indent=2, sort_keys=True)
        return response
    except ValueError as e:
        return 'HTTP Status 400: {}'.format(e.args[0]), 400


if __name__ == '__main__':
    if 'daemon' not in sys.argv:
        pid_file = './nyt-movie-reviews21.pid'
        if os.path.isfile(pid_file):
            pid = int(open(pid_file).read())
            os.remove(pid_file)
            try:
                p = psutil.Process(pid)
                p.terminate()
            except:
                pass
        try:
            p = subprocess.Popen(['python3', 'nyt-movie-reviews21-server.py', 'daemon'])
            open(pid_file, 'w').write(str(p.pid))
        except subprocess.CalledProcessError:
            raise ValueError("error starting nyt-movie-reviews21-server.py daemon")
    else:
        print ("Server running...")
        app.run(host='0.0.0.0', port=6006)
