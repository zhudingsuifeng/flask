# coding = utf-8

__author__ = 'fly'

from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

from config import config

bootstrap = Bootstrap()
db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    # 使用扩展对象初始化app对象
    bootstrap.init_app(app)
    db.init_app(app)
    
    # 注册blueprint
    from .sales import sales as sales_blueprint
    app.register_blueprint(sales_blueprint, url_prefix = '/sales')   # url_prefix 前缀
    # 对应sales文件夹__init__.py中声明的blueprint 对象sales
 
    return app