import os, datetime, json, csv
from flask import Flask, render_template, session, url_for, request, jsonify, Response
# jsonify 用来生成json格式数据， Response 用于自定义响应形式, request 用于获取url参数数据
from flask_script import Manager
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

from flask import make_response   # 自定义响应
import mimetypes   # 用于设置响应headers['Content-Type']
import tablib      # 用于导出各种格式的文件
from sqlalchemy import func   # 用于func.count()统计行数

# 导入自定义orm文件
from models.pos_transmst import db, PosTransmst

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)   # 创建Flask类的对象，即程序实例
app.config['SECRET_KEY'] = 'flaskOracle'   # app.config字典用来存储框架，扩展和程序本身的配置变量。
# SECRET_KEY 配置变量通用密钥。
app.config['SQLALCHEMY_DATABASE_URI'] = 'oracle+cx_oracle://HEX_SPCC:HEX_SPCC@frps.hexcloud.cn:31733/HEXDB'
# oracle数据库连接字符串
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.config['SQLALCHEMY_ECHO'] = True

db.init_app(app)   # 将db对象
Bootstrap(app)     # 模板
manager = Manager(app)  # 添加命令行解析器

@app.route('/', methods=['GET', 'POST'])
def index():
    # return request.data
    return render_template('index.html')

# 前端请求URL为：127.0.0.1:5000/search?deptcd=123&bizdt=123
# 给出门店的号码(DEPTCD)和时间(BIZDT)返回门店对应时间交易量
@app.route('/search')
def search():
    info = {"DEPTCD" : request.args.get('deptcd'),
        "BIZDT" : request.args.get('bizdt')}
    sale = PosTransmst.query.filter_by(
        deptcd = info["DEPTCD"],
        bizdt = datetime.datetime.strptime(info["BIZDT"], "%Y-%m-%d %H:%M:%S"),
        saletp = 'SALE'
        ).count()

        # 精准查询 filter_by()
    res = {"DEPTCD": info["DEPTCD"], "BIZDT": info["BIZDT"], "SALE": sale}
    return jsonify(res)  # 向前端返回json格式数据

# 前端请求URL：127.0.0.1:5000/query?bizdt=2017-12-31 00:00:00&flag=json
# 127.0.0.1:5000/query?bizdt=2017-12-31 00:00:00&flag=csv
# 给出时间(BIZDT)返回所有门店对应时间交易量列表
@app.route('/query')
def query():
    # request.args.get() 以获取字典值的形式获取URL参数
    info = {"BIZDT" : request.args.get('bizdt'),
            "FLAG" : request.args.get('flag')}
    # PosTransmst 在pos_transmst.py文件中定义的PosTransmst类,对应数据库中的POSTRANSMST表
    # 按门店号分组group by，并统计每个门店指定日期的交易量
    result = db.session.query(PosTransmst.deptcd, func.count()).filter_by(
        bizdt = datetime.datetime.strptime(info["BIZDT"], "%Y-%m-%d %H:%M:%S"),
        saletp = 'SALE'
        ).group_by(PosTransmst.deptcd).all()
    # datetime.datetime.strptime(res["BIZDT"], "%Y-%m-%d %H:%M:%S")  
    # 将字符串转换为数据库可以识别的datetime格式

    '''
    result = db.session.query(PosTransmst.deptcd, func.count()).filter_by(   
        bizdt = datetime.datetime.strptime(info["BIZDT"], "%Y-%m-%d %H:%M:%S"),
        saletp = 'SALE'
        ).group_by(PosTransmst.deptcd).limit(10).all()
    # session.query() 要查询的列  select 
    # func.count()   统计结果行数 count
    # filter_by()    过滤条件   where
    # group_by()     分组      group by
    # limit()      限制显示结果行数  limit
    # all()        最终结果
    '''

    # 将查询结果包装成想要的格式， 使用yield 应该能提高些效率
    # 将[(1,2),(1,2)...] 格式转换为 [[0,1,2],[0,1,2]...]
    def convert():
        for dept, sale in result:
            yield [dept, info["BIZDT"], sale]
            # yield {"DEPTCD": dept, "BIZDT": info["BIZDT"], "SALE": sale} 

    # 将字符格式的数据转换成json格式
    def str2json():
        for dept, sale in result:
            yield {"DEPTCD": dept, "BIZDT": info["BIZDT"], "SALE": sale}

    res = convert()   # res 数据list,tablib 导入的格式
    data = tablib.Dataset(*res, headers = ["DEPTCD", "BIZDT", "SALE"])
    # *res 数据， headers 表头

    if info['FLAG'] == 'json':
        return jsonify(list(str2json()))

    elif info['FLAG'] == 'csv_file':
        resp = make_response(data.csv)
        filename = ''.join([info["BIZDT"], '.csv'])
        mime_type = mimetypes.guess_type(filename)[0]
        resp.headers['Content-Type'] = mime_type
        resp.headers['Content-Disposition'] = 'attachment; filename={}'.format(filename)
        return resp
        
    elif info['FLAG'] == 'json_file':
        resp = make_response(data.json)                    # 创建相应对象
        filename = ''.join([info["BIZDT"], '.json'])       # 响应下载的文件名
        mime_type = mimetypes.guess_type(filename)[0]      # 响应类型
        resp.headers['Content-Type'] = mime_type           # 设置响应头
        resp.headers['Content-Disposition'] = 'attachment; filename={}'.format(filename)
        return resp

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

if __name__ == "__main__":
    manager.run()