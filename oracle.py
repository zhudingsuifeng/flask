from flask import Flask
from flask_sqlalchemy import SQLAlchemy, BaseQuery
# BaseQuery 查询用

# 导入自己些的数据库连接配置文件 config.py
'''import config

app = Flask(__name__)

app.config.from_object(config)    # SQLAlchemy自动从配置文件读取URI字符串
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False'''


# db = SQLAlchemy(app)


    # dept = db.Column('DEPTCD', db.String(20))     # 门店号
    # date = db.Column('BIZDT', db.Date)            # 日期
    # volume = db.Column('SALETP', db.String(20))   # 交易量


import cx_Oracle as oracle 

db = oracle.connect('HEX_SPCC/HEX_SPCC@frps.hexcloud.cn:31733/HEXDB')

cursor = db.cursor()

cursor.execute("select count(*) from POS_TRANSMST where BIZDT = to_date('2017-12-31 00:00:00' , 'yyyy-mm-dd hh24:mi:ss') and DEPTCD = '170407'")

data = cursor.fetchone()

print('BIZDT : 2017-12-31 00:00:00, DEPTCD : 170407, SALE :', data[0])

cursor.close()
db.close()
