# coding: utf-8
from sqlalchemy import Column, Date, DateTime, Index, Integer, Numeric, String, Time
from sqlalchemy.schema import FetchedValue
from flask_sqlalchemy import SQLAlchemy

from app import db     # db对象在app/__init__.py中创建

class PosTransmst(db.Model):
    __bind_key__ = 'oracle'
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

class PtmDish(db.Model):
    __bind_key__ = 'mysql'
    __tablename__ = 'ptm_dish'

    dish_id = db.Column(db.Integer, primary_key=True)
    order_count = db.Column(db.Integer)
    goods_no = db.Column(db.String(255, 'utf8_bin'))
    goods_spec = db.Column(db.String(255, 'utf8_bin'))
    goods_num = db.Column(db.Integer)
    goods_suitflag = db.Column(db.String(255, 'utf8_bin'))
    suit_no = db.Column(db.String(255, 'utf8_bin'))
    goods_final_price = db.Column(db.Numeric(10, 2))
    goods_org_price = db.Column(db.Numeric(10, 2))
    good_add_price = db.Column(db.Numeric(10, 2))
    goods_discount = db.Column(db.Numeric(10, 2))
    present_flag = db.Column(db.String(255, 'utf8_bin'))
    order_time = db.Column(db.DateTime)
    page_flag = db.Column(db.String(255, 'utf8_bin'))
    menber_no = db.Column(db.Integer)
    bonus_point = db.Column(db.String(255, 'utf8_bin'))
    goods_extend_param = db.Column(db.String(255, 'utf8_bin'))
    good_remark = db.Column(db.String(255, 'utf8_bin'))
    trade_id = db.Column(db.Integer)
    bill_no = db.Column(db.String(255, 'utf8_bin'), index=True)


class PtmPay(db.Model):
    __bind_key__ = 'mysql'
    __tablename__ = 'ptm_pay'

    pay_id = db.Column(db.Integer, primary_key=True)
    pay_count = db.Column(db.Integer)
    pay_mode = db.Column(db.String(255, 'utf8_bin'))
    pay_amount = db.Column(db.Numeric(10, 2))
    big_rate = db.Column(db.String(255, 'utf8_bin'))
    big_change = db.Column(db.Numeric(10, 2))
    amount_diff = db.Column(db.Numeric(10, 2))
    real_amount = db.Column(db.Numeric(10, 2))
    proof_no = db.Column(db.String(255, 'utf8_bin'))
    pay_extend_param = db.Column(db.String(255, 'utf8_bin'))
    pay_remark = db.Column(db.String(255, 'utf8_bin'))
    trade_id = db.Column(db.Integer)
    bill_no = db.Column(db.String(255, 'utf8_bin'), index=True)


class PtmTrade(db.Model):
    __bind_key__ = 'mysql'
    __tablename__ = 'ptm_trade'
    __table_args__ = (
        db.Index('g_b_f', 'global_storeid', 'bill_no', 'business_day'),
    )

    trade_id = db.Column(db.Integer, primary_key=True)
    trade_day = db.Column(db.Date)
    trade_time = db.Column(db.Time)
    ptm_storeid = db.Column(db.Integer)
    global_storeid = db.Column(db.String(255, 'utf8_bin'), nullable=False)
    pos_no = db.Column(db.String(255, 'utf8_bin'))
    bill_no = db.Column(db.String(255, 'utf8_bin'), unique=True)
    pay_no = db.Column(db.String(255, 'utf8_bin'))
    cashier = db.Column(db.String(255, 'utf8_bin'))
    operator_id = db.Column(db.String(255, 'utf8_bin'))
    menber_no = db.Column(db.String(255, 'utf8_bin'))
    cost_amount = db.Column(db.Numeric(10, 2))
    discount_amount = db.Column(db.Numeric(10, 2))
    invice_amount = db.Column(db.Numeric(10, 2))
    business_extend_param = db.Column(db.String(255, 'utf8_bin'), index=True)
    business_day = db.Column(db.Date)
    person_no = db.Column(db.Integer)
    bill_status = db.Column(db.String(255, 'utf8_bin'))
    bill_cancel_operator = db.Column(db.String(255, 'utf8_bin'))
    bill_cancel_date = db.Column(db.DateTime)
    cash_registe = db.Column(db.String(255, 'utf8_bin'))
    business_remark = db.Column(db.String(255, 'utf8_bin'))
    day_time = db.Column(db.DateTime)
    total_amount = db.Column(db.Numeric(10, 0))
    total_num = db.Column(db.Integer)