# coding = utf-8

import os
import os, datetime, json, csv
from flask import render_template, session, url_for, request, jsonify, Response
from flask_bootstrap import Bootstrap
from flask_script import Manager

from app import create_app
from app.models import PosTransmst
from config import config

app = create_app(os.getenv('development') or 'development')
manager = Manager(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    # return request.data
    return render_template('index.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

if __name__ == "__main__":
    manager.run()