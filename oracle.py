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


from sqlalchemy import create_engine

# 数据库连接字符串，根据连接的数据库不同，选择不同的连接字符串
DB_CONNECT_STRING = 'oracle+cx_oracle://HEX_SPCC:HEX_SPCC@frps.hexcloud.cn:31733/HEXDB'

# 创建数据库引擎，echo=True，会打印所有的sql语句
# engine = create_engine(DB_CONNECT_STRING, echo=True)
engine = create_engine(DB_CONNECT_STRING)

# 创建一个connection
with engine.connect() as con:
    # 执行sql语句，不需要commit
    rs = con.execute("select count(*) from POS_TRANSMST where BIZDT = to_date('2017-12-31 00:00:00' , 'yyyy-mm-dd hh24:mi:ss') and DEPTCD = '170407'")
    data = rs.fetchone()[0]
    print('BIZDT : 2017-12-31 00:00:00, DEPTCD : 170407, SALE :', data)

