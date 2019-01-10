# coding: utf-8
from sqlalchemy import Column, DateTime, Index, Integer, Numeric, String
from sqlalchemy.schema import FetchedValue
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


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
