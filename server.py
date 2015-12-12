import os
import json

from flask import Flask
from flask import request 
from flask.ext.responses import json_response

from two1.lib.wallet import Wallet
from two1.lib.bitserv.flask import Payment

from cfgtodict import ConfigToDictionary
from settings import *

app = Flask(__name__)
wallet = Wallet()
payment = Payment(app, wallet)

@app.route('/')
@app.route('/info')
@app.route('/help')
def home():
    '''Document the API so that other services could consume automatically.'''
    about = ConfigToDictionary('info.cfg').dict()
    return json_response(about)

@app.route('/example')
@payment.required(PRICE)
def example_function():
    # do stuff
    return json.dumps({'first_return':'your data goes here'})

if __name__ == '__main__':
    if DEBUG:
        app.debug = True
    app.run(host='0.0.0.0', port=PORT)
