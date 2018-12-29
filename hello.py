#coding = utf-8

from flask import Flask, render_template
from flask_script import Manager
from flask_bootstrap import Bootstrap
from flask_moment import Moment

from datetime import datetime

app = Flask(__name__)   # 创建Flask类的对象，即程序实例
# app.run(debug=True)

Bootstrap(app)
Moment(app)
manager = Manager(app)  # 添加命令行解析器

@app.route('/')  # app.route修饰器，把修饰的函数注册为路由，访问对应URL时的相应函数
def index():
    return render_template('index.html',current_time=datetime.utcnow())
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

