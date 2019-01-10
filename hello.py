#coding = utf-8

import os
from flask import Flask, render_template, session, redirect, url_for, flash
from flask_script import Manager
from flask_bootstrap import Bootstrap
from flask_moment import Moment

from flask_wtf import Form
from wtforms import StringField,SubmitField
from wtforms.validators import Required

from flask_sqlalchemy import SQLAlchemy

from datetime import datetime

class NameForm(Form):
    name = StringField('What is your name?', validators=[Required()])
    submit = SubmitField('Submit')


basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)   # 创建Flask类的对象，即程序实例
app.config['SECRET_KEY'] = 'flaskMysql'   # app.config字典用来存储框架，扩展和程序本身的配置变量。
# SECRET_KEY 配置变量通用密钥。
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://fly:huangzongwen_123@localhost:3306/web'
# 连接mysql数据库的配置
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)   # 创建SQLAlchemy对象

with app.app_context():
    db.init_app(app)
    db.create_all()

# app.run(debug=True)

Bootstrap(app)     # 模板
Moment(app)        # 时间
manager = Manager(app)  # 添加命令行解析器

class Role(db.Model):
    __tablename__ = 'roles'   # 指定对应的数据表
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)

    def __repr__(self):
        return '<Role %r>' % self.name

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column(db.String(64),unique=True, index=True)

    def __init__(self, id=None, name='fly'):
        self.id = id
        self.name = name
        
    def __repr__(self):
        return '<User %r>' % self.username

@app.route('/',methods=['GET','POST'])  # app.route修饰器，把修饰的函数注册为路由，访问对应URL时的相应函数
def index():
    form = NameForm()
    if form.validate_on_submit():
        old_name = session.get('name')
        if old_name is not None and old_name != form.name.data:
            flash('Looks like you have changed your name!')
        session['name'] = form.name.data   # 
        return redirect(url_for('index'))
    return render_template('index.html', form = form, name = session.get('name'), current_time=datetime.utcnow())
    # render_template函数第一个参数是模板的文件名。随后的参数是键值对，表示模板中变量对应的真实值。

@app.route('/user/<name>')
def user(name):
    return render_template('user.html',name=name)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

if __name__ == "__main__":
    
    manager.run()