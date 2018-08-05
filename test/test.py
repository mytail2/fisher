#!/usr/bin/env python

from flask import Flask, current_app


app = Flask(__name__)

with app.app_context():
    a = current_app
    b = current_app.config['DEBUG']

print('hah')