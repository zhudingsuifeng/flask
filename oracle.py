import os
from flask import Flask, render_template, session, redirect, url_for, flash
from flask_script import Manager
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

# 导入自定义orm文件
from models.pos_transmst import db, PosTransmst

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)   # 创建Flask类的对象，即程序实例
app.config['SECRET_KEY'] = 'flaskOracle'   # app.config字典用来存储框架，扩展和程序本身的配置变量。
# SECRET_KEY 配置变量通用密钥。
app.config['SQLALCHEMY_DATABASE_URI'] = 'oracle+cx_oracle://HEX_SPCC:HEX_SPCC@frps.hexcloud.cn:31733/HEXDB'
# oracle数据库连接字符串
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
Bootstrap(app)     # 模板
manager = Manager(app)  # 添加命令行解析器

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<DEPTCD>/<BIZDT>')
def query(DEPTCD, BIZDT=None):

    # data = PosTransmst.query.filter_by(deptcd = DEPTCD).count()


    return 'BIZDT : 2017-12-31 00:00:00, DEPTCD : 170407, SALE :', 100 #data

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

if __name__ == "__main__":
    manager.run()