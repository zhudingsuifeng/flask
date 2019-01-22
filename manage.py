#coding = utf-8

import os
from flask import Flask
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
manager = Manager(app)

if __name__ == "__main__":
    manager.run()