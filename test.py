import os, datetime
from flask import Flask, session, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)   # 创建Flask类的对象，即程序实例
# app.config['SECRET_KEY'] = 'flaskOracle'   # app.config字典用来存储框架，扩展和程序本身的配置变量。
app.config['SQLALCHEMY_DATABASE_URI'] = 'oracle+cx_oracle://HEX_SPCC:HEX_SPCC@frps.hexcloud.cn:31733/HEXDB'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.config['SQLALCHEMY_ECHO'] = True

from sqlalchemy import Column, DateTime, Index, Integer, Numeric, String, func
from sqlalchemy.schema import FetchedValue
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)   # 创建SQLAlchemy对象

class PosTransmst(db.Model):
    __tablename__ = 'pos_transmst'
    __table_args__ = (
        db.Index('idx_pos_transmst_bizdt_dept', 'bizdt', 'deptcd'),
    )

    transno = db.Column(db.Numeric(20, 0, asdecimal=False), primary_key=True)
    bizdt = db.Column(db.DateTime, index=True)
    ctrno = db.Column(db.Numeric(20, 0, asdecimal=False), index=True)
    tillcd = db.Column(db.String(20))
    saleid = db.Column(db.Integer)
    transtp = db.Column(db.String(1))
    transrsn = db.Column(db.String(10))
    saletp = db.Column(db.String(10))
    deptcd = db.Column(db.String(10))
    opercd = db.Column(db.String(10))
    membercd = db.Column(db.String(20))
    grossamt = db.Column(db.Numeric(19, 4), server_default=db.FetchedValue())
    netamt = db.Column(db.Numeric(19, 4))
    discamt = db.Column(db.Numeric(19, 4))
    curqty = db.Column(db.Numeric(19, 4), server_default=db.FetchedValue())
    ctmcount = db.Column(db.Integer, server_default=db.FetchedValue())
    ctmtp = db.Column(db.String(10))
    tablecd = db.Column(db.String(20))
    tradedt = db.Column(db.DateTime)
    procdt = db.Column(db.DateTime)
    salesmethod = db.Column(db.Integer)
    orddt = db.Column(db.DateTime)
    orderby = db.Column(db.String(20))
    point = db.Column(db.Numeric(19, 4))
    tableregion = db.Column(db.String(50))
    upddt = db.Column(db.DateTime)
    memberid = db.Column(db.Numeric(20, 0, asdecimal=False))
    emccd = db.Column(db.String(10))
    cvno = db.Column(db.String(30))
    emcd = db.Column(db.String(20))


info = {"DEPTCD" : '131101',
        "BIZDT" : '2017-12-31 00:00:00'}
        
sale = db.session.query(func.count(PosTransmst.saletp)).filter_by(
            deptcd = info["DEPTCD"],
            bizdt = datetime.datetime.strptime(info["BIZDT"], "%Y-%m-%d %H:%M:%S"),
            saletp = 'SALE'
        ).all()

info["SALE"] = sale

print(jsonify(info))

result = [i for i in range(20)]

def z():
    for dept in result:
        yield {"DEPTCD": dept, "BIZDT": "2017-12-31 00:00:00", "SALE": 10} 

print(list(z()))
# print("hello")