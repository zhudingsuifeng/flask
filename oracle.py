import os, datetime
from flask import Flask, render_template, session, url_for, request, jsonify
from flask_script import Manager
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import and_

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

@app.route('/', methods=['GET', 'POST'])
def index():
    # return request.data
    return render_template('index.html')

# 前端请求URL为：127.0.0.1:5000/query?deptcd=123&bizdt=123
# 给出门店的号码(DEPTCD)和时间(BIZDT)返回门店对应时间交易量
@app.route('/query')
def query():
    res = {"DEPTCD" : request.args.get('deptcd'),
           "BIZDT" : request.args.get('bizdt')}
    # PosTransmst 在pos_transmst.py文件中定义的PosTransmst类,对应数据库中的POSTRANSMST表
    # and_() 用于支持select 中的and 查询
    '''
    # filter形式查询
    sale = PosTransmst.query.filter(
        and_(PosTransmst.deptcd == res["DEPTCD"], 
        PosTransmst.bizdt == datetime.datetime.strptime(res["BIZDT"], "%Y-%m-%d %H:%M:%S"))
        ).count()
    '''

    # filter_by形式查询
    sale = PosTransmst.query.filter_by(
        deptcd = res["DEPTCD"], 
        bizdt = datetime.datetime.strptime(res["BIZDT"], "%Y-%m-%d %H:%M:%S")
        ).count()
    # datetime.datetime.strptime(res["BIZDT"], "%Y-%m-%d %H:%M:%S")  
    # # 将字符串转换为数据库可以识别的datetime格式
    res["SALE"] = sale

    return jsonify(res)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

if __name__ == "__main__":
    manager.run()