# coding: utf-8
from sqlalchemy import Column, DateTime, Float, Index, Integer, Numeric, String, Table, Text, Unicode
from sqlalchemy.schema import FetchedValue
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


t_a_20161121 = db.Table(
    'a_20161121',
    db.Column('ctrno', db.Numeric(20, 0, asdecimal=False)),
    db.Column('plucd', db.String(20)),
    db.Column('pluprc', db.Numeric(19, 4)),
    db.Column('discamt', db.Numeric(19, 4)),
    db.Column('netamt', db.Numeric(19, 4)),
    db.Column('curqty', db.Numeric(19, 4)),
    db.Column('disccd', db.Numeric(asdecimal=False))
)


t_aa1 = db.Table(
    'aa1',
    db.Column('inttransnum', db.Numeric(20, 0, asdecimal=False))
)


t_aa2 = db.Table(
    'aa2',
    db.Column('inttransnum', db.Numeric(20, 0, asdecimal=False))
)


t_aa3 = db.Table(
    'aa3',
    db.Column('inttransnum', db.Numeric(20, 0, asdecimal=False))
)


t_aa4 = db.Table(
    'aa4',
    db.Column('inttransnum', db.Numeric(20, 0, asdecimal=False))
)


t_aa_20161121 = db.Table(
    'aa_20161121',
    db.Column('transno', db.Numeric(20, 0, asdecimal=False), nullable=False),
    db.Column('bizdt', db.DateTime),
    db.Column('ctrno', db.Numeric(20, 0, asdecimal=False)),
    db.Column('disctp', db.String(1)),
    db.Column('disccd', db.String(10)),
    db.Column('discamt', db.Numeric(19, 4))
)


t_aaa5 = db.Table(
    'aaa5',
    db.Column('inttransnum', db.Numeric(20, 0, asdecimal=False))
)


t_aaa_20161121 = db.Table(
    'aaa_20161121',
    db.Column('ctrno', db.Numeric(20, 0, asdecimal=False)),
    db.Column('plucatid', db.Integer),
    db.Column('nm_l_zh', db.Unicode(100), nullable=False),
    db.Column('nm_l_zh1', db.Unicode(50), nullable=False),
    db.Column('plucd', db.String(20)),
    db.Column('pluprc', db.Numeric(19, 4)),
    db.Column('disccd', db.String(10)),
    db.Column('discamt', db.Numeric(19, 4)),
    db.Column('netamt', db.Numeric(19, 4))
)


class AccAccount(db.Model):
    __tablename__ = 'acc_account'

    id = db.Column(db.Integer, primary_key=True)
    tp = db.Column(db.String(10))
    cd = db.Column(db.String(30), index=True)
    secondcd = db.Column(db.String(30))
    nm_l_zh = db.Column(db.Unicode(50))
    nm_l_en = db.Column(db.Unicode(50))
    nm_l_ja = db.Column(db.Unicode(50))
    pid = db.Column(db.Integer)
    lvl = db.Column(db.Integer)
    pth = db.Column(db.String(100))
    leafflg = db.Column(db.String(1))
    auxtp = db.Column(db.String(10))
    cashflw = db.Column(db.String(50))
    updby = db.Column(db.String(20))
    upddt = db.Column(db.DateTime)
    sta = db.Column(db.String(3), nullable=False)
    execflg = db.Column(db.String(1))
    nxtsta = db.Column(db.String(3))


t_acc_addtax = db.Table(
    'acc_addtax',
    db.Column('ptid', db.Integer),
    db.Column('deptid', db.Integer),
    db.Column('amt_type', db.String(20)),
    db.Column('tax_amt', db.Numeric(20, 6)),
    db.Column('account_d', db.String(10)),
    db.Column('account_nd', db.String(50)),
    db.Column('account_c', db.String(10)),
    db.Column('account_nc', db.String(50)),
    db.Column('updby', db.String(20), server_default=db.FetchedValue()),
    db.Column('upddt', db.DateTime, server_default=db.FetchedValue()),
    db.Column('subtp', db.String(50)),
    db.Index('idx_acc_addtax', 'ptid', 'deptid')
)


t_acc_addtax_adj = db.Table(
    'acc_addtax_adj',
    db.Column('ptid', db.Integer, index=True),
    db.Column('pluid', db.Integer),
    db.Column('deptcd', db.String(20)),
    db.Column('catcd', db.String(20)),
    db.Column('adjrsn', db.String(20)),
    db.Column('grpcd', db.String(20)),
    db.Column('salprc', db.Numeric(12, 4)),
    db.Column('csprc', db.Numeric(16, 6)),
    db.Column('qty', db.Numeric(20, 6)),
    db.Column('taxtp', db.String(20)),
    db.Column('amt', db.Numeric(20, 6)),
    db.Column('taxamt', db.Numeric(20, 6)),
    db.Column('upddt', db.DateTime),
    db.Column('txrt', db.Numeric(12, 4)),
    db.Column('acccd', db.String(20))
)


t_acc_addtax_adj_gl = db.Table(
    'acc_addtax_adj_gl',
    db.Column('ptid', db.Integer, index=True),
    db.Column('pluid', db.Integer),
    db.Column('deptcd', db.String(20)),
    db.Column('catcd', db.String(20)),
    db.Column('adjrsn', db.String(20)),
    db.Column('grpcd', db.String(20)),
    db.Column('salprc', db.Numeric(12, 4)),
    db.Column('csprc', db.Numeric(16, 6)),
    db.Column('qty', db.Numeric(20, 6)),
    db.Column('taxtp', db.String(20)),
    db.Column('amt', db.Numeric(20, 6)),
    db.Column('taxamt', db.Numeric(20, 6)),
    db.Column('upddt', db.DateTime),
    db.Column('txrt', db.Numeric(12, 4)),
    db.Column('acccd', db.String(20))
)


t_acc_addtax_disc = db.Table(
    'acc_addtax_disc',
    db.Column('ptid', db.Integer, index=True),
    db.Column('deptcd', db.String(20)),
    db.Column('deptname', db.String(100)),
    db.Column('tax', db.Numeric(10, 2)),
    db.Column('grpcd', db.String(20)),
    db.Column('plucd', db.String(20)),
    db.Column('pluname', db.String(100)),
    db.Column('disccd', db.String(20)),
    db.Column('discname', db.String(100)),
    db.Column('disamt', db.Numeric(20, 2)),
    db.Column('taxamt', db.Numeric(20, 6)),
    db.Column('acccd', db.String(20))
)


t_acc_addtax_disc_gl = db.Table(
    'acc_addtax_disc_gl',
    db.Column('ptid', db.Integer, index=True),
    db.Column('deptcd', db.String(20)),
    db.Column('deptname', db.String(100)),
    db.Column('tax', db.Numeric(10, 2)),
    db.Column('grpcd', db.String(20)),
    db.Column('plucd', db.String(20)),
    db.Column('pluname', db.String(100)),
    db.Column('disccd', db.String(20)),
    db.Column('discname', db.String(100)),
    db.Column('disamt', db.Numeric(20, 2)),
    db.Column('taxamt', db.Numeric(20, 6)),
    db.Column('acccd', db.String(20))
)


t_acc_addtax_new = db.Table(
    'acc_addtax_new',
    db.Column('ptid', db.Integer),
    db.Column('deptid', db.Integer),
    db.Column('amt_type', db.String(20)),
    db.Column('tax_amt', db.Numeric(20, 6)),
    db.Column('account_d', db.String(10)),
    db.Column('account_nd', db.String(50)),
    db.Column('account_c', db.String(10)),
    db.Column('account_nc', db.String(50)),
    db.Column('updby', db.String(20)),
    db.Column('upddt', db.DateTime, server_default=db.FetchedValue()),
    db.Column('subtp', db.String(20)),
    db.Index('idx_acc_addtax_new', 'ptid', 'deptid')
)


t_acc_addtax_new_gl = db.Table(
    'acc_addtax_new_gl',
    db.Column('ptid', db.Integer),
    db.Column('deptid', db.Integer),
    db.Column('amt_type', db.String(20)),
    db.Column('tax_amt', db.Numeric(20, 6)),
    db.Column('account_d', db.String(10)),
    db.Column('account_nd', db.String(50)),
    db.Column('account_c', db.String(10)),
    db.Column('account_nc', db.String(50)),
    db.Column('updby', db.String(20)),
    db.Column('upddt', db.DateTime, server_default=db.FetchedValue()),
    db.Column('subtp', db.String(20)),
    db.Index('idx_acc_addtax_new_gl', 'ptid', 'deptid')
)


t_acc_addtax_sal = db.Table(
    'acc_addtax_sal',
    db.Column('ptid', db.Integer, index=True),
    db.Column('deptcd', db.String(20)),
    db.Column('deptname', db.String(100)),
    db.Column('grpcd', db.String(20)),
    db.Column('catcd', db.String(20)),
    db.Column('catname', db.String(100)),
    db.Column('taxrt', db.Numeric(10, 2)),
    db.Column('netamt', db.Numeric(20, 4)),
    db.Column('taxamt', db.Numeric(20, 6)),
    db.Column('acccd', db.String(20)),
    db.Column('bizdt', db.DateTime)
)


t_acc_addtax_sal_gl = db.Table(
    'acc_addtax_sal_gl',
    db.Column('ptid', db.Integer, index=True),
    db.Column('deptcd', db.String(20)),
    db.Column('deptname', db.String(100)),
    db.Column('grpcd', db.String(20)),
    db.Column('catcd', db.String(20)),
    db.Column('catname', db.String(100)),
    db.Column('taxrt', db.Numeric(10, 2)),
    db.Column('netamt', db.Numeric(20, 4)),
    db.Column('taxamt', db.Numeric(20, 6)),
    db.Column('acccd', db.String(20)),
    db.Column('bizdt', db.DateTime)
)


t_acc_cal_temp = db.Table(
    'acc_cal_temp',
    db.Column('deptcd', db.String(20)),
    db.Column('bizdt', db.String(10)),
    db.Column('plucd', db.String(50)),
    db.Column('qty', db.Numeric(20, 6)),
    db.Column('cur_cost', db.Numeric(20, 6)),
    db.Column('dept_no', db.String(10)),
    db.Column('cat_no', db.String(10)),
    db.Column('group_no', db.String(10)),
    db.Column('plu_type', db.String(1)),
    db.Column('strans_type', db.String(3)),
    db.Column('reason_type', db.String(100)),
    db.Column('remark1', db.String(50)),
    db.Column('remark2', db.String(50)),
    db.Column('invoice_amt', db.Numeric(30, 6)),
    db.Column('fee_amt', db.Numeric(30, 6))
)


t_acc_cal_temp_ap = db.Table(
    'acc_cal_temp_ap',
    db.Column('deptcd', db.String(20)),
    db.Column('vencd', db.String(30)),
    db.Column('comcd', db.String(20)),
    db.Column('bizdt', db.String(20)),
    db.Column('actdt', db.String(20)),
    db.Column('invcd', db.String(50)),
    db.Column('invid', db.String(50)),
    db.Column('qty', db.Numeric(20, 6)),
    db.Column('inv_amt1', db.Numeric(20, 6)),
    db.Column('inv_amt2', db.Numeric(20, 6)),
    db.Column('inv_amt3', db.Numeric(20, 6)),
    db.Column('remark1', db.String(50), index=True),
    db.Column('remark2', db.String(50), index=True),
    db.Column('page_no', db.Integer),
    db.Column('page_row_no', db.Integer),
    db.Column('page_group_count', db.Integer),
    db.Column('rn', db.Integer),
    db.Column('batch_id', db.String(10), index=True),
    db.Column('rc', db.String(50)),
    db.Column('acc', db.String(50)),
    db.Column('total', db.Integer),
    db.Column('group_id', db.Integer),
    db.Column('vensitecd', db.String(50)),
    db.Column('fin_year', db.String(4)),
    db.Column('fin_month', db.String(2)),
    db.Column('updby', db.String(20))
)


t_acc_cal_temp_gl = db.Table(
    'acc_cal_temp_gl',
    db.Column('deptcd', db.String(20)),
    db.Column('bizdt', db.String(20)),
    db.Column('plucd', db.String(50)),
    db.Column('qty', db.Numeric(20, 6)),
    db.Column('cur_cost', db.Numeric(20, 6)),
    db.Column('dept_no', db.String(10)),
    db.Column('cat_no', db.String(10)),
    db.Column('group_no', db.String(10)),
    db.Column('plu_type', db.String(1)),
    db.Column('strans_type', db.String(3)),
    db.Column('reason_type', db.String(100)),
    db.Column('remark1', db.String(50), index=True),
    db.Column('remark2', db.String(50), index=True),
    db.Column('invoice_amt', db.Numeric(30, 6)),
    db.Column('fee_amt', db.Numeric(30, 6)),
    db.Column('page_no', db.Integer),
    db.Column('page_row_no', db.Integer),
    db.Column('page_group_count', db.Integer),
    db.Column('vencd', db.String(20)),
    db.Column('rn', db.Integer),
    db.Column('dacccd', db.String(20)),
    db.Column('batch_id', db.Integer),
    db.Column('actdt', db.String(20)),
    db.Column('rc', db.String(20)),
    db.Column('acc', db.String(20)),
    db.Column('voucher_code', db.String(20)),
    db.Column('major_no', db.String(30)),
    db.Column('ic', db.String(20))
)


t_acc_dlvdtl = db.Table(
    'acc_dlvdtl',
    db.Column('id', db.Numeric(12, 0, asdecimal=False)),
    db.Column('mstid', db.Numeric(12, 0, asdecimal=False), index=True),
    db.Column('deptid', db.Integer, nullable=False),
    db.Column('amt', db.Numeric(20, 6)),
    db.Column('rmk', db.Unicode(150)),
    db.Column('updby', db.String(20)),
    db.Column('upddt', db.DateTime),
    db.Column('sta', db.String(3), nullable=False)
)


t_acc_dlvmst = db.Table(
    'acc_dlvmst',
    db.Column('id', db.Numeric(12, 0, asdecimal=False)),
    db.Column('ptid', db.Integer, nullable=False),
    db.Column('tp', db.String(10)),
    db.Column('groupid', db.Integer),
    db.Column('amt', db.Numeric(20, 6)),
    db.Column('dacccd', db.String(20)),
    db.Column('cacccd', db.Unicode(50)),
    db.Column('rmk', db.Unicode(150)),
    db.Column('updby', db.String(20)),
    db.Column('upddt', db.DateTime),
    db.Column('sta', db.String(3), nullable=False),
    db.Column('execflg', db.String(1)),
    db.Column('nxtsta', db.String(3)),
    db.Index('idx_acc_dlvmst', 'groupid', 'ptid')
)


class AccInterface(db.Model):
    __tablename__ = 'acc_interface'
    __table_args__ = (
        db.Index('indx_acc_interface2', 'remark', 'account_code', 'accounting_month'),
        db.Index('indx_acc_interface4', 'type', 'accounting_month')
    )

    id = db.Column(db.Numeric(12, 0, asdecimal=False), primary_key=True)
    is_transfer = db.Column(db.String(2), server_default=db.FetchedValue())
    create_date = db.Column(db.String(12))
    voucher_type = db.Column(db.String(20), server_default=db.FetchedValue())
    voucher_no = db.Column(db.String(20), index=True)
    invoice_count = db.Column(db.String(6))
    remark = db.Column(db.String(500))
    account_code = db.Column(db.String(20))
    debit_amt = db.Column(db.String(50))
    cridit_amt = db.Column(db.String(50))
    qty = db.Column(db.String(50))
    currency_code = db.Column(db.String(30))
    exchange_rate = db.Column(db.String(30))
    create_optor = db.Column(db.String(20), server_default=db.FetchedValue())
    account_type = db.Column(db.String(20))
    bill_no = db.Column(db.String(20))
    bill_date = db.Column(db.String(12))
    subbill_no = db.Column(db.String(8))
    check_rule = db.Column(db.String(50), server_default=db.FetchedValue())
    accounting_year = db.Column(db.String(8))
    accounting_period = db.Column(db.String(8))
    aduit_optor = db.Column(db.String(20), server_default=db.FetchedValue())
    account_optor = db.Column(db.String(20), server_default=db.FetchedValue())
    is_account = db.Column(db.String(20))
    cash_optor = db.Column(db.String(20))
    currency_name = db.Column(db.String(20))
    price = db.Column(db.String(20))
    voucher_flag = db.Column(db.String(8))
    business_date = db.Column(db.DateTime)
    type = db.Column(db.String(20))
    is_curchange = db.Column(db.String(1), index=True)
    accounting_month = db.Column(db.String(6))
    reason_code = db.Column(db.String(20))
    update_date = db.Column(db.DateTime)
    update_by = db.Column(db.String(50), server_default=db.FetchedValue())
    net_no = db.Column(db.String(50))
    category_code = db.Column(db.String(150))
    net_no_cal = db.Column(db.String(50))
    lkid = db.Column(db.String(250))
    descamt = db.Column(db.Numeric(20, 2))


t_acc_interface_101 = db.Table(
    'acc_interface_101',
    db.Column('acc_month', db.String(6), nullable=False),
    db.Column('acc_rmk', db.String(50), nullable=False),
    db.Column('area_zone', db.String(6), nullable=False),
    db.Column('acc_no', db.Numeric(asdecimal=False))
)


t_acc_interface_body = db.Table(
    'acc_interface_body',
    db.Column('pid', db.String(400)),
    db.Column('entry_id', db.String(50)),
    db.Column('account_code', db.String(50)),
    db.Column('abstract', db.String(450)),
    db.Column('settlement', db.String(50)),
    db.Column('document_id', db.String(50)),
    db.Column('document_date', db.String(50)),
    db.Column('currency', db.String(50)),
    db.Column('unit_price', db.String(50)),
    db.Column('exchange_rate1', db.String(50)),
    db.Column('exchange_rate2', db.String(50)),
    db.Column('debit_quantity', db.String(50)),
    db.Column('primary_debit_amount', db.String(50)),
    db.Column('secondary_debit_amount', db.String(50)),
    db.Column('natural_debit_currency', db.String(50)),
    db.Column('credit_quantity', db.String(50)),
    db.Column('primary_credit_amount', db.String(50)),
    db.Column('secondary_credit_amount', db.String(50)),
    db.Column('natural_credit_currency', db.String(50)),
    db.Column('bill_type', db.String(50)),
    db.Column('bill_id', db.String(50)),
    db.Column('bill_date', db.String(50)),
    db.Column('voucher_no', db.String(50), index=True),
    db.Column('sno', db.Numeric(20, 0, asdecimal=False))
)


t_acc_interface_ddtl = db.Table(
    'acc_interface_ddtl',
    db.Column('item_1', db.String(50)),
    db.Column('item_2', db.String(50)),
    db.Column('item_3', db.String(50)),
    db.Column('item_4', db.String(50)),
    db.Column('pid', db.String(400), index=True)
)


t_acc_interface_ddtl2 = db.Table(
    'acc_interface_ddtl2',
    db.Column('pid', db.String(400), index=True),
    db.Column('money', db.String(50)),
    db.Column('moneyass', db.String(50)),
    db.Column('moneymain', db.String(50)),
    db.Column('pk_cashflow', db.String(50))
)


t_acc_interface_head = db.Table(
    'acc_interface_head',
    db.Column('company', db.String(50)),
    db.Column('voucher_type', db.String(50)),
    db.Column('fiscal_year', db.String(50)),
    db.Column('accounting_period', db.String(50)),
    db.Column('voucher_id', db.String(50)),
    db.Column('attachment_number', db.String(50)),
    db.Column('prepareddate', db.String(50)),
    db.Column('enter', db.String(50)),
    db.Column('cashier', db.String(50)),
    db.Column('signature', db.String(50)),
    db.Column('checker', db.String(50)),
    db.Column('operator', db.String(50)),
    db.Column('posting_date', db.String(50)),
    db.Column('posting_person', db.String(50)),
    db.Column('revokeflag', db.String(50)),
    db.Column('voucherkind', db.String(50)),
    db.Column('voucher_making_system', db.String(50)),
    db.Column('memo1', db.String(50)),
    db.Column('memo2', db.String(50)),
    db.Column('reserve1', db.String(50)),
    db.Column('reserve2', db.String(50)),
    db.Column('voucher_no', db.String(50))
)


t_acc_interface_hhs = db.Table(
    'acc_interface_hhs',
    db.Column('id', db.Numeric(12, 0, asdecimal=False), nullable=False),
    db.Column('is_transfer', db.String(2), server_default=db.FetchedValue()),
    db.Column('create_date', db.String(12)),
    db.Column('voucher_type', db.String(20), server_default=db.FetchedValue()),
    db.Column('voucher_no', db.String(20)),
    db.Column('invoice_count', db.String(6)),
    db.Column('remark', db.String(200)),
    db.Column('account_code', db.String(20)),
    db.Column('debit_amt', db.String(50)),
    db.Column('cridit_amt', db.String(50)),
    db.Column('qty', db.String(50)),
    db.Column('currency_code', db.String(30)),
    db.Column('exchange_rate', db.String(30)),
    db.Column('create_optor', db.String(20), server_default=db.FetchedValue()),
    db.Column('account_type', db.String(20)),
    db.Column('bill_no', db.String(20)),
    db.Column('bill_date', db.String(12)),
    db.Column('subbill_no', db.String(8)),
    db.Column('check_rule', db.String(50), server_default=db.FetchedValue()),
    db.Column('accounting_year', db.String(8)),
    db.Column('accounting_period', db.String(8)),
    db.Column('aduit_optor', db.String(20), server_default=db.FetchedValue()),
    db.Column('account_optor', db.String(20), server_default=db.FetchedValue()),
    db.Column('is_account', db.String(20)),
    db.Column('cash_optor', db.String(20)),
    db.Column('currency_name', db.String(20)),
    db.Column('price', db.String(20)),
    db.Column('voucher_flag', db.String(8)),
    db.Column('business_date', db.DateTime),
    db.Column('type', db.String(20)),
    db.Column('is_curchange', db.String(1)),
    db.Column('accounting_month', db.String(6)),
    db.Column('reason_code', db.String(20)),
    db.Column('update_date', db.DateTime),
    db.Column('update_by', db.String(50), server_default=db.FetchedValue()),
    db.Column('net_no', db.String(50)),
    db.Column('category_code', db.String(150)),
    db.Column('net_no_cal', db.String(50)),
    db.Column('lkid', db.String(250))
)


class AccInterfaceNo(db.Model):
    __tablename__ = 'acc_interface_no'
    __table_args__ = (
        db.Index('idx_acc_interface_no', 'voucher_no', 'table_type'),
    )

    voucher_no = db.Column(db.String(20))
    out_voucher_no = db.Column(db.String(20), primary_key=True)
    out_seq = db.Column(db.Numeric(asdecimal=False))
    table_type = db.Column(db.String(1))
    month_mm = db.Column(db.String(6))
    strans_tyep = db.Column(db.String(3))
    remarks = db.Column(db.String(150))
    isexp = db.Column(db.String(1), index=True, server_default=db.FetchedValue())
    step = db.Column(db.Integer, server_default=db.FetchedValue())
    expdt = db.Column(db.DateTime)
    nexid = db.Column(db.Numeric(asdecimal=False))
    isexpdtl = db.Column(db.String(1), index=True, server_default=db.FetchedValue())
    rmk = db.Column(db.String(150))


t_acc_interface_no_hhs = db.Table(
    'acc_interface_no_hhs',
    db.Column('voucher_no', db.String(20)),
    db.Column('out_voucher_no', db.String(20), nullable=False),
    db.Column('out_seq', db.Numeric(asdecimal=False)),
    db.Column('table_type', db.String(1)),
    db.Column('month_mm', db.String(6)),
    db.Column('strans_tyep', db.String(3)),
    db.Column('remarks', db.String(150)),
    db.Column('isexp', db.String(1), server_default=db.FetchedValue()),
    db.Column('step', db.Integer, server_default=db.FetchedValue()),
    db.Column('expdt', db.DateTime)
)


t_acc_interfacedtl = db.Table(
    'acc_interfacedtl',
    db.Column('id', db.Numeric(18, 0, asdecimal=False)),
    db.Column('accounting_month', db.String(10)),
    db.Column('vtyp', db.String(5)),
    db.Column('voucd', db.String(150), index=True),
    db.Column('isdc', db.String(1)),
    db.Column('typ', db.String(20)),
    db.Column('cd', db.String(20)),
    db.Column('name', db.String(150)),
    db.Column('acccd', db.String(20)),
    db.Column('accname', db.String(150)),
    db.Column('plucd', db.String(20)),
    db.Column('pluname', db.String(150)),
    db.Column('qty', db.Numeric(20, 6)),
    db.Column('price', db.Numeric(20, 6)),
    db.Column('amt', db.Numeric(20, 6)),
    db.Column('billcd', db.String(50)),
    db.Column('deptcd', db.String(50)),
    db.Column('deptname', db.String(150)),
    db.Column('lkcd', db.String(120)),
    db.Column('lkname', db.String(150)),
    db.Column('remark1', db.String(150)),
    db.Column('remark2', db.String(150)),
    db.Column('mstid', db.Numeric(18, 0, asdecimal=False))
)


t_acc_outboud_ap_tmp = db.Table(
    'acc_outboud_ap_tmp',
    db.Column('invcd', db.String(20), nullable=False),
    db.Column('sta', db.Integer, nullable=False),
    db.Column('msg', db.String(100)),
    db.Column('cddt', db.DateTime, server_default=db.FetchedValue()),
    db.Column('updt', db.DateTime, server_default=db.FetchedValue()),
    db.Index('idx_acc_outboud_ap_tmp_invid', 'invcd', 'sta')
)


t_acc_swinfo = db.Table(
    'acc_swinfo',
    db.Column('cd', db.String(10), nullable=False),
    db.Column('gsbh', db.String(20), nullable=False),
    db.Column('gsnm', db.String(20), nullable=False),
    db.Column('nsrsbh', db.String(50)),
    db.Column('gstt', db.String(150)),
    db.Column('gsaddr', db.String(250)),
    db.Column('gsyhnm', db.String(250)),
    db.Column('gsyhzh', db.String(250)),
    db.Column('skr', db.String(30)),
    db.Column('shr', db.String(30)),
    db.Column('kpr', db.String(30)),
    db.Column('appid', db.String(100)),
    db.Column('upddt', db.DateTime),
    db.Column('rc', db.String(10))
)


class AccVouacc(db.Model):
    __tablename__ = 'acc_vouacc'
    __table_args__ = (
        db.Index('idx_accvouacc', 'voutpcd', 'isdc'),
    )

    id = db.Column(db.Numeric(12, 0, asdecimal=False), primary_key=True)
    voutpcd = db.Column(db.String(50))
    isdc = db.Column(db.String(1))
    dtyp = db.Column(db.String(1))
    dcd = db.Column(db.String(50))
    dname = db.Column(db.String(50))
    dacccd = db.Column(db.String(50))
    ctyp = db.Column(db.String(1))
    ccd = db.Column(db.String(50))
    cname = db.Column(db.String(50))
    cacccd = db.Column(db.String(50))
    lktp = db.Column(db.String(5))
    lkcd = db.Column(db.String(50))
    isdept = db.Column(db.String(1), server_default=db.FetchedValue())
    deptcd = db.Column(db.String(50))
    ispluac = db.Column(db.String(1))
    rmk = db.Column(db.String(255))
    updby = db.Column(db.String(20))
    upddt = db.Column(db.DateTime)
    sta = db.Column(db.String(3), nullable=False)
    execflg = db.Column(db.String(1))
    nxtsta = db.Column(db.String(3))
    lkname = db.Column(db.String(50))


t_acc_vouacc_gc = db.Table(
    'acc_vouacc_gc',
    db.Column('id', db.Numeric(12, 0, asdecimal=False), nullable=False),
    db.Column('voutpcd', db.String(50)),
    db.Column('isdc', db.String(1)),
    db.Column('dtyp', db.String(1)),
    db.Column('dcd', db.String(50)),
    db.Column('dname', db.String(50)),
    db.Column('dacccd', db.String(50)),
    db.Column('ctyp', db.String(1)),
    db.Column('ccd', db.String(50)),
    db.Column('cname', db.String(50)),
    db.Column('cacccd', db.String(50)),
    db.Column('lktp', db.String(5)),
    db.Column('lkcd', db.String(50)),
    db.Column('isdept', db.String(1)),
    db.Column('deptcd', db.String(50)),
    db.Column('ispluac', db.String(1)),
    db.Column('rmk', db.String(255)),
    db.Column('updby', db.String(20)),
    db.Column('upddt', db.DateTime),
    db.Column('sta', db.String(3), nullable=False),
    db.Column('execflg', db.String(1)),
    db.Column('nxtsta', db.String(3)),
    db.Column('lkname', db.String(50))
)


t_acc_vouimpdtl = db.Table(
    'acc_vouimpdtl',
    db.Column('id', db.Numeric(12, 0, asdecimal=False), nullable=False),
    db.Column('vouid', db.Numeric(12, 0, asdecimal=False)),
    db.Column('month', db.Numeric(10, 0, asdecimal=False)),
    db.Column('accrmk', db.String(100)),
    db.Column('acccd', db.String(20)),
    db.Column('acctype', db.String(50)),
    db.Column('damt', db.Numeric(16, 2)),
    db.Column('camt', db.Numeric(16, 2)),
    db.Column('upddt', db.DateTime),
    db.Column('updby', db.String(50)),
    db.Column('sta', db.String(3), nullable=False),
    db.Column('execflg', db.String(1)),
    db.Column('nxtsta', db.String(3)),
    db.Column('acclkcd', db.String(50)),
    db.Column('execlog', db.String(255))
)


class AccVouimpmst(db.Model):
    __tablename__ = 'acc_vouimpmst'

    id = db.Column(db.Numeric(12, 0, asdecimal=False), primary_key=True)
    voucd = db.Column(db.String(20))
    rmk = db.Column(db.String(255))
    updby = db.Column(db.String(50))
    upddt = db.Column(db.DateTime)
    sta = db.Column(db.String(3), nullable=False)
    execflg = db.Column(db.String(1))
    nxtsta = db.Column(db.String(3))
    execlog = db.Column(db.String(255))


class AccVourcherImp(db.Model):
    __tablename__ = 'acc_vourcher_imp'

    pid = db.Column(db.String(50), primary_key=True)
    account_term = db.Column(db.String(6), nullable=False)
    remarks = db.Column(db.String(150))
    account_code = db.Column(db.String(20))
    fz_type = db.Column(db.String(20))
    fz_code = db.Column(db.String(20))
    d_amt = db.Column(db.Numeric(20, 6))
    c_amt = db.Column(db.Numeric(20, 6))
    status = db.Column(db.String(1), server_default=db.FetchedValue())
    update_date = db.Column(db.DateTime, server_default=db.FetchedValue())
    update_by = db.Column(db.String(50))


t_asn_inventory = db.Table(
    'asn_inventory',
    db.Column('id', db.Numeric(10, 0, asdecimal=False), nullable=False),
    db.Column('collect_date', db.String(255)),
    db.Column('currency_code', db.String(255)),
    db.Column('initial_record_ind', db.String(255)),
    db.Column('item_number', db.String(255)),
    db.Column('md_doc_type', db.String(255)),
    db.Column('md_extract_date', db.String(255)),
    db.Column('md_extract_id', db.String(255)),
    db.Column('md_group_count', db.String(255)),
    db.Column('md_group_id', db.String(255)),
    db.Column('org_code', db.String(255)),
    db.Column('reserved_qty', db.String(255)),
    db.Column('segment_ind', db.String(255)),
    db.Column('source_code', db.String(255)),
    db.Column('source_publish_date', db.String(255)),
    db.Column('total_onhand_qty', db.String(255)),
    db.Column('unit_moving_average_cost', db.String(255)),
    db.Column('get_date', db.DateTime, server_default=db.FetchedValue())
)


t_asn_inventory_his = db.Table(
    'asn_inventory_his',
    db.Column('id', db.Numeric(10, 0, asdecimal=False), nullable=False),
    db.Column('collect_date', db.String(255)),
    db.Column('currency_code', db.String(255)),
    db.Column('initial_record_ind', db.String(255)),
    db.Column('item_number', db.String(255)),
    db.Column('md_doc_type', db.String(255)),
    db.Column('md_extract_date', db.String(255)),
    db.Column('md_extract_id', db.String(255)),
    db.Column('md_group_count', db.String(255)),
    db.Column('md_group_id', db.String(255)),
    db.Column('org_code', db.String(255)),
    db.Column('reserved_qty', db.String(255)),
    db.Column('segment_ind', db.String(255)),
    db.Column('source_code', db.String(255)),
    db.Column('source_publish_date', db.String(255)),
    db.Column('total_onhand_qty', db.String(255)),
    db.Column('unit_moving_average_cost', db.String(255)),
    db.Column('get_date', db.DateTime, server_default=db.FetchedValue())
)


class AsnShipment(db.Model):
    __tablename__ = 'asn_shipment'

    id = db.Column(db.Integer, primary_key=True)
    datedelivery = db.Column(db.DateTime)
    dateshipment = db.Column(db.DateTime)
    deliveryid = db.Column(db.Numeric(10, 0, asdecimal=False))
    mddc = db.Column(db.String(255))
    mdextractdate = db.Column(db.DateTime)
    mdextractid = db.Column(db.Numeric(10, 0, asdecimal=False))
    mdgmtoffset = db.Column(db.String(255))
    mdgroupcount = db.Column(db.String(255))
    mdgroupid = db.Column(db.Numeric(10, 0, asdecimal=False))
    mdtxlinecount = db.Column(db.String(255))
    storeno = db.Column(db.Numeric(10, 0, asdecimal=False))
    date_delivery = db.Column(db.DateTime)
    date_shipment = db.Column(db.DateTime)
    md_extract_date = db.Column(db.DateTime)
    md_extractid = db.Column(db.Numeric(10, 0, asdecimal=False))
    md_gmt_offset = db.Column(db.String(255))
    md_group_count = db.Column(db.String(255))
    md_groupid = db.Column(db.Numeric(10, 0, asdecimal=False))
    md_tx_line_count = db.Column(db.String(255))
    store_no = db.Column(db.Numeric(10, 0, asdecimal=False))


class AsnShipmentFile(db.Model):
    __tablename__ = 'asn_shipment_file'

    id = db.Column(db.Numeric(10, 0, asdecimal=False), primary_key=True)
    date_delivery = db.Column(db.String(255))
    date_shipment = db.Column(db.String(255))
    deliveryid = db.Column(db.String(255))
    mddc = db.Column(db.String(255))
    md_extract_date = db.Column(db.String(255))
    md_extractid = db.Column(db.String(255))
    md_gmt_offset = db.Column(db.String(255))
    md_group_count = db.Column(db.String(255))
    md_groupid = db.Column(db.String(255))
    md_tx_line_count = db.Column(db.String(255))
    store_no = db.Column(db.String(255))


class AsnShipmentLine(db.Model):
    __tablename__ = 'asn_shipment_line'

    id = db.Column(db.Numeric(10, 0, asdecimal=False), primary_key=True)
    item_no = db.Column(db.String(255))
    local_currency_code = db.Column(db.String(255))
    md_extractid = db.Column(db.String(255))
    md_groupid = db.Column(db.String(255))
    order_line_price = db.Column(db.String(255))
    order_source_reference = db.Column(db.String(255))
    primary_uom_code = db.Column(db.String(255))
    qty_shipped = db.Column(db.String(255))
    store_no = db.Column(db.String(255))
    subst_item_no = db.Column(db.String(255))
    deliveryid = db.Column(db.String(255))
    lineid = db.Column(db.String(255))


class BasAdjtax(db.Model):
    __tablename__ = 'bas_adjtax'

    id = db.Column(db.Integer, primary_key=True)
    adjrsn = db.Column(db.String(20))
    taxtp = db.Column(db.String(1))
    rmk = db.Column(db.String(255))
    updby = db.Column(db.String(50))
    upddt = db.Column(db.DateTime)
    sta = db.Column(db.String(3), nullable=False)
    execflg = db.Column(db.String(1))
    nxtsta = db.Column(db.String(3))


class BasBank(db.Model):
    __tablename__ = 'bas_bank'

    id = db.Column(db.Integer, primary_key=True)
    coid = db.Column(db.Integer)
    tp = db.Column(db.String(20))
    cd = db.Column(db.String(50))
    secondcd = db.Column(db.String(30))
    bankcd = db.Column(db.String(50))
    dpsttp = db.Column(db.String(20))
    crcd = db.Column(db.String(3))
    acctcd = db.Column(db.String(20))
    acctnm = db.Column(db.String(50))
    nm_l_zh = db.Column(db.Unicode(50))
    nm_l_en = db.Column(db.Unicode(50))
    nm_l_ja = db.Column(db.Unicode(50))
    addr = db.Column(db.String(100))
    rmk = db.Column(db.Unicode(255))
    updby = db.Column(db.String(20))
    upddt = db.Column(db.DateTime, server_default=db.FetchedValue())
    sta = db.Column(db.String(3), nullable=False)
    stdt = db.Column(db.DateTime)


t_bas_bankdept = db.Table(
    'bas_bankdept',
    db.Column('id', db.Integer, nullable=False),
    db.Column('bankid', db.Integer),
    db.Column('deptid', db.Integer),
    db.Column('rmk', db.String(255)),
    db.Column('updby', db.String(50)),
    db.Column('upddt', db.DateTime),
    db.Column('sta', db.String(3), nullable=False),
    db.Column('execflg', db.String(1)),
    db.Column('nxtsta', db.String(3)),
    db.Column('stdt', db.DateTime),
    db.Column('eddt', db.DateTime)
)


class BasBomin(db.Model):
    __tablename__ = 'bas_bomin'

    id = db.Column(db.Integer, primary_key=True)
    bommstid = db.Column(db.Integer, nullable=False)
    inpluid = db.Column(db.Integer)
    uomcd = db.Column(db.String(6))
    qty = db.Column(db.Numeric(16, 6))
    cwflg = db.Column(db.String(1), server_default=db.FetchedValue())
    putouttp = db.Column(db.String(10))
    woseq = db.Column(db.String(20))
    plrt = db.Column(db.Numeric(6, 2))
    costrt = db.Column(db.Numeric(6, 2))
    optinpluid = db.Column(db.Integer)
    saleprc = db.Column(db.Numeric(16, 4))
    costprc = db.Column(db.Numeric(16, 4))
    scraprt = db.Column(db.Numeric(6, 2))
    rsvflg = db.Column(db.String(1), server_default=db.FetchedValue())
    rmk = db.Column(db.Unicode(255))
    updby = db.Column(db.String(20))
    upddt = db.Column(db.DateTime)
    sta = db.Column(db.String(3), nullable=False)
    execflg = db.Column(db.String(1), server_default=db.FetchedValue())
    nxtsta = db.Column(db.String(3))


class BasBommst(db.Model):
    __tablename__ = 'bas_bommst'

    id = db.Column(db.Integer, primary_key=True)
    deptlktp = db.Column(db.String(10))
    deptlkid = db.Column(db.Integer)
    pluid = db.Column(db.Integer, nullable=False)
    bomtp = db.Column(db.String(10))
    uomcd = db.Column(db.String(6))
    subcpyflg = db.Column(db.String(1), server_default=db.FetchedValue())
    stdt = db.Column(db.DateTime)
    eddt = db.Column(db.DateTime)
    wotp = db.Column(db.String(10))
    rmk = db.Column(db.Unicode(255))
    updby = db.Column(db.String(20))
    upddt = db.Column(db.DateTime)
    sta = db.Column(db.String(3), nullable=False)
    execflg = db.Column(db.String(1), server_default=db.FetchedValue())
    nxtsta = db.Column(db.String(3))
    srctp = db.Column(db.String(1), server_default=db.FetchedValue())


class BasBomout(db.Model):
    __tablename__ = 'bas_bomout'

    id = db.Column(db.Integer, primary_key=True)
    bommstid = db.Column(db.Integer, nullable=False)
    outpluid = db.Column(db.Integer)
    uomcd = db.Column(db.String(6))
    qty = db.Column(db.Numeric(16, 6))
    costrt = db.Column(db.Numeric(6, 2))
    saleprc = db.Column(db.Numeric(16, 4))
    scraprt = db.Column(db.Numeric(6, 2))
    costprc = db.Column(db.Numeric(16, 4))
    resrt = db.Column(db.Numeric(6, 2))
    woseq = db.Column(db.String(20))
    primflg = db.Column(db.String(1), server_default=db.FetchedValue())
    rmk = db.Column(db.Unicode(255))
    updby = db.Column(db.String(20))
    upddt = db.Column(db.DateTime)
    sta = db.Column(db.String(3), nullable=False)
    execflg = db.Column(db.String(1), server_default=db.FetchedValue())
    nxtsta = db.Column(db.String(3))


class BasBomrep(db.Model):
    __tablename__ = 'bas_bomrep'

    id = db.Column(db.Integer, primary_key=True)
    deptgpid = db.Column(db.Integer)
    pluid = db.Column(db.Integer, nullable=False, index=True)
    reppluid = db.Column(db.Integer, nullable=False)
    rprt = db.Column(db.Numeric(8, 4))
    stdt = db.Column(db.DateTime)
    eddt = db.Column(db.DateTime)
    rmk = db.Column(db.String(255))
    updby = db.Column(db.String(20))
    upddt = db.Column(db.DateTime)
    sta = db.Column(db.String(3), nullable=False)
    execflg = db.Column(db.String(1))
    nxtsta = db.Column(db.String(3))


t_bas_bomrephis = db.Table(
    'bas_bomrephis',
    db.Column('bizdt', db.DateTime, nullable=False),
    db.Column('deptid', db.Integer, nullable=False),
    db.Column('pluid', db.Integer, nullable=False),
    db.Column('reppluid', db.Integer, nullable=False),
    db.Column('uomcd', db.String(6)),
    db.Column('rprt', db.Numeric(8, 4))
)


class BasBomstk(db.Model):
    __tablename__ = 'bas_bomstk'

    deptlkid = db.Column(db.Integer)
    plumstid = db.Column(db.Integer)
    pluid = db.Column(db.Integer)
    lntp = db.Column(db.String(10))
    uomcd = db.Column(db.String(6))
    qty = db.Column(db.Numeric(16, 6))
    id = db.Column(db.Integer, primary_key=True)


class BasBomstkhi(db.Model):
    __tablename__ = 'bas_bomstkhis'

    bizdt = db.Column(db.DateTime, primary_key=True, nullable=False)
    deptlkid = db.Column(db.Integer, primary_key=True, nullable=False)
    plumstid = db.Column(db.Integer, primary_key=True, nullable=False)
    pluid = db.Column(db.Integer, primary_key=True, nullable=False)
    lntp = db.Column(db.String(10))
    uomcd = db.Column(db.String(6))
    qty = db.Column(db.Numeric(16, 6))


class BasCategory(db.Model):
    __tablename__ = 'bas_category'

    id = db.Column(db.Integer, primary_key=True)
    cd = db.Column(db.String(20))
    tp = db.Column(db.String(10))
    secondcd = db.Column(db.String(20))
    nm_l_zh = db.Column(db.Unicode(50), nullable=False)
    nm_l_en = db.Column(db.Unicode(50))
    nm_l_ja = db.Column(db.Unicode(50))
    pid = db.Column(db.Integer)
    lvl = db.Column(db.Integer)
    pth = db.Column(db.String(100))
    leafflg = db.Column(db.String(1), server_default=db.FetchedValue())
    rmk = db.Column(db.Unicode(255))
    updby = db.Column(db.String(20))
    upddt = db.Column(db.DateTime)
    sta = db.Column(db.String(3), nullable=False)
    execflg = db.Column(db.String(1), server_default=db.FetchedValue())
    nxtsta = db.Column(db.String(3))
    taxgp = db.Column(db.String(10))


t_bas_category_gc = db.Table(
    'bas_category_gc',
    db.Column('id', db.Integer, nullable=False),
    db.Column('cd', db.String(20)),
    db.Column('tp', db.String(10)),
    db.Column('secondcd', db.String(20)),
    db.Column('nm_l_zh', db.Unicode(50), nullable=False),
    db.Column('nm_l_en', db.Unicode(50)),
    db.Column('nm_l_ja', db.Unicode(50)),
    db.Column('pid', db.Integer),
    db.Column('lvl', db.Integer),
    db.Column('pth', db.String(100)),
    db.Column('leafflg', db.String(1)),
    db.Column('rmk', db.Unicode(255)),
    db.Column('updby', db.String(20)),
    db.Column('upddt', db.DateTime),
    db.Column('sta', db.String(3), nullable=False),
    db.Column('execflg', db.String(1)),
    db.Column('nxtsta', db.String(3)),
    db.Column('taxgp', db.String(10))
)


class BasCattax(db.Model):
    __tablename__ = 'bas_cattax'

    id = db.Column(db.Integer, primary_key=True)
    groupid = db.Column(db.Integer)
    catid = db.Column(db.Integer)
    taxtp = db.Column(db.String(1))
    tax = db.Column(db.Numeric(18, 6))
    acccd = db.Column(db.String(20))
    rmk = db.Column(db.String(50))
    updby = db.Column(db.String(50))
    upddt = db.Column(db.DateTime)
    sta = db.Column(db.String(3), nullable=False)
    execflg = db.Column(db.String(1))
    nxtsta = db.Column(db.String(3))
    etaxdesc = db.Column(db.String(20))


t_bas_cattax_201804 = db.Table(
    'bas_cattax_201804',
    db.Column('id', db.Integer, nullable=False),
    db.Column('groupid', db.Integer),
    db.Column('catid', db.Integer),
    db.Column('taxtp', db.String(1)),
    db.Column('tax', db.Numeric(18, 6)),
    db.Column('acccd', db.String(20)),
    db.Column('rmk', db.String(50)),
    db.Column('updby', db.String(50)),
    db.Column('upddt', db.DateTime),
    db.Column('sta', db.String(3), nullable=False),
    db.Column('execflg', db.String(1)),
    db.Column('nxtsta', db.String(3)),
    db.Column('etaxdesc', db.String(20))
)


t_bas_crrt = db.Table(
    'bas_crrt',
    db.Column('id', db.Integer, nullable=False),
    db.Column('stdt', db.DateTime, nullable=False),
    db.Column('eddt', db.DateTime, nullable=False),
    db.Column('scrcd', db.String(3), nullable=False),
    db.Column('tcrcd', db.String(3), nullable=False),
    db.Column('crrt', db.Numeric(12, 6), nullable=False),
    db.Column('rmk', db.Unicode(255)),
    db.Column('updby', db.String(20)),
    db.Column('upddt', db.DateTime),
    db.Column('sta', db.String(3), nullable=False),
    db.Column('execflg', db.String(1)),
    db.Column('nxtsta', db.String(3))
)


class BasCustomer(db.Model):
    __tablename__ = 'bas_customer'

    id = db.Column(db.Integer, primary_key=True)
    coid = db.Column(db.Integer)
    cd = db.Column(db.String(20))
    secondcd = db.Column(db.String(20))
    nm_l_zh = db.Column(db.Unicode(50), nullable=False)
    nm_l_en = db.Column(db.Unicode(50))
    nm_l_ja = db.Column(db.Unicode(50))
    snm = db.Column(db.Unicode(30))
    ltrhdr = db.Column(db.Unicode(50), nullable=False)
    taxcd = db.Column(db.String(30))
    bizcd = db.Column(db.Unicode(20))
    cstmlvl = db.Column(db.String(10))
    cp = db.Column(db.Unicode(30))
    lr = db.Column(db.Unicode(30))
    invaddr = db.Column(db.Unicode(100))
    invzipcd = db.Column(db.String(20))
    coaddr = db.Column(db.Unicode(100))
    cozipcd = db.Column(db.String(20))
    country = db.Column(db.Unicode(20))
    province = db.Column(db.Unicode(20))
    city = db.Column(db.Unicode(20))
    officefax = db.Column(db.String(30))
    officetel = db.Column(db.String(30))
    crcd = db.Column(db.String(20))
    taxa = db.Column(db.String(20))
    taxrt = db.Column(db.Numeric(6, 2))
    banknm = db.Column(db.Unicode(50))
    bankaccount = db.Column(db.String(30))
    arrule = db.Column(db.String(10))
    artp = db.Column(db.String(10))
    keepamt = db.Column(db.Numeric(14, 2))
    creditamt = db.Column(db.Numeric(14, 2))
    aldnum = db.Column(db.Integer)
    aednum = db.Column(db.Integer)
    minamt = db.Column(db.Numeric(14, 2))
    maxamt = db.Column(db.Numeric(14, 2))
    rmk = db.Column(db.Unicode(255))
    updby = db.Column(db.String(20))
    upddt = db.Column(db.DateTime)
    sta = db.Column(db.String(3), nullable=False)
    execflg = db.Column(db.String(1))
    nxtsta = db.Column(db.String(3))


class BasCustplu(db.Model):
    __tablename__ = 'bas_custplu'

    id = db.Column(db.Integer, primary_key=True)
    custid = db.Column(db.Integer)
    plulktp = db.Column(db.String(10))
    plulkid = db.Column(db.Integer)
    alwqtyrt = db.Column(db.Numeric(7, 2))
    alwqty = db.Column(db.Numeric(16, 6))
    dstplid = db.Column(db.Integer)
    rmk = db.Column(db.Unicode(255))
    updby = db.Column(db.String(20))
    upddt = db.Column(db.DateTime)
    sta = db.Column(db.String(3))
    execflg = db.Column(db.String(1))
    nxtsta = db.Column(db.String(3))


class BasDeptgroup(db.Model):
    __tablename__ = 'bas_deptgroup'
    __table_args__ = (
        db.Index('idx_grpid', 'groupid', 'deptid'),
    )

    id = db.Column(db.Integer, primary_key=True)
    groupid = db.Column(db.Integer)
    deptid = db.Column(db.Integer)
    rmk = db.Column(db.Unicode(255))
    updby = db.Column(db.String(20))
    upddt = db.Column(db.DateTime)
    sta = db.Column(db.String(3), nullable=False)
    execflg = db.Column(db.String(1))
    nxtsta = db.Column(db.String(3))


class BasDeptif(db.Model):
    __tablename__ = 'bas_deptif'

    id = db.Column(db.Integer, primary_key=True)
    deptid = db.Column(db.Integer, nullable=False)
    twrt = db.Column(db.Integer)
    ifflg = db.Column(db.String(1), server_default=db.FetchedValue())
    rmk = db.Column(db.Unicode(255))
    updby = db.Column(db.String(20))
    upddt = db.Column(db.DateTime)
    sta = db.Column(db.String(3), nullable=False)
    execflg = db.Column(db.String(1), server_default=db.FetchedValue())
    nxtsta = db.Column(db.String(3))


class BasDepttpl(db.Model):
    __tablename__ = 'bas_depttpl'

    id = db.Column(db.Integer, primary_key=True)
    coid = db.Column(db.Integer)
    cd = db.Column(db.String(20))
    tp = db.Column(db.String(10))
    secondcd = db.Column(db.String(20))
    nm_l_zh = db.Column(db.Unicode(50), nullable=False)
    nm_l_en = db.Column(db.Unicode(50))
    nm_l_ja = db.Column(db.Unicode(50))
    pid = db.Column(db.Integer)
    lvl = db.Column(db.Integer)
    pth = db.Column(db.String(200))
    leafflg = db.Column(db.String(1), server_default=db.FetchedValue())
    rmk = db.Column(db.Unicode(255))
    updby = db.Column(db.String(20))
    upddt = db.Column(db.DateTime)
    sta = db.Column(db.String(3), nullable=False)
    execflg = db.Column(db.String(1), server_default=db.FetchedValue())
    nxtsta = db.Column(db.String(3))


class BasDisctax(db.Model):
    __tablename__ = 'bas_disctax'

    id = db.Column(db.Integer, primary_key=True)
    groupid = db.Column(db.Integer)
    discid = db.Column(db.Integer)
    taxtp = db.Column(db.String(1))
    tax = db.Column(db.Numeric(18, 2))
    rmk = db.Column(db.String(50))
    updby = db.Column(db.String(50))
    upddt = db.Column(db.DateTime)
    sta = db.Column(db.String(3), nullable=False)
    execflg = db.Column(db.String(1))
    nxtsta = db.Column(db.String(3))


class BasGroup(db.Model):
    __tablename__ = 'bas_group'

    id = db.Column(db.Integer, primary_key=True)
    cd = db.Column(db.String(20))
    secondcd = db.Column(db.String(20))
    tp = db.Column(db.String(10))
    nm_l_zh = db.Column(db.Unicode(50), nullable=False)
    nm_l_en = db.Column(db.Unicode(50))
    nm_l_ja = db.Column(db.Unicode(50))
    pid = db.Column(db.Integer)
    lvl = db.Column(db.Integer)
    pth = db.Column(db.String(100))
    leafflg = db.Column(db.String(1))
    rmk = db.Column(db.Unicode(255))
    updby = db.Column(db.String(20))
    upddt = db.Column(db.DateTime)
    sta = db.Column(db.String(3), nullable=False)
    execflg = db.Column(db.String(1))
    nxtsta = db.Column(db.String(3))
    val1 = db.Column(db.String(50))
    val2 = db.Column(db.String(50))
    val3 = db.Column(db.String(50))


class BasLoc(db.Model):
    __tablename__ = 'bas_loc'

    id = db.Column(db.Integer, primary_key=True)
    cd = db.Column(db.String(20))
    deptid = db.Column(db.Integer)
    secondcd = db.Column(db.String(20), nullable=False)
    nm_l_zh = db.Column(db.Unicode(50), nullable=False)
    nm_l_en = db.Column(db.Unicode(50))
    nm_l_ja = db.Column(db.Unicode(50))
    pid = db.Column(db.Integer)
    lvl = db.Column(db.Integer)
    pth = db.Column(db.String(100))
    leafflg = db.Column(db.String(1), server_default=db.FetchedValue())
    waydsc = db.Column(db.Unicode(20))
    shelfdsc = db.Column(db.Unicode(20))
    mixflg = db.Column(db.String(1), server_default=db.FetchedValue())
    rmk = db.Column(db.Unicode(255))
    updby = db.Column(db.String(20))
    upddt = db.Column(db.DateTime)
    sta = db.Column(db.String(3), nullable=False)
    execflg = db.Column(db.String(1), server_default=db.FetchedValue())
    nxtsta = db.Column(db.String(3))


t_bas_majortax = db.Table(
    'bas_majortax',
    db.Column('id', db.Integer, nullable=False, index=True),
    db.Column('groupid', db.Integer),
    db.Column('catid', db.String(20)),
    db.Column('taxtp', db.String(1)),
    db.Column('tax', db.Numeric(18, 6)),
    db.Column('acccd', db.String(20)),
    db.Column('rmk', db.String(50)),
    db.Column('updby', db.String(50)),
    db.Column('upddt', db.DateTime),
    db.Column('sta', db.String(3), nullable=False),
    db.Column('execflg', db.String(1)),
    db.Column('nxtsta', db.String(3)),
    db.Column('etaxdesc', db.String(20))
)


t_bas_periodcfg = db.Table(
    'bas_periodcfg',
    db.Column('id', db.Integer, nullable=False),
    db.Column('tp', db.String(10), nullable=False),
    db.Column('colnm', db.String(30)),
    db.Column('stktp', db.String(20)),
    db.Column('billtp', db.String(20)),
    db.Column('iotp', db.String(10)),
    db.Column('rmk', db.Unicode(255)),
    db.Column('updby', db.String(20)),
    db.Column('upddt', db.DateTime),
    db.Column('sta', db.String(3), nullable=False),
    db.Column('tp1', db.String(10))
)


class BasPlubcd(db.Model):
    __tablename__ = 'bas_plubcd'

    id = db.Column(db.Integer, primary_key=True)
    pluid = db.Column(db.Integer, nullable=False)
    bcd = db.Column(db.String(50), nullable=False, server_default=db.FetchedValue())
    bcdtp = db.Column(db.String(20), nullable=False)
    primflg = db.Column(db.String(1))
    updby = db.Column(db.String(20))
    upddt = db.Column(db.DateTime)
    sta = db.Column(db.String(3), nullable=False)
    execflg = db.Column(db.String(1))
    nxtsta = db.Column(db.String(3))


t_bas_plucat_yulei = db.Table(
    'bas_plucat_yulei',
    db.Column('categoryname', db.String(150)),
    db.Column('itemcode', db.String(50))
)


class BasPlucosttpl(db.Model):
    __tablename__ = 'bas_plucosttpl'

    id = db.Column(db.Integer, primary_key=True)
    deptlktp = db.Column(db.String(10))
    deptlkid = db.Column(db.Integer)
    pluid = db.Column(db.Integer, nullable=False)
    ocrule = db.Column(db.String(10))
    ocprc = db.Column(db.Numeric(16, 4))
    icrule = db.Column(db.String(10))
    icprc = db.Column(db.Numeric(16, 4))
    crcd = db.Column(db.String(3))
    rmk = db.Column(db.Unicode(255))
    updby = db.Column(db.String(20))
    upddt = db.Column(db.DateTime)
    sta = db.Column(db.String(3), nullable=False)
    execflg = db.Column(db.String(1))
    nxtsta = db.Column(db.String(3))
    srctp = db.Column(db.String(1), server_default=db.FetchedValue())


class BasPludepttpl(db.Model):
    __tablename__ = 'bas_pludepttpl'

    id = db.Column(db.Integer, primary_key=True)
    deptlktp = db.Column(db.String(10))
    deptlkid = db.Column(db.Integer)
    pluid = db.Column(db.Integer, nullable=False)
    stkflg = db.Column(db.String(1), server_default=db.FetchedValue())
    bomtp = db.Column(db.String(10))
    dscflg = db.Column(db.String(1), server_default=db.FetchedValue())
    adjflg = db.Column(db.String(1), server_default=db.FetchedValue())
    invflg = db.Column(db.String(1), server_default=db.FetchedValue())
    upkflg = db.Column(db.String(1), server_default=db.FetchedValue())
    chkqtyflg = db.Column(db.String(1), server_default=db.FetchedValue())
    ivtcyctp = db.Column(db.String(10))
    advordrule = db.Column(db.String(10))
    tucyc = db.Column(db.String(10))
    saftqtyrule = db.Column(db.String(10))
    maxsaftqty = db.Column(db.Numeric(16, 6))
    minsaftqty = db.Column(db.Numeric(16, 6))
    lottp = db.Column(db.String(10))
    lotsta = db.Column(db.String(2))
    lotrule = db.Column(db.String(2))
    lotiorule = db.Column(db.String(2))
    lotexprule = db.Column(db.String(2))
    sld = db.Column(db.Integer)
    expd = db.Column(db.Integer)
    defd = db.Column(db.Integer)
    mld = db.Column(db.Integer)
    pld = db.Column(db.Integer)
    bld1 = db.Column(db.Integer)
    bld2 = db.Column(db.Integer)
    bld3 = db.Column(db.Integer)
    bld4 = db.Column(db.Integer)
    bld5 = db.Column(db.Integer)
    subcpyflg = db.Column(db.String(1), server_default=db.FetchedValue())
    stdt = db.Column(db.DateTime)
    eddt = db.Column(db.DateTime)
    rmk = db.Column(db.Unicode(255))
    updby = db.Column(db.String(20))
    upddt = db.Column(db.DateTime)
    sta = db.Column(db.String(3), nullable=False)
    execflg = db.Column(db.String(1), server_default=db.FetchedValue())
    nxtsta = db.Column(db.String(3))
    srctp = db.Column(db.String(1), server_default=db.FetchedValue())
    txfflg = db.Column(db.String(1), server_default=db.FetchedValue())


class BasPludlvtpl(db.Model):
    __tablename__ = 'bas_pludlvtpl'

    id = db.Column(db.Integer, primary_key=True)
    deptlktp = db.Column(db.String(10))
    deptlkid = db.Column(db.Integer, index=True)
    astp = db.Column(db.String(10))
    dlvtp = db.Column(db.String(10))
    dcid = db.Column(db.Integer)
    wcid = db.Column(db.Integer)
    venid = db.Column(db.Integer)
    plulktp = db.Column(db.String(10), index=True)
    plulkid = db.Column(db.String(10), nullable=False)
    ordflg = db.Column(db.String(1), server_default=db.FetchedValue())
    ordrqflg = db.Column(db.String(1), server_default=db.FetchedValue())
    ordmxflg = db.Column(db.String(1), server_default=db.FetchedValue())
    obilltp = db.Column(db.String(20))
    olntp = db.Column(db.String(2))
    osta = db.Column(db.String(3))
    ibilltp = db.Column(db.String(20))
    ilntp = db.Column(db.String(2))
    ista = db.Column(db.String(3))
    cycrule = db.Column(db.String(10))
    monflg = db.Column(db.String(1), server_default=db.FetchedValue())
    tuesflg = db.Column(db.String(1), server_default=db.FetchedValue())
    wedflg = db.Column(db.String(1), server_default=db.FetchedValue())
    thurflg = db.Column(db.String(1), server_default=db.FetchedValue())
    friflg = db.Column(db.String(1), server_default=db.FetchedValue())
    satflg = db.Column(db.String(1), server_default=db.FetchedValue())
    sunflg = db.Column(db.String(1), server_default=db.FetchedValue())
    cycday = db.Column(db.Integer)
    initorddt = db.Column(db.DateTime)
    uomcd = db.Column(db.String(6))
    incqty = db.Column(db.Numeric(16, 6))
    minqty = db.Column(db.Numeric(16, 6))
    maxqty = db.Column(db.Numeric(16, 6))
    snddays = db.Column(db.Integer)
    arvdays = db.Column(db.Integer)
    subcpyflg = db.Column(db.String(1), server_default=db.FetchedValue())
    stdt = db.Column(db.DateTime)
    eddt = db.Column(db.DateTime)
    rmk = db.Column(db.Unicode(255))
    updby = db.Column(db.String(20))
    upddt = db.Column(db.DateTime)
    sta = db.Column(db.String(3), nullable=False)
    execflg = db.Column(db.String(1), server_default=db.FetchedValue())
    nxtsta = db.Column(db.String(3))
    srctp = db.Column(db.String(1), server_default=db.FetchedValue())
    dlvflg = db.Column(db.String(1), server_default=db.FetchedValue())


class BasPlumain(db.Model):
    __tablename__ = 'bas_plumain'

    id = db.Column(db.Integer, primary_key=True)
    cd = db.Column(db.String(20), index=True)
    secondcd = db.Column(db.String(50))
    nm_l_zh = db.Column(db.Unicode(100), nullable=False)
    nm_l_ja = db.Column(db.Unicode(100))
    nm_l_en = db.Column(db.Unicode(100))
    snm_l_zh = db.Column(db.Unicode(100), nullable=False)
    snm_l_en = db.Column(db.Unicode(100))
    snm_l_ja = db.Column(db.Unicode(100))
    lnm_l_zh = db.Column(db.Unicode(100))
    lnm_l_en = db.Column(db.Unicode(100))
    lnm_l_ja = db.Column(db.Unicode(100))
    spec = db.Column(db.Unicode(30))
    plutp = db.Column(db.String(10))
    bomtp = db.Column(db.String(10))
    stkflg = db.Column(db.String(1), server_default=db.FetchedValue())
    storetp = db.Column(db.Unicode(10), nullable=False)
    plucatid = db.Column(db.Integer)
    pickcatid = db.Column(db.Integer)
    ordcatid = db.Column(db.Integer)
    salecatid = db.Column(db.Integer)
    catcd = db.Column(db.String(20))
    cat1cd = db.Column(db.String(20))
    cat2cd = db.Column(db.String(20))
    cat3cd = db.Column(db.String(20))
    cat4cd = db.Column(db.String(20))
    pkuomcd = db.Column(db.String(6), nullable=False)
    lntp = db.Column(db.String(2), nullable=False)
    daypart = db.Column(db.String(50))
    tastetp = db.Column(db.String(10))
    plusize = db.Column(db.String(20))
    smtscrcd = db.Column(db.String(20))
    disseq = db.Column(db.Integer)
    agrillflg = db.Column(db.String(1), server_default=db.FetchedValue())
    grillflg = db.Column(db.String(1), server_default=db.FetchedValue())
    nprngrillflg = db.Column(db.String(1), server_default=db.FetchedValue())
    kvsmfyflg = db.Column(db.String(1), server_default=db.FetchedValue())
    kvssumflg = db.Column(db.String(1), server_default=db.FetchedValue())
    kvsndvmflg = db.Column(db.String(1), server_default=db.FetchedValue())
    kvsmainflg = db.Column(db.String(1), server_default=db.FetchedValue())
    pkvsc = db.Column(db.String(20))
    pdc = db.Column(db.String(20))
    pbgn = db.Column(db.String(20))
    pbgp = db.Column(db.String(20))
    pfgn = db.Column(db.String(20))
    pfgp = db.Column(db.String(20))
    ptitle = db.Column(db.Unicode(50))
    rmdprio = db.Column(db.String(10))
    rmdtitle = db.Column(db.String(50))
    imgfilenm = db.Column(db.String(100))
    diswflg = db.Column(db.String(1), server_default=db.FetchedValue())
    mdfflg = db.Column(db.String(1), server_default=db.FetchedValue())
    purflg = db.Column(db.String(1), server_default=db.FetchedValue())
    saleflg = db.Column(db.String(1), server_default=db.FetchedValue())
    saleolflg = db.Column(db.String(1), server_default=db.FetchedValue())
    presaleflg = db.Column(db.String(1), server_default=db.FetchedValue())
    discflg = db.Column(db.String(1), server_default=db.FetchedValue())
    ordflg = db.Column(db.String(1), server_default=db.FetchedValue())
    ordrqflg = db.Column(db.String(1), server_default=db.FetchedValue())
    ordmxflg = db.Column(db.String(1), server_default=db.FetchedValue())
    dlvflg = db.Column(db.String(1), server_default=db.FetchedValue())
    adjflg = db.Column(db.String(1), server_default=db.FetchedValue())
    invflg = db.Column(db.String(1), server_default=db.FetchedValue())
    dscflg = db.Column(db.String(1), server_default=db.FetchedValue())
    upkflg = db.Column(db.String(1), server_default=db.FetchedValue())
    cpngcflg = db.Column(db.String(1), server_default=db.FetchedValue())
    chkqtyflg = db.Column(db.String(1), server_default=db.FetchedValue())
    ivtcyctp = db.Column(db.String(10))
    advordrule = db.Column(db.String(10))
    tucyc = db.Column(db.String(10))
    saftqtyrule = db.Column(db.String(10))
    minsaftqty = db.Column(db.Numeric(16, 6))
    maxsaftqty = db.Column(db.Numeric(16, 6))
    lottp = db.Column(db.String(10))
    lotsta = db.Column(db.String(2))
    lotrule = db.Column(db.String(2))
    lotiorule = db.Column(db.String(2))
    lotexprule = db.Column(db.String(2))
    sld = db.Column(db.Integer)
    expd = db.Column(db.Integer)
    defd = db.Column(db.Integer)
    mld = db.Column(db.Integer)
    pld = db.Column(db.Integer)
    bld1 = db.Column(db.Integer)
    bld2 = db.Column(db.Integer)
    bld3 = db.Column(db.Integer)
    bld4 = db.Column(db.Integer)
    bld5 = db.Column(db.Integer)
    cpncrtp = db.Column(db.String(10))
    cpnmd = db.Column(db.String(10))
    cpntp = db.Column(db.String(10))
    exattr1 = db.Column(db.String(100))
    exattr2 = db.Column(db.String(100))
    exattr3 = db.Column(db.String(100))
    exattr4 = db.Column(db.String(100))
    exattr5 = db.Column(db.String(100))
    exattr6 = db.Column(db.String(100))
    exattr7 = db.Column(db.String(100))
    exattr8 = db.Column(db.String(100))
    exattr9 = db.Column(db.String(100))
    exattr10 = db.Column(db.String(100))
    exattr11 = db.Column(db.String(100))
    exattr12 = db.Column(db.String(100))
    exattr13 = db.Column(db.String(100))
    exattr14 = db.Column(db.String(100))
    exattr15 = db.Column(db.String(100))
    exattr16 = db.Column(db.String(100))
    exattr17 = db.Column(db.String(100))
    exattr18 = db.Column(db.String(100))
    exattr19 = db.Column(db.String(100))
    exattr20 = db.Column(db.String(100))
    exattr21 = db.Column(db.String(100))
    exattr22 = db.Column(db.String(100))
    exattr23 = db.Column(db.String(100))
    exattr24 = db.Column(db.String(100))
    exattr25 = db.Column(db.String(100))
    exattr26 = db.Column(db.String(100))
    exattr27 = db.Column(db.String(100))
    exattr28 = db.Column(db.String(100))
    exattr29 = db.Column(db.String(100))
    exattr30 = db.Column(db.String(100))
    rmk = db.Column(db.Unicode(255))
    updby = db.Column(db.String(20))
    upddt = db.Column(db.DateTime)
    sta = db.Column(db.String(3), nullable=False)
    execflg = db.Column(db.String(1))
    nxtsta = db.Column(db.String(3))
    brand = db.Column(db.String(20))
    matflg = db.Column(db.String(1), server_default=db.FetchedValue())
    plugrd = db.Column(db.String(20))
    taxtp = db.Column(db.String(10))
    addtxflg = db.Column(db.String(1), server_default=db.FetchedValue())
    cpncat = db.Column(db.String(20))
    cacctcd = db.Column(db.String(20))


t_bas_plumain_bak = db.Table(
    'bas_plumain_bak',
    db.Column('id', db.Integer, nullable=False),
    db.Column('cd', db.String(20)),
    db.Column('secondcd', db.String(50)),
    db.Column('nm_l_zh', db.Unicode(100), nullable=False),
    db.Column('nm_l_ja', db.Unicode(100)),
    db.Column('nm_l_en', db.Unicode(100)),
    db.Column('snm_l_zh', db.Unicode(100), nullable=False),
    db.Column('snm_l_en', db.Unicode(100)),
    db.Column('snm_l_ja', db.Unicode(100)),
    db.Column('lnm_l_zh', db.Unicode(100)),
    db.Column('lnm_l_en', db.Unicode(100)),
    db.Column('lnm_l_ja', db.Unicode(100)),
    db.Column('spec', db.Unicode(30)),
    db.Column('plutp', db.String(10)),
    db.Column('bomtp', db.String(10)),
    db.Column('stkflg', db.String(1)),
    db.Column('storetp', db.Unicode(10), nullable=False),
    db.Column('plucatid', db.Integer),
    db.Column('pickcatid', db.Integer),
    db.Column('ordcatid', db.Integer),
    db.Column('salecatid', db.Integer),
    db.Column('catcd', db.String(20)),
    db.Column('cat1cd', db.String(20)),
    db.Column('cat2cd', db.String(20)),
    db.Column('cat3cd', db.String(20)),
    db.Column('cat4cd', db.String(20)),
    db.Column('pkuomcd', db.String(6), nullable=False),
    db.Column('lntp', db.String(2), nullable=False),
    db.Column('daypart', db.String(50)),
    db.Column('tastetp', db.String(10)),
    db.Column('plusize', db.String(20)),
    db.Column('smtscrcd', db.String(20)),
    db.Column('disseq', db.Integer),
    db.Column('agrillflg', db.String(1)),
    db.Column('grillflg', db.String(1)),
    db.Column('nprngrillflg', db.String(1)),
    db.Column('kvsmfyflg', db.String(1)),
    db.Column('kvssumflg', db.String(1)),
    db.Column('kvsndvmflg', db.String(1)),
    db.Column('kvsmainflg', db.String(1)),
    db.Column('pkvsc', db.String(20)),
    db.Column('pdc', db.String(20)),
    db.Column('pbgn', db.String(20)),
    db.Column('pbgp', db.String(20)),
    db.Column('pfgn', db.String(20)),
    db.Column('pfgp', db.String(20)),
    db.Column('ptitle', db.Unicode(50)),
    db.Column('rmdprio', db.String(10)),
    db.Column('rmdtitle', db.String(50)),
    db.Column('imgfilenm', db.String(100)),
    db.Column('diswflg', db.String(1)),
    db.Column('mdfflg', db.String(1)),
    db.Column('purflg', db.String(1)),
    db.Column('saleflg', db.String(1)),
    db.Column('saleolflg', db.String(1)),
    db.Column('presaleflg', db.String(1)),
    db.Column('discflg', db.String(1)),
    db.Column('ordflg', db.String(1)),
    db.Column('ordrqflg', db.String(1)),
    db.Column('ordmxflg', db.String(1)),
    db.Column('dlvflg', db.String(1)),
    db.Column('adjflg', db.String(1)),
    db.Column('invflg', db.String(1)),
    db.Column('dscflg', db.String(1)),
    db.Column('upkflg', db.String(1)),
    db.Column('cpngcflg', db.String(1)),
    db.Column('chkqtyflg', db.String(1)),
    db.Column('ivtcyctp', db.String(10)),
    db.Column('advordrule', db.String(10)),
    db.Column('tucyc', db.String(10)),
    db.Column('saftqtyrule', db.String(10)),
    db.Column('minsaftqty', db.Numeric(16, 6)),
    db.Column('maxsaftqty', db.Numeric(16, 6)),
    db.Column('lottp', db.String(10)),
    db.Column('lotsta', db.String(2)),
    db.Column('lotrule', db.String(2)),
    db.Column('lotiorule', db.String(2)),
    db.Column('lotexprule', db.String(2)),
    db.Column('sld', db.Integer),
    db.Column('expd', db.Integer),
    db.Column('defd', db.Integer),
    db.Column('mld', db.Integer),
    db.Column('pld', db.Integer),
    db.Column('bld1', db.Integer),
    db.Column('bld2', db.Integer),
    db.Column('bld3', db.Integer),
    db.Column('bld4', db.Integer),
    db.Column('bld5', db.Integer),
    db.Column('cpncrtp', db.String(10)),
    db.Column('cpnmd', db.String(10)),
    db.Column('cpntp', db.String(10)),
    db.Column('exattr1', db.String(100)),
    db.Column('exattr2', db.String(100)),
    db.Column('exattr3', db.String(100)),
    db.Column('exattr4', db.String(100)),
    db.Column('exattr5', db.String(100)),
    db.Column('exattr6', db.String(100)),
    db.Column('exattr7', db.String(100)),
    db.Column('exattr8', db.String(100)),
    db.Column('exattr9', db.String(100)),
    db.Column('exattr10', db.String(100)),
    db.Column('exattr11', db.String(100)),
    db.Column('exattr12', db.String(100)),
    db.Column('exattr13', db.String(100)),
    db.Column('exattr14', db.String(100)),
    db.Column('exattr15', db.String(100)),
    db.Column('exattr16', db.String(100)),
    db.Column('exattr17', db.String(100)),
    db.Column('exattr18', db.String(100)),
    db.Column('exattr19', db.String(100)),
    db.Column('exattr20', db.String(100)),
    db.Column('exattr21', db.String(100)),
    db.Column('exattr22', db.String(100)),
    db.Column('exattr23', db.String(100)),
    db.Column('exattr24', db.String(100)),
    db.Column('exattr25', db.String(100)),
    db.Column('exattr26', db.String(100)),
    db.Column('exattr27', db.String(100)),
    db.Column('exattr28', db.String(100)),
    db.Column('exattr29', db.String(100)),
    db.Column('exattr30', db.String(100)),
    db.Column('rmk', db.Unicode(255)),
    db.Column('updby', db.String(20)),
    db.Column('upddt', db.DateTime),
    db.Column('sta', db.String(3), nullable=False),
    db.Column('execflg', db.String(1)),
    db.Column('nxtsta', db.String(3)),
    db.Column('brand', db.String(20)),
    db.Column('matflg', db.String(1)),
    db.Column('plugrd', db.String(20)),
    db.Column('taxtp', db.String(10)),
    db.Column('addtxflg', db.String(1)),
    db.Column('cpncat', db.String(20)),
    db.Column('cacctcd', db.String(20))
)


t_bas_plumain_temp_min = db.Table(
    'bas_plumain_temp_min',
    db.Column('id', db.Integer),
    db.Column('cd', db.String(20)),
    db.Column('secondcd', db.String(50)),
    db.Column('nm_l_zh', db.Unicode(100)),
    db.Column('nm_l_ja', db.Unicode(100)),
    db.Column('nm_l_en', db.Unicode(100)),
    db.Column('snm_l_zh', db.Unicode(100)),
    db.Column('snm_l_en', db.Unicode(100)),
    db.Column('snm_l_ja', db.Unicode(100)),
    db.Column('lnm_l_zh', db.Unicode(100)),
    db.Column('lnm_l_en', db.Unicode(100)),
    db.Column('lnm_l_ja', db.Unicode(100)),
    db.Column('spec', db.Unicode(30)),
    db.Column('plutp', db.String(10)),
    db.Column('bomtp', db.String(10)),
    db.Column('stkflg', db.String(1)),
    db.Column('storetp', db.Unicode(10)),
    db.Column('plucatid', db.Integer),
    db.Column('pickcatid', db.Integer),
    db.Column('ordcatid', db.Integer),
    db.Column('salecatid', db.Integer),
    db.Column('catcd', db.String(20)),
    db.Column('cat1cd', db.String(20)),
    db.Column('cat2cd', db.String(20)),
    db.Column('cat3cd', db.String(20)),
    db.Column('cat4cd', db.String(20)),
    db.Column('pkuomcd', db.String(6)),
    db.Column('lntp', db.String(2)),
    db.Column('daypart', db.String(50)),
    db.Column('tastetp', db.String(10)),
    db.Column('plusize', db.String(20)),
    db.Column('smtscrcd', db.String(20)),
    db.Column('disseq', db.Integer),
    db.Column('agrillflg', db.String(1)),
    db.Column('grillflg', db.String(1)),
    db.Column('nprngrillflg', db.String(1)),
    db.Column('kvsmfyflg', db.String(1)),
    db.Column('kvssumflg', db.String(1)),
    db.Column('kvsndvmflg', db.String(1)),
    db.Column('kvsmainflg', db.String(1)),
    db.Column('pkvsc', db.String(20)),
    db.Column('pdc', db.String(20)),
    db.Column('pbgn', db.String(20)),
    db.Column('pbgp', db.String(20)),
    db.Column('pfgn', db.String(20)),
    db.Column('pfgp', db.String(20)),
    db.Column('ptitle', db.Unicode(50)),
    db.Column('rmdprio', db.String(10)),
    db.Column('rmdtitle', db.String(50)),
    db.Column('imgfilenm', db.String(100)),
    db.Column('diswflg', db.String(1)),
    db.Column('mdfflg', db.String(1)),
    db.Column('purflg', db.String(1)),
    db.Column('saleflg', db.String(1)),
    db.Column('saleolflg', db.String(1)),
    db.Column('presaleflg', db.String(1)),
    db.Column('discflg', db.String(1)),
    db.Column('ordflg', db.String(1)),
    db.Column('ordrqflg', db.String(1)),
    db.Column('ordmxflg', db.String(1)),
    db.Column('dlvflg', db.String(1)),
    db.Column('adjflg', db.String(1)),
    db.Column('invflg', db.String(1)),
    db.Column('dscflg', db.String(1)),
    db.Column('upkflg', db.String(1)),
    db.Column('cpngcflg', db.String(1)),
    db.Column('chkqtyflg', db.String(1)),
    db.Column('ivtcyctp', db.String(10)),
    db.Column('advordrule', db.String(10)),
    db.Column('tucyc', db.String(10)),
    db.Column('saftqtyrule', db.String(10)),
    db.Column('minsaftqty', db.Numeric(16, 6)),
    db.Column('maxsaftqty', db.Numeric(16, 6)),
    db.Column('lottp', db.String(10)),
    db.Column('lotsta', db.String(2)),
    db.Column('lotrule', db.String(2)),
    db.Column('lotiorule', db.String(2)),
    db.Column('lotexprule', db.String(2)),
    db.Column('sld', db.Integer),
    db.Column('expd', db.Integer),
    db.Column('defd', db.Integer),
    db.Column('mld', db.Integer),
    db.Column('pld', db.Integer),
    db.Column('bld1', db.Integer),
    db.Column('bld2', db.Integer),
    db.Column('bld3', db.Integer),
    db.Column('bld4', db.Integer),
    db.Column('bld5', db.Integer),
    db.Column('cpncrtp', db.String(10)),
    db.Column('cpnmd', db.String(10)),
    db.Column('cpntp', db.String(10)),
    db.Column('exattr1', db.String(100)),
    db.Column('exattr2', db.String(100)),
    db.Column('exattr3', db.String(100)),
    db.Column('exattr4', db.String(100)),
    db.Column('exattr5', db.String(100)),
    db.Column('exattr6', db.String(100)),
    db.Column('exattr7', db.String(100)),
    db.Column('exattr8', db.String(100)),
    db.Column('exattr9', db.String(100)),
    db.Column('exattr10', db.String(100)),
    db.Column('exattr11', db.String(100)),
    db.Column('exattr12', db.String(100)),
    db.Column('exattr13', db.String(100)),
    db.Column('exattr14', db.String(100)),
    db.Column('exattr15', db.String(100)),
    db.Column('exattr16', db.String(100)),
    db.Column('exattr17', db.String(100)),
    db.Column('exattr18', db.String(100)),
    db.Column('exattr19', db.String(100)),
    db.Column('exattr20', db.String(100)),
    db.Column('exattr21', db.String(100)),
    db.Column('exattr22', db.String(100)),
    db.Column('exattr23', db.String(100)),
    db.Column('exattr24', db.String(100)),
    db.Column('exattr25', db.String(100)),
    db.Column('exattr26', db.String(100)),
    db.Column('exattr27', db.String(100)),
    db.Column('exattr28', db.String(100)),
    db.Column('exattr29', db.String(100)),
    db.Column('exattr30', db.String(100)),
    db.Column('rmk', db.Unicode(255)),
    db.Column('updby', db.String(20)),
    db.Column('upddt', db.DateTime),
    db.Column('sta', db.String(3)),
    db.Column('execflg', db.String(1)),
    db.Column('nxtsta', db.String(3)),
    db.Column('brand', db.String(20)),
    db.Column('matflg', db.String(1)),
    db.Column('plugrd', db.String(20)),
    db.Column('taxtp', db.String(10)),
    db.Column('addtxflg', db.String(1)),
    db.Column('cpncat', db.String(20)),
    db.Column('cacctcd', db.String(20))
)


class BasPlumkttpl(db.Model):
    __tablename__ = 'bas_plumkttpl'

    id = db.Column(db.Integer, primary_key=True)
    prctp = db.Column(db.String(10))
    salelktp = db.Column(db.String(10))
    salelkid = db.Column(db.Integer)
    buylktp = db.Column(db.String(10))
    buylkid = db.Column(db.Integer)
    pluid = db.Column(db.Integer, nullable=False)
    uomcd = db.Column(db.String(6))
    saleflg = db.Column(db.String(1), server_default=db.FetchedValue())
    saleolflg = db.Column(db.String(1), server_default=db.FetchedValue())
    presaleflg = db.Column(db.String(1), server_default=db.FetchedValue())
    prcrule = db.Column(db.String(10))
    prcrt = db.Column(db.Numeric(6, 2))
    prc = db.Column(db.Numeric(16, 4))
    taxrtcd = db.Column(db.String(20))
    taxrt = db.Column(db.Numeric(6, 2))
    eprc = db.Column(db.Numeric(16, 4))
    etaxrtcd = db.Column(db.String(20))
    etaxrt = db.Column(db.Numeric(6, 2))
    tprc = db.Column(db.Numeric(16, 4))
    ttaxrtcd = db.Column(db.String(20))
    ttaxrt = db.Column(db.Numeric(6, 2))
    oprc = db.Column(db.Numeric(16, 4))
    otaxrtcd = db.Column(db.String(20))
    otaxrt = db.Column(db.Numeric(6, 2))
    sprc = db.Column(db.Numeric(16, 4))
    staxrtcd = db.Column(db.String(20))
    staxrt = db.Column(db.Numeric(6, 2))
    crcd = db.Column(db.String(3))
    subcpyflg = db.Column(db.String(1), server_default=db.FetchedValue())
    stdt = db.Column(db.DateTime)
    eddt = db.Column(db.DateTime)
    rmk = db.Column(db.Unicode(255))
    updby = db.Column(db.String(20))
    upddt = db.Column(db.DateTime)
    sta = db.Column(db.String(3), nullable=False)
    execflg = db.Column(db.String(1), server_default=db.FetchedValue())
    nxtsta = db.Column(db.String(3))
    srctp = db.Column(db.String(1), server_default=db.FetchedValue())


class BasPlupotpl(db.Model):
    __tablename__ = 'bas_plupotpl'
    __table_args__ = (
        db.Index('idx_bas_pluoptpl_1', 'deptlkid', 'pluid', 'venid', 'deptlktp'),
    )

    id = db.Column(db.Integer, primary_key=True)
    deptlktp = db.Column(db.String(10))
    deptlkid = db.Column(db.Integer)
    venid = db.Column(db.Integer)
    pluid = db.Column(db.Integer, nullable=False)
    uomcd = db.Column(db.String(6))
    purflg = db.Column(db.String(1), server_default=db.FetchedValue())
    prc = db.Column(db.Numeric(18, 6))
    taxrt = db.Column(db.Numeric(6, 2))
    crcd = db.Column(db.String(3))
    primflg = db.Column(db.String(1), server_default=db.FetchedValue())
    subcpyflg = db.Column(db.String(1), server_default=db.FetchedValue())
    stdt = db.Column(db.DateTime)
    eddt = db.Column(db.DateTime)
    rmk = db.Column(db.Unicode(255))
    updby = db.Column(db.String(20))
    upddt = db.Column(db.DateTime)
    sta = db.Column(db.String(3), nullable=False)
    execflg = db.Column(db.String(1), server_default=db.FetchedValue())
    nxtsta = db.Column(db.String(3))
    srctp = db.Column(db.String(1), server_default=db.FetchedValue())
    mdfflg = db.Column(db.String(1), server_default=db.FetchedValue())


t_bas_plupotpl_bak = db.Table(
    'bas_plupotpl_bak',
    db.Column('id', db.Integer, nullable=False),
    db.Column('deptlktp', db.String(10)),
    db.Column('deptlkid', db.Integer),
    db.Column('venid', db.Integer),
    db.Column('pluid', db.Integer, nullable=False),
    db.Column('uomcd', db.String(6)),
    db.Column('purflg', db.String(1)),
    db.Column('prc', db.Numeric(18, 6)),
    db.Column('taxrt', db.Numeric(6, 2)),
    db.Column('crcd', db.String(3)),
    db.Column('primflg', db.String(1)),
    db.Column('subcpyflg', db.String(1)),
    db.Column('stdt', db.DateTime),
    db.Column('eddt', db.DateTime),
    db.Column('rmk', db.Unicode(255)),
    db.Column('updby', db.String(20)),
    db.Column('upddt', db.DateTime),
    db.Column('sta', db.String(3), nullable=False),
    db.Column('execflg', db.String(1)),
    db.Column('nxtsta', db.String(3)),
    db.Column('srctp', db.String(1)),
    db.Column('mdfflg', db.String(1))
)


class BasPluprptpl(db.Model):
    __tablename__ = 'bas_pluprptpl'

    id = db.Column(db.Integer, primary_key=True)
    deptlktp = db.Column(db.String(10))
    deptlkid = db.Column(db.Integer)
    plulktp = db.Column(db.String(10))
    plulkid = db.Column(db.String(10), nullable=False)
    uomcd = db.Column(db.String(6))
    arvdays = db.Column(db.Integer)
    stdt = db.Column(db.DateTime)
    eddt = db.Column(db.DateTime)
    rmk = db.Column(db.Unicode(255))
    updby = db.Column(db.String(20))
    upddt = db.Column(db.DateTime)
    sta = db.Column(db.String(3), nullable=False)
    execflg = db.Column(db.String(1))
    nxtsta = db.Column(db.String(3))


class BasPluquota(db.Model):
    __tablename__ = 'bas_pluquota'

    pid = db.Column(db.String(50), primary_key=True, server_default=db.FetchedValue())
    plu_id = db.Column(db.String(50))
    total_inventory = db.Column(db.Numeric(asdecimal=False), nullable=False, server_default=db.FetchedValue())
    mon_qty = db.Column(db.Numeric(asdecimal=False), nullable=False)
    tue_qty = db.Column(db.Numeric(asdecimal=False), nullable=False)
    wed_qty = db.Column(db.Numeric(asdecimal=False), nullable=False)
    thu_qty = db.Column(db.Numeric(asdecimal=False), nullable=False)
    fri_qty = db.Column(db.Numeric(asdecimal=False), nullable=False)
    sat_qty = db.Column(db.Numeric(asdecimal=False), nullable=False)
    sun_qty = db.Column(db.Numeric(asdecimal=False), nullable=False)
    is_delete = db.Column(db.String(1), nullable=False, server_default=db.FetchedValue())
    remark = db.Column(db.String(255))
    update_date = db.Column(db.DateTime, server_default=db.FetchedValue())
    update_by = db.Column(db.String(50))
    pre_date = db.Column(db.Numeric(asdecimal=False), nullable=False, server_default=db.FetchedValue())
    create_date = db.Column(db.DateTime)
    create_by = db.Column(db.String(50))
    plucd = db.Column(db.String(20))


class BasPlutax(db.Model):
    __tablename__ = 'bas_plutax'

    id = db.Column(db.Integer, primary_key=True)
    taxrule = db.Column(db.String(10), nullable=False)
    caltp = db.Column(db.String(10))
    plulktp = db.Column(db.String(10), nullable=False)
    plulkid = db.Column(db.Integer, nullable=False)
    salemtd = db.Column(db.String(10))
    taxtp = db.Column(db.String(10), nullable=False)
    taxrt = db.Column(db.Numeric(12, 4), nullable=False)
    updby = db.Column(db.String(20))
    upddt = db.Column(db.DateTime)
    sta = db.Column(db.String(3), nullable=False)
    execflg = db.Column(db.String(1))
    nxtsta = db.Column(db.String(3))


class BasPluuom(db.Model):
    __tablename__ = 'bas_pluuom'

    id = db.Column(db.Integer, primary_key=True)
    pluid = db.Column(db.Integer)
    srcuomcd = db.Column(db.String(6))
    cnvtrt = db.Column(db.Numeric(14, 7))
    trguomcd = db.Column(db.String(6))
    revcnvtrt = db.Column(db.Numeric(14, 7))
    pkuomcd = db.Column(db.String(6))
    cnvtpkrt = db.Column(db.Numeric(14, 7))
    dftpoflg = db.Column(db.String(1), server_default=db.FetchedValue())
    dftsalflg = db.Column(db.String(1), server_default=db.FetchedValue())
    dftdlvflg = db.Column(db.String(1), server_default=db.FetchedValue())
    dftwoflg = db.Column(db.String(1), server_default=db.FetchedValue())
    dftmiflg = db.Column(db.String(1), server_default=db.FetchedValue())
    dftivtflg = db.Column(db.String(1), server_default=db.FetchedValue())
    dftivtstflg = db.Column(db.String(1), server_default=db.FetchedValue())
    rmk = db.Column(db.Unicode(255))
    updby = db.Column(db.String(20))
    upddt = db.Column(db.DateTime)
    sta = db.Column(db.String(3))
    execflg = db.Column(db.String(1), server_default=db.FetchedValue())
    nxtsta = db.Column(db.String(3))


class BasPromodtl(db.Model):
    __tablename__ = 'bas_promodtl'

    pid = db.Column(db.String(50), primary_key=True)
    promomst_id = db.Column(db.String(50), nullable=False)
    plu_id = db.Column(db.String(50), nullable=False)
    is_homedelivery = db.Column(db.String(1), nullable=False, server_default=db.FetchedValue())
    is_discount = db.Column(db.String(1), nullable=False, server_default=db.FetchedValue())
    discount_code = db.Column(db.String(50))
    purchase_limit = db.Column(db.Numeric(asdecimal=False), nullable=False)
    max_number = db.Column(db.Numeric(asdecimal=False), nullable=False)
    is_delete = db.Column(db.String(1), nullable=False, server_default=db.FetchedValue())
    remark = db.Column(db.String(255))
    update_date = db.Column(db.DateTime, server_default=db.FetchedValue())
    update_by = db.Column(db.String(50))
    create_date = db.Column(db.DateTime, server_default=db.FetchedValue())
    create_by = db.Column(db.String(50))
    online_qty = db.Column(db.Numeric(asdecimal=False))
    online_qty_real = db.Column(db.Numeric(asdecimal=False))
    online_qty_last = db.Column(db.Numeric(asdecimal=False))
    online_qty_time = db.Column(db.Numeric(asdecimal=False))
    plucd = db.Column(db.String(20))


class BasPromomst(db.Model):
    __tablename__ = 'bas_promomst'

    pid = db.Column(db.String(50), primary_key=True)
    events_no = db.Column(db.String(20), nullable=False)
    events_name = db.Column(db.String(40), nullable=False)
    events_remark = db.Column(db.String(100))
    events_startdate = db.Column(db.DateTime, nullable=False)
    events_endtdate = db.Column(db.DateTime, nullable=False)
    events_attribute = db.Column(db.String(1), server_default=db.FetchedValue())
    status = db.Column(db.String(1), nullable=False, server_default=db.FetchedValue())
    is_delete = db.Column(db.String(1), nullable=False, server_default=db.FetchedValue())
    remark = db.Column(db.String(255))
    update_date = db.Column(db.DateTime)
    update_by = db.Column(db.String(50))
    create_date = db.Column(db.DateTime)
    create_by = db.Column(db.String(50))


class BasPt(db.Model):
    __tablename__ = 'bas_pt'

    id = db.Column(db.Integer, primary_key=True)
    coid = db.Column(db.Integer)
    yearno = db.Column(db.Integer)
    monthno = db.Column(db.Integer)
    ptdsc = db.Column(db.String(50))
    finstdt = db.Column(db.DateTime)
    fineddt = db.Column(db.DateTime)
    stkstdt = db.Column(db.DateTime)
    stkeddt = db.Column(db.DateTime)
    exattr1 = db.Column(db.String(100))
    exattr2 = db.Column(db.String(100))
    exattr3 = db.Column(db.String(100))
    exattr4 = db.Column(db.String(100))
    exattr5 = db.Column(db.String(100))
    exattr6 = db.Column(db.String(100))
    rmk = db.Column(db.String(100))
    updby = db.Column(db.String(20))
    upddt = db.Column(db.DateTime)
    sta = db.Column(db.String(3))
    nxtsta = db.Column(db.String(3))
    execflg = db.Column(db.String(1))
    costdt = db.Column(db.DateTime)


class BasQofk(db.Model):
    __tablename__ = 'bas_qofk'

    id = db.Column(db.Integer, primary_key=True)
    deptid = db.Column(db.Integer, nullable=False)
    pluid = db.Column(db.Integer, nullable=False)
    mkdt = db.Column(db.DateTime)
    stdt = db.Column(db.DateTime)
    eddt = db.Column(db.DateTime)
    advordrule = db.Column(db.String(10))
    tucyc = db.Column(db.String(10))
    saleamt = db.Column(db.Numeric(16, 2))
    useqty = db.Column(db.Numeric(16, 6))
    qty = db.Column(db.Numeric(16, 6), nullable=False)
    uomcd = db.Column(db.String(6), nullable=False)
    rmk = db.Column(db.Unicode(255))
    updby = db.Column(db.String(20))
    upddt = db.Column(db.DateTime)
    sta = db.Column(db.String(3), nullable=False)
    execflg = db.Column(db.String(1))
    nxtsta = db.Column(db.String(3))


class BasSaletarget(db.Model):
    __tablename__ = 'bas_saletarget'

    id = db.Column(db.Integer, primary_key=True)
    deptid = db.Column(db.Integer, nullable=False)
    tp = db.Column(db.String(10))
    fcstdt = db.Column(db.DateTime, nullable=False)
    fcstamt = db.Column(db.Numeric(16, 2), nullable=False)
    saftamt = db.Column(db.Numeric(16, 2))
    week = db.Column(db.String(3))
    rmk = db.Column(db.Unicode(255))
    updby = db.Column(db.String(20))
    upddt = db.Column(db.DateTime)
    sta = db.Column(db.String(3), nullable=False)
    execflg = db.Column(db.String(1))
    nxtsta = db.Column(db.String(3))


class BasVendor(db.Model):
    __tablename__ = 'bas_vendor'

    id = db.Column(db.Integer, primary_key=True)
    cd = db.Column(db.String(20))
    secondcd = db.Column(db.String(50))
    nm_l_zh = db.Column(db.Unicode(50), nullable=False)
    nm_l_en = db.Column(db.Unicode(50))
    nm_l_ja = db.Column(db.Unicode(50))
    snm = db.Column(db.Unicode(30))
    ltrhdr = db.Column(db.Unicode(50), nullable=False)
    taxcd = db.Column(db.String(50))
    bizcd = db.Column(db.Unicode(50))
    cp = db.Column(db.Unicode(30))
    lr = db.Column(db.Unicode(30))
    invaddr = db.Column(db.Unicode(100))
    invzipcd = db.Column(db.String(20))
    coaddr = db.Column(db.Unicode(100))
    cozipcd = db.Column(db.String(20))
    country = db.Column(db.Unicode(20))
    province = db.Column(db.Unicode(20))
    city = db.Column(db.Unicode(20))
    officefax = db.Column(db.String(30))
    officetel = db.Column(db.String(30))
    email = db.Column(db.String(50))
    dlvflg = db.Column(db.String(1), server_default=db.FetchedValue())
    fpflg = db.Column(db.String(1), server_default=db.FetchedValue())
    fcflg = db.Column(db.String(1), server_default=db.FetchedValue())
    crcd = db.Column(db.String(20))
    taxpty = db.Column(db.String(20))
    taxa = db.Column(db.String(60))
    taxrt = db.Column(db.Numeric(6, 2))
    banknm = db.Column(db.Unicode(50))
    bankaccount = db.Column(db.String(30))
    aprule = db.Column(db.String(10))
    aptp = db.Column(db.String(10))
    aldnum = db.Column(db.Integer)
    aednum = db.Column(db.Integer)
    rmk = db.Column(db.Unicode(255))
    updby = db.Column(db.String(20))
    upddt = db.Column(db.DateTime)
    sta = db.Column(db.String(3), nullable=False)
    execflg = db.Column(db.String(1), server_default=db.FetchedValue())
    nxtsta = db.Column(db.String(3))
    dlvinvflg = db.Column(db.String(1), server_default=db.FetchedValue())
    stdt = db.Column(db.DateTime)
    eddt = db.Column(db.DateTime)
    exattr1 = db.Column(db.String(20))
    exattr2 = db.Column(db.String(20))


class BasVenplu(db.Model):
    __tablename__ = 'bas_venplu'

    id = db.Column(db.Integer, primary_key=True)
    venid = db.Column(db.Integer)
    plulktp = db.Column(db.String(10))
    plulkid = db.Column(db.Integer)
    alwqtyrt = db.Column(db.Numeric(7, 2))
    alwqty = db.Column(db.Numeric(16, 6))
    mfcnm = db.Column(db.Unicode(50))
    ldnum = db.Column(db.Integer)
    rmk = db.Column(db.Unicode(255))
    updby = db.Column(db.String(20))
    upddt = db.Column(db.DateTime)
    sta = db.Column(db.String(3))
    execflg = db.Column(db.String(1))
    nxtsta = db.Column(db.String(3))


t_bb20160816 = db.Table(
    'bb20160816',
    db.Column('inttransnum', db.Numeric(20, 0, asdecimal=False))
)


t_bbb5 = db.Table(
    'bbb5',
    db.Column('inttransnum', db.Numeric(20, 0, asdecimal=False))
)


class CdAreacodeView(db.Model):
    __tablename__ = 'cd_areacode_view'

    areano = db.Column(db.String(20), primary_key=True)
    areaname = db.Column(db.String(50), nullable=False)
    parentareano = db.Column(db.String(20))
    areatype = db.Column(db.String(20), nullable=False)
    updatedate = db.Column(db.DateTime, nullable=False)


class CdCupcodeView(db.Model):
    __tablename__ = 'cd_cupcode_view'

    cupsizeno = db.Column(db.String(2), primary_key=True)
    cupname = db.Column(db.String(50))
    cupshortname = db.Column(db.String(30))
    cupenname = db.Column(db.String(50))
    updatedate = db.Column(db.DateTime, nullable=False)


class CdItemcategorycodeView(db.Model):
    __tablename__ = 'cd_itemcategorycode_view'

    categoryno = db.Column(db.String(10), primary_key=True)
    categoryname = db.Column(db.String(50))
    itemscopetype = db.Column(db.String(1))
    parentcategoryno = db.Column(db.String(10))
    updatedate = db.Column(db.DateTime, nullable=False)


class CdReasoncodeView(db.Model):
    __tablename__ = 'cd_reasoncode_view'

    reasonno = db.Column(db.String(20), primary_key=True)
    reasonname = db.Column(db.String(30))
    reasonrmk = db.Column(db.String(255))
    reasontype = db.Column(db.String(30), server_default=db.FetchedValue())
    updatedate = db.Column(db.DateTime, nullable=False)


class CdReasontypeView(db.Model):
    __tablename__ = 'cd_reasontype_view'

    reasonno = db.Column(db.String(10), primary_key=True, nullable=False)
    scopetype = db.Column(db.String(1), nullable=False, server_default=db.FetchedValue())
    scopeno = db.Column(db.String(20), primary_key=True, nullable=False)
    isinclude = db.Column(db.String(1), nullable=False, server_default=db.FetchedValue())
    updatedate = db.Column(db.DateTime, nullable=False)


t_cop_bomrpl = db.Table(
    'cop_bomrpl',
    db.Column('id', db.Integer),
    db.Column('billcd', db.Numeric(10, 0, asdecimal=False)),
    db.Column('deptlktp', db.String(10)),
    db.Column('odeptlkid', db.Integer),
    db.Column('ndeptlkid', db.Integer),
    db.Column('plvaldt', db.DateTime),
    db.Column('rlvaldt', db.DateTime),
    db.Column('rplrule', db.String(10)),
    db.Column('rmk', db.Unicode(255)),
    db.Column('updby', db.String(20)),
    db.Column('upddt', db.DateTime),
    db.Column('sta', db.String(3)),
    db.Column('execflg', db.String(1)),
    db.Column('nxtsta', db.String(3))
)


t_cop_bomrpldtl = db.Table(
    'cop_bomrpldtl',
    db.Column('id', db.Integer),
    db.Column('bomrplid', db.Integer),
    db.Column('bomiotp', db.String(10)),
    db.Column('opluid', db.Integer),
    db.Column('npluid', db.Integer),
    db.Column('rmk', db.Unicode(255)),
    db.Column('updby', db.String(20)),
    db.Column('upddt', db.DateTime),
    db.Column('sta', db.String(3)),
    db.Column('execflg', db.String(1)),
    db.Column('nxtsta', db.String(3))
)


t_cop_bomrplpladtl = db.Table(
    'cop_bomrplpladtl',
    db.Column('id', db.Integer),
    db.Column('bomrplid', db.Integer),
    db.Column('obommstid', db.Integer),
    db.Column('nbommstid', db.Integer),
    db.Column('rmk', db.Unicode(255)),
    db.Column('updby', db.String(10)),
    db.Column('upddt', db.DateTime),
    db.Column('sta', db.String(3)),
    db.Column('execflg', db.String(1)),
    db.Column('nxtsta', db.String(3))
)


class CopDepttpl(db.Model):
    __tablename__ = 'cop_depttpl'

    id = db.Column(db.Integer, primary_key=True)
    billcd = db.Column(db.Numeric(10, 0, asdecimal=False))
    plvaldt = db.Column(db.DateTime)
    rlvaldt = db.Column(db.DateTime)
    depttpltp = db.Column(db.String(10))
    odepttplid = db.Column(db.Integer)
    ndepttplid = db.Column(db.Integer, nullable=False)
    deptid = db.Column(db.Integer, nullable=False)
    rmk = db.Column(db.Unicode(255))
    updby = db.Column(db.String(20))
    upddt = db.Column(db.DateTime)
    sta = db.Column(db.String(3), nullable=False)
    execflg = db.Column(db.String(1), server_default=db.FetchedValue())
    nxtsta = db.Column(db.String(3))


t_cpn_lkcfg_1 = db.Table(
    'cpn_lkcfg_1',
    db.Column('id', db.Numeric(12, 0, asdecimal=False), nullable=False),
    db.Column('pluid', db.Integer),
    db.Column('p1p2cnvt', db.Integer),
    db.Column('p1saleflg', db.String(1)),
    db.Column('p1pluid', db.Integer),
    db.Column('p2p3cnvt', db.Integer),
    db.Column('p2saleflg', db.String(1)),
    db.Column('p2pluid', db.Integer),
    db.Column('p1p3cnvt', db.Integer),
    db.Column('p3saleflg', db.String(1)),
    db.Column('p3pluid', db.Integer),
    db.Column('acctcd', db.String(20)),
    db.Column('disccd', db.String(20)),
    db.Column('preflg', db.String(1)),
    db.Column('updby', db.String(20)),
    db.Column('upddt', db.DateTime),
    db.Column('sta', db.String(3), nullable=False),
    db.Column('execflg', db.String(1)),
    db.Column('nxtsta', db.String(3)),
    db.Column('lk1id', db.Integer),
    db.Column('lk2id', db.Integer),
    db.Column('lk3id', db.Integer),
    db.Column('lkguid', db.String(50))
)


t_crm_cardlog = db.Table(
    'crm_cardlog',
    db.Column('transno', db.Numeric(14, 0, asdecimal=False)),
    db.Column('deptcd', db.String(20)),
    db.Column('tillcd', db.String(20)),
    db.Column('giftno', db.String(50)),
    db.Column('upddt', db.DateTime),
    db.Column('saletp', db.String(10)),
    db.Column('ctrno', db.Numeric(14, 0, asdecimal=False))
)


t_crm_cardlog_h = db.Table(
    'crm_cardlog_h',
    db.Column('transno', db.Numeric(14, 0, asdecimal=False)),
    db.Column('deptcd', db.String(20)),
    db.Column('tillcd', db.String(20)),
    db.Column('giftno', db.String(50)),
    db.Column('upddt', db.DateTime),
    db.Column('saletp', db.String(10)),
    db.Column('syndt', db.DateTime),
    db.Column('rtnflg', db.String(1)),
    db.Column('rtnmsg', db.String(250)),
    db.Column('jsonbody', db.String(4000)),
    db.Column('ctrno', db.Numeric(14, 0, asdecimal=False))
)


t_crm_synlog = db.Table(
    'crm_synlog',
    db.Column('cd', db.String(50)),
    db.Column('lkcd', db.String(50)),
    db.Column('lkname', db.String(150)),
    db.Column('upddt', db.DateTime),
    db.Column('rtnmsg', db.String(1500)),
    db.Column('jsonbody', db.String(1500)),
    db.Column('execflg', db.Integer, server_default=db.FetchedValue())
)


t_crm_syntms = db.Table(
    'crm_syntms',
    db.Column('cd', db.String(20)),
    db.Column('name', db.String(50)),
    db.Column('syndate', db.DateTime)
)


t_crm_transnlog = db.Table(
    'crm_transnlog',
    db.Column('transno', db.Numeric(14, 0, asdecimal=False), index=True),
    db.Column('upddt', db.DateTime)
)


t_crm_transnlog_h = db.Table(
    'crm_transnlog_h',
    db.Column('transno', db.Numeric(14, 0, asdecimal=False)),
    db.Column('upddt', db.DateTime),
    db.Column('syndt', db.DateTime),
    db.Column('rtnflg', db.String(1)),
    db.Column('rtnmsg', db.String(250)),
    db.Column('jsonbody', db.String(4000))
)


class CvCustomervoiceView(db.Model):
    __tablename__ = 'cv_customervoice_view'

    storeno = db.Column(db.String(10), primary_key=True)
    cvno = db.Column(db.String(10), server_default=db.FetchedValue())
    begqty = db.Column(db.Numeric(asdecimal=False), nullable=False)
    updatedate = db.Column(db.DateTime, nullable=False)


t_dailysales_20160707 = db.Table(
    'dailysales_20160707',
    db.Column('inttransnum', db.Numeric(20, 0, asdecimal=False)),
    db.Column('intsaleid', db.Numeric(10, 0, asdecimal=False), nullable=False),
    db.Column('strtillcode', db.String(10), nullable=False),
    db.Column('strtradecode', db.String(10), nullable=False),
    db.Column('intdiscountcode', db.Numeric(10, 0, asdecimal=False)),
    db.Column('dtmsaledatetime', db.DateTime, nullable=False),
    db.Column('inttransnum2', db.String(40))
)


t_dailysales_20160707_1 = db.Table(
    'dailysales_20160707_1',
    db.Column('intsaleid', db.Numeric(10, 0, asdecimal=False)),
    db.Column('strtillcode', db.String(10)),
    db.Column('strtradecode', db.String(10)),
    db.Column('intdiscountcode', db.Numeric(10, 0, asdecimal=False)),
    db.Column('dtmsaledatetime', db.DateTime),
    db.Column('receiptnumber', db.String(40)),
    db.Column('order_dt', db.DateTime),
    db.Column('dsct_code', db.Numeric(10, 0, asdecimal=False)),
    db.Column('receiptnumber2', db.String(40))
)


t_dailysales_20161124 = db.Table(
    'dailysales_20161124',
    db.Column('inttransnum', db.Numeric(20, 0, asdecimal=False)),
    db.Column('cursales', db.Numeric(19, 4), nullable=False)
)


t_dailysales_20161124a = db.Table(
    'dailysales_20161124a',
    db.Column('intordercode', db.Numeric(10, 0, asdecimal=False), nullable=False),
    db.Column('???', db.String(32))
)


t_dailysales_20161124aa = db.Table(
    'dailysales_20161124aa',
    db.Column('intordercode', db.Numeric(10, 0, asdecimal=False), nullable=False),
    db.Column('???', db.String(32)),
    db.Column('cursales', db.Numeric(19, 4), nullable=False)
)


t_dailysales_20161124aaa = db.Table(
    'dailysales_20161124aaa',
    db.Column('inttransnum', db.Numeric(20, 0, asdecimal=False)),
    db.Column('qty', db.Numeric(asdecimal=False))
)


t_dailysales_20161219 = db.Table(
    'dailysales_20161219',
    db.Column('inttransnum', db.Numeric(20, 0, asdecimal=False))
)


t_dailysales_20161219_1 = db.Table(
    'dailysales_20161219_1',
    db.Column('strtillcode', db.String(10), nullable=False),
    db.Column('intsaleid', db.Numeric(10, 0, asdecimal=False), nullable=False),
    db.Column('strsaletype', db.String(1), nullable=False),
    db.Column('strtradecode', db.String(10), nullable=False),
    db.Column('intoperatorid', db.Numeric(10, 0, asdecimal=False), nullable=False),
    db.Column('dtmsaledatetime', db.DateTime, nullable=False),
    db.Column('inthour', db.Numeric(10, 0, asdecimal=False), nullable=False),
    db.Column('intminute', db.Numeric(10, 0, asdecimal=False), nullable=False),
    db.Column('lintitemnumber', db.Numeric(10, 0, asdecimal=False), nullable=False),
    db.Column('ctrcode', db.Numeric(20, 0, asdecimal=False), nullable=False),
    db.Column('cursales', db.Numeric(19, 4), nullable=False),
    db.Column('dblqtysold', db.Numeric(19, 4), nullable=False),
    db.Column('curcogs', db.Numeric(19, 4), nullable=False),
    db.Column('lintmemberid', db.Numeric(10, 0, asdecimal=False), nullable=False),
    db.Column('inttendercode', db.Numeric(10, 0, asdecimal=False), nullable=False),
    db.Column('curtenderamt', db.Numeric(19, 4), nullable=False),
    db.Column('lintcustomercount', db.Numeric(10, 0, asdecimal=False)),
    db.Column('dtmtradedate', db.DateTime, nullable=False),
    db.Column('strreason', db.String(10)),
    db.Column('dtmprocessed', db.DateTime),
    db.Column('strreference', db.String(20)),
    db.Column('strpricelevel', db.String(1)),
    db.Column('ysnstatsprocessed', db.String(1), nullable=False),
    db.Column('curnormalsell', db.Numeric(19, 4)),
    db.Column('curdiscount', db.Numeric(19, 4)),
    db.Column('intdiscountcode', db.Numeric(10, 0, asdecimal=False)),
    db.Column('intoffercode', db.Numeric(10, 0, asdecimal=False)),
    db.Column('lintparentitem', db.Numeric(10, 0, asdecimal=False)),
    db.Column('dbldiscountper', db.Numeric(19, 4)),
    db.Column('curcommlevel', db.Numeric(19, 4)),
    db.Column('strtype', db.String(10)),
    db.Column('lintdeliveryaddress', db.Numeric(10, 0, asdecimal=False)),
    db.Column('lintcontactnum', db.Numeric(10, 0, asdecimal=False)),
    db.Column('lintgiftnum', db.Numeric(10, 0, asdecimal=False)),
    db.Column('intordercode', db.Numeric(20, 0, asdecimal=False)),
    db.Column('cursalestax', db.Numeric(19, 4)),
    db.Column('strcomment', db.String(100)),
    db.Column('strtaxcode1', db.String(10)),
    db.Column('strtaxcode2', db.String(10)),
    db.Column('strtaxcode3', db.String(10)),
    db.Column('curtaxamt1', db.Numeric(19, 4)),
    db.Column('curtaxamt2', db.Numeric(19, 4)),
    db.Column('curtaxamt3', db.Numeric(19, 4)),
    db.Column('cursellprice1', db.Numeric(19, 4)),
    db.Column('ysnclaimsupplier', db.String(1)),
    db.Column('ysnclaimmanufacturer', db.String(1)),
    db.Column('ysnclaimheadoffice', db.String(1)),
    db.Column('lintpoints', db.Numeric(10, 0, asdecimal=False)),
    db.Column('dblexchangerate', db.Numeric(19, 4)),
    db.Column('curforeignamt', db.Numeric(19, 4)),
    db.Column('cursalesdiscount', db.Numeric(19, 4)),
    db.Column('intsalesdiscountcode', db.Numeric(10, 0, asdecimal=False)),
    db.Column('curofferdiscount', db.Numeric(19, 4)),
    db.Column('inttenderdiscountcode', db.Numeric(10, 0, asdecimal=False)),
    db.Column('curtenderdiscount', db.Numeric(19, 4)),
    db.Column('inttransnum', db.Numeric(20, 0, asdecimal=False)),
    db.Column('dblapn', db.Numeric(19, 4)),
    db.Column('strordercode', db.String(20)),
    db.Column('strcusttaxnum', db.String(20)),
    db.Column('strpreprintsaleid', db.String(20)),
    db.Column('strcardnum', db.String(38)),
    db.Column('ctrcode1', db.Numeric(20, 0, asdecimal=False)),
    db.Column('strcreditcardnum', db.String(20)),
    db.Column('strauthorisation', db.String(30))
)


t_dailysales_20161220 = db.Table(
    'dailysales_20161220',
    db.Column('inttransnum', db.Numeric(20, 0, asdecimal=False))
)


t_dailysales_20161220_1 = db.Table(
    'dailysales_20161220_1',
    db.Column('strtillcode', db.String(10), nullable=False),
    db.Column('intsaleid', db.Numeric(10, 0, asdecimal=False), nullable=False),
    db.Column('strsaletype', db.String(1), nullable=False),
    db.Column('strtradecode', db.String(10), nullable=False),
    db.Column('intoperatorid', db.Numeric(10, 0, asdecimal=False), nullable=False),
    db.Column('dtmsaledatetime', db.DateTime, nullable=False),
    db.Column('inthour', db.Numeric(10, 0, asdecimal=False), nullable=False),
    db.Column('intminute', db.Numeric(10, 0, asdecimal=False), nullable=False),
    db.Column('lintitemnumber', db.Numeric(10, 0, asdecimal=False), nullable=False),
    db.Column('ctrcode', db.Numeric(20, 0, asdecimal=False), nullable=False),
    db.Column('cursales', db.Numeric(19, 4), nullable=False),
    db.Column('dblqtysold', db.Numeric(19, 4), nullable=False),
    db.Column('curcogs', db.Numeric(19, 4), nullable=False),
    db.Column('lintmemberid', db.Numeric(10, 0, asdecimal=False), nullable=False),
    db.Column('inttendercode', db.Numeric(10, 0, asdecimal=False), nullable=False),
    db.Column('curtenderamt', db.Numeric(19, 4), nullable=False),
    db.Column('lintcustomercount', db.Numeric(10, 0, asdecimal=False)),
    db.Column('dtmtradedate', db.DateTime, nullable=False),
    db.Column('strreason', db.String(10)),
    db.Column('dtmprocessed', db.DateTime),
    db.Column('strreference', db.String(20)),
    db.Column('strpricelevel', db.String(1)),
    db.Column('ysnstatsprocessed', db.String(1), nullable=False),
    db.Column('curnormalsell', db.Numeric(19, 4)),
    db.Column('curdiscount', db.Numeric(19, 4)),
    db.Column('intdiscountcode', db.Numeric(10, 0, asdecimal=False)),
    db.Column('intoffercode', db.Numeric(10, 0, asdecimal=False)),
    db.Column('lintparentitem', db.Numeric(10, 0, asdecimal=False)),
    db.Column('dbldiscountper', db.Numeric(19, 4)),
    db.Column('curcommlevel', db.Numeric(19, 4)),
    db.Column('strtype', db.String(10)),
    db.Column('lintdeliveryaddress', db.Numeric(10, 0, asdecimal=False)),
    db.Column('lintcontactnum', db.Numeric(10, 0, asdecimal=False)),
    db.Column('lintgiftnum', db.Numeric(10, 0, asdecimal=False)),
    db.Column('intordercode', db.Numeric(20, 0, asdecimal=False)),
    db.Column('cursalestax', db.Numeric(19, 4)),
    db.Column('strcomment', db.String(100)),
    db.Column('strtaxcode1', db.String(10)),
    db.Column('strtaxcode2', db.String(10)),
    db.Column('strtaxcode3', db.String(10)),
    db.Column('curtaxamt1', db.Numeric(19, 4)),
    db.Column('curtaxamt2', db.Numeric(19, 4)),
    db.Column('curtaxamt3', db.Numeric(19, 4)),
    db.Column('cursellprice1', db.Numeric(19, 4)),
    db.Column('ysnclaimsupplier', db.String(1)),
    db.Column('ysnclaimmanufacturer', db.String(1)),
    db.Column('ysnclaimheadoffice', db.String(1)),
    db.Column('lintpoints', db.Numeric(10, 0, asdecimal=False)),
    db.Column('dblexchangerate', db.Numeric(19, 4)),
    db.Column('curforeignamt', db.Numeric(19, 4)),
    db.Column('cursalesdiscount', db.Numeric(19, 4)),
    db.Column('intsalesdiscountcode', db.Numeric(10, 0, asdecimal=False)),
    db.Column('curofferdiscount', db.Numeric(19, 4)),
    db.Column('inttenderdiscountcode', db.Numeric(10, 0, asdecimal=False)),
    db.Column('curtenderdiscount', db.Numeric(19, 4)),
    db.Column('inttransnum', db.Numeric(20, 0, asdecimal=False)),
    db.Column('dblapn', db.Numeric(19, 4)),
    db.Column('strordercode', db.String(20)),
    db.Column('strcusttaxnum', db.String(20)),
    db.Column('strpreprintsaleid', db.String(20)),
    db.Column('strcardnum', db.String(38)),
    db.Column('ctrcode1', db.Numeric(20, 0, asdecimal=False)),
    db.Column('strcreditcardnum', db.String(20)),
    db.Column('strauthorisation', db.String(30))
)


t_dailysales_temp20160715 = db.Table(
    'dailysales_temp20160715',
    db.Column('siebelno', db.String(100)),
    db.Column('dtmsaledatetime', db.DateTime),
    db.Column('lintitemnumber', db.Numeric(10, 0, asdecimal=False)),
    db.Column('cursales', db.Numeric(19, 4)),
    db.Column('dblqtysold', db.Numeric(19, 4)),
    db.Column('integration_id', db.String(100)),
    db.Column('strtradecode', db.String(10)),
    db.Column('strtillcode', db.String(10)),
    db.Column('intsaleid', db.Numeric(10, 0, asdecimal=False)),
    db.Column('integration_id2', db.String(100))
)


t_dailysales_temp20160715_1 = db.Table(
    'dailysales_temp20160715_1',
    db.Column('strtillcode', db.String(10), nullable=False),
    db.Column('intsaleid', db.Numeric(10, 0, asdecimal=False), nullable=False),
    db.Column('strsaletype', db.String(1), nullable=False),
    db.Column('strtradecode', db.String(10), nullable=False),
    db.Column('intoperatorid', db.Numeric(10, 0, asdecimal=False), nullable=False),
    db.Column('dtmsaledatetime', db.DateTime, nullable=False),
    db.Column('inthour', db.Numeric(10, 0, asdecimal=False), nullable=False),
    db.Column('intminute', db.Numeric(10, 0, asdecimal=False), nullable=False),
    db.Column('lintitemnumber', db.Numeric(10, 0, asdecimal=False), nullable=False),
    db.Column('ctrcode', db.Numeric(20, 0, asdecimal=False), nullable=False),
    db.Column('cursales', db.Numeric(19, 4), nullable=False),
    db.Column('dblqtysold', db.Numeric(19, 4), nullable=False),
    db.Column('curcogs', db.Numeric(19, 4), nullable=False),
    db.Column('lintmemberid', db.Numeric(10, 0, asdecimal=False), nullable=False),
    db.Column('inttendercode', db.Numeric(10, 0, asdecimal=False), nullable=False),
    db.Column('curtenderamt', db.Numeric(19, 4), nullable=False),
    db.Column('lintcustomercount', db.Numeric(10, 0, asdecimal=False)),
    db.Column('dtmtradedate', db.DateTime, nullable=False),
    db.Column('strreason', db.String(10)),
    db.Column('dtmprocessed', db.DateTime),
    db.Column('strreference', db.String(20)),
    db.Column('strpricelevel', db.String(1)),
    db.Column('ysnstatsprocessed', db.String(1), nullable=False),
    db.Column('curnormalsell', db.Numeric(19, 4)),
    db.Column('curdiscount', db.Numeric(19, 4)),
    db.Column('intdiscountcode', db.Numeric(10, 0, asdecimal=False)),
    db.Column('intoffercode', db.Numeric(10, 0, asdecimal=False)),
    db.Column('lintparentitem', db.Numeric(10, 0, asdecimal=False)),
    db.Column('dbldiscountper', db.Numeric(19, 4)),
    db.Column('curcommlevel', db.Numeric(19, 4)),
    db.Column('strtype', db.String(10)),
    db.Column('lintdeliveryaddress', db.Numeric(10, 0, asdecimal=False)),
    db.Column('lintcontactnum', db.Numeric(10, 0, asdecimal=False)),
    db.Column('lintgiftnum', db.Numeric(10, 0, asdecimal=False)),
    db.Column('intordercode', db.Numeric(20, 0, asdecimal=False)),
    db.Column('cursalestax', db.Numeric(19, 4)),
    db.Column('strcomment', db.String(100)),
    db.Column('strtaxcode1', db.String(10)),
    db.Column('strtaxcode2', db.String(10)),
    db.Column('strtaxcode3', db.String(10)),
    db.Column('curtaxamt1', db.Numeric(19, 4)),
    db.Column('curtaxamt2', db.Numeric(19, 4)),
    db.Column('curtaxamt3', db.Numeric(19, 4)),
    db.Column('cursellprice1', db.Numeric(19, 4)),
    db.Column('ysnclaimsupplier', db.String(1)),
    db.Column('ysnclaimmanufacturer', db.String(1)),
    db.Column('ysnclaimheadoffice', db.String(1)),
    db.Column('lintpoints', db.Numeric(10, 0, asdecimal=False)),
    db.Column('dblexchangerate', db.Numeric(19, 4)),
    db.Column('curforeignamt', db.Numeric(19, 4)),
    db.Column('cursalesdiscount', db.Numeric(19, 4)),
    db.Column('intsalesdiscountcode', db.Numeric(10, 0, asdecimal=False)),
    db.Column('curofferdiscount', db.Numeric(19, 4)),
    db.Column('inttenderdiscountcode', db.Numeric(10, 0, asdecimal=False)),
    db.Column('curtenderdiscount', db.Numeric(19, 4)),
    db.Column('inttransnum', db.Numeric(20, 0, asdecimal=False)),
    db.Column('dblapn', db.Numeric(19, 4)),
    db.Column('strordercode', db.String(20)),
    db.Column('strcusttaxnum', db.String(20)),
    db.Column('strpreprintsaleid', db.String(20)),
    db.Column('strcardnum', db.String(38)),
    db.Column('ctrcode1', db.Numeric(20, 0, asdecimal=False)),
    db.Column('strcreditcardnum', db.String(20)),
    db.Column('strauthorisation', db.String(30))
)


t_dailysales_temp20160715_2 = db.Table(
    'dailysales_temp20160715_2',
    db.Column('strtillcode', db.String(10), nullable=False),
    db.Column('intsaleid', db.Numeric(10, 0, asdecimal=False), nullable=False),
    db.Column('strsaletype', db.String(1), nullable=False),
    db.Column('strtradecode', db.String(10), nullable=False),
    db.Column('intoperatorid', db.Numeric(10, 0, asdecimal=False), nullable=False),
    db.Column('dtmsaledatetime', db.DateTime, nullable=False),
    db.Column('inthour', db.Numeric(10, 0, asdecimal=False), nullable=False),
    db.Column('intminute', db.Numeric(10, 0, asdecimal=False), nullable=False),
    db.Column('lintitemnumber', db.Numeric(10, 0, asdecimal=False), nullable=False),
    db.Column('ctrcode', db.Numeric(20, 0, asdecimal=False), nullable=False),
    db.Column('cursales', db.Numeric(19, 4), nullable=False),
    db.Column('dblqtysold', db.Numeric(19, 4), nullable=False),
    db.Column('curcogs', db.Numeric(19, 4), nullable=False),
    db.Column('lintmemberid', db.Numeric(10, 0, asdecimal=False), nullable=False),
    db.Column('inttendercode', db.Numeric(10, 0, asdecimal=False), nullable=False),
    db.Column('curtenderamt', db.Numeric(19, 4), nullable=False),
    db.Column('lintcustomercount', db.Numeric(10, 0, asdecimal=False)),
    db.Column('dtmtradedate', db.DateTime, nullable=False),
    db.Column('strreason', db.String(10)),
    db.Column('dtmprocessed', db.DateTime),
    db.Column('strreference', db.String(20)),
    db.Column('strpricelevel', db.String(1)),
    db.Column('ysnstatsprocessed', db.String(1), nullable=False),
    db.Column('curnormalsell', db.Numeric(19, 4)),
    db.Column('curdiscount', db.Numeric(19, 4)),
    db.Column('intdiscountcode', db.Numeric(10, 0, asdecimal=False)),
    db.Column('intoffercode', db.Numeric(10, 0, asdecimal=False)),
    db.Column('lintparentitem', db.Numeric(10, 0, asdecimal=False)),
    db.Column('dbldiscountper', db.Numeric(19, 4)),
    db.Column('curcommlevel', db.Numeric(19, 4)),
    db.Column('strtype', db.String(10)),
    db.Column('lintdeliveryaddress', db.Numeric(10, 0, asdecimal=False)),
    db.Column('lintcontactnum', db.Numeric(10, 0, asdecimal=False)),
    db.Column('lintgiftnum', db.Numeric(10, 0, asdecimal=False)),
    db.Column('intordercode', db.Numeric(20, 0, asdecimal=False)),
    db.Column('cursalestax', db.Numeric(19, 4)),
    db.Column('strcomment', db.String(100)),
    db.Column('strtaxcode1', db.String(10)),
    db.Column('strtaxcode2', db.String(10)),
    db.Column('strtaxcode3', db.String(10)),
    db.Column('curtaxamt1', db.Numeric(19, 4)),
    db.Column('curtaxamt2', db.Numeric(19, 4)),
    db.Column('curtaxamt3', db.Numeric(19, 4)),
    db.Column('cursellprice1', db.Numeric(19, 4)),
    db.Column('ysnclaimsupplier', db.String(1)),
    db.Column('ysnclaimmanufacturer', db.String(1)),
    db.Column('ysnclaimheadoffice', db.String(1)),
    db.Column('lintpoints', db.Numeric(10, 0, asdecimal=False)),
    db.Column('dblexchangerate', db.Numeric(19, 4)),
    db.Column('curforeignamt', db.Numeric(19, 4)),
    db.Column('cursalesdiscount', db.Numeric(19, 4)),
    db.Column('intsalesdiscountcode', db.Numeric(10, 0, asdecimal=False)),
    db.Column('curofferdiscount', db.Numeric(19, 4)),
    db.Column('inttenderdiscountcode', db.Numeric(10, 0, asdecimal=False)),
    db.Column('curtenderdiscount', db.Numeric(19, 4)),
    db.Column('inttransnum', db.Numeric(20, 0, asdecimal=False)),
    db.Column('dblapn', db.Numeric(19, 4)),
    db.Column('strordercode', db.String(20)),
    db.Column('strcusttaxnum', db.String(20)),
    db.Column('strpreprintsaleid', db.String(20)),
    db.Column('strcardnum', db.String(38)),
    db.Column('ctrcode1', db.Numeric(20, 0, asdecimal=False)),
    db.Column('strcreditcardnum', db.String(20)),
    db.Column('strauthorisation', db.String(30))
)


t_dailysales_temp20160715_3 = db.Table(
    'dailysales_temp20160715_3',
    db.Column('strtillcode', db.String(10), nullable=False),
    db.Column('intsaleid', db.Numeric(10, 0, asdecimal=False), nullable=False),
    db.Column('strsaletype', db.String(1), nullable=False),
    db.Column('strtradecode', db.String(10), nullable=False),
    db.Column('intoperatorid', db.Numeric(10, 0, asdecimal=False), nullable=False),
    db.Column('dtmsaledatetime', db.DateTime, nullable=False),
    db.Column('inthour', db.Numeric(10, 0, asdecimal=False), nullable=False),
    db.Column('intminute', db.Numeric(10, 0, asdecimal=False), nullable=False),
    db.Column('lintitemnumber', db.Numeric(10, 0, asdecimal=False), nullable=False),
    db.Column('ctrcode', db.Numeric(20, 0, asdecimal=False), nullable=False),
    db.Column('cursales', db.Numeric(19, 4), nullable=False),
    db.Column('dblqtysold', db.Numeric(19, 4), nullable=False),
    db.Column('curcogs', db.Numeric(19, 4), nullable=False),
    db.Column('lintmemberid', db.Numeric(10, 0, asdecimal=False), nullable=False),
    db.Column('inttendercode', db.Numeric(10, 0, asdecimal=False), nullable=False),
    db.Column('curtenderamt', db.Numeric(19, 4), nullable=False),
    db.Column('lintcustomercount', db.Numeric(10, 0, asdecimal=False)),
    db.Column('dtmtradedate', db.DateTime, nullable=False),
    db.Column('strreason', db.String(10)),
    db.Column('dtmprocessed', db.DateTime),
    db.Column('strreference', db.String(20)),
    db.Column('strpricelevel', db.String(1)),
    db.Column('ysnstatsprocessed', db.String(1), nullable=False),
    db.Column('curnormalsell', db.Numeric(19, 4)),
    db.Column('curdiscount', db.Numeric(19, 4)),
    db.Column('intdiscountcode', db.Numeric(10, 0, asdecimal=False)),
    db.Column('intoffercode', db.Numeric(10, 0, asdecimal=False)),
    db.Column('lintparentitem', db.Numeric(10, 0, asdecimal=False)),
    db.Column('dbldiscountper', db.Numeric(19, 4)),
    db.Column('curcommlevel', db.Numeric(19, 4)),
    db.Column('strtype', db.String(10)),
    db.Column('lintdeliveryaddress', db.Numeric(10, 0, asdecimal=False)),
    db.Column('lintcontactnum', db.Numeric(10, 0, asdecimal=False)),
    db.Column('lintgiftnum', db.Numeric(10, 0, asdecimal=False)),
    db.Column('intordercode', db.Numeric(20, 0, asdecimal=False)),
    db.Column('cursalestax', db.Numeric(19, 4)),
    db.Column('strcomment', db.String(100)),
    db.Column('strtaxcode1', db.String(10)),
    db.Column('strtaxcode2', db.String(10)),
    db.Column('strtaxcode3', db.String(10)),
    db.Column('curtaxamt1', db.Numeric(19, 4)),
    db.Column('curtaxamt2', db.Numeric(19, 4)),
    db.Column('curtaxamt3', db.Numeric(19, 4)),
    db.Column('cursellprice1', db.Numeric(19, 4)),
    db.Column('ysnclaimsupplier', db.String(1)),
    db.Column('ysnclaimmanufacturer', db.String(1)),
    db.Column('ysnclaimheadoffice', db.String(1)),
    db.Column('lintpoints', db.Numeric(10, 0, asdecimal=False)),
    db.Column('dblexchangerate', db.Numeric(19, 4)),
    db.Column('curforeignamt', db.Numeric(19, 4)),
    db.Column('cursalesdiscount', db.Numeric(19, 4)),
    db.Column('intsalesdiscountcode', db.Numeric(10, 0, asdecimal=False)),
    db.Column('curofferdiscount', db.Numeric(19, 4)),
    db.Column('inttenderdiscountcode', db.Numeric(10, 0, asdecimal=False)),
    db.Column('curtenderdiscount', db.Numeric(19, 4)),
    db.Column('inttransnum', db.Numeric(20, 0, asdecimal=False)),
    db.Column('dblapn', db.Numeric(19, 4)),
    db.Column('strordercode', db.String(20)),
    db.Column('strcusttaxnum', db.String(20)),
    db.Column('strpreprintsaleid', db.String(20)),
    db.Column('strcardnum', db.String(38)),
    db.Column('ctrcode1', db.Numeric(20, 0, asdecimal=False)),
    db.Column('strcreditcardnum', db.String(20)),
    db.Column('strauthorisation', db.String(30))
)


class DalAcc(db.Model):
    __tablename__ = 'dal_acc'

    id = db.Column(db.Integer, primary_key=True)
    cd = db.Column(db.String(20))
    nm_l_zh = db.Column(db.Unicode(50), nullable=False)
    nm_l_en = db.Column(db.Unicode(50))
    nm_l_ja = db.Column(db.String(50))
    acctyp = db.Column(db.String(4))
    caltyp = db.Column(db.String(4))
    lkcd = db.Column(db.String(20))
    ishq = db.Column(db.String(1))
    rmk = db.Column(db.String(255))
    updby = db.Column(db.String(50))
    upddt = db.Column(db.DateTime)
    sta = db.Column(db.String(3), nullable=False)
    execflg = db.Column(db.String(1))
    nxtsta = db.Column(db.String(3))
    ordcd = db.Column(db.Integer)
    isdc = db.Column(db.String(1))
    finacccd = db.Column(db.String(20))
    aduamt = db.Column(db.Numeric(12, 2), server_default=db.FetchedValue())
    isprint = db.Column(db.String(1))


class DalAcccal(db.Model):
    __tablename__ = 'dal_acccal'

    id = db.Column(db.Integer, primary_key=True)
    toaccid = db.Column(db.Integer)
    fromaccid = db.Column(db.Integer, nullable=False)
    callv = db.Column(db.Integer)
    calrate = db.Column(db.Integer)
    updby = db.Column(db.String(50))
    upddt = db.Column(db.DateTime)


t_dal_bank = db.Table(
    'dal_bank',
    db.Column('id', db.Numeric(12, 0, asdecimal=False), nullable=False),
    db.Column('dalid', db.Numeric(12, 0, asdecimal=False), nullable=False, index=True),
    db.Column('bankid', db.Integer),
    db.Column('stval', db.Numeric(18, 2)),
    db.Column('hqval', db.Numeric(18, 2)),
    db.Column('lastdt', db.DateTime),
    db.Column('rmk', db.String(255)),
    db.Column('updbyst', db.String(20)),
    db.Column('upddt', db.DateTime),
    db.Column('sta', db.String(3), nullable=False),
    db.Column('updby', db.String(20))
)


class DalBox(db.Model):
    __tablename__ = 'dal_box'
    __table_args__ = (
        db.Index('idx_dal_shftmst_4', 'bizdt', 'sta'),
    )

    id = db.Column(db.Numeric(12, 0, asdecimal=False), primary_key=True)
    cd = db.Column(db.String(20))
    bizdt = db.Column(db.DateTime)
    rmk = db.Column(db.String(255))
    updby = db.Column(db.String(20))
    upddt = db.Column(db.DateTime)
    sta = db.Column(db.String(3), nullable=False)


class DalDtl(db.Model):
    __tablename__ = 'dal_dtl'

    id = db.Column(db.Numeric(12, 0, asdecimal=False), primary_key=True)
    dalid = db.Column(db.Numeric(12, 0, asdecimal=False), nullable=False, index=True)
    accid = db.Column(db.Integer)
    stval = db.Column(db.Numeric(18, 2))
    hqval = db.Column(db.Numeric(18, 2))
    rmk = db.Column(db.String(255))
    updbyst = db.Column(db.String(20))
    updbyhq = db.Column(db.String(20))
    upddtst = db.Column(db.DateTime)
    upddthq = db.Column(db.DateTime)
    updby = db.Column(db.String(20))
    upddt = db.Column(db.DateTime)


t_dal_lkcfg = db.Table(
    'dal_lkcfg',
    db.Column('id', db.Numeric(12, 0, asdecimal=False), nullable=False),
    db.Column('pluid', db.Integer),
    db.Column('acctcd', db.String(20)),
    db.Column('updby', db.String(20)),
    db.Column('upddt', db.DateTime),
    db.Column('sta', db.String(3), nullable=False),
    db.Column('execflg', db.String(1)),
    db.Column('nxtsta', db.String(3)),
    db.Index('idx_dallkcfg', 'pluid', 'acctcd')
)


class DalMst(db.Model):
    __tablename__ = 'dal_mst'
    __table_args__ = (
        db.Index('idx_dal_shftmst_2', 'deptid', 'bizdt', 'sta'),
    )

    id = db.Column(db.Numeric(12, 0, asdecimal=False), primary_key=True)
    deptid = db.Column(db.Integer)
    bizdt = db.Column(db.DateTime)
    lastdt = db.Column(db.DateTime)
    rmk = db.Column(db.String(255))
    updbyst = db.Column(db.String(20))
    updbyhq = db.Column(db.String(20))
    upddtst = db.Column(db.DateTime)
    upddthq = db.Column(db.DateTime)
    upddt = db.Column(db.DateTime, index=True)
    sta = db.Column(db.String(3), nullable=False)
    updby = db.Column(db.String(20))
    boxid = db.Column(db.Numeric(12, 0, asdecimal=False))
    rmkhq = db.Column(db.String(255))


t_dal_rpt1 = db.Table(
    'dal_rpt1',
    db.Column('dalid', db.Numeric(12, 0, asdecimal=False), nullable=False, index=True),
    db.Column('totalamount', db.Numeric(18, 2)),
    db.Column('customernum', db.Integer),
    db.Column('eatin', db.Numeric(18, 2)),
    db.Column('takeaway', db.Numeric(18, 2)),
    db.Column('delivery', db.Numeric(18, 2)),
    db.Column('avgprice', db.Numeric(18, 2))
)


t_dal_rpt2 = db.Table(
    'dal_rpt2',
    db.Column('dalid', db.Numeric(12, 0, asdecimal=False), nullable=False, index=True),
    db.Column('catcd', db.String(20)),
    db.Column('catname', db.Unicode(50)),
    db.Column('grossamt', db.Numeric(18, 2)),
    db.Column('adjamt', db.Numeric(18, 2)),
    db.Column('adjrate', db.Numeric(18, 2))
)


t_dal_shiftdtl = db.Table(
    'dal_shiftdtl',
    db.Column('shiftid', db.Numeric(12, 0, asdecimal=False), index=True),
    db.Column('sn', db.Integer),
    db.Column('grp', db.String(10)),
    db.Column('cd', db.String(10)),
    db.Column('dsc', db.String(200)),
    db.Column('val', db.Numeric(16, 2))
)


t_dal_shiftdtltrans = db.Table(
    'dal_shiftdtltrans',
    db.Column('shiftid', db.Numeric(12, 0, asdecimal=False), index=True),
    db.Column('transno', db.Numeric(20, 0, asdecimal=False), index=True)
)


t_dal_shiftdtltrans_hhs = db.Table(
    'dal_shiftdtltrans_hhs',
    db.Column('shiftid', db.Numeric(12, 0, asdecimal=False), index=True),
    db.Column('transno', db.Numeric(20, 0, asdecimal=False), index=True),
    db.Column('upddt', db.DateTime, server_default=db.FetchedValue())
)


class DalShiftmst(db.Model):
    __tablename__ = 'dal_shiftmst'
    __table_args__ = (
        db.Index('idx_dal_shftmst_1', 'deptid', 'bizdt', 'sta'),
    )

    id = db.Column(db.Numeric(12, 0, asdecimal=False), primary_key=True)
    deptid = db.Column(db.Integer)
    bizdt = db.Column(db.DateTime)
    opercd = db.Column(db.String(20))
    tillcd = db.Column(db.String(20))
    calamt = db.Column(db.Numeric(16, 2))
    relamt = db.Column(db.Numeric(16, 2))
    salamt = db.Column(db.Numeric(16, 2))
    rtnamt = db.Column(db.Numeric(16, 2))
    disamt = db.Column(db.Numeric(16, 2))
    lastdt = db.Column(db.DateTime)
    rmk = db.Column(db.String(255))
    updby = db.Column(db.String(20))
    upddt = db.Column(db.DateTime)
    sta = db.Column(db.String(3), nullable=False)


t_dg_storecode = db.Table(
    'dg_storecode',
    db.Column('storecode', db.String(20), nullable=False),
    db.Column('tillid', db.String(20), nullable=False),
    db.Column('txdate', db.String(20), nullable=False),
    db.Column('txtime', db.String(5), nullable=False),
    db.Column('docno', db.String(10), nullable=False),
    db.Column('plu', db.String(20)),
    db.Column('vipcode', db.String(8)),
    db.Column('ch', db.Numeric(16, 2)),
    db.Column('ci', db.Numeric(16, 2)),
    db.Column('co', db.Numeric(16, 2)),
    db.Column('sy', db.Numeric(16, 2)),
    db.Column('ot', db.Numeric(16, 2)),
    db.Column('ttldiscount', db.Numeric(16, 2)),
    db.Column('netamt', db.Numeric(16, 2))
)


t_dg_storecode_201144 = db.Table(
    'dg_storecode_201144',
    db.Column('storecode', db.String(20), nullable=False),
    db.Column('tillid', db.String(20), nullable=False),
    db.Column('txdate', db.String(20), nullable=False),
    db.Column('txtime', db.String(5), nullable=False),
    db.Column('docno', db.String(10), nullable=False),
    db.Column('plu', db.String(20)),
    db.Column('vipcode', db.String(8)),
    db.Column('ch', db.Numeric(16, 2)),
    db.Column('ci', db.Numeric(16, 2)),
    db.Column('co', db.Numeric(16, 2)),
    db.Column('ot', db.Numeric(16, 2)),
    db.Column('ttldiscount', db.Numeric(16, 2)),
    db.Column('netamt', db.Numeric(16, 2))
)


t_dg_storecode_gj = db.Table(
    'dg_storecode_gj',
    db.Column('line_type', db.String(10)),
    db.Column('branch_no', db.String(25)),
    db.Column('site', db.String(10)),
    db.Column('contract', db.String(10)),
    db.Column('floor', db.String(10)),
    db.Column('workstation_no', db.String(10)),
    db.Column('sale_tx_no', db.Numeric(14, 0, asdecimal=False)),
    db.Column('sale_date', db.String(20)),
    db.Column('total_amt', db.Numeric(14, 2)),
    db.Column('dkt_disc_val', db.Numeric(14, 2)),
    db.Column('dkt_disc_pct', db.Numeric(14, 2)),
    db.Column('operid', db.String(20)),
    db.Column('void_branch_no', db.Integer),
    db.Column('void_wrkst_no', db.String(10)),
    db.Column('void_tx_no', db.Numeric(14, 0, asdecimal=False)),
    db.Column('cust_code', db.String(20)),
    db.Column('amithevoid', db.Integer),
    db.Column('businessdate', db.DateTime, index=True),
    db.Column('sn', db.Integer)
)


t_dg_storecode_hl = db.Table(
    'dg_storecode_hl',
    db.Column('storecode', db.String(20), nullable=False),
    db.Column('txdate', db.String(20), nullable=False),
    db.Column('txtime', db.String(5), nullable=False),
    db.Column('tillid', db.String(20), nullable=False),
    db.Column('docno', db.String(10), nullable=False),
    db.Column('netamt', db.Numeric(16, 2))
)


t_dg_storecode_hqcf = db.Table(
    'dg_storecode_hqcf',
    db.Column('flag', db.String(20), nullable=False),
    db.Column('storecode', db.String(20), nullable=False),
    db.Column('tillid', db.String(20), nullable=False),
    db.Column('txdate', db.String(20), nullable=False),
    db.Column('txtime', db.String(5), nullable=False),
    db.Column('docno', db.String(10), nullable=False),
    db.Column('vipcode', db.String(8)),
    db.Column('ch', db.Numeric(16, 2)),
    db.Column('ci', db.Numeric(16, 2)),
    db.Column('co', db.Numeric(16, 2)),
    db.Column('ot', db.Numeric(16, 2)),
    db.Column('ttldiscount', db.Numeric(16, 2)),
    db.Column('netamt', db.Numeric(16, 2)),
    db.Column('inttransnum', db.String(20), nullable=False)
)


t_dg_storecode_hqdd = db.Table(
    'dg_storecode_hqdd',
    db.Column('flag', db.String(20), nullable=False),
    db.Column('storecode', db.String(20), nullable=False),
    db.Column('tillid', db.String(20), nullable=False),
    db.Column('txdate', db.String(20), nullable=False),
    db.Column('txtime', db.String(5), nullable=False),
    db.Column('docno', db.String(10), nullable=False),
    db.Column('vipcode', db.String(8)),
    db.Column('ch', db.Numeric(16, 2)),
    db.Column('ci', db.Numeric(16, 2)),
    db.Column('co', db.Numeric(16, 2)),
    db.Column('ot', db.Numeric(16, 2)),
    db.Column('ttldiscount', db.Numeric(16, 2)),
    db.Column('netamt', db.Numeric(16, 2)),
    db.Column('inttransnum', db.String(20), nullable=False)
)


t_dg_storecode_hzdz = db.Table(
    'dg_storecode_hzdz',
    db.Column('flag', db.String(20), nullable=False),
    db.Column('storecode', db.String(20), nullable=False),
    db.Column('tillid', db.String(20), nullable=False),
    db.Column('txdate', db.String(20), nullable=False),
    db.Column('txtime', db.String(5), nullable=False),
    db.Column('docno', db.String(10), nullable=False),
    db.Column('vipcode', db.String(8)),
    db.Column('ch', db.Numeric(16, 2)),
    db.Column('ci', db.Numeric(16, 2)),
    db.Column('co', db.Numeric(16, 2)),
    db.Column('ot', db.Numeric(16, 2)),
    db.Column('ttldiscount', db.Numeric(16, 2)),
    db.Column('netamt', db.Numeric(16, 2)),
    db.Column('inttransnum', db.String(20), nullable=False),
    db.Column('orderflag', db.String(20))
)


t_dg_storecode_hzdzcfjcd = db.Table(
    'dg_storecode_hzdzcfjcd',
    db.Column('flag', db.String(20), nullable=False),
    db.Column('storecode', db.String(20), nullable=False),
    db.Column('tillid', db.String(20), nullable=False),
    db.Column('txdate', db.String(20), nullable=False),
    db.Column('txtime', db.String(5), nullable=False),
    db.Column('docno', db.String(10), nullable=False),
    db.Column('vipcode', db.String(8)),
    db.Column('ch', db.Numeric(16, 2)),
    db.Column('ci', db.Numeric(16, 2)),
    db.Column('co', db.Numeric(16, 2)),
    db.Column('ot', db.Numeric(16, 2)),
    db.Column('ttldiscount', db.Numeric(16, 2)),
    db.Column('netamt', db.Numeric(16, 2)),
    db.Column('inttransnum', db.String(20), nullable=False),
    db.Column('orderflag', db.String(20))
)


t_dg_storecode_jgbh = db.Table(
    'dg_storecode_jgbh',
    db.Column('businessdate', db.String(20), nullable=False),
    db.Column('transdatetime', db.String(25), nullable=False),
    db.Column('countcode', db.String(12), nullable=False),
    db.Column('posno', db.String(8), nullable=False),
    db.Column('flowno', db.String(8), nullable=False),
    db.Column('payno', db.String(5), nullable=False),
    db.Column('currency', db.String(150), nullable=False),
    db.Column('cardno', db.String(8)),
    db.Column('amount', db.Numeric(16, 2))
)


t_dg_storecode_lygt = db.Table(
    'dg_storecode_lygt',
    db.Column('flag', db.String(20), nullable=False),
    db.Column('storecode', db.String(20), nullable=False),
    db.Column('tillid', db.String(20), nullable=False),
    db.Column('txdate', db.String(20), nullable=False),
    db.Column('txtime', db.String(5), nullable=False),
    db.Column('docno', db.String(10), nullable=False),
    db.Column('vipcode', db.String(8)),
    db.Column('ch', db.Numeric(16, 2)),
    db.Column('ci', db.Numeric(16, 2)),
    db.Column('co', db.Numeric(16, 2)),
    db.Column('ot', db.Numeric(16, 2)),
    db.Column('ttldiscount', db.Numeric(16, 2)),
    db.Column('netamt', db.Numeric(16, 2)),
    db.Column('inttransnum', db.String(20), nullable=False),
    db.Column('orderflag', db.String(20))
)


t_dg_storecode_nj = db.Table(
    'dg_storecode_nj',
    db.Column('flag', db.String(20), nullable=False),
    db.Column('storecode', db.String(20), nullable=False),
    db.Column('tillid', db.String(20), nullable=False),
    db.Column('txdate', db.String(20), nullable=False),
    db.Column('txtime', db.String(5), nullable=False),
    db.Column('docno', db.String(10), nullable=False),
    db.Column('vipcode', db.String(8)),
    db.Column('ch', db.Numeric(16, 2)),
    db.Column('ci', db.Numeric(16, 2)),
    db.Column('co', db.Numeric(16, 2)),
    db.Column('ot', db.Numeric(16, 2)),
    db.Column('ttldiscount', db.Numeric(16, 2)),
    db.Column('netamt', db.Numeric(16, 2)),
    db.Column('inttransnum', db.String(20), nullable=False)
)


t_dg_storecode_njdd = db.Table(
    'dg_storecode_njdd',
    db.Column('flag', db.String(20), nullable=False),
    db.Column('storecode', db.String(20), nullable=False),
    db.Column('tillid', db.String(20), nullable=False),
    db.Column('txdate', db.String(20), nullable=False),
    db.Column('txtime', db.String(5), nullable=False),
    db.Column('docno', db.String(10), nullable=False),
    db.Column('vipcode', db.String(8)),
    db.Column('ch', db.Numeric(16, 2)),
    db.Column('ci', db.Numeric(16, 2)),
    db.Column('co', db.Numeric(16, 2)),
    db.Column('ot', db.Numeric(16, 2)),
    db.Column('ttldiscount', db.Numeric(16, 2)),
    db.Column('netamt', db.Numeric(16, 2)),
    db.Column('inttransnum', db.String(20), nullable=False)
)


t_dg_storecode_njnzcfjc = db.Table(
    'dg_storecode_njnzcfjc',
    db.Column('flag', db.String(20), nullable=False),
    db.Column('storecode', db.String(20), nullable=False),
    db.Column('tillid', db.String(20), nullable=False),
    db.Column('txdate', db.String(20), nullable=False),
    db.Column('txtime', db.String(5), nullable=False),
    db.Column('docno', db.String(10), nullable=False),
    db.Column('vipcode', db.String(8)),
    db.Column('ch', db.Numeric(16, 2)),
    db.Column('ci', db.Numeric(16, 2)),
    db.Column('co', db.Numeric(16, 2)),
    db.Column('ot', db.Numeric(16, 2)),
    db.Column('ttldiscount', db.Numeric(16, 2)),
    db.Column('netamt', db.Numeric(16, 2)),
    db.Column('inttransnum', db.String(20), nullable=False)
)


t_dg_storecode_pdjcmdd_chdtp = db.Table(
    'dg_storecode_pdjcmdd_chdtp',
    db.Column('fdiscid', db.String(3), nullable=False),
    db.Column('fdesc2', db.String(20), nullable=False),
    db.Column('fdiscmeth', db.String(2), nullable=False)
)


t_dg_storecode_pdjcmdd_check = db.Table(
    'dg_storecode_pdjcmdd_check',
    db.Column('foutlet', db.String(4), nullable=False),
    db.Column('fdate', db.String(8), nullable=False),
    db.Column('fcheck', db.String(5), nullable=False),
    db.Column('ftimeopen', db.String(14), nullable=False),
    db.Column('ftimeclose', db.String(14), nullable=False),
    db.Column('fpaid', db.String(1), nullable=False),
    db.Column('fdiscpre', db.Numeric(13, 2)),
    db.Column('fitmtot', db.Numeric(13, 2)),
    db.Column('fcktot', db.Numeric(13, 2))
)


t_dg_storecode_pdjcmdd_chkdc = db.Table(
    'dg_storecode_pdjcmdd_chkdc',
    db.Column('foutlet', db.String(4), nullable=False),
    db.Column('fdate', db.String(8), nullable=False),
    db.Column('fdisckey', db.String(4), nullable=False),
    db.Column('fcheck', db.String(5), nullable=False),
    db.Column('fdiscid', db.String(3), nullable=False),
    db.Column('fdisctot', db.Numeric(13, 2))
)


t_dg_storecode_pdjcmdd_chkitm = db.Table(
    'dg_storecode_pdjcmdd_chkitm',
    db.Column('foutlet', db.String(4), nullable=False),
    db.Column('fdate', db.String(8), nullable=False),
    db.Column('fcheck', db.String(5), nullable=False),
    db.Column('fitem', db.String(8), nullable=False),
    db.Column('fitemkey', db.String(4), nullable=False),
    db.Column('fdescm2', db.String(40), nullable=False),
    db.Column('fdescs2', db.String(40), nullable=False),
    db.Column('fprice', db.Numeric(13, 2)),
    db.Column('fqty', db.Numeric(8, 3)),
    db.Column('ftotal', db.Numeric(13, 2)),
    db.Column('fordtime', db.String(14), nullable=False),
    db.Column('fmenudept', db.String(4)),
    db.Column('fmenucat', db.String(4))
)


t_dg_storecode_pdjcmdd_chkpm = db.Table(
    'dg_storecode_pdjcmdd_chkpm',
    db.Column('foutlet', db.String(4), nullable=False),
    db.Column('fdate', db.String(8), nullable=False),
    db.Column('fcheck', db.String(5), nullable=False),
    db.Column('fpayid', db.String(3), nullable=False),
    db.Column('fpaykey', db.String(4), nullable=False),
    db.Column('ftime', db.String(14), nullable=False),
    db.Column('fpayamt', db.Numeric(13, 2)),
    db.Column('fdesc1', db.String(20)),
    db.Column('fdesc2', db.String(20)),
    db.Column('fdesc3', db.String(20))
)


t_dg_storecode_pdjcmdd_chpmtp = db.Table(
    'dg_storecode_pdjcmdd_chpmtp',
    db.Column('fpayclass', db.String(2), nullable=False),
    db.Column('fpayid', db.String(3), nullable=False),
    db.Column('fdesc2', db.String(20), nullable=False),
    db.Column('fdesc1', db.String(20))
)


t_dg_storecode_pdjcmdd_menu = db.Table(
    'dg_storecode_pdjcmdd_menu',
    db.Column('fitem', db.String(8), nullable=False),
    db.Column('fdescl2', db.String(40), nullable=False),
    db.Column('fdescm2', db.String(40), nullable=False),
    db.Column('fdescs2', db.String(40), nullable=False),
    db.Column('fmenudept', db.String(4), nullable=False),
    db.Column('fmenucat', db.String(4), nullable=False),
    db.Column('fprice1', db.Numeric(13, 2), nullable=False)
)


t_dg_storecode_pdjcmdd_menucg = db.Table(
    'dg_storecode_pdjcmdd_menucg',
    db.Column('fmenucat', db.String(4), nullable=False),
    db.Column('fdesc2', db.String(30), nullable=False)
)


t_dg_storecode_pdjct1gj16_chdtp = db.Table(
    'dg_storecode_pdjct1gj16_chdtp',
    db.Column('fdiscid', db.String(3), nullable=False),
    db.Column('fdesc2', db.String(20), nullable=False),
    db.Column('fdiscmeth', db.String(2), nullable=False)
)


t_dg_storecode_pdjct1gj16_check = db.Table(
    'dg_storecode_pdjct1gj16_check',
    db.Column('foutlet', db.String(4), nullable=False),
    db.Column('fdate', db.String(8), nullable=False),
    db.Column('fcheck', db.String(5), nullable=False),
    db.Column('ftimeopen', db.String(14), nullable=False),
    db.Column('ftimeclose', db.String(14), nullable=False),
    db.Column('fpaid', db.String(1), nullable=False),
    db.Column('fdiscpre', db.Numeric(13, 2)),
    db.Column('fitmtot', db.Numeric(13, 2)),
    db.Column('fcktot', db.Numeric(13, 2))
)


t_dg_storecode_pdjct1gj16_chkdc = db.Table(
    'dg_storecode_pdjct1gj16_chkdc',
    db.Column('foutlet', db.String(4), nullable=False),
    db.Column('fdate', db.String(8), nullable=False),
    db.Column('fdisckey', db.String(4), nullable=False),
    db.Column('fcheck', db.String(5), nullable=False),
    db.Column('fdiscid', db.String(3), nullable=False),
    db.Column('fdisctot', db.Numeric(13, 2))
)


t_dg_storecode_pdjct1gj16_chkitm = db.Table(
    'dg_storecode_pdjct1gj16_chkitm',
    db.Column('foutlet', db.String(4), nullable=False),
    db.Column('fdate', db.String(8), nullable=False),
    db.Column('fcheck', db.String(5), nullable=False),
    db.Column('fitem', db.String(8), nullable=False),
    db.Column('fitemkey', db.String(4), nullable=False),
    db.Column('fdescm2', db.String(40), nullable=False),
    db.Column('fdescs2', db.String(40), nullable=False),
    db.Column('fprice', db.Numeric(13, 2)),
    db.Column('fqty', db.Numeric(8, 3)),
    db.Column('ftotal', db.Numeric(13, 2)),
    db.Column('fordtime', db.String(14), nullable=False),
    db.Column('fmenudept', db.String(4)),
    db.Column('fmenucat', db.String(4))
)


t_dg_storecode_pdjct1gj16_chkpm = db.Table(
    'dg_storecode_pdjct1gj16_chkpm',
    db.Column('foutlet', db.String(4), nullable=False),
    db.Column('fdate', db.String(8), nullable=False),
    db.Column('fcheck', db.String(5), nullable=False),
    db.Column('fpayid', db.String(3), nullable=False),
    db.Column('fpaykey', db.String(4), nullable=False),
    db.Column('ftime', db.String(14), nullable=False),
    db.Column('fpayamt', db.Numeric(13, 2)),
    db.Column('fdesc1', db.String(20)),
    db.Column('fdesc2', db.String(20)),
    db.Column('fdesc3', db.String(20))
)


t_dg_storecode_pdjct1gj16_chpmtp = db.Table(
    'dg_storecode_pdjct1gj16_chpmtp',
    db.Column('fpayclass', db.String(2), nullable=False),
    db.Column('fpayid', db.String(3), nullable=False),
    db.Column('fdesc2', db.String(20), nullable=False),
    db.Column('fdesc1', db.String(20))
)


t_dg_storecode_pdjct1gj16_menu = db.Table(
    'dg_storecode_pdjct1gj16_menu',
    db.Column('fitem', db.String(8), nullable=False),
    db.Column('fdescl2', db.String(40), nullable=False),
    db.Column('fdescm2', db.String(40), nullable=False),
    db.Column('fdescs2', db.String(40), nullable=False),
    db.Column('fmenudept', db.String(4), nullable=False),
    db.Column('fmenucat', db.String(4), nullable=False),
    db.Column('fprice1', db.Numeric(13, 2), nullable=False)
)


t_dg_storecode_pdjct1gj16_menucg = db.Table(
    'dg_storecode_pdjct1gj16_menucg',
    db.Column('fmenucat', db.String(4), nullable=False),
    db.Column('fdesc2', db.String(30), nullable=False)
)


t_dg_storecode_sjzx = db.Table(
    'dg_storecode_sjzx',
    db.Column('businessdate', db.String(20), nullable=False),
    db.Column('transdatetime', db.String(25), nullable=False),
    db.Column('countcode', db.String(12), nullable=False),
    db.Column('posno', db.String(8), nullable=False),
    db.Column('flowno', db.String(8), nullable=False),
    db.Column('payno', db.String(5), nullable=False),
    db.Column('currency', db.String(150), nullable=False),
    db.Column('cardno', db.String(8)),
    db.Column('amount', db.Numeric(16, 2))
)


t_dg_storecode_szzcfc = db.Table(
    'dg_storecode_szzcfc',
    db.Column('flag', db.String(20), nullable=False),
    db.Column('storecode', db.String(20), nullable=False),
    db.Column('tillid', db.String(20), nullable=False),
    db.Column('txdate', db.String(20), nullable=False),
    db.Column('txtime', db.String(5), nullable=False),
    db.Column('docno', db.String(10), nullable=False),
    db.Column('vipcode', db.String(8)),
    db.Column('ch', db.Numeric(16, 2)),
    db.Column('ci', db.Numeric(16, 2)),
    db.Column('co', db.Numeric(16, 2)),
    db.Column('ot', db.Numeric(16, 2)),
    db.Column('ttldiscount', db.Numeric(16, 2)),
    db.Column('netamt', db.Numeric(16, 2)),
    db.Column('inttransnum', db.String(20), nullable=False),
    db.Column('orderflag', db.String(20))
)


t_dg_storecode_wggc = db.Table(
    'dg_storecode_wggc',
    db.Column('storecode', db.String(20), nullable=False),
    db.Column('tillid', db.String(20), nullable=False),
    db.Column('txdate', db.String(20), nullable=False),
    db.Column('txtime', db.String(5), nullable=False),
    db.Column('docno', db.String(10), nullable=False),
    db.Column('plu', db.String(20)),
    db.Column('vipcode', db.String(8)),
    db.Column('ch', db.Numeric(16, 2)),
    db.Column('ci', db.Numeric(16, 2)),
    db.Column('co', db.Numeric(16, 2)),
    db.Column('ot', db.Numeric(16, 2)),
    db.Column('ttldiscount', db.Numeric(16, 2)),
    db.Column('netamt', db.Numeric(16, 2))
)


t_dg_storecode_wxgt = db.Table(
    'dg_storecode_wxgt',
    db.Column('flag', db.String(20), nullable=False),
    db.Column('storecode', db.String(20), nullable=False),
    db.Column('tillid', db.String(20), nullable=False),
    db.Column('txdate', db.String(20), nullable=False),
    db.Column('txtime', db.String(5), nullable=False),
    db.Column('docno', db.String(10), nullable=False),
    db.Column('vipcode', db.String(8)),
    db.Column('ch', db.Numeric(16, 2)),
    db.Column('ci', db.Numeric(16, 2)),
    db.Column('co', db.Numeric(16, 2)),
    db.Column('ot', db.Numeric(16, 2)),
    db.Column('ttldiscount', db.Numeric(16, 2)),
    db.Column('netamt', db.Numeric(16, 2)),
    db.Column('inttransnum', db.String(20), nullable=False),
    db.Column('orderflag', db.String(20))
)


t_dg_storecode_wxhlgc = db.Table(
    'dg_storecode_wxhlgc',
    db.Column('storecode', db.String(20), nullable=False),
    db.Column('tillid', db.String(20), nullable=False),
    db.Column('txdate', db.String(20), nullable=False),
    db.Column('txtime', db.String(5), nullable=False),
    db.Column('docno', db.String(10), nullable=False),
    db.Column('plu', db.String(20), nullable=False),
    db.Column('vipcode', db.String(8)),
    db.Column('ch', db.Numeric(16, 2)),
    db.Column('ci', db.Numeric(16, 2)),
    db.Column('co', db.Numeric(16, 2)),
    db.Column('ot', db.Numeric(16, 2)),
    db.Column('ttldiscount', db.Numeric(16, 2)),
    db.Column('netamt', db.Numeric(16, 2))
)


t_dg_storecode_xggc = db.Table(
    'dg_storecode_xggc',
    db.Column('storecode', db.String(20), nullable=False),
    db.Column('tillid', db.String(20), nullable=False),
    db.Column('txdate', db.String(20), nullable=False),
    db.Column('txtime', db.String(5), nullable=False),
    db.Column('docno', db.String(10), nullable=False),
    db.Column('plu', db.String(20)),
    db.Column('vipcode', db.String(8)),
    db.Column('ch', db.Numeric(16, 2)),
    db.Column('ci', db.Numeric(16, 2)),
    db.Column('co', db.Numeric(16, 2)),
    db.Column('ot', db.Numeric(16, 2)),
    db.Column('ttldiscount', db.Numeric(16, 2)),
    db.Column('netamt', db.Numeric(16, 2))
)


t_dg_storecode_xhtd_ad = db.Table(
    'dg_storecode_xhtd_ad',
    db.Column('tenant', db.String(20), nullable=False),
    db.Column('outlet', db.String(20), nullable=False),
    db.Column('tranid', db.String(10), nullable=False),
    db.Column('voidid', db.String(20)),
    db.Column('voidreason', db.String(5)),
    db.Column('adjdate', db.String(20), nullable=False),
    db.Column('adjtime', db.String(6), nullable=False),
    db.Column('adjemp', db.String(20)),
    db.Column('adjdisc', db.Numeric(12, 2), nullable=False),
    db.Column('adjtype', db.String(10), nullable=False),
    db.Column('adjcode', db.String(20), nullable=False),
    db.Column('adjname', db.String(50), nullable=False)
)


t_dg_storecode_xhtd_pa = db.Table(
    'dg_storecode_xhtd_pa',
    db.Column('tenant', db.String(20), nullable=False),
    db.Column('outlet', db.String(20), nullable=False),
    db.Column('tranid', db.String(10), nullable=False),
    db.Column('voidid', db.String(20)),
    db.Column('voidreason', db.String(5)),
    db.Column('paydate', db.String(20), nullable=False),
    db.Column('paytime', db.String(6), nullable=False),
    db.Column('payemp', db.String(20)),
    db.Column('payamt', db.Numeric(12, 2), nullable=False),
    db.Column('paytype', db.String(10), nullable=False),
    db.Column('paycode', db.String(20), nullable=False),
    db.Column('payname', db.String(50), nullable=False),
    db.Column('paytip', db.Numeric(12, 2), nullable=False)
)


t_dg_storecode_xhtd_sh = db.Table(
    'dg_storecode_xhtd_sh',
    db.Column('tenant', db.String(20), nullable=False),
    db.Column('outlet', db.String(20), nullable=False),
    db.Column('tranid', db.String(10), nullable=False),
    db.Column('termid', db.String(20)),
    db.Column('tblnum', db.String(20)),
    db.Column('grpnum', db.String(10)),
    db.Column('txdate', db.String(20), nullable=False),
    db.Column('voidid', db.String(20)),
    db.Column('voidreason', db.String(5)),
    db.Column('opendate', db.String(20), nullable=False),
    db.Column('opentime', db.String(6), nullable=False),
    db.Column('openemp', db.String(20)),
    db.Column('clsdate', db.String(20), nullable=False),
    db.Column('clstime', db.String(6), nullable=False),
    db.Column('clsemp', db.String(20)),
    db.Column('sales', db.Numeric(12, 2), nullable=False),
    db.Column('srvchg', db.Numeric(12, 2), nullable=False),
    db.Column('discount', db.Numeric(12, 2), nullable=False),
    db.Column('taxamt', db.Numeric(12, 2), nullable=False),
    db.Column('roundup', db.Numeric(12, 2), nullable=False),
    db.Column('cover', db.Integer),
    db.Column('memidvip', db.String(20))
)


t_dg_storecode_xhtd_si = db.Table(
    'dg_storecode_xhtd_si',
    db.Column('tenant', db.String(20), nullable=False),
    db.Column('outlet', db.String(20), nullable=False),
    db.Column('tranid', db.String(10), nullable=False),
    db.Column('voidid', db.String(20)),
    db.Column('voidreason', db.String(5)),
    db.Column('orddate', db.String(20), nullable=False),
    db.Column('ordtime', db.String(6), nullable=False),
    db.Column('ordemp', db.String(20)),
    db.Column('unitprice', db.Numeric(12, 2), nullable=False),
    db.Column('ordqty', db.Numeric(12, 2), nullable=False),
    db.Column('itemdisc', db.Numeric(12, 2), nullable=False),
    db.Column('amt', db.Numeric(12, 2), nullable=False),
    db.Column('itemcode', db.String(20), nullable=False),
    db.Column('itemname', db.String(50), nullable=False),
    db.Column('catko', db.String(10), nullable=False)
)


t_dg_storecode_xsjc01dtl = db.Table(
    'dg_storecode_xsjc01dtl',
    db.Column('storecode', db.String(20), nullable=False),
    db.Column('tillid', db.String(20), nullable=False),
    db.Column('txdate', db.String(20), nullable=False),
    db.Column('txtime', db.String(6), nullable=False),
    db.Column('docno', db.String(10), nullable=False),
    db.Column('userno', db.String(20), nullable=False),
    db.Column('huohao', db.String(20), nullable=False),
    db.Column('cur_qty', db.Numeric(16, 2)),
    db.Column('discount_amt', db.Numeric(16, 2)),
    db.Column('net_amt', db.Numeric(16, 2)),
    db.Column('cash_amt', db.Numeric(16, 2)),
    db.Column('card_amt', db.Numeric(16, 2))
)


t_dg_storecode_xsjc01itm = db.Table(
    'dg_storecode_xsjc01itm',
    db.Column('plu_no', db.String(20), nullable=False),
    db.Column('plu_name', db.String(100), nullable=False),
    db.Column('unit', db.String(20)),
    db.Column('cursell', db.Numeric(16, 2)),
    db.Column('huohao', db.String(20), nullable=False)
)


t_dg_storecode_xsjc02dtl = db.Table(
    'dg_storecode_xsjc02dtl',
    db.Column('storecode', db.String(20), nullable=False),
    db.Column('tillid', db.String(20), nullable=False),
    db.Column('txdate', db.String(20), nullable=False),
    db.Column('txtime', db.String(6), nullable=False),
    db.Column('docno', db.String(10), nullable=False),
    db.Column('userno', db.String(20), nullable=False),
    db.Column('huohao', db.String(20), nullable=False),
    db.Column('cur_qty', db.Numeric(16, 2)),
    db.Column('discount_amt', db.Numeric(16, 2)),
    db.Column('net_amt', db.Numeric(16, 2)),
    db.Column('cash_amt', db.Numeric(16, 2)),
    db.Column('card_amt', db.Numeric(16, 2))
)


t_dg_storecode_xsjc02itm = db.Table(
    'dg_storecode_xsjc02itm',
    db.Column('plu_no', db.String(20), nullable=False),
    db.Column('plu_name', db.String(100), nullable=False),
    db.Column('unit', db.String(20)),
    db.Column('cursell', db.Numeric(16, 2)),
    db.Column('huohao', db.String(20), nullable=False)
)


t_dg_storecode_yxgt = db.Table(
    'dg_storecode_yxgt',
    db.Column('flag', db.String(20), nullable=False),
    db.Column('storecode', db.String(20), nullable=False),
    db.Column('tillid', db.String(20), nullable=False),
    db.Column('txdate', db.String(20), nullable=False),
    db.Column('txtime', db.String(5), nullable=False),
    db.Column('docno', db.String(10), nullable=False),
    db.Column('vipcode', db.String(8)),
    db.Column('ch', db.Numeric(16, 2)),
    db.Column('ci', db.Numeric(16, 2)),
    db.Column('co', db.Numeric(16, 2)),
    db.Column('ot', db.Numeric(16, 2)),
    db.Column('ttldiscount', db.Numeric(16, 2)),
    db.Column('netamt', db.Numeric(16, 2)),
    db.Column('inttransnum', db.String(20), nullable=False),
    db.Column('orderflag', db.String(20))
)


t_dg_storecode_yxhqg = db.Table(
    'dg_storecode_yxhqg',
    db.Column('storecode', db.String(20), nullable=False),
    db.Column('tillid', db.String(20), nullable=False),
    db.Column('flowno', db.String(12), nullable=False),
    db.Column('itemcode', db.String(20), nullable=False),
    db.Column('itemname', db.String(50), nullable=False),
    db.Column('dblqtysold', db.Numeric(16, 2)),
    db.Column('netamt', db.Numeric(16, 2)),
    db.Column('ttldiscount', db.Numeric(16, 2)),
    db.Column('ch', db.Numeric(16, 2)),
    db.Column('ci', db.Numeric(16, 2)),
    db.Column('waiguapos', db.Numeric(16, 2)),
    db.Column('chuzhika', db.Numeric(16, 2)),
    db.Column('cheque', db.Numeric(16, 2)),
    db.Column('vouchers', db.Numeric(16, 2)),
    db.Column('transdatetime', db.String(20), nullable=False)
)


t_dhl_if_col_name = db.Table(
    'dhl_if_col_name',
    db.Column('own_name', db.String(50)),
    db.Column('table_name', db.String(50)),
    db.Column('col_name', db.String(50)),
    db.Column('output_name', db.String(50)),
    db.Column('type', db.String(50)),
    db.Column('s_no', db.Integer)
)


t_dhl_if_fsh_exel = db.Table(
    'dhl_if_fsh_exel',
    db.Column('netno', db.String(20)),
    db.Column('eng_netno', db.String(100)),
    db.Column('opendate', db.String(20)),
    db.Column('amt', db.Float),
    db.Column('cus', db.Float),
    db.Column('week_end_date', db.DateTime),
    db.Column('days', db.Integer, nullable=False)
)


t_dhl_if_fsh_item = db.Table(
    'dhl_if_fsh_item',
    db.Column('plu_id', db.String(50)),
    db.Column('plunameeng', db.String(100)),
    db.Column('spscc', db.String(20)),
    db.Column('ssscc', db.String(20)),
    db.Column('create_date', db.DateTime, server_default=db.FetchedValue()),
    db.Column('cat_no', db.String(20)),
    db.Column('group_no', db.String(20)),
    db.Column('price', db.Integer)
)


t_dhl_if_fsh_monthylsales = db.Table(
    'dhl_if_fsh_monthylsales',
    db.Column('plunameeng', db.String(100)),
    db.Column('spscc', db.String(20)),
    db.Column('ssscc', db.String(20)),
    db.Column('qty', db.Numeric(20, 5)),
    db.Column('net_count', db.Integer),
    db.Column('monthly', db.String(10)),
    db.Column('crate_date', db.DateTime, server_default=db.FetchedValue())
)


t_dhl_if_fsh_txt = db.Table(
    'dhl_if_fsh_txt',
    db.Column('sn', db.Integer),
    db.Column('text', db.String(200)),
    db.Column('header', db.String(10)),
    db.Column('create_date', db.DateTime, server_default=db.FetchedValue()),
    db.Column('file_name', db.String(50), index=True),
    db.Column('business_date', db.DateTime)
)


t_dhl_if_fsh_txt_chk_temp = db.Table(
    'dhl_if_fsh_txt_chk_temp',
    db.Column('file_name', db.String(100)),
    db.Column('week_begin', db.DateTime),
    db.Column('week_end', db.DateTime),
    db.Column('netno', db.String(10)),
    db.Column('amt', db.String(20)),
    db.Column('cus', db.String(20)),
    db.Column('days', db.String(10))
)


t_dhl_if_fsh_txt_temp = db.Table(
    'dhl_if_fsh_txt_temp',
    db.Column('sn', db.Integer),
    db.Column('text', db.String(200)),
    db.Column('header', db.String(10)),
    db.Column('create_date', db.DateTime),
    db.Column('file_name', db.String(50)),
    db.Column('business_date', db.DateTime)
)


t_dhl_if_grn_detail = db.Table(
    'dhl_if_grn_detail',
    db.Column('extractlineid', db.Integer),
    db.Column('pono', db.String(10)),
    db.Column('polineno', db.String(4)),
    db.Column('receiptqty', db.String(19)),
    db.Column('reptreference', db.String(10)),
    db.Column('auditdate', db.String(8)),
    db.Column('itemno', db.String(10)),
    db.Column('distribcenterid', db.String(5)),
    db.Index('grn_dtl', 'pono', 'itemno')
)


t_dhl_if_grn_detail_inpt = db.Table(
    'dhl_if_grn_detail_inpt',
    db.Column('extractlineid', db.Integer),
    db.Column('pono', db.String(10)),
    db.Column('polineno', db.String(4)),
    db.Column('receiptqty', db.String(19)),
    db.Column('reptreference', db.String(10)),
    db.Column('auditdate', db.String(8)),
    db.Column('itemno', db.String(10)),
    db.Column('distribcenterid', db.String(5))
)


t_dhl_if_grn_header = db.Table(
    'dhl_if_grn_header',
    db.Column('extractrcptconfid', db.Integer),
    db.Column('pono', db.String(10)),
    db.Column('grndate', db.String(8)),
    db.Column('grnref', db.String(10)),
    db.Column('comments', db.String(25)),
    db.Column('bucode', db.String(3)),
    db.Column('status', db.String(1), server_default=db.FetchedValue()),
    db.Column('create_date', db.DateTime, server_default=db.FetchedValue()),
    db.Index('grn_index', 'pono', 'create_date')
)


t_dhl_if_grn_header_inpt = db.Table(
    'dhl_if_grn_header_inpt',
    db.Column('extractrcptconfid', db.Integer),
    db.Column('pono', db.String(10)),
    db.Column('grndate', db.String(8)),
    db.Column('grnref', db.String(10)),
    db.Column('comments', db.String(25)),
    db.Column('bucode', db.String(3)),
    db.Column('status', db.String(1), server_default=db.FetchedValue()),
    db.Column('create_date', db.DateTime, server_default=db.FetchedValue())
)


t_dhl_if_grn_root = db.Table(
    'dhl_if_grn_root',
    db.Column('senderid', db.String(5)),
    db.Column('receiverid', db.String(5)),
    db.Column('extractid', db.String(35)),
    db.Column('extracttimestamp', db.String(25)),
    db.Column('extractlinecount', db.Numeric(asdecimal=False)),
    db.Column('header_name', db.String(50)),
    db.Column('detail_name', db.String(50)),
    db.Column('header_key', db.String(50)),
    db.Column('master_name', db.String(50)),
    db.Column('file_name', db.String(50))
)


t_dhl_if_iaj_header = db.Table(
    'dhl_if_iaj_header',
    db.Column('extractlineid', db.Integer),
    db.Column('movementreference', db.String(10)),
    db.Column('distribcenterid', db.String(5)),
    db.Column('itemno', db.String(15)),
    db.Column('movementdate', db.String(8)),
    db.Column('reptissueindicator', db.String(1)),
    db.Column('reptreference', db.String(10)),
    db.Column('adjustmentqty', db.Integer),
    db.Column('auditdate', db.String(8)),
    db.Column('reasoncode', db.String(15)),
    db.Column('stockunitcode', db.String(5)),
    db.Column('bucode', db.String(3))
)


t_dhl_if_iaj_header_inpt = db.Table(
    'dhl_if_iaj_header_inpt',
    db.Column('extractlineid', db.Integer),
    db.Column('movementreference', db.String(10)),
    db.Column('distribcenterid', db.String(5)),
    db.Column('itemno', db.String(15), index=True),
    db.Column('movementdate', db.String(8)),
    db.Column('reptissueindicator', db.String(1)),
    db.Column('reptreference', db.String(10)),
    db.Column('adjustmentqty', db.Integer),
    db.Column('auditdate', db.String(8)),
    db.Column('reasoncode', db.String(15)),
    db.Column('stockunitcode', db.String(5)),
    db.Column('bucode', db.String(3))
)


t_dhl_if_iaj_root = db.Table(
    'dhl_if_iaj_root',
    db.Column('senderid', db.String(5)),
    db.Column('receiverid', db.String(5)),
    db.Column('extractid', db.String(35)),
    db.Column('extracttimestamp', db.String(25)),
    db.Column('extractlinecount', db.Numeric(asdecimal=False)),
    db.Column('header_name', db.String(50)),
    db.Column('detail_name', db.String(50)),
    db.Column('header_key', db.String(50)),
    db.Column('master_name', db.String(50)),
    db.Column('file_name', db.String(50))
)


t_dhl_if_interface_root = db.Table(
    'dhl_if_interface_root',
    db.Column('senderid', db.String(5)),
    db.Column('receiverid', db.String(5)),
    db.Column('extractid', db.String(50)),
    db.Column('extracttimestamp', db.String(25)),
    db.Column('extractlinecount', db.Numeric(asdecimal=False)),
    db.Column('header_name', db.String(50)),
    db.Column('detail_name', db.String(50)),
    db.Column('header_key', db.String(50)),
    db.Column('master_name', db.String(50)),
    db.Column('file_name', db.String(50)),
    db.Column('file_header', db.String(50)),
    db.Column('header_h_name', db.String(50)),
    db.Column('detail_h_name', db.String(50)),
    db.Column('detail_key', db.String(50)),
    db.Column('ddtl_h_name', db.String(50)),
    db.Column('ddtl_name', db.String(50)),
    db.Column('own_name', db.String(50))
)


t_dhl_if_iss_header = db.Table(
    'dhl_if_iss_header',
    db.Column('extractlineid', db.Integer),
    db.Column('bucode', db.String(3)),
    db.Column('distribcenterid', db.String(5)),
    db.Column('itemno', db.String(15)),
    db.Column('reportdate', db.String(8)),
    db.Column('availableqty', db.Integer),
    db.Column('awaitingdeliverqty', db.Integer),
    db.Column('onholdqty', db.Integer),
    db.Column('stockunitcode', db.String(5)),
    db.Column('auditdate', db.String(8))
)


t_dhl_if_iss_header_inpt = db.Table(
    'dhl_if_iss_header_inpt',
    db.Column('extractlineid', db.Integer),
    db.Column('bucode', db.String(3)),
    db.Column('distribcenterid', db.String(5)),
    db.Column('itemno', db.String(15)),
    db.Column('reportdate', db.String(8)),
    db.Column('availableqty', db.Integer),
    db.Column('awaitingdeliverqty', db.Integer),
    db.Column('onholdqty', db.Integer),
    db.Column('stockunitcode', db.String(5)),
    db.Column('auditdate', db.String(8))
)


t_dhl_if_iss_root = db.Table(
    'dhl_if_iss_root',
    db.Column('senderid', db.String(5)),
    db.Column('receiverid', db.String(5)),
    db.Column('extractid', db.String(35)),
    db.Column('extracttimestamp', db.String(25)),
    db.Column('extractlinecount', db.Numeric(asdecimal=False)),
    db.Column('header_name', db.String(50)),
    db.Column('detail_name', db.String(50)),
    db.Column('header_key', db.String(50)),
    db.Column('master_name', db.String(50)),
    db.Column('file_name', db.String(50))
)


t_dhl_if_item_master_header = db.Table(
    'dhl_if_item_master_header',
    db.Column('extractlineid', db.Numeric(asdecimal=False)),
    db.Column('bucode', db.String(5)),
    db.Column('itemno', db.String(10)),
    db.Column('skucode', db.String(10)),
    db.Column('effdatefrom', db.String(8)),
    db.Column('itemdescriptionchn', db.String(60)),
    db.Column('itemdescription', db.String(30)),
    db.Column('pickpackuom', db.String(5)),
    db.Column('hscode', db.String(15)),
    db.Column('productclasscode', db.String(15)),
    db.Column('countryoforigin', db.String(15)),
    db.Column('create_date', db.DateTime, server_default=db.FetchedValue()),
    db.Column('file_name', db.String(60)),
    db.Index('idx_if_item_masterher', 'create_date', 'file_name')
)


t_dhl_if_item_master_root = db.Table(
    'dhl_if_item_master_root',
    db.Column('senderid', db.String(5)),
    db.Column('receiverid', db.String(5)),
    db.Column('extractid', db.String(50)),
    db.Column('extracttimestamp', db.String(50)),
    db.Column('extractlinecount', db.Numeric(asdecimal=False)),
    db.Column('header_name', db.String(50)),
    db.Column('detail_name', db.String(50)),
    db.Column('header_key', db.String(50)),
    db.Column('master_name', db.String(50)),
    db.Column('file_name', db.String(50)),
    db.Column('file_header', db.String(50)),
    db.Column('create_date', db.DateTime, server_default=db.FetchedValue())
)


t_dhl_if_log = db.Table(
    'dhl_if_log',
    db.Column('pid', db.String(50)),
    db.Column('task_code', db.String(50)),
    db.Column('task_setp', db.String(50)),
    db.Column('task_name', db.String(50)),
    db.Column('begin_date', db.DateTime),
    db.Column('end_date', db.DateTime),
    db.Column('type', db.String(1)),
    db.Column('message', db.String(500)),
    db.Column('file_name', db.String(150), server_default=db.FetchedValue()),
    db.Column('row_num', db.Integer)
)


t_dhl_if_po_detail = db.Table(
    'dhl_if_po_detail',
    db.Column('extractlineid', db.Integer),
    db.Column('pono', db.String(10)),
    db.Column('polineno', db.String(4)),
    db.Column('distribcenterid', db.String(5)),
    db.Column('itemno', db.String(15)),
    db.Column('orderdate', db.String(8)),
    db.Column('exptrcptqty', db.Integer),
    db.Column('rcptuom', db.String(5)),
    db.Index('id_po_detal', 'polineno', 'itemno')
)


t_dhl_if_po_detail_view = db.Table(
    'dhl_if_po_detail_view',
    db.Column('extractlineid', db.Integer),
    db.Column('pono', db.String(10)),
    db.Column('polineno', db.String(4)),
    db.Column('distribcenterid', db.String(5)),
    db.Column('itemno', db.String(15)),
    db.Column('orderdate', db.String(8)),
    db.Column('exptrcptqty', db.Integer),
    db.Column('rcptuom', db.String(5)),
    db.Index('id_po_detal_view', 'polineno', 'itemno')
)


t_dhl_if_po_header = db.Table(
    'dhl_if_po_header',
    db.Column('extractexptrcptid', db.Integer),
    db.Column('pono', db.String(10), index=True),
    db.Column('supplierid', db.String(30)),
    db.Column('orderdate', db.String(8)),
    db.Column('potype', db.String(5)),
    db.Column('exptrcptdate', db.String(8)),
    db.Column('secondref', db.String(15)),
    db.Column('comments', db.String(25)),
    db.Column('address1', db.String(35)),
    db.Column('address2', db.String(35)),
    db.Column('address3', db.String(35)),
    db.Column('address4', db.String(35)),
    db.Column('address5', db.String(35)),
    db.Column('address6', db.String(35)),
    db.Column('bucode', db.String(3)),
    db.Column('file_name', db.String(50))
)


t_dhl_if_po_header_view = db.Table(
    'dhl_if_po_header_view',
    db.Column('extractexptrcptid', db.Integer),
    db.Column('pono', db.String(10), index=True),
    db.Column('supplierid', db.String(30)),
    db.Column('orderdate', db.String(8)),
    db.Column('potype', db.String(5)),
    db.Column('exptrcptdate', db.String(8)),
    db.Column('secondref', db.String(15)),
    db.Column('comments', db.String(25)),
    db.Column('address1', db.String(35)),
    db.Column('address2', db.String(35)),
    db.Column('address3', db.String(35)),
    db.Column('address4', db.String(35)),
    db.Column('address5', db.String(35)),
    db.Column('address6', db.String(35)),
    db.Column('bucode', db.String(3)),
    db.Column('file_name', db.String(50))
)


t_dhl_if_po_root = db.Table(
    'dhl_if_po_root',
    db.Column('senderid', db.String(5)),
    db.Column('receiverid', db.String(5)),
    db.Column('extractid', db.String(50)),
    db.Column('extracttimestamp', db.String(25)),
    db.Column('extractlinecount', db.Numeric(asdecimal=False)),
    db.Column('header_name', db.String(50)),
    db.Column('detail_name', db.String(50)),
    db.Column('header_key', db.String(50)),
    db.Column('master_name', db.String(50)),
    db.Column('file_name', db.String(50)),
    db.Column('file_header', db.String(50)),
    db.Column('create_date', db.DateTime, server_default=db.FetchedValue())
)


t_dhl_if_po_root_view = db.Table(
    'dhl_if_po_root_view',
    db.Column('senderid', db.String(5)),
    db.Column('receiverid', db.String(5)),
    db.Column('extractid', db.String(50)),
    db.Column('extracttimestamp', db.String(25)),
    db.Column('extractlinecount', db.Numeric(asdecimal=False)),
    db.Column('header_name', db.String(50)),
    db.Column('detail_name', db.String(50)),
    db.Column('header_key', db.String(50)),
    db.Column('master_name', db.String(50)),
    db.Column('file_name', db.String(50)),
    db.Column('file_header', db.String(50))
)


t_dhl_if_rcv_detail = db.Table(
    'dhl_if_rcv_detail',
    db.Column('extractlineid', db.Integer),
    db.Column('sono', db.String(10)),
    db.Column('polineno', db.String(4)),
    db.Column('qty', db.String(19)),
    db.Column('reptreference', db.String(50)),
    db.Column('auditdate', db.String(8)),
    db.Column('itemno', db.String(10)),
    db.Column('distribcenterid', db.String(5))
)


t_dhl_if_rcv_detail_inpt = db.Table(
    'dhl_if_rcv_detail_inpt',
    db.Column('extractlineid', db.Integer),
    db.Column('sono', db.String(10), index=True),
    db.Column('polineno', db.String(4)),
    db.Column('qty', db.String(19)),
    db.Column('reptreference', db.String(30)),
    db.Column('auditdate', db.String(8)),
    db.Column('itemno', db.String(10)),
    db.Column('distribcenterid', db.String(5))
)


t_dhl_if_rcv_header = db.Table(
    'dhl_if_rcv_header',
    db.Column('extractrcptconfid', db.Integer),
    db.Column('sono', db.String(10), index=True),
    db.Column('rcvdate', db.String(8)),
    db.Column('grnref', db.String(10)),
    db.Column('comments', db.String(25)),
    db.Column('bucode', db.String(3)),
    db.Column('status', db.String(1), server_default=db.FetchedValue()),
    db.Column('create_date', db.DateTime, server_default=db.FetchedValue())
)


t_dhl_if_rcv_header_inpt = db.Table(
    'dhl_if_rcv_header_inpt',
    db.Column('extractrcptconfid', db.Integer),
    db.Column('sono', db.String(10)),
    db.Column('rcvdate', db.String(8)),
    db.Column('grnref', db.String(10)),
    db.Column('comments', db.String(25)),
    db.Column('bucode', db.String(3)),
    db.Column('status', db.String(1), server_default=db.FetchedValue()),
    db.Column('create_date', db.DateTime, server_default=db.FetchedValue())
)


t_dhl_if_rcv_root = db.Table(
    'dhl_if_rcv_root',
    db.Column('senderid', db.String(5)),
    db.Column('receiverid', db.String(5)),
    db.Column('extractid', db.String(35)),
    db.Column('extracttimestamp', db.String(25)),
    db.Column('extractlinecount', db.Numeric(asdecimal=False)),
    db.Column('header_name', db.String(50)),
    db.Column('detail_name', db.String(50)),
    db.Column('header_key', db.String(50)),
    db.Column('master_name', db.String(50)),
    db.Column('file_name', db.String(50))
)


t_dhl_if_shc_detail = db.Table(
    'dhl_if_shc_detail',
    db.Column('extractlineid', db.Integer),
    db.Column('sono', db.String(10), index=True),
    db.Column('orderlineno', db.String(3)),
    db.Column('distribcenterid', db.String(5)),
    db.Column('itemno', db.String(15), index=True),
    db.Column('deliverydate', db.String(8)),
    db.Column('orderqty', db.Integer),
    db.Column('actualdeliverydate', db.String(8)),
    db.Column('reptreference', db.String(10)),
    db.Column('fixedassetcode', db.String(10)),
    db.Column('unitprice', db.Numeric(asdecimal=False))
)


t_dhl_if_shc_detail_inpt = db.Table(
    'dhl_if_shc_detail_inpt',
    db.Column('extractlineid', db.Integer),
    db.Column('sono', db.String(10)),
    db.Column('orderlineno', db.String(3)),
    db.Column('distribcenterid', db.String(5)),
    db.Column('itemno', db.String(15)),
    db.Column('deliverydate', db.String(8)),
    db.Column('orderqty', db.Integer),
    db.Column('actualdeliverydate', db.String(8)),
    db.Column('reptreference', db.String(10)),
    db.Column('fixedassetcode', db.String(10)),
    db.Column('unitprice', db.Numeric(asdecimal=False))
)


t_dhl_if_shc_header = db.Table(
    'dhl_if_shc_header',
    db.Column('extractrcptconfid', db.Integer),
    db.Column('sono', db.String(10)),
    db.Column('customercode', db.String(10)),
    db.Column('customerreference', db.String(25)),
    db.Column('orderdate', db.String(8)),
    db.Column('ordertype', db.String(5)),
    db.Column('debitcreditindicator', db.String(1)),
    db.Column('deliveryaddresscode', db.String(10)),
    db.Column('bucode', db.String(3)),
    db.Column('create_date', db.DateTime, server_default=db.FetchedValue()),
    db.Column('status', db.String(1), server_default=db.FetchedValue())
)


t_dhl_if_shc_header_inpt = db.Table(
    'dhl_if_shc_header_inpt',
    db.Column('extractrcptconfid', db.Integer),
    db.Column('sono', db.String(10)),
    db.Column('customercode', db.String(10)),
    db.Column('customerreference', db.String(25)),
    db.Column('orderdate', db.String(8)),
    db.Column('ordertype', db.String(5)),
    db.Column('debitcreditindicator', db.String(1)),
    db.Column('deliveryaddresscode', db.String(10)),
    db.Column('bucode', db.String(3)),
    db.Column('create_date', db.DateTime, server_default=db.FetchedValue()),
    db.Column('status', db.String(1), server_default=db.FetchedValue())
)


t_dhl_if_shc_root = db.Table(
    'dhl_if_shc_root',
    db.Column('senderid', db.String(5)),
    db.Column('receiverid', db.String(5)),
    db.Column('extractid', db.String(35)),
    db.Column('extracttimestamp', db.String(25)),
    db.Column('extractlinecount', db.Numeric(asdecimal=False)),
    db.Column('header_name', db.String(50)),
    db.Column('detail_name', db.String(50)),
    db.Column('header_key', db.String(50)),
    db.Column('master_name', db.String(50)),
    db.Column('file_name', db.String(50))
)


t_dhl_if_so_detail = db.Table(
    'dhl_if_so_detail',
    db.Column('extractlineid', db.Integer),
    db.Column('sono', db.String(10)),
    db.Column('orderlineno', db.String(5)),
    db.Column('distribcenterid', db.String(5)),
    db.Column('itemno', db.String(15)),
    db.Column('deliverydate', db.String(8)),
    db.Column('orderqty', db.Integer),
    db.Column('uom', db.String(5)),
    db.Column('fixedassetcode', db.String(10)),
    db.Column('unitprice', db.Numeric(asdecimal=False)),
    db.Index('index_so_detail', 'sono', 'itemno')
)


t_dhl_if_so_detail_view = db.Table(
    'dhl_if_so_detail_view',
    db.Column('extractlineid', db.Integer),
    db.Column('sono', db.String(10)),
    db.Column('orderlineno', db.String(5)),
    db.Column('distribcenterid', db.String(5)),
    db.Column('itemno', db.String(15)),
    db.Column('deliverydate', db.String(8)),
    db.Column('orderqty', db.Integer),
    db.Column('uom', db.String(5)),
    db.Column('fixedassetcode', db.String(10)),
    db.Column('unitprice', db.Numeric(asdecimal=False))
)


t_dhl_if_so_header = db.Table(
    'dhl_if_so_header',
    db.Column('extractorderid', db.Integer),
    db.Column('sono', db.String(10), index=True),
    db.Column('customercode', db.String(10)),
    db.Column('orderdate', db.String(8)),
    db.Column('sotype', db.String(5)),
    db.Column('debitcreditindicator', db.String(1)),
    db.Column('deliveryaddresscode', db.String(10)),
    db.Column('customerreference', db.String(25)),
    db.Column('comments', db.String(25)),
    db.Column('address1', db.String(35)),
    db.Column('address2', db.String(50)),
    db.Column('address3', db.String(35)),
    db.Column('address4', db.String(35)),
    db.Column('address5', db.String(35)),
    db.Column('address6', db.String(35)),
    db.Column('bucode', db.String(3)),
    db.Column('printvatdetail', db.String(1)),
    db.Column('file_name', db.String(50)),
    db.Column('is_fsh_po', db.String(1), server_default=db.FetchedValue())
)


t_dhl_if_so_header_view = db.Table(
    'dhl_if_so_header_view',
    db.Column('extractorderid', db.Integer),
    db.Column('sono', db.String(10)),
    db.Column('customercode', db.String(10)),
    db.Column('orderdate', db.String(8)),
    db.Column('sotype', db.String(5)),
    db.Column('debitcreditindicator', db.String(1)),
    db.Column('deliveryaddresscode', db.String(10)),
    db.Column('customerreference', db.String(25)),
    db.Column('comments', db.String(25)),
    db.Column('address1', db.String(50)),
    db.Column('address2', db.String(50)),
    db.Column('address3', db.String(35)),
    db.Column('address4', db.String(35)),
    db.Column('address5', db.String(35)),
    db.Column('address6', db.String(35)),
    db.Column('bucode', db.String(3)),
    db.Column('printvatdetail', db.String(1)),
    db.Column('file_name', db.String(50))
)


t_dhl_if_so_root = db.Table(
    'dhl_if_so_root',
    db.Column('senderid', db.String(5)),
    db.Column('receiverid', db.String(5)),
    db.Column('extractid', db.String(35)),
    db.Column('extracttimestamp', db.String(25)),
    db.Column('extractlinecount', db.Numeric(asdecimal=False)),
    db.Column('header_name', db.String(50)),
    db.Column('detail_name', db.String(50)),
    db.Column('header_key', db.String(50)),
    db.Column('master_name', db.String(50)),
    db.Column('file_name', db.String(50)),
    db.Column('file_header', db.String(50)),
    db.Column('create_date', db.DateTime, server_default=db.FetchedValue())
)


t_dhl_if_so_root_view = db.Table(
    'dhl_if_so_root_view',
    db.Column('senderid', db.String(5)),
    db.Column('receiverid', db.String(5)),
    db.Column('extractid', db.String(35)),
    db.Column('extracttimestamp', db.String(25)),
    db.Column('extractlinecount', db.Numeric(asdecimal=False)),
    db.Column('header_name', db.String(50)),
    db.Column('detail_name', db.String(50)),
    db.Column('header_key', db.String(50)),
    db.Column('master_name', db.String(50)),
    db.Column('file_name', db.String(50)),
    db.Column('file_header', db.String(50)),
    db.Column('create_date', db.DateTime, server_default=db.FetchedValue())
)


t_dhl_if_sort_detail = db.Table(
    'dhl_if_sort_detail',
    db.Column('extractlineid', db.Numeric(asdecimal=False)),
    db.Column('sono', db.String(10)),
    db.Column('orderlineno', db.String(5)),
    db.Column('distribcenterid', db.String(5)),
    db.Column('itemno', db.String(15)),
    db.Column('deliverydate', db.String(8)),
    db.Column('orderqty', db.Numeric(asdecimal=False)),
    db.Column('uom', db.String(5)),
    db.Column('fixedassetcode', db.String(10)),
    db.Column('unitprice', db.Numeric(asdecimal=False)),
    db.Column('createdate', db.DateTime, server_default=db.FetchedValue()),
    db.Index('idx_dhl_sort1', 'sono', 'itemno')
)


t_dhl_if_sort_detail_inpt = db.Table(
    'dhl_if_sort_detail_inpt',
    db.Column('extractlineid', db.Numeric(asdecimal=False)),
    db.Column('sono', db.String(10)),
    db.Column('orderlineno', db.String(5)),
    db.Column('distribcenterid', db.String(5)),
    db.Column('itemno', db.String(15)),
    db.Column('deliverydate', db.String(8)),
    db.Column('orderqty', db.Numeric(asdecimal=False)),
    db.Column('uom', db.String(5)),
    db.Column('fixedassetcode', db.String(10)),
    db.Column('unitprice', db.Numeric(asdecimal=False)),
    db.Column('create_date', db.DateTime, server_default=db.FetchedValue())
)


t_dhl_if_sort_header = db.Table(
    'dhl_if_sort_header',
    db.Column('extractorderid', db.Numeric(asdecimal=False)),
    db.Column('sono', db.String(10)),
    db.Column('customercode', db.String(10)),
    db.Column('orderdate', db.String(8)),
    db.Column('sotype', db.String(5)),
    db.Column('debitcreditindicator', db.String(1)),
    db.Column('deliveryaddresscode', db.String(10)),
    db.Column('customerreference', db.String(25), index=True),
    db.Column('comments', db.String(25)),
    db.Column('address1', db.String(35)),
    db.Column('address2', db.String(35)),
    db.Column('address3', db.String(35)),
    db.Column('address4', db.String(35)),
    db.Column('address5', db.String(35)),
    db.Column('address6', db.String(35)),
    db.Column('bucode', db.String(3)),
    db.Column('printvatdetail', db.String(1)),
    db.Column('status', db.String(1), server_default=db.FetchedValue()),
    db.Column('create_date', db.DateTime, server_default=db.FetchedValue()),
    db.Index('if_sort_idx', 'sono', 'status')
)


t_dhl_if_sort_header_inpt = db.Table(
    'dhl_if_sort_header_inpt',
    db.Column('extractorderid', db.Numeric(asdecimal=False)),
    db.Column('sono', db.String(10)),
    db.Column('customercode', db.String(10)),
    db.Column('orderdate', db.String(8)),
    db.Column('sotype', db.String(5)),
    db.Column('debitcreditindicator', db.String(1)),
    db.Column('deliveryaddresscode', db.String(10)),
    db.Column('customerreference', db.String(25)),
    db.Column('comments', db.String(25)),
    db.Column('address1', db.String(35)),
    db.Column('address2', db.String(35)),
    db.Column('address3', db.String(35)),
    db.Column('address4', db.String(35)),
    db.Column('address5', db.String(35)),
    db.Column('address6', db.String(35)),
    db.Column('bucode', db.String(3)),
    db.Column('printvatdetail', db.String(1)),
    db.Column('status', db.String(1), server_default=db.FetchedValue()),
    db.Column('create_date', db.DateTime, server_default=db.FetchedValue())
)


t_dhl_if_sort_root = db.Table(
    'dhl_if_sort_root',
    db.Column('senderid', db.String(5)),
    db.Column('receiverid', db.String(5)),
    db.Column('extractid', db.String(35)),
    db.Column('extracttimestamp', db.String(25)),
    db.Column('extractlinecount', db.Numeric(asdecimal=False)),
    db.Column('header_name', db.String(50)),
    db.Column('detail_name', db.String(50)),
    db.Column('header_key', db.String(50)),
    db.Column('master_name', db.String(50)),
    db.Column('file_name', db.String(50)),
    db.Column('create_date', db.DateTime, server_default=db.FetchedValue())
)


t_dhl_ssscc_order = db.Table(
    'dhl_ssscc_order',
    db.Column('sku', db.String(20)),
    db.Column('begindate', db.DateTime),
    db.Column('enddate', db.DateTime),
    db.Column('qty', db.Numeric(14, 2)),
    db.Column('typ', db.String(1)),
    db.Column('createdate', db.DateTime, index=True)
)


class DhlXmlDetail(db.Model):
    __tablename__ = 'dhl_xml_detail'

    id = db.Column(db.Numeric(12, 0, asdecimal=False), primary_key=True)
    headermdextractid = db.Column(db.Numeric(12, 0, asdecimal=False), nullable=False, index=True)
    mdextractidnumber = db.Column(db.String(50), nullable=False, index=True)
    actioncode = db.Column(db.String(10))
    itemnumber = db.Column(db.String(20))
    linenumber = db.Column(db.String(50))
    linerevisionnumber = db.Column(db.String(5))
    qtyconstrained = db.Column(db.Numeric(16, 6))
    qtyminimum = db.Column(db.Numeric(16, 6))
    qtyunconstrained = db.Column(db.Numeric(16, 6))
    uomcode = db.Column(db.String(20))
    exttr1 = db.Column(db.String(20))
    exttr2 = db.Column(db.String(20))
    exttr3 = db.Column(db.String(20))
    exttr4 = db.Column(db.String(20))
    exttr5 = db.Column(db.String(20))
    deptid = db.Column(db.Integer)
    purid = db.Column(db.Numeric(12, 0, asdecimal=False))
    purpluid = db.Column(db.Numeric(12, 0, asdecimal=False))
    bizdt = db.Column(db.DateTime, index=True)
    createddt = db.Column(db.DateTime, server_default=db.FetchedValue())
    sta = db.Column(db.String(5))


class DhlXmlHeader(db.Model):
    __tablename__ = 'dhl_xml_header'

    id = db.Column(db.Numeric(12, 0, asdecimal=False), primary_key=True)
    purid = db.Column(db.Numeric(12, 0, asdecimal=False), nullable=False)
    mdextractid = db.Column(db.String(50), nullable=False, index=True)
    rootmdgroupid = db.Column(db.String(50), index=True)
    mdtxlinecount = db.Column(db.Integer)
    actioncode = db.Column(db.String(20))
    carriercode = db.Column(db.String(20))
    datecreated = db.Column(db.DateTime, index=True)
    datecutoff = db.Column(db.DateTime)
    dateexpected = db.Column(db.DateTime, index=True)
    dateshipby = db.Column(db.DateTime)
    legalentity = db.Column(db.String(20))
    hexnumber = db.Column(db.String(50))
    ordertype = db.Column(db.String(30))
    servicecode = db.Column(db.String(10))
    sourceid = db.Column(db.String(30))
    storenumber = db.Column(db.String(20))
    transfernumber = db.Column(db.String(50))
    transportmodecode = db.Column(db.String(10))
    deptid = db.Column(db.Integer)
    secondcd = db.Column(db.String(20), index=True)
    repocd = db.Column(db.String(20))
    venlktp = db.Column(db.String(5))
    exttr1 = db.Column(db.String(20))
    exttr2 = db.Column(db.String(20))
    exttr3 = db.Column(db.String(20))
    exttr4 = db.Column(db.String(20))
    exttr5 = db.Column(db.String(20))
    bizdt = db.Column(db.DateTime, index=True)
    createddt = db.Column(db.DateTime, index=True, server_default=db.FetchedValue())
    sta = db.Column(db.String(5))


class DhlXmlRoot(db.Model):
    __tablename__ = 'dhl_xml_root'

    id = db.Column(db.Numeric(12, 0, asdecimal=False), primary_key=True)
    mdgroupid = db.Column(db.String(50), nullable=False, index=True)
    mddc = db.Column(db.String(10))
    mdextractdate = db.Column(db.DateTime, index=True)
    mdgmtoffset = db.Column(db.String(20))
    mdgroupcount = db.Column(db.Integer)
    mdtxlinecount = db.Column(db.Integer)
    pickreleasestatusind = db.Column(db.String(10))
    shipprioritycode = db.Column(db.String(40))
    exttr1 = db.Column(db.String(20))
    exttr2 = db.Column(db.String(20))
    exttr3 = db.Column(db.String(20))
    exttr4 = db.Column(db.String(20))
    exttr5 = db.Column(db.String(20))
    createddt = db.Column(db.DateTime, server_default=db.FetchedValue())
    bizdt = db.Column(db.DateTime, index=True)
    sta = db.Column(db.String(5))


class DhlXmlSend(db.Model):
    __tablename__ = 'dhl_xml_send'

    id = db.Column(db.Numeric(12, 0, asdecimal=False), primary_key=True)
    dhlxmlrootid = db.Column(db.Numeric(12, 0, asdecimal=False), nullable=False)
    bizdt = db.Column(db.DateTime, index=True)
    createddt = db.Column(db.DateTime, server_default=db.FetchedValue())
    upddt = db.Column(db.DateTime, server_default=db.FetchedValue())
    sendtry = db.Column(db.Integer)
    sta = db.Column(db.String(30))


t_dim_gcbi_item_type = db.Table(
    'dim_gcbi_item_type',
    db.Column('cd', db.String(20)),
    db.Column('d_type', db.String(50)),
    db.Column('nm_l_zh', db.Unicode(100), nullable=False)
)


class DocAdjplu(db.Model):
    __tablename__ = 'doc_adjplu'

    id = db.Column(db.Numeric(12, 0, asdecimal=False), primary_key=True)
    adjid = db.Column(db.Numeric(12, 0, asdecimal=False), nullable=False, index=True)
    billrsn = db.Column(db.String(20))
    pluid = db.Column(db.Integer)
    lntp = db.Column(db.String(10))
    lnopt = db.Column(db.String(1))
    pid = db.Column(db.Numeric(12, 0, asdecimal=False))
    leafflg = db.Column(db.String(1), server_default=db.FetchedValue())
    ncflg = db.Column(db.String(1), server_default=db.FetchedValue())
    ordqty = db.Column(db.Numeric(16, 6))
    cfmqty = db.Column(db.Numeric(16, 6))
    stkqty = db.Column(db.Numeric(16, 6))
    stksign = db.Column(db.Integer, server_default=db.FetchedValue())
    uomcd = db.Column(db.String(6))
    csprc = db.Column(db.Numeric(16, 4))
    csamt = db.Column(db.Numeric(16, 4))
    locid = db.Column(db.Integer, server_default=db.FetchedValue())
    lotno = db.Column(db.String(20), server_default=db.FetchedValue())
    lotdesc = db.Column(db.String(80))
    lotstdt = db.Column(db.DateTime)
    loteddt = db.Column(db.DateTime)
    lotsta = db.Column(db.String(2))
    venlotno = db.Column(db.String(20))
    exlotno = db.Column(db.String(20))
    reqdt = db.Column(db.DateTime)
    reqby = db.Column(db.String(20))
    stkdt = db.Column(db.DateTime)
    stkby = db.Column(db.String(20))
    actdt = db.Column(db.DateTime)
    actby = db.Column(db.String(20))
    cnldt = db.Column(db.DateTime)
    cnlby = db.Column(db.String(20))
    rmk = db.Column(db.String(100))
    updby = db.Column(db.String(20))
    upddt = db.Column(db.DateTime)
    sta = db.Column(db.String(3), nullable=False)
    execflg = db.Column(db.String(1), server_default=db.FetchedValue())
    nxtsta = db.Column(db.String(3))
    caldt = db.Column(db.DateTime)
    calby = db.Column(db.String(20))
    calflg = db.Column(db.String(1))
    tgtlocid = db.Column(db.Integer, server_default=db.FetchedValue())
    billlktp = db.Column(db.String(10))
    billlkid = db.Column(db.Numeric(12, 0, asdecimal=False))


class DocAdjust(db.Model):
    __tablename__ = 'doc_adjust'
    __table_args__ = (
        db.Index('idx_doc_sta', 'sta', 'isso'),
        db.Index('idx_doc_adj', 'deptid', 'orddt', 'stkdt')
    )

    id = db.Column(db.Numeric(12, 0, asdecimal=False), primary_key=True)
    coid = db.Column(db.Integer)
    billtp = db.Column(db.String(10))
    billrsn = db.Column(db.String(20))
    deptid = db.Column(db.Integer)
    uselktp = db.Column(db.String(10))
    uselkid = db.Column(db.Integer)
    shiplktp = db.Column(db.String(10))
    shiplkid = db.Column(db.Integer)
    orddt = db.Column(db.DateTime)
    reqdt = db.Column(db.DateTime)
    reqby = db.Column(db.String(20))
    stkdt = db.Column(db.DateTime)
    stkby = db.Column(db.String(20))
    actdt = db.Column(db.DateTime)
    cnldt = db.Column(db.DateTime)
    cnlby = db.Column(db.String(20))
    rmk = db.Column(db.String(255))
    updby = db.Column(db.String(20))
    upddt = db.Column(db.DateTime, index=True)
    sta = db.Column(db.String(3), nullable=False)
    execflg = db.Column(db.String(1))
    nxtsta = db.Column(db.String(3))
    billlktp = db.Column(db.String(10))
    billlkid = db.Column(db.Numeric(12, 0, asdecimal=False), index=True)
    useby = db.Column(db.String(20))
    slflg = db.Column(db.String(1), server_default=db.FetchedValue())
    ifsocd = db.Column(db.String(20))
    isso = db.Column(db.String(1), server_default=db.FetchedValue())
    auditor = db.Column(db.String(20))
    reviewer = db.Column(db.String(20))
    preparedby = db.Column(db.String(20))


class DocDelivery(db.Model):
    __tablename__ = 'doc_delivery'
    __table_args__ = (
        db.Index('idx_doc_dlv', 'rcvdeptid', 'orddt', 'stkdt', 'actdt'),
        db.Index('idx_doc_dlv_isso', 'isso', 'sta')
    )

    id = db.Column(db.Numeric(12, 0, asdecimal=False), primary_key=True)
    coid = db.Column(db.Integer)
    billtp = db.Column(db.String(10))
    billrsn = db.Column(db.String(20))
    billlktp = db.Column(db.String(10))
    billlkid = db.Column(db.Numeric(12, 0, asdecimal=False))
    deptid = db.Column(db.Integer)
    rcvdeptid = db.Column(db.Integer)
    orddt = db.Column(db.DateTime, index=True)
    reqdt = db.Column(db.DateTime)
    reqby = db.Column(db.String(20))
    psdt = db.Column(db.DateTime)
    shipby = db.Column(db.String(20))
    dlvlncd = db.Column(db.String(20))
    wavecd = db.Column(db.String(20))
    stkdt = db.Column(db.DateTime)
    stkby = db.Column(db.String(20))
    actdt = db.Column(db.DateTime)
    cnldt = db.Column(db.DateTime)
    cnlby = db.Column(db.String(20))
    saleby = db.Column(db.String(20))
    artp = db.Column(db.String(10))
    arrule = db.Column(db.String(10))
    billcrcd = db.Column(db.String(3))
    crrt = db.Column(db.Numeric(12, 6))
    crcd = db.Column(db.String(3))
    fcflg = db.Column(db.String(1))
    txrt = db.Column(db.Numeric(6, 2))
    rmk = db.Column(db.String(255))
    updby = db.Column(db.String(20))
    upddt = db.Column(db.DateTime)
    sta = db.Column(db.String(3), nullable=False, index=True)
    execflg = db.Column(db.String(1), server_default=db.FetchedValue())
    nxtsta = db.Column(db.String(3))
    so = db.Column(db.String(20), index=True)
    isso = db.Column(db.String(1), server_default=db.FetchedValue())
    seqid = db.Column(db.Numeric(12, 0, asdecimal=False))


t_doc_delivery_hhs = db.Table(
    'doc_delivery_hhs',
    db.Column('id', db.Numeric(12, 0, asdecimal=False), nullable=False),
    db.Column('coid', db.Integer),
    db.Column('billtp', db.String(10)),
    db.Column('billrsn', db.String(20)),
    db.Column('billlktp', db.String(10)),
    db.Column('billlkid', db.Numeric(12, 0, asdecimal=False)),
    db.Column('deptid', db.Integer),
    db.Column('rcvdeptid', db.Integer),
    db.Column('orddt', db.DateTime, index=True),
    db.Column('reqdt', db.DateTime),
    db.Column('reqby', db.String(20)),
    db.Column('psdt', db.DateTime, index=True),
    db.Column('shipby', db.String(20)),
    db.Column('dlvlncd', db.String(20)),
    db.Column('wavecd', db.String(20)),
    db.Column('stkdt', db.DateTime),
    db.Column('stkby', db.String(20)),
    db.Column('actdt', db.DateTime),
    db.Column('cnldt', db.DateTime),
    db.Column('cnlby', db.String(20)),
    db.Column('saleby', db.String(20)),
    db.Column('artp', db.String(10)),
    db.Column('arrule', db.String(10)),
    db.Column('billcrcd', db.String(3)),
    db.Column('crrt', db.Numeric(12, 6)),
    db.Column('crcd', db.String(3)),
    db.Column('fcflg', db.String(1)),
    db.Column('txrt', db.Numeric(6, 2)),
    db.Column('rmk', db.String(255)),
    db.Column('updby', db.String(20)),
    db.Column('upddt', db.DateTime),
    db.Column('sta', db.String(3), nullable=False, index=True),
    db.Column('execflg', db.String(1), server_default=db.FetchedValue()),
    db.Column('nxtsta', db.String(3)),
    db.Column('so', db.String(20)),
    db.Column('isso', db.String(1), server_default=db.FetchedValue()),
    db.Column('seqid', db.Numeric(12, 0, asdecimal=False)),
    db.Index('idx_doc_dlv_isso_hhs', 'isso', 'sta'),
    db.Index('idx_doc_dlv_hhs', 'rcvdeptid', 'orddt', 'stkdt', 'actdt')
)


class DocDlvplu(db.Model):
    __tablename__ = 'doc_dlvplu'

    id = db.Column(db.Numeric(12, 0, asdecimal=False), primary_key=True)
    saleid = db.Column(db.Numeric(12, 0, asdecimal=False), nullable=False, index=True)
    billrsn = db.Column(db.String(20))
    pluid = db.Column(db.Integer)
    lntp = db.Column(db.String(10))
    lnopt = db.Column(db.String(1))
    pid = db.Column(db.Numeric(12, 0, asdecimal=False))
    leafflg = db.Column(db.String(1), server_default=db.FetchedValue())
    ordqty = db.Column(db.Numeric(16, 6))
    orduomcd = db.Column(db.String(6))
    cfmqty = db.Column(db.Numeric(16, 6))
    stkqty = db.Column(db.Numeric(16, 6))
    stksign = db.Column(db.Integer, server_default=db.FetchedValue())
    uomcd = db.Column(db.String(6))
    csprc = db.Column(db.Numeric(16, 4))
    slprc = db.Column(db.Numeric(16, 4))
    csamt = db.Column(db.Numeric(16, 4))
    slamt = db.Column(db.Numeric(16, 4))
    txrt = db.Column(db.Numeric(6, 2))
    txamt = db.Column(db.Numeric(16, 4))
    locid = db.Column(db.Integer, server_default=db.FetchedValue())
    lotno = db.Column(db.String(20), server_default=db.FetchedValue())
    lotdesc = db.Column(db.String(80))
    lotstdt = db.Column(db.DateTime)
    loteddt = db.Column(db.DateTime)
    lotsta = db.Column(db.String(2))
    venlotno = db.Column(db.String(20))
    exlotno = db.Column(db.String(20))
    reqdt = db.Column(db.DateTime)
    reqby = db.Column(db.String(20))
    psdt = db.Column(db.DateTime)
    shipby = db.Column(db.String(20))
    stkdt = db.Column(db.DateTime)
    stkby = db.Column(db.String(20))
    actdt = db.Column(db.DateTime)
    actby = db.Column(db.String(20))
    cnldt = db.Column(db.DateTime)
    cnlby = db.Column(db.String(20))
    saleby = db.Column(db.String(20))
    rmk = db.Column(db.String(100))
    updby = db.Column(db.String(20))
    upddt = db.Column(db.DateTime)
    sta = db.Column(db.String(3), nullable=False)
    execflg = db.Column(db.String(1), server_default=db.FetchedValue())
    nxtsta = db.Column(db.String(3))
    billlktp = db.Column(db.String(10))
    billlkid = db.Column(db.Numeric(12, 0, asdecimal=False))
    adjflg = db.Column(db.String(1), server_default=db.FetchedValue())
    qty = db.Column(db.Numeric(16, 6))


t_doc_dlvplu_hhs = db.Table(
    'doc_dlvplu_hhs',
    db.Column('id', db.Numeric(12, 0, asdecimal=False), nullable=False),
    db.Column('saleid', db.Numeric(12, 0, asdecimal=False), nullable=False, index=True),
    db.Column('billrsn', db.String(20)),
    db.Column('pluid', db.Integer),
    db.Column('lntp', db.String(10)),
    db.Column('lnopt', db.String(1)),
    db.Column('pid', db.Numeric(12, 0, asdecimal=False)),
    db.Column('leafflg', db.String(1), server_default=db.FetchedValue()),
    db.Column('ordqty', db.Numeric(16, 6)),
    db.Column('orduomcd', db.String(6)),
    db.Column('cfmqty', db.Numeric(16, 6)),
    db.Column('stkqty', db.Numeric(16, 6)),
    db.Column('stksign', db.Integer, server_default=db.FetchedValue()),
    db.Column('uomcd', db.String(6)),
    db.Column('csprc', db.Numeric(16, 4)),
    db.Column('slprc', db.Numeric(16, 4)),
    db.Column('csamt', db.Numeric(16, 4)),
    db.Column('slamt', db.Numeric(16, 4)),
    db.Column('txrt', db.Numeric(6, 2)),
    db.Column('txamt', db.Numeric(16, 4)),
    db.Column('locid', db.Integer, server_default=db.FetchedValue()),
    db.Column('lotno', db.String(20), server_default=db.FetchedValue()),
    db.Column('lotdesc', db.String(80)),
    db.Column('lotstdt', db.DateTime),
    db.Column('loteddt', db.DateTime),
    db.Column('lotsta', db.String(2)),
    db.Column('venlotno', db.String(20)),
    db.Column('exlotno', db.String(20)),
    db.Column('reqdt', db.DateTime),
    db.Column('reqby', db.String(20)),
    db.Column('psdt', db.DateTime),
    db.Column('shipby', db.String(20)),
    db.Column('stkdt', db.DateTime),
    db.Column('stkby', db.String(20)),
    db.Column('actdt', db.DateTime),
    db.Column('actby', db.String(20)),
    db.Column('cnldt', db.DateTime),
    db.Column('cnlby', db.String(20)),
    db.Column('saleby', db.String(20)),
    db.Column('rmk', db.String(100)),
    db.Column('updby', db.String(20)),
    db.Column('upddt', db.DateTime),
    db.Column('sta', db.String(3), nullable=False),
    db.Column('execflg', db.String(1), server_default=db.FetchedValue()),
    db.Column('nxtsta', db.String(3)),
    db.Column('billlktp', db.String(10)),
    db.Column('billlkid', db.Numeric(12, 0, asdecimal=False)),
    db.Column('adjflg', db.String(1), server_default=db.FetchedValue()),
    db.Column('qty', db.Numeric(16, 6))
)


class DocInventory(db.Model):
    __tablename__ = 'doc_inventory'

    id = db.Column(db.Numeric(12, 0, asdecimal=False), primary_key=True)
    coid = db.Column(db.Integer)
    billtp = db.Column(db.String(10))
    billrsn = db.Column(db.String(20))
    billlktp = db.Column(db.String(10))
    billlkid = db.Column(db.Numeric(12, 0, asdecimal=False))
    deptid = db.Column(db.Integer, index=True)
    invrule = db.Column(db.String(10))
    cycrule = db.Column(db.String(10))
    orddt = db.Column(db.DateTime, index=True)
    reqdt = db.Column(db.DateTime)
    reqby = db.Column(db.String(20))
    stkdt = db.Column(db.DateTime)
    stkby = db.Column(db.String(20))
    actdt = db.Column(db.DateTime, index=True)
    cnldt = db.Column(db.DateTime)
    cnlby = db.Column(db.String(20))
    calflg = db.Column(db.String(1), server_default=db.FetchedValue())
    calby = db.Column(db.String(20))
    caldt = db.Column(db.DateTime)
    rmk = db.Column(db.String(255))
    updby = db.Column(db.String(20))
    upddt = db.Column(db.DateTime, index=True)
    sta = db.Column(db.String(3), index=True)
    execflg = db.Column(db.String(1), server_default=db.FetchedValue())
    nxtsta = db.Column(db.String(3))
    auditor = db.Column(db.String(20))
    reviewer = db.Column(db.String(20))
    preparedby = db.Column(db.String(20))


class DocInvnoneplu(db.Model):
    __tablename__ = 'doc_invnoneplu'

    id = db.Column(db.Numeric(12, 0, asdecimal=False), primary_key=True)
    coid = db.Column(db.Integer)
    orddt = db.Column(db.DateTime)
    deptid = db.Column(db.Integer)
    pluid = db.Column(db.Integer)
    caldt = db.Column(db.DateTime)
    rmk = db.Column(db.String(255))
    updby = db.Column(db.String(20))
    upddt = db.Column(db.DateTime)
    sta = db.Column(db.String(3), nullable=False)
    execflg = db.Column(db.String(1))
    nxtsta = db.Column(db.String(3))


class DocInvpla(db.Model):
    __tablename__ = 'doc_invpla'

    id = db.Column(db.Numeric(12, 0, asdecimal=False), primary_key=True)
    coid = db.Column(db.Integer)
    deptid = db.Column(db.Integer, nullable=False)
    billtp = db.Column(db.String(10), nullable=False)
    orddt = db.Column(db.DateTime, nullable=False)
    invrule = db.Column(db.String(10))
    cycrule = db.Column(db.String(10))
    wkday = db.Column(db.String(10))
    mtday = db.Column(db.String(10))
    stdt = db.Column(db.DateTime)
    eddt = db.Column(db.DateTime)
    lastinvdt = db.Column(db.DateTime)
    predays = db.Column(db.Integer, nullable=False)
    rmk = db.Column(db.String(255))
    updby = db.Column(db.String(20))
    upddt = db.Column(db.DateTime)
    sta = db.Column(db.String(3), nullable=False)
    execflg = db.Column(db.String(1))
    nxtsta = db.Column(db.String(3))


class DocInvpladept(db.Model):
    __tablename__ = 'doc_invpladept'

    id = db.Column(db.Numeric(12, 0, asdecimal=False), primary_key=True)
    invplaid = db.Column(db.Numeric(12, 0, asdecimal=False))
    deptid = db.Column(db.Integer, nullable=False)
    rmk = db.Column(db.String(255))
    updby = db.Column(db.String(20))
    upddt = db.Column(db.DateTime)
    sta = db.Column(db.String(3), nullable=False)
    execflg = db.Column(db.String(1))
    nxtsta = db.Column(db.String(3))
    depttp = db.Column(db.String(10))


class DocInvplaplu(db.Model):
    __tablename__ = 'doc_invplaplu'

    id = db.Column(db.Numeric(12, 0, asdecimal=False), primary_key=True)
    invplaid = db.Column(db.Numeric(12, 0, asdecimal=False))
    plulktp = db.Column(db.String(10))
    plulkid = db.Column(db.Integer, nullable=False)
    rmk = db.Column(db.String(255))
    updby = db.Column(db.String(20))
    upddt = db.Column(db.DateTime)
    sta = db.Column(db.String(3), nullable=False)
    execflg = db.Column(db.String(1))
    nxtsta = db.Column(db.String(3))


class DocInvplu(db.Model):
    __tablename__ = 'doc_invplu'

    id = db.Column(db.Numeric(12, 0, asdecimal=False), primary_key=True)
    invid = db.Column(db.Numeric(12, 0, asdecimal=False), index=True)
    billrsn = db.Column(db.String(20))
    pluid = db.Column(db.Integer)
    lntp = db.Column(db.String(10))
    lnopt = db.Column(db.String(1))
    pid = db.Column(db.Numeric(12, 0, asdecimal=False))
    leafflg = db.Column(db.String(1), server_default=db.FetchedValue())
    cvtflg = db.Column(db.String(1), server_default=db.FetchedValue())
    bookqty = db.Column(db.Numeric(16, 6))
    inputqty = db.Column(db.Numeric(16, 6))
    cvtqty = db.Column(db.Numeric(16, 6))
    stkqty = db.Column(db.Numeric(16, 6))
    uomcd = db.Column(db.String(6))
    csprc = db.Column(db.Numeric(16, 4))
    csamt = db.Column(db.Numeric(16, 4))
    locid = db.Column(db.Integer)
    lotno = db.Column(db.String(20))
    lotdesc = db.Column(db.String(80))
    lotstdt = db.Column(db.DateTime)
    loteddt = db.Column(db.DateTime)
    lotsta = db.Column(db.String(2))
    venlotno = db.Column(db.String(20))
    exlotno = db.Column(db.String(20))
    reqdt = db.Column(db.DateTime)
    reqby = db.Column(db.String(20))
    stkdt = db.Column(db.DateTime)
    stkby = db.Column(db.String(20))
    actdt = db.Column(db.DateTime)
    actby = db.Column(db.String(20))
    cnldt = db.Column(db.DateTime)
    cnlby = db.Column(db.String(20))
    calflg = db.Column(db.String(1), server_default=db.FetchedValue())
    calby = db.Column(db.String(20))
    caldt = db.Column(db.DateTime)
    rmk = db.Column(db.String(255))
    updby = db.Column(db.String(20))
    upddt = db.Column(db.DateTime)
    sta = db.Column(db.String(3))
    execflg = db.Column(db.String(1), server_default=db.FetchedValue())
    nxtsta = db.Column(db.String(3))
    dlvqty = db.Column(db.Numeric(16, 6))


t_doc_invplu_tmp = db.Table(
    'doc_invplu_tmp',
    db.Column('id', db.Numeric(12, 0, asdecimal=False), nullable=False),
    db.Column('invid', db.Numeric(12, 0, asdecimal=False)),
    db.Column('billrsn', db.String(20)),
    db.Column('pluid', db.Integer),
    db.Column('lntp', db.String(10)),
    db.Column('lnopt', db.String(1)),
    db.Column('pid', db.Numeric(12, 0, asdecimal=False)),
    db.Column('leafflg', db.String(1), server_default=db.FetchedValue()),
    db.Column('cvtflg', db.String(1), server_default=db.FetchedValue()),
    db.Column('bookqty', db.Numeric(16, 6)),
    db.Column('inputqty', db.Numeric(16, 6)),
    db.Column('cvtqty', db.Numeric(16, 6)),
    db.Column('stkqty', db.Numeric(16, 6)),
    db.Column('uomcd', db.String(6)),
    db.Column('csprc', db.Numeric(16, 4)),
    db.Column('csamt', db.Numeric(16, 4)),
    db.Column('locid', db.Integer),
    db.Column('lotno', db.String(20)),
    db.Column('lotdesc', db.String(80)),
    db.Column('lotstdt', db.DateTime),
    db.Column('loteddt', db.DateTime),
    db.Column('lotsta', db.String(2)),
    db.Column('venlotno', db.String(20)),
    db.Column('exlotno', db.String(20)),
    db.Column('reqdt', db.DateTime),
    db.Column('reqby', db.String(20)),
    db.Column('stkdt', db.DateTime),
    db.Column('stkby', db.String(20)),
    db.Column('actdt', db.DateTime),
    db.Column('actby', db.String(20)),
    db.Column('cnldt', db.DateTime),
    db.Column('cnlby', db.String(20)),
    db.Column('calflg', db.String(1), server_default=db.FetchedValue()),
    db.Column('calby', db.String(20)),
    db.Column('caldt', db.DateTime),
    db.Column('rmk', db.String(255)),
    db.Column('updby', db.String(20)),
    db.Column('upddt', db.DateTime),
    db.Column('sta', db.String(3)),
    db.Column('execflg', db.String(1), server_default=db.FetchedValue()),
    db.Column('nxtsta', db.String(3)),
    db.Column('dlvqty', db.Numeric(16, 6))
)


class DocPurchase(db.Model):
    __tablename__ = 'doc_purchase'

    id = db.Column(db.Numeric(12, 0, asdecimal=False), primary_key=True)
    coid = db.Column(db.Integer)
    billtp = db.Column(db.String(10))
    billrsn = db.Column(db.String(20))
    billlktp = db.Column(db.String(10))
    billlkid = db.Column(db.Numeric(12, 0, asdecimal=False), index=True)
    deptid = db.Column(db.Integer)
    venid = db.Column(db.Integer)
    shiplktp = db.Column(db.String(10))
    shiplkid = db.Column(db.Integer)
    orddt = db.Column(db.DateTime, index=True)
    reqdt = db.Column(db.DateTime)
    reqby = db.Column(db.String(20))
    psdt = db.Column(db.DateTime, index=True)
    shipby = db.Column(db.String(20))
    stkdt = db.Column(db.DateTime, index=True)
    stkby = db.Column(db.String(20))
    actdt = db.Column(db.DateTime)
    cnldt = db.Column(db.DateTime)
    cnlby = db.Column(db.String(20))
    purby = db.Column(db.String(20))
    aptp = db.Column(db.String(10))
    aprule = db.Column(db.String(10))
    billcrcd = db.Column(db.String(3))
    crrt = db.Column(db.Numeric(12, 6))
    crcd = db.Column(db.String(3))
    fcflg = db.Column(db.String(1))
    txrt = db.Column(db.Numeric(6, 2))
    rejrsn = db.Column(db.String(10))
    exattr1 = db.Column(db.String(100))
    exattr2 = db.Column(db.String(100))
    exattr3 = db.Column(db.String(100))
    exattr4 = db.Column(db.String(100))
    exattr5 = db.Column(db.String(100))
    rmk = db.Column(db.String(255))
    ifflg = db.Column(db.String(1))
    updby = db.Column(db.String(20))
    upddt = db.Column(db.DateTime, index=True)
    sta = db.Column(db.String(3), nullable=False, index=True)
    execflg = db.Column(db.String(1))
    nxtsta = db.Column(db.String(3))
    invid = db.Column(db.Numeric(12, 0, asdecimal=False))
    so = db.Column(db.String(20))
    lstdt = db.Column(db.DateTime)
    isso = db.Column(db.String(1), server_default=db.FetchedValue())
    ispo = db.Column(db.String(1), server_default=db.FetchedValue())
    po = db.Column(db.String(20), index=True)
    is_send_mail = db.Column(db.String(1), server_default=db.FetchedValue())
    findt = db.Column(db.DateTime)
    seqid = db.Column(db.Numeric(12, 0, asdecimal=False))


t_doc_purchase_hhs = db.Table(
    'doc_purchase_hhs',
    db.Column('id', db.Numeric(12, 0, asdecimal=False), nullable=False),
    db.Column('coid', db.Integer),
    db.Column('billtp', db.String(10)),
    db.Column('billrsn', db.String(20)),
    db.Column('billlktp', db.String(10)),
    db.Column('billlkid', db.Numeric(12, 0, asdecimal=False)),
    db.Column('deptid', db.Integer),
    db.Column('venid', db.Integer),
    db.Column('shiplktp', db.String(10)),
    db.Column('shiplkid', db.Integer),
    db.Column('orddt', db.DateTime, index=True),
    db.Column('reqdt', db.DateTime),
    db.Column('reqby', db.String(20)),
    db.Column('psdt', db.DateTime),
    db.Column('shipby', db.String(20)),
    db.Column('stkdt', db.DateTime, index=True),
    db.Column('stkby', db.String(20)),
    db.Column('actdt', db.DateTime),
    db.Column('cnldt', db.DateTime),
    db.Column('cnlby', db.String(20)),
    db.Column('purby', db.String(20)),
    db.Column('aptp', db.String(10)),
    db.Column('aprule', db.String(10)),
    db.Column('billcrcd', db.String(3)),
    db.Column('crrt', db.Numeric(12, 6)),
    db.Column('crcd', db.String(3)),
    db.Column('fcflg', db.String(1)),
    db.Column('txrt', db.Numeric(6, 2)),
    db.Column('rejrsn', db.String(10)),
    db.Column('exattr1', db.String(100)),
    db.Column('exattr2', db.String(100)),
    db.Column('exattr3', db.String(100)),
    db.Column('exattr4', db.String(100)),
    db.Column('exattr5', db.String(100)),
    db.Column('rmk', db.String(255)),
    db.Column('ifflg', db.String(1)),
    db.Column('updby', db.String(20)),
    db.Column('upddt', db.DateTime),
    db.Column('sta', db.String(3), nullable=False, index=True),
    db.Column('execflg', db.String(1)),
    db.Column('nxtsta', db.String(3)),
    db.Column('invid', db.Numeric(12, 0, asdecimal=False)),
    db.Column('so', db.String(20)),
    db.Column('lstdt', db.DateTime),
    db.Column('isso', db.String(1), server_default=db.FetchedValue()),
    db.Column('ispo', db.String(1), index=True, server_default=db.FetchedValue()),
    db.Column('po', db.String(20)),
    db.Column('is_send_mail', db.String(1), server_default=db.FetchedValue()),
    db.Column('seqid', db.Numeric(12, 0, asdecimal=False)),
    db.Index('idx_doc_purstkdt_hhs1', 'psdt', 'isso', 'deptid'),
    db.Index('idx_doc_pur_hhs', 'billtp', 'deptid', 'venid'),
    db.Index('idx_doc_pur4_hhs', 'billtp', 'is_send_mail')
)


class DocPurchasePar(db.Model):
    __tablename__ = 'doc_purchase_par'
    __table_args__ = (
        db.Index('idx_doc_pur4', 'billtp', 'is_send_mail'),
        db.Index('idx_doc_pur', 'billtp', 'deptid', 'venid', 'psdt')
    )

    id = db.Column(db.Numeric(12, 0, asdecimal=False), primary_key=True)
    coid = db.Column(db.Integer)
    billtp = db.Column(db.String(10))
    billrsn = db.Column(db.String(20))
    billlktp = db.Column(db.String(10))
    billlkid = db.Column(db.Numeric(12, 0, asdecimal=False))
    deptid = db.Column(db.Integer)
    venid = db.Column(db.Integer)
    shiplktp = db.Column(db.String(10))
    shiplkid = db.Column(db.Integer)
    orddt = db.Column(db.DateTime, index=True)
    reqdt = db.Column(db.DateTime)
    reqby = db.Column(db.String(20))
    psdt = db.Column(db.DateTime)
    shipby = db.Column(db.String(20))
    stkdt = db.Column(db.DateTime, index=True)
    stkby = db.Column(db.String(20))
    actdt = db.Column(db.DateTime)
    cnldt = db.Column(db.DateTime)
    cnlby = db.Column(db.String(20))
    purby = db.Column(db.String(20))
    aptp = db.Column(db.String(10))
    aprule = db.Column(db.String(10))
    billcrcd = db.Column(db.String(3))
    crrt = db.Column(db.Numeric(12, 6))
    crcd = db.Column(db.String(3))
    fcflg = db.Column(db.String(1))
    txrt = db.Column(db.Numeric(6, 2))
    rejrsn = db.Column(db.String(10))
    exattr1 = db.Column(db.String(100))
    exattr2 = db.Column(db.String(100))
    exattr3 = db.Column(db.String(100))
    exattr4 = db.Column(db.String(100))
    exattr5 = db.Column(db.String(100))
    rmk = db.Column(db.String(255))
    ifflg = db.Column(db.String(1))
    updby = db.Column(db.String(20))
    upddt = db.Column(db.DateTime)
    sta = db.Column(db.String(3), nullable=False, index=True)
    execflg = db.Column(db.String(1))
    nxtsta = db.Column(db.String(3))
    invid = db.Column(db.Numeric(12, 0, asdecimal=False))
    so = db.Column(db.String(20), index=True)
    lstdt = db.Column(db.DateTime)
    isso = db.Column(db.String(1), index=True, server_default=db.FetchedValue())
    ispo = db.Column(db.String(1), index=True, server_default=db.FetchedValue())
    po = db.Column(db.String(20))
    is_send_mail = db.Column(db.String(1), server_default=db.FetchedValue())
    findt = db.Column(db.DateTime)
    seqid = db.Column(db.Numeric(12, 0, asdecimal=False))


t_doc_purfee = db.Table(
    'doc_purfee',
    db.Column('id', db.Numeric(12, 0, asdecimal=False), nullable=False),
    db.Column('purid', db.Numeric(12, 0, asdecimal=False), nullable=False, index=True),
    db.Column('billrsn', db.String(20)),
    db.Column('feecd', db.String(20)),
    db.Column('fcamt', db.Numeric(20, 6)),
    db.Column('crrt', db.Numeric(12, 6)),
    db.Column('amt', db.Numeric(20, 6)),
    db.Column('calflg', db.String(1), server_default=db.FetchedValue()),
    db.Column('rmk', db.String(255)),
    db.Column('updby', db.String(20)),
    db.Column('upddt', db.DateTime),
    db.Column('sta', db.String(3), nullable=False),
    db.Column('execflg', db.String(1), server_default=db.FetchedValue()),
    db.Column('nxtsta', db.String(3)),
    db.Column('crcd', db.String(3)),
    db.Column('billcrcd', db.String(3))
)


t_doc_purfeedtl = db.Table(
    'doc_purfeedtl',
    db.Column('purid', db.Numeric(12, 0, asdecimal=False)),
    db.Column('pluid', db.Integer),
    db.Column('rcvamt', db.Numeric(20, 6)),
    db.Column('feeamt', db.Numeric(20, 6)),
    db.Column('invid', db.Numeric(12, 0, asdecimal=False)),
    db.Index('idx_docpurfeedtl', 'purid', 'invid')
)


class DocPurplu(db.Model):
    __tablename__ = 'doc_purplu'

    id = db.Column(db.Numeric(12, 0, asdecimal=False), primary_key=True)
    purid = db.Column(db.Numeric(12, 0, asdecimal=False), nullable=False, index=True)
    billrsn = db.Column(db.String(20))
    pluid = db.Column(db.Integer)
    lntp = db.Column(db.String(10))
    lnopt = db.Column(db.String(1))
    pid = db.Column(db.Numeric(12, 0, asdecimal=False))
    leafflg = db.Column(db.String(1), server_default=db.FetchedValue())
    ordqty = db.Column(db.Numeric(16, 6))
    orduomcd = db.Column(db.String(6))
    cfmqty = db.Column(db.Numeric(16, 6))
    stkqty = db.Column(db.Numeric(16, 6))
    stksign = db.Column(db.Integer, server_default=db.FetchedValue())
    uomcd = db.Column(db.String(6))
    csprc = db.Column(db.Numeric(18, 6))
    exprc1 = db.Column(db.Numeric(18, 6))
    csamt = db.Column(db.Numeric(18, 6))
    examt1 = db.Column(db.Numeric(18, 6))
    ncflg = db.Column(db.String(1), server_default=db.FetchedValue())
    txrt = db.Column(db.Numeric(8, 4))
    extxrt1 = db.Column(db.Numeric(8, 4))
    txamt = db.Column(db.Numeric(16, 6))
    extxamt1 = db.Column(db.Numeric(16, 6))
    locid = db.Column(db.Integer, server_default=db.FetchedValue())
    lotno = db.Column(db.String(20), server_default=db.FetchedValue())
    lotdesc = db.Column(db.String(80))
    lotstdt = db.Column(db.DateTime)
    loteddt = db.Column(db.DateTime)
    lotsta = db.Column(db.String(2))
    venlotno = db.Column(db.String(20))
    exlotno = db.Column(db.String(20))
    reqdt = db.Column(db.DateTime)
    reqby = db.Column(db.String(20))
    psdt = db.Column(db.DateTime)
    shipby = db.Column(db.String(20))
    stkdt = db.Column(db.DateTime)
    stkby = db.Column(db.String(20))
    actdt = db.Column(db.DateTime)
    actby = db.Column(db.String(20))
    cnldt = db.Column(db.DateTime)
    cnlby = db.Column(db.String(20))
    purby = db.Column(db.String(20))
    rmk = db.Column(db.String(100))
    updby = db.Column(db.String(20))
    upddt = db.Column(db.DateTime)
    finadjflg = db.Column(db.String(1), server_default=db.FetchedValue())
    sta = db.Column(db.String(3), nullable=False)
    execflg = db.Column(db.String(1))
    nxtsta = db.Column(db.String(3))
    billlktp = db.Column(db.String(10))
    billlkid = db.Column(db.Numeric(12, 0, asdecimal=False))
    qty = db.Column(db.Numeric(16, 6))


t_doc_purplu_hhs = db.Table(
    'doc_purplu_hhs',
    db.Column('id', db.Numeric(12, 0, asdecimal=False), nullable=False),
    db.Column('purid', db.Numeric(12, 0, asdecimal=False), nullable=False, index=True),
    db.Column('billrsn', db.String(20)),
    db.Column('pluid', db.Integer),
    db.Column('lntp', db.String(10)),
    db.Column('lnopt', db.String(1)),
    db.Column('pid', db.Numeric(12, 0, asdecimal=False)),
    db.Column('leafflg', db.String(1), server_default=db.FetchedValue()),
    db.Column('ordqty', db.Numeric(16, 6)),
    db.Column('orduomcd', db.String(6)),
    db.Column('cfmqty', db.Numeric(16, 6)),
    db.Column('stkqty', db.Numeric(16, 6)),
    db.Column('stksign', db.Integer, server_default=db.FetchedValue()),
    db.Column('uomcd', db.String(6)),
    db.Column('csprc', db.Numeric(18, 6)),
    db.Column('exprc1', db.Numeric(18, 6)),
    db.Column('csamt', db.Numeric(18, 6)),
    db.Column('examt1', db.Numeric(18, 6)),
    db.Column('ncflg', db.String(1), server_default=db.FetchedValue()),
    db.Column('txrt', db.Numeric(8, 4)),
    db.Column('extxrt1', db.Numeric(8, 4)),
    db.Column('txamt', db.Numeric(16, 6)),
    db.Column('extxamt1', db.Numeric(16, 6)),
    db.Column('locid', db.Integer, server_default=db.FetchedValue()),
    db.Column('lotno', db.String(20), server_default=db.FetchedValue()),
    db.Column('lotdesc', db.String(80)),
    db.Column('lotstdt', db.DateTime),
    db.Column('loteddt', db.DateTime),
    db.Column('lotsta', db.String(2)),
    db.Column('venlotno', db.String(20)),
    db.Column('exlotno', db.String(20)),
    db.Column('reqdt', db.DateTime),
    db.Column('reqby', db.String(20)),
    db.Column('psdt', db.DateTime),
    db.Column('shipby', db.String(20)),
    db.Column('stkdt', db.DateTime),
    db.Column('stkby', db.String(20)),
    db.Column('actdt', db.DateTime),
    db.Column('actby', db.String(20)),
    db.Column('cnldt', db.DateTime),
    db.Column('cnlby', db.String(20)),
    db.Column('purby', db.String(20)),
    db.Column('rmk', db.String(100)),
    db.Column('updby', db.String(20)),
    db.Column('upddt', db.DateTime),
    db.Column('finadjflg', db.String(1), server_default=db.FetchedValue()),
    db.Column('sta', db.String(3), nullable=False),
    db.Column('execflg', db.String(1)),
    db.Column('nxtsta', db.String(3)),
    db.Column('billlktp', db.String(10)),
    db.Column('billlkid', db.Numeric(12, 0, asdecimal=False)),
    db.Column('qty', db.Numeric(16, 6))
)


class DocPurpluPar(db.Model):
    __tablename__ = 'doc_purplu_par'

    id = db.Column(db.Numeric(12, 0, asdecimal=False), primary_key=True)
    purid = db.Column(db.Numeric(12, 0, asdecimal=False), nullable=False, index=True)
    billrsn = db.Column(db.String(20))
    pluid = db.Column(db.Integer)
    lntp = db.Column(db.String(10))
    lnopt = db.Column(db.String(1))
    pid = db.Column(db.Numeric(12, 0, asdecimal=False))
    leafflg = db.Column(db.String(1), server_default=db.FetchedValue())
    ordqty = db.Column(db.Numeric(16, 6))
    orduomcd = db.Column(db.String(6))
    cfmqty = db.Column(db.Numeric(16, 6))
    stkqty = db.Column(db.Numeric(16, 6))
    stksign = db.Column(db.Integer, server_default=db.FetchedValue())
    uomcd = db.Column(db.String(6))
    csprc = db.Column(db.Numeric(18, 6))
    exprc1 = db.Column(db.Numeric(18, 6))
    csamt = db.Column(db.Numeric(18, 6))
    examt1 = db.Column(db.Numeric(18, 6))
    ncflg = db.Column(db.String(1), server_default=db.FetchedValue())
    txrt = db.Column(db.Numeric(8, 4))
    extxrt1 = db.Column(db.Numeric(8, 4))
    txamt = db.Column(db.Numeric(16, 6))
    extxamt1 = db.Column(db.Numeric(16, 6))
    locid = db.Column(db.Integer, server_default=db.FetchedValue())
    lotno = db.Column(db.String(20), server_default=db.FetchedValue())
    lotdesc = db.Column(db.String(80))
    lotstdt = db.Column(db.DateTime)
    loteddt = db.Column(db.DateTime)
    lotsta = db.Column(db.String(2))
    venlotno = db.Column(db.String(20))
    exlotno = db.Column(db.String(20))
    reqdt = db.Column(db.DateTime)
    reqby = db.Column(db.String(20))
    psdt = db.Column(db.DateTime)
    shipby = db.Column(db.String(20))
    stkdt = db.Column(db.DateTime)
    stkby = db.Column(db.String(20))
    actdt = db.Column(db.DateTime)
    actby = db.Column(db.String(20))
    cnldt = db.Column(db.DateTime)
    cnlby = db.Column(db.String(20))
    purby = db.Column(db.String(20))
    rmk = db.Column(db.String(100))
    updby = db.Column(db.String(20))
    upddt = db.Column(db.DateTime, index=True)
    finadjflg = db.Column(db.String(1), server_default=db.FetchedValue())
    sta = db.Column(db.String(3), nullable=False)
    execflg = db.Column(db.String(1))
    nxtsta = db.Column(db.String(3))
    billlktp = db.Column(db.String(10))
    billlkid = db.Column(db.Numeric(12, 0, asdecimal=False))
    qty = db.Column(db.Numeric(16, 6))


class DocPurprc(db.Model):
    __tablename__ = 'doc_purprc'

    id = db.Column(db.Numeric(12, 0, asdecimal=False), primary_key=True)
    purpluid = db.Column(db.Numeric(12, 0, asdecimal=False), nullable=False, index=True)
    ptid = db.Column(db.Integer)
    oprc = db.Column(db.Numeric(20, 6))
    nprc = db.Column(db.Numeric(20, 6))
    otax = db.Column(db.Numeric(18, 4))
    ntax = db.Column(db.Numeric(18, 4))
    updby = db.Column(db.String(20))
    upddt = db.Column(db.DateTime)
    sta = db.Column(db.String(3), nullable=False)
    execflg = db.Column(db.String(1))
    nxtsta = db.Column(db.String(3))
    syndate = db.Column(db.DateTime)
    synflg = db.Column(db.String(1), index=True, server_default=db.FetchedValue())


t_doc_purprc_back = db.Table(
    'doc_purprc_back',
    db.Column('id', db.Numeric(12, 0, asdecimal=False), nullable=False),
    db.Column('purpluid', db.Numeric(12, 0, asdecimal=False), nullable=False),
    db.Column('ptid', db.Integer),
    db.Column('oprc', db.Numeric(20, 6)),
    db.Column('nprc', db.Numeric(20, 6)),
    db.Column('otax', db.Numeric(18, 4)),
    db.Column('ntax', db.Numeric(18, 4)),
    db.Column('updby', db.String(20)),
    db.Column('upddt', db.DateTime),
    db.Column('sta', db.String(3), nullable=False),
    db.Column('execflg', db.String(1)),
    db.Column('nxtsta', db.String(3)),
    db.Column('syndate', db.DateTime),
    db.Column('synflg', db.String(1), server_default=db.FetchedValue())
)


class DocRcvplu(db.Model):
    __tablename__ = 'doc_rcvplu'

    id = db.Column(db.Numeric(12, 0, asdecimal=False), primary_key=True)
    rcvid = db.Column(db.Numeric(12, 0, asdecimal=False), nullable=False, index=True)
    billrsn = db.Column(db.String(20))
    pluid = db.Column(db.Integer)
    lntp = db.Column(db.String(10))
    lnopt = db.Column(db.String(1))
    pid = db.Column(db.Numeric(12, 0, asdecimal=False))
    leafflg = db.Column(db.String(1), server_default=db.FetchedValue())
    ordqty = db.Column(db.Numeric(16, 6))
    orduomcd = db.Column(db.String(6))
    cfmqty = db.Column(db.Numeric(16, 6))
    stkqty = db.Column(db.Numeric(16, 6))
    stksign = db.Column(db.Integer, server_default=db.FetchedValue())
    uomcd = db.Column(db.String(6))
    csprc = db.Column(db.Numeric(16, 4))
    exprc1 = db.Column(db.Numeric(16, 4))
    csamt = db.Column(db.Numeric(16, 4))
    examt1 = db.Column(db.Numeric(16, 4))
    ncflg = db.Column(db.String(1), server_default=db.FetchedValue())
    txrt = db.Column(db.Numeric(8, 4))
    extxrt1 = db.Column(db.Numeric(8, 4))
    txamt = db.Column(db.Numeric(16, 4))
    extxamt1 = db.Column(db.Numeric(16, 4))
    locid = db.Column(db.Integer, server_default=db.FetchedValue())
    lotno = db.Column(db.String(20), server_default=db.FetchedValue())
    lotdesc = db.Column(db.String(80))
    lotstdt = db.Column(db.DateTime)
    loteddt = db.Column(db.DateTime)
    lotsta = db.Column(db.String(2))
    venlotno = db.Column(db.String(20))
    exlotno = db.Column(db.String(20))
    reqdt = db.Column(db.DateTime)
    reqby = db.Column(db.String(20))
    psdt = db.Column(db.DateTime)
    shipby = db.Column(db.String(20))
    stkdt = db.Column(db.DateTime)
    stkby = db.Column(db.String(20))
    actdt = db.Column(db.DateTime)
    actby = db.Column(db.String(20))
    cnldt = db.Column(db.DateTime)
    cnlby = db.Column(db.String(20))
    purby = db.Column(db.String(20))
    rmk = db.Column(db.String(100))
    updby = db.Column(db.String(20))
    upddt = db.Column(db.DateTime)
    finadjflg = db.Column(db.String(1), server_default=db.FetchedValue())
    sta = db.Column(db.String(3), nullable=False)
    execflg = db.Column(db.String(1), server_default=db.FetchedValue())
    nxtsta = db.Column(db.String(3))
    billlktp = db.Column(db.String(10))
    billlkid = db.Column(db.Numeric(12, 0, asdecimal=False))
    adjflg = db.Column(db.String(1), server_default=db.FetchedValue())
    qty = db.Column(db.Numeric(16, 6))


t_doc_rcvplu_hhs = db.Table(
    'doc_rcvplu_hhs',
    db.Column('id', db.Numeric(12, 0, asdecimal=False), nullable=False),
    db.Column('rcvid', db.Numeric(12, 0, asdecimal=False), nullable=False),
    db.Column('billrsn', db.String(20)),
    db.Column('pluid', db.Integer),
    db.Column('lntp', db.String(10)),
    db.Column('lnopt', db.String(1)),
    db.Column('pid', db.Numeric(12, 0, asdecimal=False)),
    db.Column('leafflg', db.String(1), server_default=db.FetchedValue()),
    db.Column('ordqty', db.Numeric(16, 6)),
    db.Column('orduomcd', db.String(6)),
    db.Column('cfmqty', db.Numeric(16, 6)),
    db.Column('stkqty', db.Numeric(16, 6)),
    db.Column('stksign', db.Integer, server_default=db.FetchedValue()),
    db.Column('uomcd', db.String(6)),
    db.Column('csprc', db.Numeric(16, 4)),
    db.Column('exprc1', db.Numeric(16, 4)),
    db.Column('csamt', db.Numeric(16, 4)),
    db.Column('examt1', db.Numeric(16, 4)),
    db.Column('ncflg', db.String(1), server_default=db.FetchedValue()),
    db.Column('txrt', db.Numeric(8, 4)),
    db.Column('extxrt1', db.Numeric(8, 4)),
    db.Column('txamt', db.Numeric(16, 4)),
    db.Column('extxamt1', db.Numeric(16, 4)),
    db.Column('locid', db.Integer, server_default=db.FetchedValue()),
    db.Column('lotno', db.String(20), server_default=db.FetchedValue()),
    db.Column('lotdesc', db.String(80)),
    db.Column('lotstdt', db.DateTime),
    db.Column('loteddt', db.DateTime),
    db.Column('lotsta', db.String(2)),
    db.Column('venlotno', db.String(20)),
    db.Column('exlotno', db.String(20)),
    db.Column('reqdt', db.DateTime),
    db.Column('reqby', db.String(20)),
    db.Column('psdt', db.DateTime),
    db.Column('shipby', db.String(20)),
    db.Column('stkdt', db.DateTime),
    db.Column('stkby', db.String(20)),
    db.Column('actdt', db.DateTime),
    db.Column('actby', db.String(20)),
    db.Column('cnldt', db.DateTime),
    db.Column('cnlby', db.String(20)),
    db.Column('purby', db.String(20)),
    db.Column('rmk', db.String(100)),
    db.Column('updby', db.String(20)),
    db.Column('upddt', db.DateTime),
    db.Column('finadjflg', db.String(1), server_default=db.FetchedValue()),
    db.Column('sta', db.String(3), nullable=False),
    db.Column('execflg', db.String(1), server_default=db.FetchedValue()),
    db.Column('nxtsta', db.String(3)),
    db.Column('billlktp', db.String(10)),
    db.Column('billlkid', db.Numeric(12, 0, asdecimal=False)),
    db.Column('adjflg', db.String(1), server_default=db.FetchedValue()),
    db.Column('qty', db.Numeric(16, 6))
)


class DocReceive(db.Model):
    __tablename__ = 'doc_receive'
    __table_args__ = (
        db.Index('idx_doc_rcv1', 'billtp', 'is_send_mail'),
        db.Index('idx_doc_rcv', 'orddt', 'psdt', 'stkdt', 'actdt', 'deptid')
    )

    id = db.Column(db.Numeric(12, 0, asdecimal=False), primary_key=True)
    coid = db.Column(db.Integer)
    billtp = db.Column(db.String(10))
    billrsn = db.Column(db.String(20))
    billlktp = db.Column(db.String(10))
    billlkid = db.Column(db.Numeric(12, 0, asdecimal=False), index=True)
    deptid = db.Column(db.Integer)
    dlvdeptid = db.Column(db.Integer)
    orddt = db.Column(db.DateTime)
    reqdt = db.Column(db.DateTime)
    reqby = db.Column(db.String(20))
    psdt = db.Column(db.DateTime, index=True)
    shipby = db.Column(db.String(20))
    stkdt = db.Column(db.DateTime)
    stkby = db.Column(db.String(20))
    actdt = db.Column(db.DateTime)
    cnldt = db.Column(db.DateTime)
    cnlby = db.Column(db.String(20))
    purby = db.Column(db.String(20))
    aptp = db.Column(db.String(10))
    aprule = db.Column(db.String(10))
    billcrcd = db.Column(db.String(3))
    crrt = db.Column(db.Numeric(12, 6))
    crcd = db.Column(db.String(3))
    fcflg = db.Column(db.String(1))
    txrt = db.Column(db.Numeric(6, 2))
    rejrsn = db.Column(db.String(10))
    exattr1 = db.Column(db.String(100))
    exattr2 = db.Column(db.String(100))
    exattr3 = db.Column(db.String(100))
    exattr4 = db.Column(db.String(100))
    exattr5 = db.Column(db.String(100))
    rmk = db.Column(db.String(255))
    ifflg = db.Column(db.String(1))
    updby = db.Column(db.String(20))
    upddt = db.Column(db.DateTime)
    sta = db.Column(db.String(3), nullable=False)
    execflg = db.Column(db.String(1))
    nxtsta = db.Column(db.String(3))
    so = db.Column(db.String(20))
    is_send_mail = db.Column(db.String(1), server_default=db.FetchedValue())


class DocReqplu(db.Model):
    __tablename__ = 'doc_reqplu'

    id = db.Column(db.Numeric(12, 0, asdecimal=False), primary_key=True)
    reqid = db.Column(db.Numeric(12, 0, asdecimal=False), index=True)
    billrsn = db.Column(db.String(20))
    venlktp = db.Column(db.String(10))
    venlkid = db.Column(db.Integer)
    deptid = db.Column(db.Integer)
    pluid = db.Column(db.Integer)
    lntp = db.Column(db.String(10))
    lnopt = db.Column(db.String(1))
    pid = db.Column(db.Numeric(12, 0, asdecimal=False))
    ordqty = db.Column(db.Numeric(16, 6))
    cfmqty = db.Column(db.Numeric(16, 6))
    uomcd = db.Column(db.String(6))
    locid = db.Column(db.Integer, server_default=db.FetchedValue())
    lotno = db.Column(db.String(20), server_default=db.FetchedValue())
    reqdt = db.Column(db.DateTime)
    reqby = db.Column(db.String(20))
    psdt = db.Column(db.DateTime)
    shipby = db.Column(db.String(20))
    cnldt = db.Column(db.DateTime)
    cnlby = db.Column(db.String(20))
    rmk = db.Column(db.String(100))
    updby = db.Column(db.String(20))
    upddt = db.Column(db.DateTime)
    sta = db.Column(db.String(3), nullable=False)
    execflg = db.Column(db.String(1), server_default=db.FetchedValue())
    nxtsta = db.Column(db.String(3))
    leafflg = db.Column(db.String(1), server_default=db.FetchedValue())
    lktp = db.Column(db.String(10))
    lkid = db.Column(db.Numeric(12, 0, asdecimal=False))
    lkdtlid = db.Column(db.Numeric(12, 0, asdecimal=False), index=True)
    adjflg = db.Column(db.String(1), server_default=db.FetchedValue())
    qty = db.Column(db.Numeric(16, 6))


class DocReqpluBak(db.Model):
    __tablename__ = 'doc_reqplu_bak'

    id = db.Column(db.Numeric(12, 0, asdecimal=False), primary_key=True)
    reqid = db.Column(db.Numeric(12, 0, asdecimal=False), index=True)
    billrsn = db.Column(db.String(20))
    venlktp = db.Column(db.String(10))
    venlkid = db.Column(db.Integer)
    deptid = db.Column(db.Integer)
    pluid = db.Column(db.Integer)
    lntp = db.Column(db.String(10))
    lnopt = db.Column(db.String(1))
    pid = db.Column(db.Numeric(12, 0, asdecimal=False))
    ordqty = db.Column(db.Numeric(16, 6))
    cfmqty = db.Column(db.Numeric(16, 6))
    uomcd = db.Column(db.String(6))
    locid = db.Column(db.Integer, server_default=db.FetchedValue())
    lotno = db.Column(db.String(20), server_default=db.FetchedValue())
    reqdt = db.Column(db.DateTime)
    reqby = db.Column(db.String(20))
    psdt = db.Column(db.DateTime)
    shipby = db.Column(db.String(20))
    cnldt = db.Column(db.DateTime)
    cnlby = db.Column(db.String(20))
    rmk = db.Column(db.String(100))
    updby = db.Column(db.String(20))
    upddt = db.Column(db.DateTime)
    sta = db.Column(db.String(3), nullable=False)
    execflg = db.Column(db.String(1), server_default=db.FetchedValue())
    nxtsta = db.Column(db.String(3))
    leafflg = db.Column(db.String(1), server_default=db.FetchedValue())
    lktp = db.Column(db.String(10))
    lkid = db.Column(db.Numeric(12, 0, asdecimal=False))
    lkdtlid = db.Column(db.Numeric(12, 0, asdecimal=False))
    adjflg = db.Column(db.String(1), server_default=db.FetchedValue())


t_doc_reqplu_mail = db.Table(
    'doc_reqplu_mail',
    db.Column('reqid', db.Numeric(12, 0, asdecimal=False))
)


t_doc_reqplutmp = db.Table(
    'doc_reqplutmp',
    db.Column('id', db.Numeric(12, 0, asdecimal=False), nullable=False),
    db.Column('reqid', db.Numeric(12, 0, asdecimal=False)),
    db.Column('billrsn', db.String(20)),
    db.Column('venlktp', db.String(10)),
    db.Column('venlkid', db.Integer),
    db.Column('deptid', db.Integer),
    db.Column('pluid', db.Integer),
    db.Column('lntp', db.String(10)),
    db.Column('lnopt', db.String(1)),
    db.Column('pid', db.Numeric(12, 0, asdecimal=False)),
    db.Column('ordqty', db.Numeric(16, 6)),
    db.Column('cfmqty', db.Numeric(16, 6)),
    db.Column('uomcd', db.String(6)),
    db.Column('locid', db.Integer, server_default=db.FetchedValue()),
    db.Column('lotno', db.String(20), server_default=db.FetchedValue()),
    db.Column('reqdt', db.DateTime),
    db.Column('reqby', db.String(20)),
    db.Column('psdt', db.DateTime),
    db.Column('shipby', db.String(20)),
    db.Column('cnldt', db.DateTime),
    db.Column('cnlby', db.String(20)),
    db.Column('rmk', db.String(100)),
    db.Column('updby', db.String(20)),
    db.Column('upddt', db.DateTime),
    db.Column('sta', db.String(3), nullable=False),
    db.Column('execflg', db.String(1), server_default=db.FetchedValue()),
    db.Column('nxtsta', db.String(3)),
    db.Column('leafflg', db.String(1), server_default=db.FetchedValue()),
    db.Column('lktp', db.String(10)),
    db.Column('lkid', db.Numeric(12, 0, asdecimal=False)),
    db.Column('lkdtlid', db.Numeric(12, 0, asdecimal=False)),
    db.Column('adjflg', db.String(1), server_default=db.FetchedValue()),
    db.Column('qty', db.Numeric(16, 6))
)


class DocRequest(db.Model):
    __tablename__ = 'doc_request'
    __table_args__ = (
        db.Index('idx_doc_reqest1', 'deptid', 'orddt'),
    )

    id = db.Column(db.Numeric(12, 0, asdecimal=False), primary_key=True)
    coid = db.Column(db.Integer)
    billtp = db.Column(db.String(10))
    billrsn = db.Column(db.String(20))
    deptid = db.Column(db.Integer)
    pluid = db.Column(db.Integer)
    venlktp = db.Column(db.String(10))
    venlkid = db.Column(db.Integer)
    orddt = db.Column(db.DateTime, index=True)
    reqdeptid = db.Column(db.Integer)
    reqdt = db.Column(db.DateTime)
    reqby = db.Column(db.String(20))
    psdt = db.Column(db.DateTime)
    shipby = db.Column(db.String(20))
    cnldt = db.Column(db.DateTime)
    cnlby = db.Column(db.String(20))
    rmk = db.Column(db.String(255))
    updby = db.Column(db.String(20))
    upddt = db.Column(db.DateTime)
    sta = db.Column(db.String(3), nullable=False)
    execflg = db.Column(db.String(1))
    nxtsta = db.Column(db.String(3))


class DocSale(db.Model):
    __tablename__ = 'doc_sale'

    id = db.Column(db.Numeric(12, 0, asdecimal=False), primary_key=True)
    coid = db.Column(db.Integer)
    billtp = db.Column(db.String(10))
    billrsn = db.Column(db.String(20))
    billlktp = db.Column(db.String(10))
    billlkid = db.Column(db.Numeric(12, 0, asdecimal=False))
    deptid = db.Column(db.Integer)
    salelktp = db.Column(db.String(10))
    salelkid = db.Column(db.Integer)
    shiplktp = db.Column(db.String(10))
    shiplkid = db.Column(db.Integer)
    orddt = db.Column(db.DateTime)
    reqdt = db.Column(db.DateTime)
    reqby = db.Column(db.String(20))
    psdt = db.Column(db.DateTime)
    shipby = db.Column(db.String(20))
    dlvlncd = db.Column(db.String(20))
    wavecd = db.Column(db.String(20))
    stkdt = db.Column(db.DateTime)
    stkby = db.Column(db.String(20))
    actdt = db.Column(db.DateTime)
    cnldt = db.Column(db.DateTime)
    cnlby = db.Column(db.String(20))
    saleby = db.Column(db.String(20))
    artp = db.Column(db.String(10))
    arrule = db.Column(db.String(10))
    billcrcd = db.Column(db.String(3))
    crrt = db.Column(db.Numeric(12, 6))
    crcd = db.Column(db.String(3))
    fcflg = db.Column(db.String(1))
    txrt = db.Column(db.Numeric(6, 2))
    rmk = db.Column(db.String(255))
    updby = db.Column(db.String(20))
    upddt = db.Column(db.DateTime)
    sta = db.Column(db.String(3), nullable=False)
    execflg = db.Column(db.String(1), server_default=db.FetchedValue())
    nxtsta = db.Column(db.String(3))


class DocSaleplu(db.Model):
    __tablename__ = 'doc_saleplu'

    id = db.Column(db.Numeric(12, 0, asdecimal=False), primary_key=True)
    saleid = db.Column(db.Numeric(12, 0, asdecimal=False), nullable=False)
    billrsn = db.Column(db.String(20))
    pluid = db.Column(db.Integer)
    lntp = db.Column(db.String(10))
    lnopt = db.Column(db.String(1))
    pid = db.Column(db.Numeric(12, 0, asdecimal=False))
    leafflg = db.Column(db.String(1), server_default=db.FetchedValue())
    ordqty = db.Column(db.Numeric(16, 6))
    orduomcd = db.Column(db.String(6))
    cfmqty = db.Column(db.Numeric(16, 6))
    stkqty = db.Column(db.Numeric(16, 6))
    stksign = db.Column(db.Integer, server_default=db.FetchedValue())
    uomcd = db.Column(db.String(6))
    csprc = db.Column(db.Numeric(16, 4))
    slprc = db.Column(db.Numeric(16, 4))
    csamt = db.Column(db.Numeric(16, 4))
    slamt = db.Column(db.Numeric(16, 4))
    txrt = db.Column(db.Numeric(6, 2))
    txamt = db.Column(db.Numeric(16, 4))
    locid = db.Column(db.Integer, server_default=db.FetchedValue())
    lotno = db.Column(db.String(20), server_default=db.FetchedValue())
    lotdesc = db.Column(db.String(80))
    lotstdt = db.Column(db.DateTime)
    loteddt = db.Column(db.DateTime)
    lotsta = db.Column(db.String(2))
    venlotno = db.Column(db.String(20))
    exlotno = db.Column(db.String(20))
    reqdt = db.Column(db.DateTime)
    reqby = db.Column(db.String(20))
    psdt = db.Column(db.DateTime)
    shipby = db.Column(db.String(20))
    stkdt = db.Column(db.DateTime)
    stkby = db.Column(db.String(20))
    actdt = db.Column(db.DateTime)
    actby = db.Column(db.String(20))
    cnldt = db.Column(db.DateTime)
    cnlby = db.Column(db.String(20))
    saleby = db.Column(db.String(20))
    rmk = db.Column(db.String(100))
    updby = db.Column(db.String(20))
    upddt = db.Column(db.DateTime)
    sta = db.Column(db.String(3), nullable=False)
    execflg = db.Column(db.String(1), server_default=db.FetchedValue())
    nxtsta = db.Column(db.String(3))
    billlktp = db.Column(db.String(10))
    billlkid = db.Column(db.Numeric(12, 0, asdecimal=False))


class DocSosta(db.Model):
    __tablename__ = 'doc_sosta'

    id = db.Column(db.Numeric(12, 0, asdecimal=False), primary_key=True)
    storeid = db.Column(db.Numeric(12, 0, asdecimal=False), index=True)
    storecd = db.Column(db.String(20))
    repocd = db.Column(db.String(20))
    reqsta = db.Column(db.String(20))
    requpddt = db.Column(db.DateTime, server_default=db.FetchedValue())
    reqtry = db.Column(db.Integer, server_default=db.FetchedValue())
    headersta = db.Column(db.String(20))
    headerupddt = db.Column(db.DateTime, server_default=db.FetchedValue())
    headertry = db.Column(db.Integer, server_default=db.FetchedValue())
    rootsta = db.Column(db.String(20))
    rootupddt = db.Column(db.DateTime, server_default=db.FetchedValue())
    roottry = db.Column(db.Integer, server_default=db.FetchedValue())
    bizdt = db.Column(db.DateTime, index=True)
    exttr1 = db.Column(db.String(30))
    exttr2 = db.Column(db.String(30))
    exttr3 = db.Column(db.String(30))
    createddt = db.Column(db.DateTime, server_default=db.FetchedValue())
    upddt = db.Column(db.DateTime, server_default=db.FetchedValue())


class DocTxfin(db.Model):
    __tablename__ = 'doc_txfin'
    __table_args__ = (
        db.Index('idx_doc_txfin2', 'orddt', 'stkdt', 'deptid'),
    )

    id = db.Column(db.Numeric(12, 0, asdecimal=False), primary_key=True)
    coid = db.Column(db.Integer)
    billtp = db.Column(db.String(10))
    billrsn = db.Column(db.String(20))
    billlktp = db.Column(db.String(10))
    billlkid = db.Column(db.Numeric(12, 0, asdecimal=False))
    deptid = db.Column(db.Integer)
    outdeptid = db.Column(db.Integer)
    orddt = db.Column(db.DateTime)
    reqdt = db.Column(db.DateTime)
    reqby = db.Column(db.String(20))
    psdt = db.Column(db.DateTime)
    shipby = db.Column(db.String(20))
    stkdt = db.Column(db.DateTime)
    stkby = db.Column(db.String(20))
    actdt = db.Column(db.DateTime)
    cnldt = db.Column(db.DateTime)
    cnlby = db.Column(db.String(20))
    purby = db.Column(db.String(20))
    aptp = db.Column(db.String(10))
    aprule = db.Column(db.String(10))
    billcrcd = db.Column(db.String(3))
    crrt = db.Column(db.Numeric(12, 6))
    crcd = db.Column(db.String(3))
    fcflg = db.Column(db.String(1))
    txrt = db.Column(db.Numeric(6, 2))
    rejrsn = db.Column(db.String(10))
    exattr1 = db.Column(db.String(100))
    exattr2 = db.Column(db.String(100))
    exattr3 = db.Column(db.String(100))
    exattr4 = db.Column(db.String(100))
    exattr5 = db.Column(db.String(100))
    rmk = db.Column(db.String(255))
    ifflg = db.Column(db.String(1), index=True)
    updby = db.Column(db.String(20))
    upddt = db.Column(db.DateTime, index=True)
    sta = db.Column(db.String(3), nullable=False)
    execflg = db.Column(db.String(1))
    nxtsta = db.Column(db.String(3))


class DocTxfinplu(db.Model):
    __tablename__ = 'doc_txfinplu'

    id = db.Column(db.Numeric(12, 0, asdecimal=False), primary_key=True)
    txinid = db.Column(db.Numeric(12, 0, asdecimal=False), nullable=False, index=True)
    billrsn = db.Column(db.String(20))
    pluid = db.Column(db.Integer)
    lntp = db.Column(db.String(10))
    lnopt = db.Column(db.String(1))
    pid = db.Column(db.Numeric(12, 0, asdecimal=False))
    leafflg = db.Column(db.String(1), server_default=db.FetchedValue())
    ordqty = db.Column(db.Numeric(16, 6))
    orduomcd = db.Column(db.String(6))
    cfmqty = db.Column(db.Numeric(16, 6))
    stkqty = db.Column(db.Numeric(16, 6))
    stksign = db.Column(db.Integer, server_default=db.FetchedValue())
    uomcd = db.Column(db.String(6))
    csprc = db.Column(db.Numeric(16, 4))
    exprc1 = db.Column(db.Numeric(16, 4))
    csamt = db.Column(db.Numeric(16, 4))
    examt1 = db.Column(db.Numeric(16, 4))
    ncflg = db.Column(db.String(1), server_default=db.FetchedValue())
    txrt = db.Column(db.Numeric(8, 4))
    extxrt1 = db.Column(db.Numeric(8, 4))
    txamt = db.Column(db.Numeric(16, 4))
    extxamt1 = db.Column(db.Numeric(16, 4))
    locid = db.Column(db.Integer, server_default=db.FetchedValue())
    lotno = db.Column(db.String(20), server_default=db.FetchedValue())
    lotdesc = db.Column(db.String(80))
    lotstdt = db.Column(db.DateTime)
    loteddt = db.Column(db.DateTime)
    lotsta = db.Column(db.String(2))
    venlotno = db.Column(db.String(20))
    exlotno = db.Column(db.String(20))
    reqdt = db.Column(db.DateTime)
    reqby = db.Column(db.String(20))
    psdt = db.Column(db.DateTime)
    shipby = db.Column(db.String(20))
    stkdt = db.Column(db.DateTime)
    stkby = db.Column(db.String(20))
    actdt = db.Column(db.DateTime)
    actby = db.Column(db.String(20))
    cnldt = db.Column(db.DateTime)
    cnlby = db.Column(db.String(20))
    purby = db.Column(db.String(20))
    rmk = db.Column(db.String(100))
    updby = db.Column(db.String(20))
    upddt = db.Column(db.DateTime)
    finadjflg = db.Column(db.String(1), server_default=db.FetchedValue())
    sta = db.Column(db.String(3), nullable=False)
    execflg = db.Column(db.String(1), server_default=db.FetchedValue())
    nxtsta = db.Column(db.String(3))
    billlktp = db.Column(db.String(10))
    billlkid = db.Column(db.Numeric(12, 0, asdecimal=False))


class DocTxfout(db.Model):
    __tablename__ = 'doc_txfout'
    __table_args__ = (
        db.Index('idx_doctxfupd1', 'deptid', 'orddt'),
    )

    id = db.Column(db.Numeric(12, 0, asdecimal=False), primary_key=True)
    coid = db.Column(db.Integer)
    billtp = db.Column(db.String(10))
    billrsn = db.Column(db.String(20))
    billlktp = db.Column(db.String(10))
    billlkid = db.Column(db.Numeric(12, 0, asdecimal=False))
    deptid = db.Column(db.Integer)
    indeptid = db.Column(db.Integer)
    orddt = db.Column(db.DateTime)
    reqdt = db.Column(db.DateTime)
    reqby = db.Column(db.String(20))
    psdt = db.Column(db.DateTime)
    shipby = db.Column(db.String(20))
    stkdt = db.Column(db.DateTime)
    stkby = db.Column(db.String(20))
    actdt = db.Column(db.DateTime)
    cnldt = db.Column(db.DateTime)
    cnlby = db.Column(db.String(20))
    saleby = db.Column(db.String(20))
    artp = db.Column(db.String(10))
    arrule = db.Column(db.String(10))
    billcrcd = db.Column(db.String(3))
    crrt = db.Column(db.Numeric(12, 6))
    crcd = db.Column(db.String(3))
    fcflg = db.Column(db.String(1))
    txrt = db.Column(db.Numeric(6, 2))
    rmk = db.Column(db.String(255))
    updby = db.Column(db.String(20))
    upddt = db.Column(db.DateTime, index=True)
    sta = db.Column(db.String(3), nullable=False)
    execflg = db.Column(db.String(1), server_default=db.FetchedValue())
    nxtsta = db.Column(db.String(3))


class DocTxfoutplu(db.Model):
    __tablename__ = 'doc_txfoutplu'

    id = db.Column(db.Numeric(12, 0, asdecimal=False), primary_key=True)
    txfoutid = db.Column(db.Numeric(12, 0, asdecimal=False), nullable=False, index=True)
    billrsn = db.Column(db.String(20))
    pluid = db.Column(db.Integer)
    lntp = db.Column(db.String(10))
    lnopt = db.Column(db.String(1))
    pid = db.Column(db.Numeric(12, 0, asdecimal=False))
    leafflg = db.Column(db.String(1), server_default=db.FetchedValue())
    ordqty = db.Column(db.Numeric(16, 6))
    orduomcd = db.Column(db.String(6))
    cfmqty = db.Column(db.Numeric(16, 6))
    stkqty = db.Column(db.Numeric(16, 6))
    stksign = db.Column(db.Integer, server_default=db.FetchedValue())
    uomcd = db.Column(db.String(6))
    csprc = db.Column(db.Numeric(16, 4))
    slprc = db.Column(db.Numeric(16, 4))
    csamt = db.Column(db.Numeric(16, 4))
    slamt = db.Column(db.Numeric(16, 4))
    txrt = db.Column(db.Numeric(6, 2))
    txamt = db.Column(db.Numeric(16, 4))
    locid = db.Column(db.Integer, server_default=db.FetchedValue())
    lotno = db.Column(db.String(20), server_default=db.FetchedValue())
    lotdesc = db.Column(db.String(80))
    lotstdt = db.Column(db.DateTime)
    loteddt = db.Column(db.DateTime)
    lotsta = db.Column(db.String(2))
    venlotno = db.Column(db.String(20))
    exlotno = db.Column(db.String(20))
    reqdt = db.Column(db.DateTime)
    reqby = db.Column(db.String(20))
    psdt = db.Column(db.DateTime)
    shipby = db.Column(db.String(20))
    stkdt = db.Column(db.DateTime)
    stkby = db.Column(db.String(20))
    actdt = db.Column(db.DateTime)
    actby = db.Column(db.String(20))
    cnldt = db.Column(db.DateTime)
    cnlby = db.Column(db.String(20))
    saleby = db.Column(db.String(20))
    rmk = db.Column(db.String(100))
    updby = db.Column(db.String(20))
    upddt = db.Column(db.DateTime)
    sta = db.Column(db.String(3), nullable=False)
    execflg = db.Column(db.String(1), server_default=db.FetchedValue())
    nxtsta = db.Column(db.String(3))
    billlktp = db.Column(db.String(10))
    billlkid = db.Column(db.Numeric(12, 0, asdecimal=False))


t_ds_temp = db.Table(
    'ds_temp',
    db.Column('transno', db.Numeric(20, 0, asdecimal=False), nullable=False)
)


t_ds_tmp = db.Table(
    'ds_tmp',
    db.Column('store_no', db.String(10), nullable=False),
    db.Column('pos_no', db.String(10), nullable=False),
    db.Column('busi_date', db.DateTime, nullable=False),
    db.Column('card_no', db.String(50)),
    db.Column('pos_amt', db.Numeric(10, 2)),
    db.Column('flow_no', db.String(20)),
    db.Column('busi_no', db.String(30)),
    db.Column('eternal_no', db.String(30)),
    db.Column('batch_no', db.String(30)),
    db.Column('card_type', db.String(30)),
    db.Column('issue_no', db.String(30)),
    db.Column('sys_no', db.String(30))
)


t_ds_tmp2 = db.Table(
    'ds_tmp2',
    db.Column('trade_code', db.String(20), nullable=False),
    db.Column('dal_id', db.Numeric(12, 0, asdecimal=False), nullable=False),
    db.Column('tran_date', db.DateTime),
    db.Column('dal_status', db.String(3), nullable=False),
    db.Column('acid', db.Integer),
    db.Column('dal_stval', db.Numeric(18, 2)),
    db.Column('dal_hqval', db.Numeric(18, 2))
)


t_ds_tmp_scrap = db.Table(
    'ds_tmp_scrap',
    db.Column('deptcd', db.String(20), nullable=False),
    db.Column('deptname', db.Unicode(50), nullable=False),
    db.Column('orddt', db.DateTime),
    db.Column('stkqty', db.Numeric(16, 6)),
    db.Column('billrsn', db.String(20)),
    db.Column('cd', db.String(20)),
    db.Column('nm_l_zh', db.Unicode(100)),
    db.Column('prc', db.Numeric(asdecimal=False)),
    db.Column('prc2', db.Numeric(asdecimal=False))
)


t_emp_disc = db.Table(
    'emp_disc',
    db.Column('userid', db.Integer),
    db.Column('month', db.String(8)),
    db.Column('cnt', db.Integer),
    db.Column('discno', db.Integer),
    db.Column('upddt', db.DateTime),
    db.Column('rmk', db.String(20)),
    db.Index('idx_emp_disc', 'month', 'userid'),
    db.Index('idx$$_117590001', 'month', 'userid', 'discno')
)


t_emp_discdtl = db.Table(
    'emp_discdtl',
    db.Column('userid', db.Integer),
    db.Column('month', db.String(8)),
    db.Column('cnt', db.Integer),
    db.Column('transno', db.Numeric(16, 0, asdecimal=False)),
    db.Column('discno', db.Integer),
    db.Column('upddt', db.DateTime),
    db.Column('deptcd', db.String(20)),
    db.Column('traddate', db.DateTime),
    db.Column('bizdt', db.DateTime),
    db.Column('saleid', db.Integer)
)


class EstDept(db.Model):
    __tablename__ = 'est_dept'
    __table_args__ = (
        db.Index('idx_est_parplu2', 'deptid', 'partp'),
    )

    id = db.Column(db.Integer, primary_key=True)
    deptid = db.Column(db.Integer, nullable=False)
    w1 = db.Column(db.String(1))
    w2 = db.Column(db.String(1))
    w3 = db.Column(db.String(1))
    w4 = db.Column(db.String(1))
    w5 = db.Column(db.String(1))
    w6 = db.Column(db.String(1))
    w7 = db.Column(db.String(1))
    isopenord = db.Column(db.String(1))
    partp = db.Column(db.String(1), nullable=False, server_default=db.FetchedValue())
    stdt = db.Column(db.DateTime)
    eddt = db.Column(db.DateTime)
    rmk = db.Column(db.String(250))
    updby = db.Column(db.String(50))
    upddt = db.Column(db.DateTime)
    sta = db.Column(db.String(3), nullable=False)
    execflg = db.Column(db.String(1))
    nxtsta = db.Column(db.String(3))


class EstOrderitem(db.Model):
    __tablename__ = 'est_orderitem'
    __table_args__ = (
        db.Index('idx_net_id', 'deptid', 'pluid', 'bizdt'),
    )

    id = db.Column(db.Integer, primary_key=True)
    deptid = db.Column(db.Integer)
    dcid = db.Column(db.Integer)
    pluid = db.Column(db.Integer)
    bizdt = db.Column(db.DateTime)
    advord_qty = db.Column(db.Numeric(14, 4), server_default=db.FetchedValue())
    radvord_qty = db.Column(db.Numeric(14, 4), server_default=db.FetchedValue())
    advmax_qty = db.Column(db.Numeric(14, 4), server_default=db.FetchedValue())
    radvmax_qty = db.Column(db.Numeric(14, 4), server_default=db.FetchedValue())
    minord_qty = db.Column(db.Numeric(14, 4), server_default=db.FetchedValue())
    maxord_qty = db.Column(db.Numeric(14, 4), server_default=db.FetchedValue())
    incord_qty = db.Column(db.Numeric(14, 4), server_default=db.FetchedValue())
    dlvstk_qty = db.Column(db.Numeric(14, 4), server_default=db.FetchedValue())
    ref_qty = db.Column(db.Numeric(14, 4), server_default=db.FetchedValue())
    planpdc_rate = db.Column(db.Numeric(14, 4), server_default=db.FetchedValue())
    lwk_qty = db.Column(db.Numeric(14, 4), server_default=db.FetchedValue())
    lday_qty = db.Column(db.Numeric(14, 4), server_default=db.FetchedValue())
    cday_qty = db.Column(db.Numeric(14, 4), server_default=db.FetchedValue())
    lwkrcv_qty = db.Column(db.Numeric(14, 4), server_default=db.FetchedValue())
    lwkti_qty = db.Column(db.Numeric(14, 4), server_default=db.FetchedValue())
    lwkto_qty = db.Column(db.Numeric(14, 4), server_default=db.FetchedValue())
    lmthsal_qty = db.Column(db.Numeric(14, 4), server_default=db.FetchedValue())
    lmthede_qty = db.Column(db.Numeric(14, 4), server_default=db.FetchedValue())
    lmthbgn_qty = db.Column(db.Numeric(14, 4), server_default=db.FetchedValue())
    lmthend_qty = db.Column(db.Numeric(14, 4), server_default=db.FetchedValue())
    lmthrcv_qty = db.Column(db.Numeric(14, 4), server_default=db.FetchedValue())
    lmthti_qty = db.Column(db.Numeric(14, 4), server_default=db.FetchedValue())
    lmthto_qty = db.Column(db.Numeric(14, 4), server_default=db.FetchedValue())
    splanpdc_rate = db.Column(db.Numeric(14, 4), server_default=db.FetchedValue())
    slwkepd_qty = db.Column(db.Numeric(14, 4), server_default=db.FetchedValue())
    slmthinv_qty = db.Column(db.Numeric(14, 4), server_default=db.FetchedValue())
    stermrcv_qty = db.Column(db.Numeric(14, 4), server_default=db.FetchedValue())
    slmthinv_date = db.Column(db.DateTime)
    thismthsal_qty = db.Column(db.Numeric(14, 4), server_default=db.FetchedValue())
    thismthede_qty = db.Column(db.Numeric(14, 4), server_default=db.FetchedValue())
    cal_no = db.Column(db.String(20))
    is_cal = db.Column(db.String(1), server_default=db.FetchedValue())
    sta = db.Column(db.String(1), server_default=db.FetchedValue())
    update_date = db.Column(db.DateTime, server_default=db.FetchedValue())
    update_by = db.Column(db.String(50))
    is_delete = db.Column(db.String(1), server_default=db.FetchedValue())


t_est_ordftp = db.Table(
    'est_ordftp',
    db.Column('id', db.Integer, nullable=False),
    db.Column('ordfno', db.String(20)),
    db.Column('ordfname', db.String(50)),
    db.Column('ratio1', db.Numeric(16, 4)),
    db.Column('ratio2', db.Numeric(16, 4)),
    db.Column('ratio3', db.Numeric(16, 4)),
    db.Column('maxord_rt', db.Numeric(16, 4)),
    db.Column('remark', db.String(255)),
    db.Column('is_delete', db.String(1), nullable=False, server_default=db.FetchedValue()),
    db.Column('update_date', db.DateTime, server_default=db.FetchedValue()),
    db.Column('update_by', db.String(50))
)


class EstPar(db.Model):
    __tablename__ = 'est_par'
    __table_args__ = (
        db.Index('idx_est_par', 'deptid', 'pluid', 'partp'),
    )

    id = db.Column(db.Integer, primary_key=True)
    deptid = db.Column(db.Integer, nullable=False)
    pluid = db.Column(db.Integer, nullable=False)
    parqty = db.Column(db.Integer, server_default=db.FetchedValue())
    partp = db.Column(db.String(1), nullable=False, server_default=db.FetchedValue())
    updby = db.Column(db.String(50))
    upddt = db.Column(db.DateTime)
    rmk = db.Column(db.String(250))
    sta = db.Column(db.String(3), nullable=False)
    execflg = db.Column(db.String(1))
    nxtsta = db.Column(db.String(3))


class EstParTmp(db.Model):
    __tablename__ = 'est_par_tmp'
    __table_args__ = (
        db.Index('idx_est_par_tmp', 'deptid', 'pluid', 'partp'),
    )

    id = db.Column(db.Integer, primary_key=True)
    deptid = db.Column(db.Integer, nullable=False)
    pluid = db.Column(db.Integer, nullable=False)
    parqty = db.Column(db.Integer, server_default=db.FetchedValue())
    partp = db.Column(db.String(1), nullable=False, server_default=db.FetchedValue())
    updby = db.Column(db.String(50))
    upddt = db.Column(db.DateTime)
    rmk = db.Column(db.String(250))
    sta = db.Column(db.String(3), nullable=False)
    execflg = db.Column(db.String(1))
    nxtsta = db.Column(db.String(3))


class EstParplu(db.Model):
    __tablename__ = 'est_parplu'
    __table_args__ = (
        db.Index('idx_est_parplu', 'pluid', 'partp'),
    )

    id = db.Column(db.Integer, primary_key=True)
    pluid = db.Column(db.Integer, nullable=False)
    stdt = db.Column(db.DateTime)
    eddt = db.Column(db.DateTime)
    rmk = db.Column(db.String(250))
    partp = db.Column(db.String(1), nullable=False)
    updby = db.Column(db.String(50))
    upddt = db.Column(db.DateTime)
    sta = db.Column(db.String(3), nullable=False)
    execflg = db.Column(db.String(1))
    nxtsta = db.Column(db.String(3))


t_fd_asn_dept_daily = db.Table(
    'fd_asn_dept_daily',
    db.Column('deptcd', db.String(20)),
    db.Column('plucd', db.String(20)),
    db.Column('plunm', db.String(50)),
    db.Column('qty', db.Integer),
    db.Column('created', db.DateTime, server_default=db.FetchedValue()),
    db.Column('updated', db.DateTime, server_default=db.FetchedValue()),
    db.Column('sta', db.Integer, server_default=db.FetchedValue()),
    db.Column('bizdt', db.DateTime)
)


t_fd_sales_dept_weekly = db.Table(
    'fd_sales_dept_weekly',
    db.Column('deptcd', db.String(20)),
    db.Column('weekno', db.Integer),
    db.Column('plucd', db.String(20)),
    db.Column('plunm', db.String(50)),
    db.Column('q1', db.Integer),
    db.Column('q2', db.Integer),
    db.Column('q3', db.Integer),
    db.Column('q4', db.Integer),
    db.Column('q5', db.Integer),
    db.Column('q6', db.Integer),
    db.Column('q7', db.Integer),
    db.Column('sta', db.Integer, server_default=db.FetchedValue()),
    db.Column('created', db.DateTime, server_default=db.FetchedValue()),
    db.Column('updated', db.DateTime, server_default=db.FetchedValue()),
    db.Column('bizdt', db.DateTime)
)


t_fd_sales_hundred = db.Table(
    'fd_sales_hundred',
    db.Column('deptcd', db.String(20)),
    db.Column('bizdt', db.DateTime),
    db.Column('qty', db.Integer),
    db.Column('created', db.DateTime, server_default=db.FetchedValue()),
    db.Column('updated', db.DateTime, server_default=db.FetchedValue()),
    db.Column('sta', db.Integer, server_default=db.FetchedValue())
)


t_fd_sales_log = db.Table(
    'fd_sales_log',
    db.Column('process_cd', db.String(20)),
    db.Column('stacd', db.String(50)),
    db.Column('bizdt', db.DateTime, index=True, server_default=db.FetchedValue()),
    db.Column('sta', db.Integer),
    db.Column('created', db.DateTime, server_default=db.FetchedValue()),
    db.Column('updated', db.DateTime, server_default=db.FetchedValue())
)


class FinAmtadj(db.Model):
    __tablename__ = 'fin_amtadj'

    ptid = db.Column(db.Integer, primary_key=True, nullable=False)
    pluid = db.Column(db.Integer, primary_key=True, nullable=False)
    costtplid = db.Column(db.Integer, primary_key=True, nullable=False)
    amt = db.Column(db.Numeric(18, 6))
    rmk = db.Column(db.String(255))


t_fin_bomstk = db.Table(
    'fin_bomstk',
    db.Column('ptid', db.Integer, index=True),
    db.Column('yearno', db.Integer, nullable=False),
    db.Column('monthno', db.Integer, nullable=False),
    db.Column('deptlktp', db.String(10), nullable=False),
    db.Column('deptlkid', db.Integer, nullable=False),
    db.Column('pluid', db.Integer, nullable=False),
    db.Column('adjqty', db.Numeric(20, 6), server_default=db.FetchedValue()),
    db.Column('endcost', db.Numeric(20, 6), server_default=db.FetchedValue()),
    db.Column('inpluid', db.Integer, nullable=False),
    db.Column('adjinqty', db.Numeric(18, 6), server_default=db.FetchedValue()),
    db.Column('calcost', db.Numeric(20, 6), server_default=db.FetchedValue()),
    db.Column('crcd', db.String(3), server_default=db.FetchedValue()),
    db.Column('upddt', db.DateTime),
    db.Column('sta', db.String(3)),
    db.Column('saleqty', db.Numeric(20, 6), server_default=db.FetchedValue()),
    db.Column('saleinqty', db.Numeric(20, 6), server_default=db.FetchedValue()),
    db.Column('bgncost', db.Numeric(20, 6), server_default=db.FetchedValue()),
    db.Column('inbgncost', db.Numeric(20, 6), server_default=db.FetchedValue()),
    db.Column('inendcost', db.Numeric(20, 6), server_default=db.FetchedValue()),
    db.Column('rmk', db.String(255)),
    db.Index('idx_fin_bomstk2', 'ptid', 'deptlktp', 'deptlkid')
)


t_fin_bomstk_sun2018 = db.Table(
    'fin_bomstk_sun2018',
    db.Column('ptid', db.Integer),
    db.Column('yearno', db.Integer, nullable=False),
    db.Column('monthno', db.Integer, nullable=False),
    db.Column('deptlktp', db.String(10), nullable=False),
    db.Column('deptlkid', db.Integer, nullable=False),
    db.Column('pluid', db.Integer, nullable=False),
    db.Column('adjqty', db.Numeric(20, 6)),
    db.Column('endcost', db.Numeric(20, 6)),
    db.Column('inpluid', db.Integer, nullable=False),
    db.Column('adjinqty', db.Numeric(18, 6)),
    db.Column('calcost', db.Numeric(20, 6)),
    db.Column('crcd', db.String(3)),
    db.Column('upddt', db.DateTime),
    db.Column('sta', db.String(3)),
    db.Column('saleqty', db.Numeric(20, 6)),
    db.Column('saleinqty', db.Numeric(20, 6)),
    db.Column('bgncost', db.Numeric(20, 6)),
    db.Column('inbgncost', db.Numeric(20, 6)),
    db.Column('inendcost', db.Numeric(20, 6)),
    db.Column('rmk', db.String(255))
)


class FinCostmp(db.Model):
    __tablename__ = 'fin_costmp'
    __table_args__ = (
        db.Index('idx_fin_costmp_01', 'deptlktp', 'pluid'),
    )

    ptid = db.Column(db.Integer, index=True)
    yearno = db.Column(db.Integer, primary_key=True, nullable=False)
    monthno = db.Column(db.Integer, primary_key=True, nullable=False)
    deptlktp = db.Column(db.String(10), primary_key=True, nullable=False)
    deptlkid = db.Column(db.Integer, primary_key=True, nullable=False)
    pluid = db.Column(db.Integer, primary_key=True, nullable=False)
    lotno = db.Column(db.String(20), nullable=False, server_default=db.FetchedValue())
    bgnqty = db.Column(db.Numeric(18, 6))
    bgncost = db.Column(db.Numeric(18, 6))
    bgnamt = db.Column(db.Numeric(18, 6))
    purqty = db.Column(db.Numeric(18, 6))
    puramt = db.Column(db.Numeric(18, 6))
    feeamt = db.Column(db.Numeric(18, 6))
    invadjamt = db.Column(db.Numeric(18, 6))
    puradjamt = db.Column(db.Numeric(18, 6))
    txoqty = db.Column(db.Numeric(18, 6))
    txiqty = db.Column(db.Numeric(18, 6))
    adjqty = db.Column(db.Numeric(18, 6))
    bomoutqty = db.Column(db.Numeric(18, 6))
    bomcsamt = db.Column(db.Numeric(20, 6))
    bomprcinqty = db.Column(db.Numeric(18, 6))
    saleqty = db.Column(db.Numeric(18, 6))
    dlvqty = db.Column(db.Numeric(18, 6))
    rcvqty = db.Column(db.Numeric(18, 6))
    invqty = db.Column(db.Numeric(18, 6))
    endqty = db.Column(db.Numeric(18, 6))
    endcost = db.Column(db.Numeric(18, 6))
    endamt = db.Column(db.Numeric(18, 6))
    enddtqty = db.Column(db.Numeric(18, 6))
    enddtamt = db.Column(db.Numeric(18, 6))
    defqty = db.Column(db.Numeric(18, 6))
    defamt = db.Column(db.Numeric(18, 6))
    estprc = db.Column(db.Numeric(20, 6))
    accendamt = db.Column(db.Numeric(18, 6))
    crcd = db.Column(db.String(10), server_default=db.FetchedValue())
    upddt = db.Column(db.DateTime)
    sta = db.Column(db.String(3))
    bomadjinqty = db.Column(db.Numeric(18, 6))
    bomsaleinqty = db.Column(db.Numeric(18, 6))


t_fin_costmp_sun2018 = db.Table(
    'fin_costmp_sun2018',
    db.Column('ptid', db.Integer),
    db.Column('yearno', db.Integer, nullable=False),
    db.Column('monthno', db.Integer, nullable=False),
    db.Column('deptlktp', db.String(10), nullable=False),
    db.Column('deptlkid', db.Integer, nullable=False),
    db.Column('pluid', db.Integer, nullable=False),
    db.Column('lotno', db.String(20)),
    db.Column('bgnqty', db.Numeric(18, 6)),
    db.Column('bgncost', db.Numeric(18, 6)),
    db.Column('bgnamt', db.Numeric(18, 6)),
    db.Column('purqty', db.Numeric(18, 6)),
    db.Column('puramt', db.Numeric(18, 6)),
    db.Column('feeamt', db.Numeric(18, 6)),
    db.Column('invadjamt', db.Numeric(18, 6)),
    db.Column('puradjamt', db.Numeric(18, 6)),
    db.Column('txoqty', db.Numeric(18, 6)),
    db.Column('txiqty', db.Numeric(18, 6)),
    db.Column('adjqty', db.Numeric(18, 6)),
    db.Column('bomoutqty', db.Numeric(18, 6)),
    db.Column('bomcsamt', db.Numeric(20, 6)),
    db.Column('bomprcinqty', db.Numeric(18, 6)),
    db.Column('saleqty', db.Numeric(18, 6)),
    db.Column('dlvqty', db.Numeric(18, 6)),
    db.Column('rcvqty', db.Numeric(18, 6)),
    db.Column('invqty', db.Numeric(18, 6)),
    db.Column('endqty', db.Numeric(18, 6)),
    db.Column('endcost', db.Numeric(18, 6)),
    db.Column('endamt', db.Numeric(18, 6)),
    db.Column('enddtqty', db.Numeric(18, 6)),
    db.Column('enddtamt', db.Numeric(18, 6)),
    db.Column('defqty', db.Numeric(18, 6)),
    db.Column('defamt', db.Numeric(18, 6)),
    db.Column('estprc', db.Numeric(20, 6)),
    db.Column('accendamt', db.Numeric(18, 6)),
    db.Column('crcd', db.String(10)),
    db.Column('upddt', db.DateTime),
    db.Column('sta', db.String(3)),
    db.Column('bomadjinqty', db.Numeric(18, 6)),
    db.Column('bomsaleinqty', db.Numeric(18, 6))
)


class FinCostmphi(db.Model):
    __tablename__ = 'fin_costmphis'
    __table_args__ = (
        db.Index('idx_fin_costmphis_01', 'ptid', 'deptlkid'),
    )

    ptid = db.Column(db.Integer, index=True)
    yearno = db.Column(db.Integer, primary_key=True, nullable=False)
    monthno = db.Column(db.Integer, primary_key=True, nullable=False)
    deptlktp = db.Column(db.String(10), primary_key=True, nullable=False)
    deptlkid = db.Column(db.Integer, primary_key=True, nullable=False)
    pluid = db.Column(db.Integer, primary_key=True, nullable=False)
    lotno = db.Column(db.String(20), nullable=False, server_default=db.FetchedValue())
    bgnqty = db.Column(db.Numeric(18, 6))
    bgncost = db.Column(db.Numeric(18, 6))
    bgnamt = db.Column(db.Numeric(18, 6))
    purqty = db.Column(db.Numeric(18, 6))
    puramt = db.Column(db.Numeric(18, 6))
    feeamt = db.Column(db.Numeric(18, 6))
    invadjamt = db.Column(db.Numeric(18, 6))
    puradjamt = db.Column(db.Numeric(18, 6))
    txoqty = db.Column(db.Numeric(18, 6))
    txiqty = db.Column(db.Numeric(18, 6))
    adjqty = db.Column(db.Numeric(18, 6))
    bomoutqty = db.Column(db.Numeric(18, 6))
    bomcsamt = db.Column(db.Numeric(20, 6))
    bomprcinqty = db.Column(db.Numeric(18, 6))
    saleqty = db.Column(db.Numeric(18, 6))
    dlvqty = db.Column(db.Numeric(18, 6))
    rcvqty = db.Column(db.Numeric(18, 6))
    invqty = db.Column(db.Numeric(18, 6))
    endqty = db.Column(db.Numeric(18, 6))
    endcost = db.Column(db.Numeric(18, 6))
    endamt = db.Column(db.Numeric(18, 6))
    enddtqty = db.Column(db.Numeric(18, 6))
    enddtamt = db.Column(db.Numeric(18, 6))
    defqty = db.Column(db.Numeric(18, 6))
    defamt = db.Column(db.Numeric(18, 6))
    estprc = db.Column(db.Numeric(20, 6))
    accendamt = db.Column(db.Numeric(18, 6))
    upddt = db.Column(db.DateTime)
    crcd = db.Column(db.String(3), server_default=db.FetchedValue())
    sta = db.Column(db.String(3))
    bomadjinqty = db.Column(db.Numeric(18, 6), server_default=db.FetchedValue())
    bomsaleinqty = db.Column(db.Numeric(18, 6), server_default=db.FetchedValue())


class FinInvadj(db.Model):
    __tablename__ = 'fin_invadj'

    id = db.Column(db.Numeric(12, 0, asdecimal=False), primary_key=True)
    invid = db.Column(db.Numeric(12, 0, asdecimal=False))
    pluid = db.Column(db.Integer)
    adjamt = db.Column(db.Numeric(18, 6))
    adjtax = db.Column(db.Numeric(18, 6))
    upddt = db.Column(db.DateTime)
    updby = db.Column(db.String(20))
    rmk = db.Column(db.String(250))
    sta = db.Column(db.String(3), nullable=False)
    execflg = db.Column(db.String(1))
    nxtsta = db.Column(db.String(3))


t_fin_invadj_hhs = db.Table(
    'fin_invadj_hhs',
    db.Column('id', db.Numeric(12, 0, asdecimal=False), nullable=False),
    db.Column('invid', db.Numeric(12, 0, asdecimal=False)),
    db.Column('pluid', db.Integer),
    db.Column('adjamt', db.Numeric(18, 6)),
    db.Column('adjtax', db.Numeric(18, 6)),
    db.Column('upddt', db.DateTime),
    db.Column('updby', db.String(20)),
    db.Column('rmk', db.String(250)),
    db.Column('sta', db.String(3), nullable=False),
    db.Column('execflg', db.String(1)),
    db.Column('nxtsta', db.String(3))
)


class FinInvdoc(db.Model):
    __tablename__ = 'fin_invdoc'

    id = db.Column(db.Numeric(12, 0, asdecimal=False), primary_key=True)
    invid = db.Column(db.Numeric(12, 0, asdecimal=False), index=True)
    billlktp = db.Column(db.String(10))
    billlkid = db.Column(db.Numeric(12, 0, asdecimal=False), index=True)
    venid = db.Column(db.Integer)
    rcvamt = db.Column(db.Numeric(20, 6))
    rcvtaxamt = db.Column(db.Numeric(20, 6))
    updby = db.Column(db.String(20))
    upddt = db.Column(db.DateTime)
    sta = db.Column(db.String(3), nullable=False)
    execflg = db.Column(db.String(1))
    nxtsta = db.Column(db.String(3))


class FinInvdtl(db.Model):
    __tablename__ = 'fin_invdtl'

    id = db.Column(db.Numeric(12, 0, asdecimal=False), primary_key=True)
    invid = db.Column(db.Numeric(12, 0, asdecimal=False), nullable=False)
    invcd = db.Column(db.String(250))
    invscd = db.Column(db.String(50))
    invdt = db.Column(db.DateTime)
    amt = db.Column(db.Numeric(20, 6))
    taxamt = db.Column(db.Numeric(20, 6))
    updby = db.Column(db.String(20))
    upddt = db.Column(db.DateTime)
    sta = db.Column(db.String(3), nullable=False)
    execflg = db.Column(db.String(1))
    nxtsta = db.Column(db.String(3))
    branchcompany = db.Column(db.String(50))


class FinInvoice(db.Model):
    __tablename__ = 'fin_invoice'

    id = db.Column(db.Numeric(12, 0, asdecimal=False), primary_key=True)
    coid = db.Column(db.Integer)
    billtp = db.Column(db.String(10))
    billcd = db.Column(db.Numeric(12, 0, asdecimal=False))
    billrsn = db.Column(db.String(20))
    deptid = db.Column(db.Integer)
    orddt = db.Column(db.DateTime)
    actdt = db.Column(db.DateTime)
    venid = db.Column(db.Integer)
    invamt = db.Column(db.Numeric(20, 6), server_default=db.FetchedValue())
    txamt = db.Column(db.Numeric(20, 6), server_default=db.FetchedValue())
    rcvamt = db.Column(db.Numeric(20, 6), server_default=db.FetchedValue())
    rcvtaxamt = db.Column(db.Numeric(20, 6), server_default=db.FetchedValue())
    adjamt = db.Column(db.Numeric(18, 6), server_default=db.FetchedValue())
    adjtax = db.Column(db.Numeric(18, 6), server_default=db.FetchedValue())
    rmk = db.Column(db.String(255))
    updby = db.Column(db.String(20))
    upddt = db.Column(db.DateTime)
    sta = db.Column(db.String(3), nullable=False)
    execflg = db.Column(db.String(1), server_default=db.FetchedValue())
    nxtsta = db.Column(db.String(3))
    adjflg = db.Column(db.String(1), server_default=db.FetchedValue())
    bizdt = db.Column(db.DateTime)


t_fin_period = db.Table(
    'fin_period',
    db.Column('yearno', db.Integer, nullable=False),
    db.Column('monthno', db.Integer, nullable=False),
    db.Column('weekno', db.Integer, nullable=False),
    db.Column('deptid', db.Integer, nullable=False),
    db.Column('pluid', db.Integer, nullable=False),
    db.Column('bgnqty', db.Numeric(16, 6)),
    db.Column('bgnamt', db.Numeric(16, 4)),
    db.Column('endqty', db.Numeric(16, 6)),
    db.Column('endamt', db.Numeric(16, 4)),
    db.Column('wbgnqty', db.Numeric(16, 6)),
    db.Column('wbgnamt', db.Numeric(16, 4)),
    db.Column('wendqty', db.Numeric(16, 6)),
    db.Column('wendamt', db.Numeric(16, 4)),
    db.Column('lqty1', db.Numeric(16, 6)),
    db.Column('lamt1', db.Numeric(16, 4)),
    db.Column('lqty2', db.Numeric(16, 6)),
    db.Column('lamt2', db.Numeric(16, 4)),
    db.Column('lqty3', db.Numeric(16, 6)),
    db.Column('lamt3', db.Numeric(16, 4)),
    db.Column('lqty4', db.Numeric(16, 6)),
    db.Column('lamt4', db.Numeric(16, 4)),
    db.Column('lqty5', db.Numeric(16, 6)),
    db.Column('lamt5', db.Numeric(16, 4)),
    db.Column('lqty6', db.Numeric(16, 6)),
    db.Column('lamt6', db.Numeric(16, 4)),
    db.Column('lqty7', db.Numeric(16, 6)),
    db.Column('lamt7', db.Numeric(16, 4)),
    db.Column('lqty8', db.Numeric(16, 6)),
    db.Column('lamt8', db.Numeric(16, 4)),
    db.Column('lqty9', db.Numeric(16, 6)),
    db.Column('lamt9', db.Numeric(16, 4)),
    db.Column('lqty10', db.Numeric(16, 6)),
    db.Column('lamt10', db.Numeric(16, 4)),
    db.Column('lqty11', db.Numeric(16, 6)),
    db.Column('lamt11', db.Numeric(16, 4)),
    db.Column('lqty12', db.Numeric(16, 6)),
    db.Column('lamt12', db.Numeric(16, 4)),
    db.Column('lqty13', db.Numeric(16, 6)),
    db.Column('lamt13', db.Numeric(16, 4)),
    db.Column('lqty14', db.Numeric(16, 6)),
    db.Column('lamt14', db.Numeric(16, 4)),
    db.Column('lqty15', db.Numeric(16, 6)),
    db.Column('lamt15', db.Numeric(16, 4)),
    db.Column('lqty16', db.Numeric(16, 6)),
    db.Column('lamt16', db.Numeric(16, 4))
)


class FinPlucost(db.Model):
    __tablename__ = 'fin_plucost'

    ptid = db.Column(db.Integer)
    yearno = db.Column(db.Integer, primary_key=True, nullable=False)
    monthno = db.Column(db.Integer, primary_key=True, nullable=False)
    deptlktp = db.Column(db.String(10), primary_key=True, nullable=False)
    deptlkid = db.Column(db.Integer, primary_key=True, nullable=False)
    pluid = db.Column(db.Integer, primary_key=True, nullable=False)
    lotno = db.Column(db.String(20), nullable=False, server_default=db.FetchedValue())
    bgncsprc = db.Column(db.Numeric(20, 6))
    csprc = db.Column(db.Numeric(20, 6))
    estprc = db.Column(db.Numeric(20, 6))
    crcd = db.Column(db.String(3), server_default=db.FetchedValue())
    upddt = db.Column(db.DateTime)


class FinPlucosthi(db.Model):
    __tablename__ = 'fin_plucosthis'

    ptid = db.Column(db.Integer)
    yearno = db.Column(db.Integer, primary_key=True, nullable=False)
    monthno = db.Column(db.Integer, primary_key=True, nullable=False)
    deptlktp = db.Column(db.String(10), primary_key=True, nullable=False)
    deptlkid = db.Column(db.Integer, primary_key=True, nullable=False)
    pluid = db.Column(db.Integer, primary_key=True, nullable=False)
    lotno = db.Column(db.String(20), nullable=False, server_default=db.FetchedValue())
    bgncsprc = db.Column(db.Numeric(20, 6))
    csprc = db.Column(db.Numeric(20, 6))
    estprc = db.Column(db.Numeric(20, 6))
    crcd = db.Column(db.String(3), server_default=db.FetchedValue())
    upddt = db.Column(db.DateTime)


t_fin_plucosthis_sun2018 = db.Table(
    'fin_plucosthis_sun2018',
    db.Column('ptid', db.Integer),
    db.Column('yearno', db.Integer, nullable=False),
    db.Column('monthno', db.Integer, nullable=False),
    db.Column('deptlktp', db.String(10), nullable=False),
    db.Column('deptlkid', db.Integer, nullable=False),
    db.Column('pluid', db.Integer, nullable=False),
    db.Column('lotno', db.String(20)),
    db.Column('bgncsprc', db.Numeric(20, 6)),
    db.Column('csprc', db.Numeric(20, 6)),
    db.Column('estprc', db.Numeric(20, 6)),
    db.Column('crcd', db.String(3)),
    db.Column('upddt', db.DateTime)
)


t_fin_purplu = db.Table(
    'fin_purplu',
    db.Column('ptid', db.Integer, index=True),
    db.Column('id', db.Numeric(12, 0, asdecimal=False), nullable=False),
    db.Column('purid', db.Numeric(12, 0, asdecimal=False), nullable=False, index=True),
    db.Column('billtp', db.String(10)),
    db.Column('deptid', db.Integer),
    db.Column('venid', db.Integer),
    db.Column('billrsn', db.String(20)),
    db.Column('pluid', db.Integer),
    db.Column('ordqty', db.Numeric(16, 6)),
    db.Column('orduomcd', db.String(6)),
    db.Column('cfmqty', db.Numeric(16, 6)),
    db.Column('stkqty', db.Numeric(16, 6)),
    db.Column('stksign', db.Integer, server_default=db.FetchedValue()),
    db.Column('uomcd', db.String(6)),
    db.Column('csprc', db.Numeric(18, 6)),
    db.Column('txrt', db.Numeric(8, 4)),
    db.Column('stkdt', db.DateTime),
    db.Column('stkby', db.String(20)),
    db.Column('actdt', db.DateTime),
    db.Column('actby', db.String(20)),
    db.Column('updby', db.String(20)),
    db.Column('upddt', db.DateTime),
    db.Column('finadjflg', db.String(1), server_default=db.FetchedValue()),
    db.Column('sta', db.String(3), nullable=False),
    db.Column('mstkdt', db.DateTime),
    db.Column('mupdby', db.String(20)),
    db.Column('mupddt', db.DateTime),
    db.Column('msta', db.String(3), nullable=False),
    db.Column('fcflg', db.String(1))
)


t_fin_purplu_gc = db.Table(
    'fin_purplu_gc',
    db.Column('ptid', db.Integer, index=True),
    db.Column('id', db.Numeric(12, 0, asdecimal=False), nullable=False),
    db.Column('purid', db.Numeric(12, 0, asdecimal=False), nullable=False, index=True),
    db.Column('billtp', db.String(10)),
    db.Column('deptid', db.Integer),
    db.Column('venid', db.Integer),
    db.Column('billrsn', db.String(20)),
    db.Column('pluid', db.Integer),
    db.Column('ordqty', db.Numeric(16, 6)),
    db.Column('orduomcd', db.String(6)),
    db.Column('cfmqty', db.Numeric(16, 6)),
    db.Column('stkqty', db.Numeric(16, 6)),
    db.Column('stksign', db.Integer, server_default=db.FetchedValue()),
    db.Column('uomcd', db.String(6)),
    db.Column('csprc', db.Numeric(18, 6)),
    db.Column('txrt', db.Numeric(8, 4)),
    db.Column('stkdt', db.DateTime),
    db.Column('stkby', db.String(20)),
    db.Column('actdt', db.DateTime),
    db.Column('actby', db.String(20)),
    db.Column('updby', db.String(20)),
    db.Column('upddt', db.DateTime),
    db.Column('finadjflg', db.String(1), server_default=db.FetchedValue()),
    db.Column('sta', db.String(3), nullable=False),
    db.Column('mstkdt', db.DateTime),
    db.Column('mupdby', db.String(20)),
    db.Column('mupddt', db.DateTime),
    db.Column('msta', db.String(3), nullable=False),
    db.Column('fcflg', db.String(1))
)


t_fin_purpt = db.Table(
    'fin_purpt',
    db.Column('ptid', db.Integer, index=True),
    db.Column('yearno', db.Integer, nullable=False),
    db.Column('monthno', db.Integer, nullable=False),
    db.Column('deptlktp', db.String(10), nullable=False),
    db.Column('deptlkid', db.Integer, nullable=False),
    db.Column('venid', db.Integer),
    db.Column('pluid', db.Integer),
    db.Column('amt', db.Numeric(20, 6)),
    db.Column('taxamt', db.Numeric(20, 6)),
    db.Column('crcd', db.String(3), server_default=db.FetchedValue()),
    db.Column('upddt', db.DateTime),
    db.Index('idx_purpt1', 'yearno', 'monthno')
)


t_fin_purptadj = db.Table(
    'fin_purptadj',
    db.Column('ptid', db.Integer),
    db.Column('yearno', db.Integer, nullable=False),
    db.Column('monthno', db.Integer, nullable=False),
    db.Column('deptlktp', db.String(10), nullable=False),
    db.Column('deptlkid', db.Integer, nullable=False),
    db.Column('lktp', db.String(1)),
    db.Column('venid', db.Integer),
    db.Column('pluid', db.Integer),
    db.Column('amt', db.Numeric(20, 6)),
    db.Column('taxamt', db.Numeric(20, 6)),
    db.Column('crcd', db.String(3), server_default=db.FetchedValue()),
    db.Column('upddt', db.DateTime)
)


class FinTask(db.Model):
    __tablename__ = 'fin_task'

    id = db.Column(db.Numeric(12, 0, asdecimal=False), primary_key=True)
    coid = db.Column(db.Integer)
    ptid = db.Column(db.Integer, index=True)
    caltp = db.Column(db.String(10))
    vouid = db.Column(db.Integer)
    plexecdt = db.Column(db.DateTime, nullable=False)
    rlexecdt = db.Column(db.DateTime)
    rtnflag = db.Column(db.String(1))
    rmk = db.Column(db.String(255))
    updby = db.Column(db.String(20))
    upddt = db.Column(db.DateTime)
    sta = db.Column(db.String(3), nullable=False)
    execflg = db.Column(db.String(1))
    nxtsta = db.Column(db.String(3))
    expflg = db.Column(db.String(1), server_default=db.FetchedValue())
    expdt = db.Column(db.DateTime)


t_fin_tasklog = db.Table(
    'fin_tasklog',
    db.Column('id', db.Numeric(12, 0, asdecimal=False), nullable=False),
    db.Column('taskid', db.Numeric(12, 0, asdecimal=False)),
    db.Column('logcd', db.String(20)),
    db.Column('rmk', db.String(255)),
    db.Column('lktp', db.String(10)),
    db.Column('lkid', db.Numeric(asdecimal=False)),
    db.Column('lkcd', db.String(20)),
    db.Column('updby', db.String(20)),
    db.Column('upddt', db.DateTime),
    db.Column('sta', db.String(3), nullable=False),
    db.Column('execflg', db.String(1)),
    db.Column('nxtsta', db.String(3))
)


t_fzn_temp1 = db.Table(
    'fzn_temp1',
    db.Column('plu', db.String(10), nullable=False),
    db.Column('grp1', db.String(10)),
    db.Column('grp2', db.String(10))
)


t_gc_discount_mapping_master = db.Table(
    'gc_discount_mapping_master',
    db.Column('discount_type_id', db.Numeric(asdecimal=False), nullable=False),
    db.Column('drs_id', db.String(512))
)


t_gcbi_dim_discounttype = db.Table(
    'gcbi_dim_discounttype',
    db.Column('DiscountTypeID', db.String(20)),
    db.Column('PollPOSID', db.String(100)),
    db.Column('Code', db.String(50), nullable=False),
    db.Column('Description', db.String(50), nullable=False),
    db.Column('id', db.Integer),
    db.Column('cd', db.String(20)),
    db.Column('poscd', db.String(20)),
    db.Column('priotp', db.String(10)),
    db.Column('tp', db.String(10)),
    db.Column('nm_l_zh', db.String(50), nullable=False),
    db.Column('nm_l_en', db.String(50)),
    db.Column('nm_l_ja', db.String(50)),
    db.Column('rmk', db.String(250)),
    db.Column('updby', db.String(20)),
    db.Column('upddt', db.DateTime),
    db.Column('sta', db.String(3), nullable=False),
    db.Column('bdate', db.DateTime),
    db.Column('edate', db.DateTime)
)


t_gcbi_dim_discounttype_mk2 = db.Table(
    'gcbi_dim_discounttype_mk2',
    db.Column('DiscountTypeID', db.String(20)),
    db.Column('PollPOSID', db.String(100)),
    db.Column('Code', db.String(50), nullable=False),
    db.Column('Description', db.String(50), nullable=False),
    db.Column('id', db.Integer),
    db.Column('cd', db.String(20)),
    db.Column('poscd', db.String(20)),
    db.Column('priotp', db.String(10)),
    db.Column('tp', db.String(10)),
    db.Column('nm_l_zh', db.String(50), nullable=False),
    db.Column('nm_l_en', db.String(50)),
    db.Column('nm_l_ja', db.String(50)),
    db.Column('rmk', db.String(250)),
    db.Column('updby', db.String(20)),
    db.Column('upddt', db.DateTime),
    db.Column('sta', db.String(3), nullable=False),
    db.Column('bdate', db.DateTime),
    db.Column('edate', db.DateTime)
)


t_gcbi_dim_itemmapping = db.Table(
    'gcbi_dim_itemmapping',
    db.Column('menuid', db.String(100)),
    db.Column('hexcd', db.String(20))
)


t_gcbi_dim_saleitem = db.Table(
    'gcbi_dim_saleitem',
    db.Column('SaleItemID', db.String(20)),
    db.Column('SalesItemCode', db.String(20)),
    db.Column('SalesItemDesc', db.Unicode(2000)),
    db.Column('SaleItemType', db.String(8)),
    db.Column('FamilyGroup', db.String(4000)),
    db.Column('SaleUnit', db.String(6), nullable=False),
    db.Column('Department', db.Unicode(50), nullable=False),
    db.Column('Category', db.String(4000)),
    db.Column('Product_Group', db.Unicode(50), nullable=False),
    db.Column('Generic_Product_Name', db.Unicode(100)),
    db.Column('Size', db.String(100)),
    db.Column('Classification', db.String(100)),
    db.Column('Positioning', db.String(100)),
    db.Column('Coffee', db.String(100)),
    db.Column('Daypart', db.String(100)),
    db.Column('Flavor', db.String(100)),
    db.Column('ProductType', db.String(100)),
    db.Column('MajorGroup', db.String(100)),
    db.Column('ReportCategory', db.String(4000))
)


t_gcbi_dim_saleitem_mk2 = db.Table(
    'gcbi_dim_saleitem_mk2',
    db.Column('SaleItemID', db.String(20)),
    db.Column('SalesItemCode', db.String(20)),
    db.Column('SalesItemDesc', db.Unicode(2000)),
    db.Column('SaleItemType', db.String(8)),
    db.Column('FamilyGroup', db.String(4000)),
    db.Column('SaleUnit', db.String(6), nullable=False),
    db.Column('Department', db.Unicode(50), nullable=False),
    db.Column('Category', db.String(4000)),
    db.Column('Product_Group', db.Unicode(50), nullable=False),
    db.Column('Generic_Product_Name', db.Unicode(100)),
    db.Column('Size', db.String(100)),
    db.Column('Classification', db.String(100)),
    db.Column('Positioning', db.String(100)),
    db.Column('Coffee', db.String(100)),
    db.Column('Daypart', db.String(100)),
    db.Column('Flavor', db.String(100)),
    db.Column('ProductType', db.String(100)),
    db.Column('MajorGroup', db.String(100)),
    db.Column('ReportCategory', db.String(4000))
)


t_gcbi_dim_storeinfo = db.Table(
    'gcbi_dim_storeinfo',
    db.Column('Region', db.String(4)),
    db.Column('Market', db.String(8)),
    db.Column('Market_Store', db.Numeric(asdecimal=False)),
    db.Column('Starbucks_Store', db.String(20)),
    db.Column('Entity_Name', db.Unicode(50), nullable=False),
    db.Column('Store_Name', db.Unicode(50)),
    db.Column('Opening_Date', db.DateTime),
    db.Column('Store_Status', db.String(6)),
    db.Column('Area_L2', db.String(100)),
    db.Column('AreaL2En', db.String(100)),
    db.Column('Area_L1', db.String(50)),
    db.Column('AreaL1En', db.String(100)),
    db.Column('District', db.String(50)),
    db.Column('DistriceEn', db.String(100)),
    db.Column('Ageclass', db.String(8)),
    db.Column('City', db.String(100)),
    db.Column('Province', db.String(100)),
    db.Column('Trade_Zone', db.String(100)),
    db.Column('Trade_Area', db.String(100)),
    db.Column('City_Tier', db.String(100)),
    db.Column('Alliance', db.String(100)),
    db.Column('StoreID', db.Numeric(asdecimal=False)),
    db.Column('LegalCity', db.String(100)),
    db.Column('dm', db.String(100)),
    db.Column('dm_nm', db.String(100)),
    db.Column('om_ado', db.String(100)),
    db.Column('om_ado_nm', db.String(100)),
    db.Column('rdo', db.String(100)),
    db.Column('rdo_nm', db.String(100)),
    db.Column('bgm', db.String(7)),
    db.Column('DistrictCode', db.String(50)),
    db.Column('Area_L2Code', db.String(100))
)


t_gcbi_dim_storeinfo_mk2 = db.Table(
    'gcbi_dim_storeinfo_mk2',
    db.Column('Region', db.String(4)),
    db.Column('Market', db.String(8)),
    db.Column('Market_Store', db.Numeric(asdecimal=False)),
    db.Column('Starbucks_Store', db.String(20)),
    db.Column('Entity_Name', db.Unicode(50), nullable=False),
    db.Column('Store_Name', db.Unicode(50)),
    db.Column('Opening_Date', db.DateTime),
    db.Column('Store_Status', db.String(6)),
    db.Column('Area_L2', db.String(100)),
    db.Column('AreaL2En', db.String(100)),
    db.Column('Area_L1', db.String(50)),
    db.Column('AreaL1En', db.String(100)),
    db.Column('District', db.String(50)),
    db.Column('DistriceEn', db.String(100)),
    db.Column('Ageclass', db.String(8)),
    db.Column('City', db.String(100)),
    db.Column('Province', db.String(100)),
    db.Column('Trade_Zone', db.String(100)),
    db.Column('Trade_Area', db.String(100)),
    db.Column('City_Tier', db.String(100)),
    db.Column('Alliance', db.String(100)),
    db.Column('StoreID', db.Numeric(asdecimal=False)),
    db.Column('LegalCity', db.String(100)),
    db.Column('dm', db.String(100)),
    db.Column('dm_nm', db.String(100)),
    db.Column('om_ado', db.String(100)),
    db.Column('om_ado_nm', db.String(100)),
    db.Column('rdo', db.String(100)),
    db.Column('rdo_nm', db.String(100)),
    db.Column('bgm', db.String(7)),
    db.Column('DistrictCode', db.String(50)),
    db.Column('Area_L2Code', db.String(100))
)


t_gcbi_dim_tender = db.Table(
    'gcbi_dim_tender',
    db.Column('TenderTypeID', db.String(20)),
    db.Column('PollPOSID', db.String(100)),
    db.Column('Code', db.String(50), nullable=False),
    db.Column('Description', db.String(50), nullable=False)
)


t_gcbi_dim_tender_mk2 = db.Table(
    'gcbi_dim_tender_mk2',
    db.Column('TenderTypeID', db.String(20)),
    db.Column('PollPOSID', db.String(100)),
    db.Column('Code', db.String(50), nullable=False),
    db.Column('Description', db.String(50), nullable=False)
)


t_gcbi_fact_discount = db.Table(
    'gcbi_fact_discount',
    db.Column('deptcd', db.Numeric(asdecimal=False)),
    db.Column('DateID', db.DateTime),
    db.Column('TimeID', db.Numeric(asdecimal=False)),
    db.Column('StoreID', db.Numeric(asdecimal=False)),
    db.Column('RevenueCentreID', db.Numeric(asdecimal=False)),
    db.Column('DiscountTypeID', db.String(10)),
    db.Column('SaleItemID', db.String(20)),
    db.Column('DiscountAmount', db.Numeric(scale=2)),
    db.Column('DiscountQuantity', db.Numeric(scale=2))
)


t_gcbi_fact_payment = db.Table(
    'gcbi_fact_payment',
    db.Column('deptcd', db.Numeric(asdecimal=False)),
    db.Column('DateID', db.DateTime),
    db.Column('TimeID', db.Numeric(asdecimal=False)),
    db.Column('StoreID', db.Numeric(asdecimal=False)),
    db.Column('tdrcd', db.String(10)),
    db.Column('tdramt', db.Numeric(scale=2))
)


t_gcbi_fact_saleitem = db.Table(
    'gcbi_fact_saleitem',
    db.Column('DateID', db.DateTime),
    db.Column('TimeID', db.Numeric(asdecimal=False)),
    db.Column('StoreID', db.Numeric(asdecimal=False)),
    db.Column('ServiceTypeID', db.Numeric(asdecimal=False)),
    db.Column('RevenueCentreID', db.Numeric(asdecimal=False)),
    db.Column('CashierID', db.String(10)),
    db.Column('SaleItemID', db.String(20)),
    db.Column('BusinessDay', db.DateTime),
    db.Column('Item_GrossSales', db.Numeric(asdecimal=False)),
    db.Column('Item_NetSales', db.Numeric(asdecimal=False)),
    db.Column('Item_Tax', db.Numeric(asdecimal=False)),
    db.Column('Item_Quantity', db.Numeric(asdecimal=False)),
    db.Column('SalesCost', db.Numeric(asdecimal=False))
)


t_gcbi_fact_sales = db.Table(
    'gcbi_fact_sales',
    db.Column('DateID', db.DateTime),
    db.Column('TimeID', db.Numeric(asdecimal=False)),
    db.Column('StoreID', db.Numeric(asdecimal=False)),
    db.Column('ServiceTypeID', db.Numeric(asdecimal=False)),
    db.Column('RevenueCentreID', db.Numeric(asdecimal=False)),
    db.Column('posid', db.String(20)),
    db.Column('CashierID', db.String(10)),
    db.Column('GlobalNumber', db.String(20)),
    db.Column('TransactionCount', db.Numeric(asdecimal=False)),
    db.Column('StoreSales', db.Numeric(asdecimal=False)),
    db.Column('NetStoreSales', db.Numeric(asdecimal=False)),
    db.Column('NonSales', db.String(100)),
    db.Column('Tax', db.Numeric(asdecimal=False)),
    db.Column('SalesQty', db.Numeric(asdecimal=False)),
    db.Column('DiscountAmount', db.Numeric(asdecimal=False)),
    db.Column('DiscountQuantity', db.Numeric(asdecimal=False))
)


t_gcbi_fact_sales_hourly = db.Table(
    'gcbi_fact_sales_hourly',
    db.Column('DateID', db.DateTime),
    db.Column('TimeID', db.Numeric(asdecimal=False)),
    db.Column('StoreID', db.Numeric(asdecimal=False)),
    db.Column('ServiceTypeID', db.Numeric(asdecimal=False)),
    db.Column('RevenueCentreID', db.Numeric(asdecimal=False)),
    db.Column('posid', db.String(20)),
    db.Column('CashierID', db.String(10)),
    db.Column('GlobalNumber', db.String(20)),
    db.Column('TransactionCount', db.Numeric(asdecimal=False)),
    db.Column('StoreSales', db.Numeric(scale=2)),
    db.Column('NetStoreSales', db.Numeric(scale=2)),
    db.Column('NonSales', db.String(100)),
    db.Column('Tax', db.Numeric(scale=2)),
    db.Column('SalesQty', db.Numeric(asdecimal=False)),
    db.Column('DiscountAmount', db.Numeric(asdecimal=False)),
    db.Column('DiscountQuantity', db.Numeric(asdecimal=False))
)


t_gcbi_pt = db.Table(
    'gcbi_pt',
    db.Column('id', db.Integer, nullable=False),
    db.Column('coid', db.Integer),
    db.Column('yearno', db.Integer),
    db.Column('monthno', db.Integer),
    db.Column('ptdsc', db.String(50)),
    db.Column('finstdt', db.DateTime),
    db.Column('fineddt', db.DateTime),
    db.Column('stkstdt', db.DateTime),
    db.Column('stkeddt', db.DateTime),
    db.Column('exattr1', db.String(100)),
    db.Column('exattr2', db.String(100)),
    db.Column('exattr3', db.String(100)),
    db.Column('exattr4', db.String(100)),
    db.Column('exattr5', db.String(100)),
    db.Column('exattr6', db.String(100)),
    db.Column('rmk', db.String(100)),
    db.Column('updby', db.String(20)),
    db.Column('upddt', db.DateTime),
    db.Column('sta', db.String(3)),
    db.Column('nxtsta', db.String(3)),
    db.Column('execflg', db.String(1)),
    db.Column('costdt', db.DateTime)
)


t_hhs_basplu = db.Table(
    'hhs_basplu',
    db.Column('id', db.Integer),
    db.Column('plucd', db.String(50)),
    db.Column('pludsc', db.String(150)),
    db.Column('catcd', db.String(50)),
    db.Column('catdsc', db.String(150))
)


t_hhs_pictrans = db.Table(
    'hhs_pictrans',
    db.Column('gid', db.String(50)),
    db.Column('lineid', db.Integer),
    db.Column('lineidn', db.Integer)
)


t_hhs_pictrans2 = db.Table(
    'hhs_pictrans2',
    db.Column('transno', db.Numeric(20, 0, asdecimal=False)),
    db.Column('ctrno', db.Numeric(20, 0, asdecimal=False)),
    db.Column('nctrno', db.Numeric(20, 0, asdecimal=False)),
    db.Column('upddt', db.DateTime)
)


t_hhs_plu = db.Table(
    'hhs_plu',
    db.Column('plucd', db.String(20)),
    db.Column('amt', db.Numeric(18, 6)),
    db.Column('tp', db.String(20))
)


t_hhs_store_inv = db.Table(
    'hhs_store_inv',
    db.Column('item_code', db.String(20)),
    db.Column('item_name', db.String(50), nullable=False),
    db.Column('qty', db.Numeric(asdecimal=False), nullable=False)
)


t_hhs_t1 = db.Table(
    'hhs_t1',
    db.Column('transno', db.Numeric(20, 0, asdecimal=False)),
    db.Column('ctrno', db.Numeric(20, 0, asdecimal=False)),
    db.Column('upddt', db.DateTime, server_default=db.FetchedValue()),
    db.Column('bizdt', db.DateTime),
    db.Column('hh', db.Integer),
    db.Column('rmk', db.String(10))
)


t_hhs_t10 = db.Table(
    'hhs_t10',
    db.Column('id', db.Numeric(15, 0, asdecimal=False)),
    db.Column('code', db.Numeric(15, 0, asdecimal=False)),
    db.Column('status', db.String(10)),
    db.Column('flg', db.Integer, index=True, server_default=db.FetchedValue())
)


t_hhs_t12 = db.Table(
    'hhs_t12',
    db.Column('a', db.Integer),
    db.Column('b', db.Integer)
)


t_hhs_t13 = db.Table(
    'hhs_t13',
    db.Column('pluid', db.Integer),
    db.Column('billkid', db.Integer),
    db.Column('deptid', db.Integer),
    db.Column('billdtlid', db.Integer),
    db.Column('tp', db.String(100)),
    db.Column('qty', db.Numeric(16, 6))
)


t_hhs_t14 = db.Table(
    'hhs_t14',
    db.Column('deptid', db.Integer),
    db.Column('bizdt', db.DateTime),
    db.Column('sta', db.String(1), index=True, server_default=db.FetchedValue()),
    db.Column('upddt', db.DateTime)
)


t_hhs_t15 = db.Table(
    'hhs_t15',
    db.Column('deptid', db.Integer),
    db.Column('bizdt', db.DateTime),
    db.Column('pluid', db.Integer),
    db.Column('rcv', db.Numeric(14, 5)),
    db.Column('adj', db.Numeric(14, 5)),
    db.Column('sal', db.Numeric(14, 5)),
    db.Column('inv', db.Numeric(14, 5)),
    db.Index('idx_hhst15', 'deptid', 'bizdt')
)


t_hhs_t2 = db.Table(
    'hhs_t2',
    db.Column('pluid', db.Integer),
    db.Column('deptid', db.Integer),
    db.Column('stkqty', db.Numeric(16, 4))
)


t_hhs_t3 = db.Table(
    'hhs_t3',
    db.Column('pid', db.String(50)),
    db.Column('net_no', db.String(20)),
    db.Column('plu_no', db.String(20)),
    db.Column('upddate', db.DateTime),
    db.Column('reqid', db.Numeric(13, 0, asdecimal=False)),
    db.Column('dtlid', db.Numeric(13, 0, asdecimal=False)),
    db.Column('fg', db.String(1)),
    db.Column('rmk', db.String(2000))
)


t_hhs_t4 = db.Table(
    'hhs_t4',
    db.Column('dtlid', db.String(30)),
    db.Column('rcvno', db.String(30)),
    db.Column('qty', db.Numeric(20, 6)),
    db.Column('price', db.Numeric(20, 6)),
    db.Column('tx', db.Numeric(20, 6)),
    db.Column('pluno', db.String(30)),
    db.Column('pludsc', db.String(130)),
    db.Column('txn', db.Numeric(20, 6)),
    db.Column('price_n', db.Numeric(20, 6)),
    db.Column('price_n_t', db.Numeric(20, 6)),
    db.Column('venid', db.Integer),
    db.Column('msttx', db.Numeric(20, 6)),
    db.Column('mstprice', db.Numeric(20, 6)),
    db.Column('mstprice1', db.Numeric(20, 6))
)


t_hhs_t5 = db.Table(
    'hhs_t5',
    db.Column('pluno', db.String(20)),
    db.Column('price', db.Numeric(18, 6))
)


t_hhs_t6 = db.Table(
    'hhs_t6',
    db.Column('plucd', db.String(20)),
    db.Column('bizdt', db.DateTime),
    db.Column('deptcd', db.String(20)),
    db.Column('pid', db.String(50)),
    db.Column('typ', db.String(1)),
    db.Column('qty', db.Numeric(20, 4)),
    db.Column('dcid', db.String(50))
)


t_hhs_t7 = db.Table(
    'hhs_t7',
    db.Column('id', db.Numeric(20, 0, asdecimal=False)),
    db.Column('pric', db.Numeric(20, 6)),
    db.Column('tx', db.Numeric(20, 6))
)


t_hhs_t8 = db.Table(
    'hhs_t8',
    db.Column('deptcd', db.String(20)),
    db.Column('bizdt', db.DateTime),
    db.Column('plucd', db.String(20)),
    db.Column('qty', db.Numeric(12, 2)),
    db.Column('rmk', db.String(200)),
    db.Column('transno', db.Numeric(20, 0, asdecimal=False))
)


t_hhs_t9 = db.Table(
    'hhs_t9',
    db.Column('deptid', db.Numeric(asdecimal=False)),
    db.Column('bizdt', db.DateTime),
    db.Column('catid', db.Integer),
    db.Column('net_val', db.Numeric(20, 2))
)


t_hhs_trd = db.Table(
    'hhs_trd',
    db.Column('transno', db.Numeric(14, 0, asdecimal=False)),
    db.Column('plucd', db.String(10)),
    db.Column('netamt', db.Numeric(18, 2)),
    db.Column('qty', db.Numeric(18, 2)),
    db.Column('discamt', db.Numeric(18, 2))
)


t_hhs_trdis = db.Table(
    'hhs_trdis',
    db.Column('transno', db.Numeric(14, 0, asdecimal=False)),
    db.Column('disccd', db.String(10)),
    db.Column('discamt', db.Numeric(18, 2))
)


t_hhs_trm = db.Table(
    'hhs_trm',
    db.Column('transno', db.Numeric(15, 0, asdecimal=False)),
    db.Column('bizdt', db.DateTime),
    db.Column('deptcd', db.String(10)),
    db.Column('saldate', db.DateTime),
    db.Column('netamt', db.Numeric(18, 2)),
    db.Column('tp', db.String(10)),
    db.Column('membercd', db.String(25))
)


t_hhs_trtdr = db.Table(
    'hhs_trtdr',
    db.Column('transno', db.Numeric(14, 0, asdecimal=False)),
    db.Column('tdrcd', db.String(10)),
    db.Column('amt', db.Numeric(18, 2))
)


t_hhsv_acc_interface_body = db.Table(
    'hhsv_acc_interface_body',
    db.Column('?????', db.String(20)),
    db.Column('????', db.String(6)),
    db.Column('??', db.Numeric(asdecimal=False)),
    db.Column('??????', db.String(0)),
    db.Column('??1', db.Numeric(asdecimal=False)),
    db.Column('??2', db.String(4000)),
    db.Column('???????', db.Numeric(asdecimal=False)),
    db.Column('pid', db.String(612))
)


t_if_col_name = db.Table(
    'if_col_name',
    db.Column('own_name', db.String(50)),
    db.Column('table_name', db.String(50)),
    db.Column('col_name', db.String(50)),
    db.Column('output_name', db.String(50)),
    db.Column('type', db.String(50)),
    db.Column('s_no', db.Integer),
    db.Column('is_delete', db.String(1), server_default=db.FetchedValue()),
    db.Column('is_show', db.String(1), server_default=db.FetchedValue())
)


t_if_col_name_h = db.Table(
    'if_col_name_h',
    db.Column('own_name', db.String(50)),
    db.Column('table_name', db.String(50)),
    db.Column('col_name', db.String(50)),
    db.Column('output_name', db.String(50)),
    db.Column('type', db.String(50)),
    db.Column('s_no', db.Integer)
)


class IfCouponHex(db.Model):
    __tablename__ = 'if_coupon_hex'

    bizdt = db.Column(db.DateTime, index=True)
    trans_no = db.Column(db.Numeric(20, 0, asdecimal=False))
    ctrcode = db.Column(db.Numeric(20, 0, asdecimal=False), primary_key=True)
    process_dt = db.Column(db.DateTime)
    net_no = db.Column(db.String(6))
    strcomment = db.Column(db.String(100))
    cardnumber = db.Column(db.String(20))
    transdate = db.Column(db.String(10))
    transtime = db.Column(db.String(8))
    merchantcode = db.Column(db.String(20))
    merchantno = db.Column(db.String(6))
    trantypecode = db.Column(db.String(4))
    tranamount = db.Column(db.Numeric(24, 4))
    cardtypecode = db.Column(db.String(3))
    referenceno = db.Column(db.String(20))
    update_date = db.Column(db.DateTime)
    szbalance = db.Column(db.Numeric(24, 4))
    szreserved = db.Column(db.Numeric(24, 4))
    strauthorisation = db.Column(db.String(30))


t_if_ebuy_activitycode = db.Table(
    'if_ebuy_activitycode',
    db.Column('pid', db.String(50), nullable=False, server_default=db.FetchedValue()),
    db.Column('activity_no', db.String(50)),
    db.Column('activity_name', db.String(50)),
    db.Column('start_time', db.DateTime),
    db.Column('end_time', db.DateTime),
    db.Column('update_date', db.DateTime, server_default=db.FetchedValue())
)


t_if_ebuy_empdata = db.Table(
    'if_ebuy_empdata',
    db.Column('usercode', db.String(50)),
    db.Column('username', db.String(50)),
    db.Column('deptname', db.String(100)),
    db.Column('joindate', db.String(10)),
    db.Column('resigndate', db.String(10)),
    db.Column('cidcode', db.String(30)),
    db.Column('uppdt', db.DateTime),
    db.Column('deptid', db.String(10)),
    db.Column('gongzhong', db.String(10)),
    db.Column('regname', db.String(30))
)


class IfEbuyHHex(db.Model):
    __tablename__ = 'if_ebuy_h_hex'

    pid = db.Column(db.String(50), primary_key=True, server_default=db.FetchedValue())
    possaleid = db.Column(db.String(24), index=True)
    activity_code = db.Column(db.String(10), index=True)
    trans_date = db.Column(db.String(8))
    trans_time = db.Column(db.String(6))
    rmk = db.Column(db.String(12))
    plu_no = db.Column(db.String(6))
    trans_qty = db.Column(db.Numeric(19, 4))
    trans_amt = db.Column(db.String(18))
    pay_amt = db.Column(db.String(18))
    business_date = db.Column(db.DateTime, index=True)
    net_no = db.Column(db.String(6))
    trans_no = db.Column(db.String(50))
    update_date = db.Column(db.DateTime)
    rmk_desc = db.Column(db.String(21))
    strcomment = db.Column(db.String(200))
    user_no = db.Column(db.String(50))


class IfEbuyHex(db.Model):
    __tablename__ = 'if_ebuy_hex'

    pid = db.Column(db.String(50), primary_key=True, server_default=db.FetchedValue())
    possaleid = db.Column(db.String(24), index=True)
    activity_code = db.Column(db.String(10))
    trans_date = db.Column(db.String(8))
    trans_time = db.Column(db.String(6))
    rmk = db.Column(db.String(12))
    plu_no = db.Column(db.String(6))
    trans_qty = db.Column(db.Numeric(19, 4))
    trans_amt = db.Column(db.String(18))
    pay_amt = db.Column(db.String(18))
    business_date = db.Column(db.DateTime, index=True)
    net_no = db.Column(db.String(6))
    trans_no = db.Column(db.String(50))
    update_date = db.Column(db.DateTime)
    rmk_desc = db.Column(db.String(21))
    strcomment = db.Column(db.String(200))


class IfEbuyImp(db.Model):
    __tablename__ = 'if_ebuy_imp'

    pid = db.Column(db.String(50), primary_key=True, server_default=db.FetchedValue())
    bo_code = db.Column(db.String(15))
    saleid = db.Column(db.String(6))
    pos_code = db.Column(db.String(8))
    possaleid = db.Column(db.String(24), index=True)
    activity_code = db.Column(db.String(10))
    trans_date = db.Column(db.String(8), index=True)
    trans_time = db.Column(db.String(6))
    rmk = db.Column(db.String(12))
    plu_no = db.Column(db.String(6))
    trans_qty = db.Column(db.String(4))
    trans_amt = db.Column(db.String(18))
    pay_amt = db.Column(db.String(18))
    update_date = db.Column(db.DateTime, server_default=db.FetchedValue())
    rmk_desc = db.Column(db.String(21))


t_if_ebuy_imp_tem = db.Table(
    'if_ebuy_imp_tem',
    db.Column('pid', db.String(50), nullable=False, server_default=db.FetchedValue()),
    db.Column('bo_code', db.String(15)),
    db.Column('saleid', db.String(6)),
    db.Column('pos_code', db.String(8)),
    db.Column('possaleid', db.String(24)),
    db.Column('activity_code', db.String(10)),
    db.Column('trans_date', db.String(8)),
    db.Column('trans_time', db.String(6)),
    db.Column('rmk', db.String(12)),
    db.Column('plu_no', db.String(6)),
    db.Column('trans_qty', db.String(4)),
    db.Column('trans_amt', db.String(18)),
    db.Column('pay_amt', db.String(18)),
    db.Column('update_date', db.DateTime, server_default=db.FetchedValue()),
    db.Column('rmk_desc', db.String(21))
)


t_if_ebuy_itemdata = db.Table(
    'if_ebuy_itemdata',
    db.Column('pid', db.String(50), nullable=False, server_default=db.FetchedValue()),
    db.Column('plu_no', db.String(50)),
    db.Column('bf_chsname', db.String(100)),
    db.Column('cat_name', db.String(100)),
    db.Column('sl_prc', db.String(50)),
    db.Column('group_name', db.String(50))
)


t_if_exp_carddata = db.Table(
    'if_exp_carddata',
    db.Column('pid', db.String(50), nullable=False),
    db.Column('net_no', db.String(10)),
    db.Column('biz_date', db.String(8), index=True),
    db.Column('strcomment', db.String(100)),
    db.Column('curtenderamt', db.Numeric(19, 4)),
    db.Column('pos_no', db.String(10)),
    db.Column('inttransnum', db.Numeric(20, 0, asdecimal=False)),
    db.Column('strcreditcardnum', db.String(20)),
    db.Column('tag', db.String(4)),
    db.Column('strauthorisation', db.String(30)),
    db.Column('update_date', db.DateTime, nullable=False)
)


t_if_exp_carddata_1 = db.Table(
    'if_exp_carddata_1',
    db.Column('net_no', db.String(10)),
    db.Column('biz_date', db.String(8)),
    db.Column('curtenderamt', db.Numeric(19, 4)),
    db.Column('strcreditcardnum', db.String(20))
)


t_if_exp_carddata_19 = db.Table(
    'if_exp_carddata_19',
    db.Column('net_no', db.String(10)),
    db.Column('biz_date', db.String(8)),
    db.Column('strcomment', db.String(100)),
    db.Column('curtenderamt', db.Numeric(19, 4)),
    db.Column('pos_no', db.String(10)),
    db.Column('inttransnum', db.Numeric(20, 0, asdecimal=False)),
    db.Column('strcreditcardnum', db.String(20)),
    db.Column('tag', db.String(4)),
    db.Column('strauthorisation', db.String(30)),
    db.Column('update_date', db.DateTime, nullable=False)
)


t_if_exp_carddata_2 = db.Table(
    'if_exp_carddata_2',
    db.Column('net_no', db.String(10)),
    db.Column('biz_date', db.String(8)),
    db.Column('curtenderamt', db.Numeric(19, 4)),
    db.Column('strcreditcardnum', db.String(20))
)


t_if_exp_carddata_new = db.Table(
    'if_exp_carddata_new',
    db.Column('pid', db.String(50), nullable=False),
    db.Column('net_no', db.String(10)),
    db.Column('biz_date', db.String(8), index=True),
    db.Column('strcomment', db.String(100)),
    db.Column('curtenderamt', db.Numeric(19, 4)),
    db.Column('pos_no', db.String(10)),
    db.Column('inttransnum', db.Numeric(20, 0, asdecimal=False)),
    db.Column('strcreditcardnum', db.String(20)),
    db.Column('tag', db.String(4)),
    db.Column('strauthorisation', db.String(30)),
    db.Column('update_date', db.DateTime, nullable=False),
    db.Column('merchantid', db.String(15)),
    db.Column('terminalid', db.String(8)),
    db.Column('settlenum', db.String(24)),
    db.Column('systraceno', db.String(6)),
    db.Column('cardtype', db.String(2)),
    db.Column('bankno', db.String(12)),
    db.Column('cardno', db.String(19)),
    db.Column('transdate', db.String(8)),
    db.Column('transtime', db.String(6)),
    db.Column('amount', db.String(12)),
    db.Column('sysrefno', db.String(12))
)


t_if_interface_root = db.Table(
    'if_interface_root',
    db.Column('senderid', db.String(5)),
    db.Column('receiverid', db.String(5)),
    db.Column('extractid', db.String(50)),
    db.Column('extracttimestamp', db.String(25)),
    db.Column('extractlinecount', db.Numeric(asdecimal=False)),
    db.Column('header_name', db.String(50)),
    db.Column('detail_name', db.String(50)),
    db.Column('header_key', db.String(50)),
    db.Column('master_name', db.String(50)),
    db.Column('file_name', db.String(50)),
    db.Column('file_header', db.String(50)),
    db.Column('header_h_name', db.String(50)),
    db.Column('detail_h_name', db.String(50)),
    db.Column('detail_key', db.String(50)),
    db.Column('ddtl_h_name', db.String(50)),
    db.Column('ddtl_name', db.String(50)),
    db.Column('own_name', db.String(50)),
    db.Column('sender', db.String(50)),
    db.Column('ddtl_h_name2', db.String(50)),
    db.Column('ddtl_name2', db.String(50))
)


t_if_nextctr_hqjc = db.Table(
    'if_nextctr_hqjc',
    db.Column('strtradecode', db.String(50)),
    db.Column('inttransnum', db.Numeric(asdecimal=False)),
    db.Column('ctrcode', db.Numeric(asdecimal=False)),
    db.Column('flag', db.Integer),
    db.Column('up_date', db.String(50))
)


t_if_nextctr_no = db.Table(
    'if_nextctr_no',
    db.Column('strtradecode', db.String(50)),
    db.Column('maxctrcode', db.Numeric(asdecimal=False)),
    db.Column('num', db.Integer, nullable=False),
    db.Column('bizdt', db.DateTime),
    db.Column('up_date', db.DateTime),
    db.Column('error_cnt', db.Integer)
)


class IfSimphonyDeptMap(db.Model):
    __tablename__ = 'if_simphony_dept_map'

    s_deptcode = db.Column(db.String(20))
    h_deptcode = db.Column(db.String(20), primary_key=True)


class IfSimphonyDiscMap(db.Model):
    __tablename__ = 'if_simphony_disc_map'

    s_disccode = db.Column(db.String(50), primary_key=True)
    h_disccode = db.Column(db.String(50))


t_if_simphony_discounttype = db.Table(
    'if_simphony_discounttype',
    db.Column('discounttypecode', db.String(50)),
    db.Column('sourcecode', db.String(50)),
    db.Column('traceid', db.String(50)),
    db.Column('discounttypeid', db.String(50)),
    db.Column('discountdescription', db.String(50)),
    db.Column('filename', db.String(50))
)


t_if_simphony_dtl_disc = db.Table(
    'if_simphony_dtl_disc',
    db.Column('sequencenumber', db.Numeric(20, 0, asdecimal=False), index=True),
    db.Column('dtlsequencenumber', db.Numeric(10, 0, asdecimal=False)),
    db.Column('discsequencenumber', db.Numeric(10, 0, asdecimal=False)),
    db.Column('amount', db.Numeric(20, 6)),
    db.Column('previousprice', db.Numeric(20, 6)),
    db.Column('reasoncode', db.String(20))
)


t_if_simphony_dtl_payinout = db.Table(
    'if_simphony_dtl_payinout',
    db.Column('sequencenumber', db.Numeric(20, 0, asdecimal=False), index=True),
    db.Column('amount', db.Numeric(14, 4)),
    db.Column('count', db.Integer),
    db.Column('reason', db.String(50))
)


t_if_simphony_dtl_sale = db.Table(
    'if_simphony_dtl_sale',
    db.Column('sequencenumber', db.Numeric(20, 0, asdecimal=False), index=True),
    db.Column('linetype', db.String(20)),
    db.Column('positemid', db.String(20)),
    db.Column('itemid', db.String(20)),
    db.Column('itemname', db.String(100)),
    db.Column('regularsalesunitprice', db.Numeric(20, 6)),
    db.Column('extendedamount', db.Numeric(20, 6)),
    db.Column('quantity', db.Numeric(20, 2)),
    db.Column('dtlsequencenumber', db.Numeric(10, 0, asdecimal=False)),
    db.Column('upddt', db.DateTime, server_default=db.FetchedValue()),
    db.Column('cardnumber', db.String(40))
)


t_if_simphony_dtl_tender = db.Table(
    'if_simphony_dtl_tender',
    db.Column('sequencenumber', db.Numeric(20, 0, asdecimal=False), index=True),
    db.Column('dtlsequencenumber', db.Numeric(10, 0, asdecimal=False)),
    db.Column('cancelflag', db.String(1)),
    db.Column('tenderid', db.String(10)),
    db.Column('reasoncode', db.String(20)),
    db.Column('amount', db.Numeric(20, 6)),
    db.Column('tendertype', db.String(20))
)


t_if_simphony_in_log = db.Table(
    'if_simphony_in_log',
    db.Column('filename', db.String(200), index=True),
    db.Column('type', db.String(20)),
    db.Column('sta', db.Integer, index=True),
    db.Column('created', db.DateTime, server_default=db.FetchedValue()),
    db.Column('updated', db.DateTime, server_default=db.FetchedValue()),
    db.Column('path', db.String(255))
)


t_if_simphony_newmenuitemcode = db.Table(
    'if_simphony_newmenuitemcode',
    db.Column('itemcode', db.String(50)),
    db.Column('description', db.String(50)),
    db.Column('groupname', db.String(50)),
    db.Column('departmentname', db.String(150)),
    db.Column('categoryname', db.String(150)),
    db.Column('sellinguom', db.String(50)),
    db.Column('sellingamount', db.String(150)),
    db.Column('filename', db.String(50))
)


t_if_simphony_pc_errorlog = db.Table(
    'if_simphony_pc_errorlog',
    db.Column('transno', db.Numeric(20, 0, asdecimal=False), nullable=False),
    db.Column('bizdt', db.DateTime),
    db.Column('ctrno', db.Numeric(20, 0, asdecimal=False))
)


class IfSimphonyPluMap(db.Model):
    __tablename__ = 'if_simphony_plu_map'

    s_plucode = db.Column(db.String(50))
    h_plucode = db.Column(db.String(50), primary_key=True)


t_if_simphony_tender_map = db.Table(
    'if_simphony_tender_map',
    db.Column('s_tendercode', db.String(30)),
    db.Column('h_tendercode', db.String(30))
)


t_if_simphony_tendertype = db.Table(
    'if_simphony_tendertype',
    db.Column('tendertype', db.String(50)),
    db.Column('sourcecode', db.String(50)),
    db.Column('traceid', db.String(50)),
    db.Column('tendertypeid', db.String(50)),
    db.Column('tenderdescription', db.String(150)),
    db.Column('filename', db.String(50))
)


t_if_simphony_transaction = db.Table(
    'if_simphony_transaction',
    db.Column('retailstoreid', db.String(50)),
    db.Column('sequencenumber', db.Numeric(20, 0, asdecimal=False), index=True),
    db.Column('poslogdatetime', db.DateTime),
    db.Column('receiptnumber', db.Numeric(10, 0, asdecimal=False)),
    db.Column('operatorid', db.String(50)),
    db.Column('transactionstatus', db.String(50)),
    db.Column('transactiongrossamount', db.Numeric(12, 4)),
    db.Column('transactionnetamount', db.Numeric(12, 4)),
    db.Column('transactiontaxamount', db.Numeric(12, 4)),
    db.Column('transactiongrandamount', db.Numeric(12, 4)),
    db.Column('transactionnonsalesamount', db.Numeric(12, 4)),
    db.Column('filename', db.String(150), index=True),
    db.Column('revenuecenterid', db.String(50)),
    db.Column('sta', db.String(1), server_default=db.FetchedValue()),
    db.Column('dsc', db.String(50)),
    db.Column('upddt', db.DateTime, server_default=db.FetchedValue()),
    db.Column('workstationid', db.String(50)),
    db.Column('mxposservicetype', db.String(50)),
    db.Index('if_simphony_transaction2', 'revenuecenterid', 'sta')
)


class IfSimphonyXml(db.Model):
    __tablename__ = 'if_simphony_xml'

    id = db.Column(db.Numeric(15, 0, asdecimal=False))
    sta = db.Column(db.String(1), index=True, server_default=db.FetchedValue())
    upddt = db.Column(db.DateTime, server_default=db.FetchedValue())
    transdt = db.Column(db.DateTime)
    xmlfilename = db.Column(db.String(300), primary_key=True)
    dsc = db.Column(db.String(100))
    xmltype = db.Column(db.String(100))
    xmlfilepath = db.Column(db.String(300))


t_if_trans_log = db.Table(
    'if_trans_log',
    db.Column('trans_no', db.Numeric(20, 0, asdecimal=False), nullable=False),
    db.Column('status', db.String(1)),
    db.Column('update_date', db.DateTime),
    db.Column('ctr_code', db.Numeric(20, 0, asdecimal=False), nullable=False),
    db.Column('discsta', db.String(1)),
    db.Column('dis_type', db.Numeric(20, 0, asdecimal=False))
)


t_if_wylist = db.Table(
    'if_wylist',
    db.Column('pid', db.String(50), server_default=db.FetchedValue()),
    db.Column('storecode', db.String(50)),
    db.Column('wy_type', db.String(50)),
    db.Column('last_value', db.String(200)),
    db.Column('cur_value', db.String(200)),
    db.Column('bizdt', db.String(200)),
    db.Column('rmk', db.String(1000)),
    db.Column('up_date', db.DateTime),
    db.Column('is_active', db.String(1)),
    db.Column('update_date', db.DateTime),
    db.Column('update_by', db.String(50)),
    db.Column('is_delete', db.String(1), server_default=db.FetchedValue()),
    db.Column('create_date', db.DateTime),
    db.Column('create_by', db.String(50)),
    db.Index('idx_if_wylist01', 'storecode', 'wy_type', 'is_active')
)


t_if_wylist_new = db.Table(
    'if_wylist_new',
    db.Column('pid', db.String(50), server_default=db.FetchedValue()),
    db.Column('storecode', db.String(50)),
    db.Column('wy_type', db.String(50)),
    db.Column('last_value', db.String(200)),
    db.Column('cur_value', db.String(200)),
    db.Column('bizdt', db.String(200)),
    db.Column('rmk', db.String(1000)),
    db.Column('up_date', db.DateTime),
    db.Column('is_active', db.String(1)),
    db.Column('update_date', db.DateTime),
    db.Column('update_by', db.String(50)),
    db.Index('idx_if_wylistnew01', 'storecode', 'wy_type', 'is_active')
)


t_if_wylistdtl = db.Table(
    'if_wylistdtl',
    db.Column('pid', db.String(50)),
    db.Column('wylist_id', db.String(50)),
    db.Column('exec_time', db.String(4)),
    db.Column('rmk', db.String(100)),
    db.Column('is_delete', db.String(1), server_default=db.FetchedValue()),
    db.Column('update_date', db.DateTime),
    db.Column('update_by', db.String(50)),
    db.Column('create_date', db.DateTime),
    db.Column('create_by', db.String(50))
)


t_if_wylistdtl_new = db.Table(
    'if_wylistdtl_new',
    db.Column('pid', db.String(50)),
    db.Column('wylist_id', db.String(50)),
    db.Column('exec_time', db.String(4)),
    db.Column('rmk', db.String(100)),
    db.Column('is_delete', db.String(1), server_default=db.FetchedValue()),
    db.Column('update_date', db.DateTime),
    db.Column('update_by', db.String(50))
)


t_if_wylog = db.Table(
    'if_wylog',
    db.Column('storecode', db.String(50), index=True),
    db.Column('wy_desc', db.String(200)),
    db.Column('rmk', db.String(1000)),
    db.Column('up_date', db.DateTime),
    db.Column('atc_tp', db.String(1), index=True),
    db.Index('idx_if_wylog01', 'storecode', 'up_date')
)


t_if_wylog_20180202 = db.Table(
    'if_wylog_20180202',
    db.Column('storecode', db.String(50)),
    db.Column('wy_desc', db.String(200)),
    db.Column('rmk', db.String(1000)),
    db.Column('up_date', db.DateTime),
    db.Column('atc_tp', db.String(1))
)


t_if_wylog_20180207 = db.Table(
    'if_wylog_20180207',
    db.Column('storecode', db.String(50)),
    db.Column('wy_desc', db.String(200)),
    db.Column('rmk', db.String(1000)),
    db.Column('up_date', db.DateTime),
    db.Column('atc_tp', db.String(1))
)


t_if_wylog_tmp = db.Table(
    'if_wylog_tmp',
    db.Column('pid', db.String(50), nullable=False),
    db.Column('storecode', db.String(50)),
    db.Column('net_name', db.String(50)),
    db.Column('wy_type', db.String(250)),
    db.Column('cur_value', db.String(200)),
    db.Column('bizdt', db.DateTime),
    db.Column('net_rmk', db.String(1000)),
    db.Column('wy_desc', db.String(200)),
    db.Column('rmk', db.String(1000)),
    db.Column('update_date', db.DateTime),
    db.Column('dsc', db.String(1))
)


class IfXbk(db.Model):
    __tablename__ = 'if_xbk'
    __table_args__ = (
        db.Index('idx_xbk1', 'businessdate', 'net_no'),
    )

    pid = db.Column(db.String(50), primary_key=True)
    businessdate = db.Column(db.String(8))
    net_no = db.Column(db.String(10))
    nk = db.Column(db.Numeric(11, 4))
    wk = db.Column(db.Numeric(11, 4))
    qk = db.Column(db.Numeric(11, 4))
    status = db.Column(db.String(1), index=True, server_default=db.FetchedValue())
    ext_f = db.Column(db.Numeric(11, 4))
    update_date = db.Column(db.DateTime)
    net_no_old = db.Column(db.String(10))
    nk_s = db.Column(db.Numeric(11, 4), server_default=db.FetchedValue())


class ItItembarcodeView(db.Model):
    __tablename__ = 'it_itembarcode_view'

    itemno = db.Column(db.String(20), nullable=False)
    barcode = db.Column(db.String(50), primary_key=True)
    updatedate = db.Column(db.DateTime, nullable=False)


class ItItemmView(db.Model):
    __tablename__ = 'it_itemm_view'

    itemno = db.Column(db.String(20), primary_key=True)
    itemname = db.Column(db.Unicode(100), nullable=False)
    posname = db.Column(db.Unicode(100), nullable=False)
    printname = db.Column(db.Unicode(100), nullable=False)
    enposname = db.Column(db.Unicode(100))
    enprintname = db.Column(db.Unicode(100))
    deptno = db.Column(db.String(10), nullable=False)
    categoryno = db.Column(db.String(10), nullable=False)
    groupno = db.Column(db.String(10), nullable=False)
    cupclusterno = db.Column(db.String(4))
    cupsizeno = db.Column(db.String(2))
    taxno = db.Column(db.String(2))
    taxrat = db.Column(db.Numeric(6, 2))
    updatedate = db.Column(db.DateTime, nullable=False)


class ItItempreaccountView(db.Model):
    __tablename__ = 'it_itempreaccount_view'

    itemno = db.Column(db.String(20), primary_key=True)
    accountno = db.Column(db.String(10), nullable=False)
    accountname = db.Column(db.String(50), nullable=False)
    updatedate = db.Column(db.DateTime)


class ItItempriceView(db.Model):
    __tablename__ = 'it_itemprice_view'

    itemno = db.Column(db.String(20), primary_key=True, nullable=False)
    marketareano = db.Column(db.String(20), primary_key=True, nullable=False)
    begindate = db.Column(db.DateTime, primary_key=True, nullable=False)
    enddate = db.Column(db.DateTime, nullable=False)
    price = db.Column(db.Numeric(10, 2), nullable=False)
    iscover = db.Column(db.String(1), nullable=False)
    issale = db.Column(db.String(1), nullable=False)
    status = db.Column(db.String(3), primary_key=True, nullable=False)
    updatedate = db.Column(db.DateTime, nullable=False)


t_jane_taxrt_view = db.Table(
    'jane_taxrt_view',
    db.Column('id', db.Integer, nullable=False),
    db.Column('cd', db.String(20)),
    db.Column('nm_l_zh', db.Unicode(100), nullable=False),
    db.Column('taxrt', db.Numeric(6, 2)),
    db.Column('deptlkid', db.Integer)
)


class JobCalendar(db.Model):
    __tablename__ = 'job_calendar'

    id = db.Column(db.Integer, primary_key=True)
    coid = db.Column(db.Integer, nullable=False)
    tp = db.Column(db.String(10))
    cd = db.Column(db.String(20))
    nm_l_zh = db.Column(db.Unicode(50), nullable=False)
    nm_l_en = db.Column(db.Unicode(50))
    nm_l_ja = db.Column(db.Unicode(50))
    updby = db.Column(db.String(20))
    upddt = db.Column(db.DateTime)
    rmk = db.Column(db.Unicode(255))
    sta = db.Column(db.String(3))


class JobCalrel(db.Model):
    __tablename__ = 'job_calrel'

    id = db.Column(db.Integer, primary_key=True)
    calid = db.Column(db.Integer, nullable=False)
    jobid = db.Column(db.Integer)
    updby = db.Column(db.String(20))
    upddt = db.Column(db.DateTime)
    sta = db.Column(db.String(3))


class JobConfig(db.Model):
    __tablename__ = 'job_config'

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    jobcd = db.Column(db.String(60), primary_key=True, nullable=False)
    pcd = db.Column(db.String(30))
    aptp = db.Column(db.String(50), nullable=False)
    jobtp = db.Column(db.String(50))
    jobdsc = db.Column(db.String(255))
    objtp = db.Column(db.String(50))
    cronex = db.Column(db.String(200))
    stdt = db.Column(db.DateTime)
    eddt = db.Column(db.DateTime)
    cytp = db.Column(db.String(50), nullable=False)
    cytime = db.Column(db.String(10), nullable=False)
    bizdt = db.Column(db.DateTime, nullable=False)
    lastexecdt = db.Column(db.DateTime)
    updby = db.Column(db.String(20))
    upddt = db.Column(db.DateTime)
    sta = db.Column(db.String(3), nullable=False)
    rmk = db.Column(db.String(255))
    coid = db.Column(db.Integer)


t_job_log = db.Table(
    'job_log',
    db.Column('id', db.Integer, nullable=False),
    db.Column('jobid', db.Integer),
    db.Column('jobcd', db.String(60), nullable=False),
    db.Column('bizdt', db.DateTime),
    db.Column('stdt', db.DateTime),
    db.Column('eddt', db.DateTime),
    db.Column('rtnflag', db.String(1)),
    db.Column('logmsg', db.String(500)),
    db.Column('updby', db.String(20)),
    db.Column('upddt', db.DateTime),
    db.Column('sta', db.String(3))
)


class JobParam(db.Model):
    __tablename__ = 'job_param'

    id = db.Column(db.Integer, primary_key=True)
    jobid = db.Column(db.Integer)
    pmtnm = db.Column(db.String(50))
    pmtval = db.Column(db.String(50))
    datatp = db.Column(db.String(20))
    seq = db.Column(db.Integer)
    updby = db.Column(db.String(20))
    upddt = db.Column(db.DateTime)
    sta = db.Column(db.String(3))


class JobRpt(db.Model):
    __tablename__ = 'job_rpt'

    id = db.Column(db.Integer, primary_key=True)
    moduleid = db.Column(db.Integer)
    tp = db.Column(db.String(10), nullable=False)
    bizdt = db.Column(db.DateTime, nullable=False)
    pldt = db.Column(db.DateTime, nullable=False)
    stdt = db.Column(db.DateTime)
    eddt = db.Column(db.DateTime)
    dbnm = db.Column(db.String(10))
    execsql = db.Column(db.String(4000))
    exppth = db.Column(db.String(100))
    expfilenm = db.Column(db.String(100))
    rmk = db.Column(db.String(2000))
    sta = db.Column(db.String(3))
    updby = db.Column(db.String(20))
    upddt = db.Column(db.DateTime)


class JobRptcol(db.Model):
    __tablename__ = 'job_rptcol'

    id = db.Column(db.Integer, primary_key=True)
    jobrptid = db.Column(db.Integer)
    colnm = db.Column(db.String(50))
    coldsc = db.Column(db.String(50))
    datatp = db.Column(db.String(20))
    seq = db.Column(db.Integer)
    updby = db.Column(db.String(20))
    upddt = db.Column(db.DateTime)
    sta = db.Column(db.String(3))


t_job_rptdata = db.Table(
    'job_rptdata',
    db.Column('jobrptid', db.Integer),
    db.Column('col1', db.String(100)),
    db.Column('col2', db.String(100)),
    db.Column('col3', db.String(100)),
    db.Column('col4', db.String(100)),
    db.Column('col5', db.String(100)),
    db.Column('col6', db.String(100)),
    db.Column('col7', db.String(100)),
    db.Column('col8', db.String(100)),
    db.Column('col9', db.String(100)),
    db.Column('col10', db.String(100)),
    db.Column('col11', db.String(100)),
    db.Column('col12', db.String(100)),
    db.Column('col13', db.String(100)),
    db.Column('col14', db.String(100)),
    db.Column('col15', db.String(100)),
    db.Column('col16', db.String(100)),
    db.Column('col17', db.String(100)),
    db.Column('col18', db.String(100)),
    db.Column('col19', db.String(100)),
    db.Column('col20', db.String(100)),
    db.Column('col21', db.String(100)),
    db.Column('col22', db.String(100)),
    db.Column('col23', db.String(100)),
    db.Column('col24', db.String(100)),
    db.Column('col25', db.String(100)),
    db.Column('col26', db.String(100)),
    db.Column('col27', db.String(100)),
    db.Column('col28', db.String(100)),
    db.Column('col29', db.String(100)),
    db.Column('col30', db.String(100)),
    db.Column('id', db.Integer)
)


class JobRptpmt(db.Model):
    __tablename__ = 'job_rptpmt'

    id = db.Column(db.Integer, primary_key=True)
    jobrptid = db.Column(db.Integer)
    pmtnm = db.Column(db.String(50))
    pmtdsc = db.Column(db.String(50))
    pmtval = db.Column(db.String(50))
    datatp = db.Column(db.String(20))
    seq = db.Column(db.Integer)
    updby = db.Column(db.String(20))
    upddt = db.Column(db.DateTime)
    sta = db.Column(db.String(3))


t_lg_housekeep = db.Table(
    'lg_housekeep',
    db.Column('process_id', db.String(50)),
    db.Column('seq_id', db.Numeric(asdecimal=False)),
    db.Column('table_name', db.String(50)),
    db.Column('error_loc', db.String(50)),
    db.Column('error_desc', db.String(1000)),
    db.Column('process_dt', db.DateTime)
)


t_lg_o2o = db.Table(
    'lg_o2o',
    db.Column('bizdt', db.DateTime),
    db.Column('docid', db.Numeric(12, 0, asdecimal=False)),
    db.Column('sta', db.Numeric(1, 0, asdecimal=False)),
    db.Column('typ', db.Unicode(10))
)


class LngFile(db.Model):
    __tablename__ = 'lng_file'

    id = db.Column(db.Integer, primary_key=True)
    filepath = db.Column(db.Unicode(200), nullable=False)
    filenm = db.Column(db.Unicode(80), nullable=False)
    filenmzh = db.Column(db.Unicode(80))
    tp = db.Column(db.String(10))
    updby = db.Column(db.String(20))
    upddt = db.Column(db.DateTime)
    sta = db.Column(db.String(3), nullable=False)


class LngFilexlat(db.Model):
    __tablename__ = 'lng_filexlat'

    id = db.Column(db.Integer, primary_key=True)
    fileid = db.Column(db.Integer)
    keynm = db.Column(db.Unicode(80), nullable=False)
    xlatid = db.Column(db.Integer)
    nm_l_zh = db.Column(db.Unicode(400))
    nm_l_en = db.Column(db.Unicode(400))
    nm_l_ja = db.Column(db.Unicode(400))
    updby = db.Column(db.String(20))
    upddt = db.Column(db.DateTime)
    sta = db.Column(db.String(3), nullable=False)


class LngMessage(db.Model):
    __tablename__ = 'lng_message'

    id = db.Column(db.Numeric(6, 0, asdecimal=False), primary_key=True)
    tp = db.Column(db.String(10))
    cd = db.Column(db.String(20))
    nm_l_zh = db.Column(db.Unicode(400))
    nm_l_en = db.Column(db.Unicode(400))
    nm_l_ja = db.Column(db.Unicode(400))
    updby = db.Column(db.String(20))
    upddt = db.Column(db.DateTime)
    sta = db.Column(db.String(3), nullable=False)


class LngXlat(db.Model):
    __tablename__ = 'lng_xlat'

    id = db.Column(db.Integer, primary_key=True)
    nm_l_zh = db.Column(db.Unicode(400))
    nm_l_en = db.Column(db.Unicode(400))
    nm_l_ja = db.Column(db.Unicode(400))
    updby = db.Column(db.String(20))
    upddt = db.Column(db.DateTime)
    sta = db.Column(db.String(3), nullable=False)


t_log_proceed_data = db.Table(
    'log_proceed_data',
    db.Column('transno', db.Numeric(20, 0, asdecimal=False), unique=True),
    db.Column('tradedt', db.DateTime, index=True),
    db.Column('flag', db.String(1)),
    db.Column('transdate', db.DateTime)
)


t_log_proceed_data_170525 = db.Table(
    'log_proceed_data_170525',
    db.Column('transno', db.Numeric(20, 0, asdecimal=False)),
    db.Column('tradedt', db.DateTime),
    db.Column('flag', db.String(1)),
    db.Column('transdate', db.DateTime)
)


class Loyaltygroup(db.Model):
    __tablename__ = 'loyaltygroup'

    pid = db.Column(db.String(50), primary_key=True, server_default=db.FetchedValue())
    groupid = db.Column(db.String(4), nullable=False)
    id = db.Column(db.String(50), nullable=False)
    remark = db.Column(db.String(255))
    isdelete = db.Column(db.String(1), nullable=False, server_default=db.FetchedValue())
    updatedate = db.Column(db.DateTime, nullable=False)
    updateby = db.Column(db.String(50), nullable=False)
    createdate = db.Column(db.DateTime, nullable=False)
    createby = db.Column(db.String(50), nullable=False)


t_lqh_test = db.Table(
    'lqh_test',
    db.Column('q1', db.String(30)),
    db.Column('q2', db.String(30)),
    db.Column('q3', db.String(30)),
    db.Column('q4', db.String(30)),
    db.Column('q5', db.String(30)),
    db.Column('q6', db.String(30)),
    db.Column('q7', db.String(30)),
    db.Column('q8', db.String(30)),
    db.Column('q9', db.String(30)),
    db.Column('q10', db.String(30))
)


class NorReqplu(db.Model):
    __tablename__ = 'nor_reqplu'

    id = db.Column(db.Numeric(12, 0, asdecimal=False), primary_key=True)
    reqid = db.Column(db.Numeric(12, 0, asdecimal=False), index=True)
    billrsn = db.Column(db.String(20))
    price = db.Column(db.Numeric(16, 6))
    lsthrqty = db.Column(db.Numeric(16, 6))
    outofsto1 = db.Column(db.String(20))
    lstwoqty = db.Column(db.Numeric(16, 6))
    outofsto2 = db.Column(db.String(20))
    lsqty = db.Column(db.Numeric(16, 6))
    outofsto3 = db.Column(db.String(20))
    thqty = db.Column(db.Numeric(16, 6))
    outofsto4 = db.Column(db.String(20))
    thestqty = db.Column(db.Numeric(16, 6))
    neestqty = db.Column(db.Numeric(16, 6))
    ordqty = db.Column(db.Numeric(16, 6))
    ordamt = db.Column(db.Numeric(16, 6))
    rmk = db.Column(db.String(100))
    updby = db.Column(db.String(20))
    upddt = db.Column(db.DateTime)
    sta = db.Column(db.String(3), nullable=False)
    execflg = db.Column(db.String(1), server_default=db.FetchedValue())
    nxtsta = db.Column(db.String(3))
    pluid = db.Column(db.Integer, nullable=False)
    lntp = db.Column(db.String(10))
    neestordqty = db.Column(db.Numeric(16, 6))
    neestordamt = db.Column(db.Numeric(16, 6))
    neestordqty1 = db.Column(db.Numeric(16, 6))


class NorRequest(db.Model):
    __tablename__ = 'nor_request'
    __table_args__ = (
        db.Index('idxnor_request1', 'deptid', 'orddt'),
    )

    id = db.Column(db.Numeric(12, 0, asdecimal=False), primary_key=True)
    coid = db.Column(db.Integer)
    billtp = db.Column(db.String(10))
    billrsn = db.Column(db.String(20))
    deptid = db.Column(db.Integer)
    pluid = db.Column(db.Integer)
    venlktp = db.Column(db.String(10))
    venlkid = db.Column(db.Integer)
    orddt = db.Column(db.DateTime)
    reqdeptid = db.Column(db.Integer)
    reqdt = db.Column(db.DateTime)
    reqby = db.Column(db.String(20))
    psdt = db.Column(db.DateTime)
    shipby = db.Column(db.String(20))
    cnldt = db.Column(db.DateTime)
    cnlby = db.Column(db.String(20))
    rmk = db.Column(db.String(255))
    updby = db.Column(db.String(20))
    upddt = db.Column(db.DateTime)
    sta = db.Column(db.String(3), nullable=False)
    execflg = db.Column(db.String(1))
    nxtsta = db.Column(db.String(3))


class NormPlu(db.Model):
    __tablename__ = 'norm_plu'
    __table_args__ = (
        db.Index('idx_norm_plu', 'pluid', 'ordflg'),
    )

    id = db.Column(db.Integer, primary_key=True)
    pluid = db.Column(db.Integer, nullable=False)
    stdt = db.Column(db.DateTime)
    eddt = db.Column(db.DateTime)
    rmk = db.Column(db.String(250))
    ordflg = db.Column(db.Integer, server_default=db.FetchedValue())
    updby = db.Column(db.String(50))
    upddt = db.Column(db.DateTime)
    sta = db.Column(db.String(3), nullable=False)
    execflg = db.Column(db.String(1))
    nxtsta = db.Column(db.String(3))


t_oto_io_po = db.Table(
    'oto_io_po',
    db.Column('sno', db.String(20)),
    db.Column('bizdt', db.DateTime),
    db.Column('po_type', db.String(1)),
    db.Column('rev_date', db.DateTime),
    db.Column('net_no', db.String(20)),
    db.Column('plu_no', db.String(20)),
    db.Column('qty', db.Numeric(14, 2)),
    db.Column('rmk', db.String(100)),
    db.Column('potp', db.String(8)),
    db.Column('createdate', db.DateTime),
    db.Index('oto_io_po_1', 'sno', 'bizdt')
)


t_oto_po_tmp = db.Table(
    'oto_po_tmp',
    db.Column('sno', db.String(20)),
    db.Column('bizdt', db.String(8)),
    db.Column('po_type', db.String(1)),
    db.Column('rev_date', db.String(8)),
    db.Column('net_no', db.String(20)),
    db.Column('plu_no', db.String(20)),
    db.Column('qty', db.Numeric(14, 2)),
    db.Column('rmk', db.String(100)),
    db.Column('potp', db.String(8)),
    db.Column('createdate', db.DateTime, server_default=db.FetchedValue())
)


t_partner_user = db.Table(
    'partner_user',
    db.Column('userid', db.String(10), nullable=False, index=True),
    db.Column('username', db.Unicode(50)),
    db.Column('id', db.String(10)),
    db.Column('corp', db.String(10)),
    db.Column('aa', db.String(10))
)


t_partner_user_20170210 = db.Table(
    'partner_user_20170210',
    db.Column('userid', db.String(10), nullable=False),
    db.Column('username', db.Unicode(50)),
    db.Column('id', db.Numeric(12, 0, asdecimal=False)),
    db.Column('corp', db.String(10))
)


t_partner_user_bak = db.Table(
    'partner_user_bak',
    db.Column('userid', db.String(10), nullable=False),
    db.Column('username', db.Unicode(50)),
    db.Column('id', db.Numeric(12, 0, asdecimal=False)),
    db.Column('corp', db.String(10))
)


t_partner_user_temp = db.Table(
    'partner_user_temp',
    db.Column('userid', db.String(10), nullable=False),
    db.Column('username', db.Unicode(50)),
    db.Column('id', db.Numeric(12, 0, asdecimal=False)),
    db.Column('userid2', db.String(10), nullable=False)
)


t_partner_user_temp1 = db.Table(
    'partner_user_temp1',
    db.Column('userid', db.String(10), nullable=False),
    db.Column('username', db.Unicode(50)),
    db.Column('id', db.Numeric(12, 0, asdecimal=False)),
    db.Column('corp', db.String(10))
)


t_pos_adjlog_pic = db.Table(
    'pos_adjlog_pic',
    db.Column('sid', db.Numeric(asdecimal=False)),
    db.Column('guid', db.String(50)),
    db.Column('upddt', db.DateTime)
)


t_pos_depositdtl = db.Table(
    'pos_depositdtl',
    db.Column('storeno', db.String(10)),
    db.Column('depositno', db.String(20)),
    db.Column('tradetype', db.Numeric(asdecimal=False)),
    db.Column('lineid', db.Numeric(asdecimal=False)),
    db.Column('tenderno', db.String(3)),
    db.Column('curtenderamt', db.Numeric(10, 2)),
    db.Column('paycardtype', db.String(50)),
    db.Column('paycardno', db.String(50)),
    db.Column('cardexpired', db.DateTime),
    db.Column('cardissuecode', db.String(20)),
    db.Column('payauthcode', db.String(20)),
    db.Column('extpaycode', db.String(20)),
    db.Column('extpaymsg', db.String(100)),
    db.Column('balancebefore', db.Numeric(10, 2)),
    db.Column('balanceafter', db.Numeric(10, 2)),
    db.Column('exttransno', db.String(20)),
    db.Column('termid', db.String(20)),
    db.Column('depositdate', db.DateTime),
    db.Index('idx_pos_depositdtl', 'storeno', 'depositno', 'tradetype')
)


class PosDeposithdr(db.Model):
    __tablename__ = 'pos_deposithdr'
    __table_args__ = (
        db.Index('idx_posdisc', 'storeno', 'bizdt'),
        db.Index('idx_posdisc2', 'storeno', 'depositno')
    )

    sid = db.Column(db.Integer, primary_key=True)
    storeno = db.Column(db.String(10))
    posno = db.Column(db.String(10))
    depositno = db.Column(db.String(20))
    tradetype = db.Column(db.Numeric(asdecimal=False))
    deposit = db.Column(db.Numeric(10, 2))
    depositdate = db.Column(db.DateTime)
    depositduedate = db.Column(db.DateTime)
    customerphone = db.Column(db.String(20))
    staffno = db.Column(db.String(10))
    lintguid = db.Column(db.String(36))
    tradedate = db.Column(db.DateTime)
    tradestaffno = db.Column(db.String(10))
    bizdt = db.Column(db.DateTime, index=True)
    shiftflg = db.Column(db.String(1), server_default=db.FetchedValue())
    shiftid = db.Column(db.Numeric(12, 0, asdecimal=False))


t_pos_discount = db.Table(
    'pos_discount',
    db.Column('id', db.Integer),
    db.Column('cd', db.String(20)),
    db.Column('poscd', db.String(20)),
    db.Column('priotp', db.String(10)),
    db.Column('tp', db.String(10)),
    db.Column('nm_l_zh', db.String(50), nullable=False),
    db.Column('nm_l_en', db.String(50)),
    db.Column('nm_l_ja', db.String(50)),
    db.Column('rmk', db.String(250)),
    db.Column('updby', db.String(20)),
    db.Column('upddt', db.DateTime),
    db.Column('sta', db.String(3), nullable=False),
    db.Column('bdate', db.DateTime),
    db.Column('edate', db.DateTime)
)


t_pos_discount_view = db.Table(
    'pos_discount_view',
    db.Column('id', db.Integer),
    db.Column('tp', db.String(10)),
    db.Column('nm_l_zh', db.String(100)),
    db.Column('isstaffdisc', db.Integer),
    db.Column('upddt', db.DateTime),
    db.Column('staffdisccounter', db.Integer)
)


t_pos_membercd_temp_min = db.Table(
    'pos_membercd_temp_min',
    db.Column('membercd', db.String(50)),
    db.Column('nm_l_zh', db.String(20))
)


t_pos_msrlog = db.Table(
    'pos_msrlog',
    db.Column('transno', db.Numeric(14, 0, asdecimal=False), index=True),
    db.Column('status', db.String(1), index=True),
    db.Column('upddt', db.DateTime, server_default=db.FetchedValue())
)


class PosReason(db.Model):
    __tablename__ = 'pos_reason'

    id = db.Column(db.Integer, primary_key=True)
    cd = db.Column(db.String(20))
    poscd = db.Column(db.String(20))
    nm_l_zh = db.Column(db.String(50), nullable=False)
    nm_l_en = db.Column(db.String(50))
    nm_l_ja = db.Column(db.String(50))
    rmk = db.Column(db.String(255))
    updby = db.Column(db.String(20))
    upddt = db.Column(db.DateTime)
    sta = db.Column(db.String(3), nullable=False)


t_pos_sales = db.Table(
    'pos_sales',
    db.Column('transno', db.Numeric(20, 0, asdecimal=False), nullable=False)
)


t_pos_tender = db.Table(
    'pos_tender',
    db.Column('id', db.Integer),
    db.Column('cd', db.String(20)),
    db.Column('poscd', db.String(20)),
    db.Column('nm_l_zh', db.String(50), nullable=False),
    db.Column('nm_l_en', db.String(50)),
    db.Column('nm_l_ja', db.String(50)),
    db.Column('rmk', db.String(255)),
    db.Column('updby', db.String(20)),
    db.Column('upddt', db.DateTime),
    db.Column('sta', db.String(3), nullable=False),
    db.Column('tp', db.String(10)),
    db.Column('arrt', db.Numeric(12, 4)),
    db.Column('aracctcd', db.String(20)),
    db.Column('bankrt', db.Numeric(12, 4)),
    db.Column('discrt', db.Numeric(12, 4)),
    db.Column('valrule', db.String(10)),
    db.Column('paytp1', db.String(10)),
    db.Column('paytp2', db.String(10)),
    db.Column('bbfeert', db.Numeric(12, 4)),
    db.Column('taxflg', db.String(1), server_default=db.FetchedValue()),
    db.Column('thirdcd', db.String(20)),
    db.Column('lkpluid', db.String(20))
)


t_pos_till = db.Table(
    'pos_till',
    db.Column('id', db.Integer, nullable=False),
    db.Column('cd', db.String(20)),
    db.Column('poscd', db.String(20)),
    db.Column('deptid', db.Integer),
    db.Column('deptcd', db.String(20)),
    db.Column('tp', db.String(10)),
    db.Column('secondcd', db.String(20), nullable=False),
    db.Column('nm_l_zh', db.String(50), nullable=False),
    db.Column('nm_l_en', db.String(50)),
    db.Column('nm_l_ja', db.String(50)),
    db.Column('pcnm', db.String(50)),
    db.Column('ipadr', db.String(20)),
    db.Column('macadr', db.String(30)),
    db.Column('rmk', db.String(250)),
    db.Column('updby', db.String(20)),
    db.Column('upddt', db.DateTime),
    db.Column('sta', db.String(3), nullable=False),
    db.Column('ysnpt_svc_active', db.String(1)),
    db.Column('ysnpt_svc_cancelactive', db.String(1)),
    db.Column('ysnpt_svc_addvalue', db.String(1)),
    db.Column('ysnpt_svc_canceladdvalue', db.String(1)),
    db.Column('ysnpt_svc_paylessthan200', db.String(1)),
    db.Column('ysnpt_svc_payreturn', db.String(1)),
    db.Column('ysnpt_svc_paymorethan200', db.String(1)),
    db.Column('ysnpt_svc_checkout', db.String(1)),
    db.Column('ysnpt_svc_checkoutsum', db.String(1))
)


t_pos_tilldev = db.Table(
    'pos_tilldev',
    db.Column('id', db.Integer, nullable=False),
    db.Column('tillid', db.Integer),
    db.Column('tillcd', db.String(20)),
    db.Column('cd', db.String(20)),
    db.Column('poscd', db.String(20)),
    db.Column('tp', db.String(10)),
    db.Column('nm_l_zh', db.Unicode(50), nullable=False),
    db.Column('nm_l_en', db.Unicode(50)),
    db.Column('nm_l_ja', db.Unicode(50)),
    db.Column('devport', db.String(10)),
    db.Column('baudrt', db.Integer),
    db.Column('devmodel', db.String(50)),
    db.Column('rmk', db.Unicode(255)),
    db.Column('updby', db.String(20)),
    db.Column('upddt', db.DateTime),
    db.Column('sta', db.String(3), nullable=False)
)


t_pos_transdisc = db.Table(
    'pos_transdisc',
    db.Column('transno', db.Numeric(20, 0, asdecimal=False), nullable=False, index=True),
    db.Column('bizdt', db.DateTime),
    db.Column('ctrno', db.Numeric(20, 0, asdecimal=False)),
    db.Column('disctp', db.String(1)),
    db.Column('disccd', db.String(10)),
    db.Column('discamt', db.Numeric(19, 4), server_default=db.FetchedValue())
)


t_pos_transdiscdtl = db.Table(
    'pos_transdiscdtl',
    db.Column('transno', db.Numeric(20, 0, asdecimal=False), nullable=False, index=True),
    db.Column('bizdt', db.DateTime),
    db.Column('ctrno', db.Numeric(20, 0, asdecimal=False)),
    db.Column('disccd', db.String(10)),
    db.Column('giftno', db.String(50))
)


t_pos_transdtl = db.Table(
    'pos_transdtl',
    db.Column('transno', db.Numeric(20, 0, asdecimal=False), nullable=False, index=True),
    db.Column('bizdt', db.DateTime, index=True),
    db.Column('tradedt', db.DateTime),
    db.Column('ctrno', db.Numeric(20, 0, asdecimal=False)),
    db.Column('plucd', db.String(20)),
    db.Column('pluid', db.Integer),
    db.Column('pluprc', db.Numeric(19, 4), server_default=db.FetchedValue()),
    db.Column('grossamt', db.Numeric(19, 4), server_default=db.FetchedValue()),
    db.Column('netamt', db.Numeric(19, 4)),
    db.Column('discamt', db.Numeric(19, 4)),
    db.Column('curqty', db.Numeric(19, 4), server_default=db.FetchedValue()),
    db.Column('billuom', db.Integer),
    db.Column('convrate', db.Numeric(16, 6)),
    db.Column('pkuom', db.Integer),
    db.Column('transtp', db.String(10)),
    db.Column('strcomment', db.String(100)),
    db.Column('msr', db.Numeric(19, 4)),
    db.Column('giftno', db.String(30))
)


t_pos_transdtl_170615 = db.Table(
    'pos_transdtl_170615',
    db.Column('transno', db.Numeric(20, 0, asdecimal=False), nullable=False),
    db.Column('bizdt', db.DateTime),
    db.Column('tradedt', db.DateTime),
    db.Column('ctrno', db.Numeric(20, 0, asdecimal=False)),
    db.Column('plucd', db.String(20)),
    db.Column('pluid', db.Integer),
    db.Column('pluprc', db.Numeric(19, 4)),
    db.Column('grossamt', db.Numeric(19, 4)),
    db.Column('netamt', db.Numeric(19, 4)),
    db.Column('discamt', db.Numeric(19, 4)),
    db.Column('curqty', db.Numeric(19, 4)),
    db.Column('billuom', db.Integer),
    db.Column('convrate', db.Numeric(16, 6)),
    db.Column('pkuom', db.Integer),
    db.Column('transtp', db.String(10)),
    db.Column('strcomment', db.String(100)),
    db.Column('msr', db.Numeric(19, 4)),
    db.Column('giftno', db.String(30))
)


t_pos_transdtl_hhs20161227 = db.Table(
    'pos_transdtl_hhs20161227',
    db.Column('transno', db.Numeric(20, 0, asdecimal=False), nullable=False),
    db.Column('bizdt', db.DateTime),
    db.Column('tradedt', db.DateTime),
    db.Column('ctrno', db.Numeric(20, 0, asdecimal=False)),
    db.Column('plucd', db.String(20)),
    db.Column('pluid', db.Integer),
    db.Column('pluprc', db.Numeric(19, 4), server_default=db.FetchedValue()),
    db.Column('grossamt', db.Numeric(19, 4), server_default=db.FetchedValue()),
    db.Column('netamt', db.Numeric(19, 4)),
    db.Column('discamt', db.Numeric(19, 4)),
    db.Column('curqty', db.Numeric(19, 4), server_default=db.FetchedValue()),
    db.Column('billuom', db.Integer),
    db.Column('convrate', db.Numeric(16, 6)),
    db.Column('pkuom', db.Integer),
    db.Column('transtp', db.String(10)),
    db.Column('strcomment', db.String(100)),
    db.Column('msr', db.Numeric(19, 4)),
    db.Column('giftno', db.String(30))
)


t_pos_translog = db.Table(
    'pos_translog',
    db.Column('transno', db.Numeric(20, 0, asdecimal=False), nullable=False, index=True),
    db.Column('ctrno', db.Numeric(20, 0, asdecimal=False), nullable=False, index=True),
    db.Column('status', db.String(1), index=True),
    db.Column('dis_type', db.Numeric(20, 0, asdecimal=False), server_default=db.FetchedValue()),
    db.Column('discsta', db.String(1), server_default=db.FetchedValue()),
    db.Column('shiftflg', db.String(1), index=True, server_default=db.FetchedValue()),
    db.Column('stkflg', db.String(1), index=True, server_default=db.FetchedValue()),
    db.Column('upddt', db.DateTime, index=True),
    db.Column('bizdt', db.DateTime, index=True),
    db.Column('stkdt', db.DateTime),
    db.Column('shiftflg1', db.String(10))
)


t_pos_translog_inv = db.Table(
    'pos_translog_inv',
    db.Column('transno', db.Numeric(20, 0, asdecimal=False), nullable=False, index=True),
    db.Column('upddt', db.DateTime),
    db.Column('sta', db.String(1), server_default=db.FetchedValue())
)


t_pos_translog_pic = db.Table(
    'pos_translog_pic',
    db.Column('transno', db.Numeric(20, 0, asdecimal=False), nullable=False, index=True),
    db.Column('ctrno', db.Numeric(20, 0, asdecimal=False), nullable=False, index=True),
    db.Column('status', db.String(1), index=True),
    db.Column('dis_type', db.Numeric(20, 0, asdecimal=False), server_default=db.FetchedValue()),
    db.Column('discsta', db.String(1), server_default=db.FetchedValue()),
    db.Column('shiftflg', db.String(1), server_default=db.FetchedValue()),
    db.Column('stkflg', db.String(1), index=True, server_default=db.FetchedValue()),
    db.Column('upddt', db.DateTime, index=True),
    db.Column('bizdt', db.DateTime, index=True),
    db.Column('stkdt', db.DateTime)
)


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


t_pos_transmst_temp_min = db.Table(
    'pos_transmst_temp_min',
    db.Column('transno', db.Numeric(20, 0, asdecimal=False), nullable=False),
    db.Column('tradedt', db.DateTime),
    db.Column('tdramt', db.Numeric(18, 4)),
    db.Column('membercd', db.String(20)),
    db.Column('paycardno', db.String(50)),
    db.Column('nm_l_zh', db.String(50))
)


class PosTransmstdsc(db.Model):
    __tablename__ = 'pos_transmstdsc'

    transno = db.Column(db.Numeric(20, 0, asdecimal=False), primary_key=True)
    bizdt = db.Column(db.DateTime)
    ctctp = db.Column(db.String(10))
    dlvadr = db.Column(db.String(50))
    salecmt = db.Column(db.String(100))
    surveygp = db.Column(db.String(20))
    ans1 = db.Column(db.String(20))
    ans2 = db.Column(db.String(20))
    ans3 = db.Column(db.String(20))
    ans4 = db.Column(db.String(20))
    ans5 = db.Column(db.String(20))


t_pos_transrmk = db.Table(
    'pos_transrmk',
    db.Column('transno', db.Numeric(20, 0, asdecimal=False), index=True),
    db.Column('bizdt', db.DateTime),
    db.Column('ctrno', db.Numeric(20, 0, asdecimal=False)),
    db.Column('transtp', db.String(10)),
    db.Column('rmk', db.String(200))
)


t_pos_transsurvery = db.Table(
    'pos_transsurvery',
    db.Column('transno', db.Numeric(20, 0, asdecimal=False), nullable=False),
    db.Column('stranswer1', db.String(20)),
    db.Column('stranswer2', db.String(20))
)


t_pos_transtdr = db.Table(
    'pos_transtdr',
    db.Column('transno', db.Numeric(20, 0, asdecimal=False), index=True),
    db.Column('bizdt', db.DateTime),
    db.Column('ctrno', db.Numeric(20, 0, asdecimal=False)),
    db.Column('tdrtp', db.String(1)),
    db.Column('tdrcd', db.String(10)),
    db.Column('tdramt', db.Numeric(18, 4), server_default=db.FetchedValue()),
    db.Column('addpoint', db.Integer),
    db.Column('rmk', db.String(100)),
    db.Column('paycardno', db.String(50))
)


t_pos_transtdrtax = db.Table(
    'pos_transtdrtax',
    db.Column('transno', db.Numeric(20, 0, asdecimal=False), nullable=False, index=True),
    db.Column('bizdt', db.DateTime, index=True),
    db.Column('tdrcd', db.String(10)),
    db.Column('invdsc', db.String(50)),
    db.Column('amt', db.Numeric(16, 2)),
    db.Column('disamt', db.Numeric(16, 2)),
    db.Column('rmk', db.String(50)),
    db.Column('upddt', db.DateTime)
)


t_pos_transtdrtax_tmpe = db.Table(
    'pos_transtdrtax_tmpe',
    db.Column('transno', db.Numeric(20, 0, asdecimal=False), nullable=False),
    db.Column('bizdt', db.DateTime),
    db.Column('tdrcd', db.String(10)),
    db.Column('invdsc', db.String(50)),
    db.Column('amt', db.Numeric(16, 2)),
    db.Column('disamt', db.Numeric(16, 2)),
    db.Column('rmk', db.String(50)),
    db.Column('upddt', db.DateTime)
)


t_pos_transttaxlog = db.Table(
    'pos_transttaxlog',
    db.Column('transno', db.Numeric(20, 0, asdecimal=False), nullable=False),
    db.Column('status', db.String(1), index=True)
)


t_pos_transttaxlog_t = db.Table(
    'pos_transttaxlog_t',
    db.Column('transno', db.Numeric(20, 0, asdecimal=False), nullable=False),
    db.Column('status', db.String(1)),
    db.Index('idx$$_1903f0001', 'status', 'transno')
)


t_rpt_callog = db.Table(
    'rpt_callog',
    db.Column('bizdt', db.DateTime, nullable=False),
    db.Column('rptcd', db.String(50), nullable=False),
    db.Column('rptnm', db.String(50)),
    db.Column('sta', db.String(3)),
    db.Column('errmsg', db.String(50)),
    db.Column('upddt', db.DateTime)
)


t_rpt_disc = db.Table(
    'rpt_disc',
    db.Column('deptid', db.Integer, nullable=False),
    db.Column('bizdt', db.DateTime, nullable=False),
    db.Column('disctp', db.String(1)),
    db.Column('discid', db.Integer, nullable=False),
    db.Column('discamt', db.Numeric(16, 4), server_default=db.FetchedValue()),
    db.Column('disccnt', db.Integer, server_default=db.FetchedValue()),
    db.Column('rtndiscamt', db.Numeric(16, 4), server_default=db.FetchedValue()),
    db.Column('qty', db.Numeric(16, 4)),
    db.Column('saleprc', db.Numeric(16, 4), server_default=db.FetchedValue()),
    db.Column('hqdiscamt', db.Numeric(16, 4)),
    db.Column('upddt', db.DateTime),
    db.Column('updby', db.String(20)),
    db.Column('id', db.Integer, index=True),
    db.Index('idx_rpt_disc', 'deptid', 'bizdt')
)


t_rpt_empdiscount = db.Table(
    'rpt_empdiscount',
    db.Column('bizdt', db.DateTime),
    db.Column('transno', db.Numeric(20, 0, asdecimal=False)),
    db.Column('customerid', db.Integer),
    db.Column('customername', db.String(100), index=True),
    db.Column('deptid', db.Integer, nullable=False),
    db.Column('pluid', db.Integer, nullable=False),
    db.Column('qty', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('price', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('grossamt', db.Numeric(12, 4), nullable=False, server_default=db.FetchedValue()),
    db.Column('netamt', db.Numeric(16, 4), nullable=False, server_default=db.FetchedValue()),
    db.Index('idx_rpt_empdisc', 'bizdt', 'deptid')
)


t_rpt_psd = db.Table(
    'rpt_psd',
    db.Column('yearmonth', db.String(10)),
    db.Column('deptid', db.Integer),
    db.Column('psd', db.Numeric(18, 0, asdecimal=False)),
    db.Column('bizcnt', db.Integer),
    db.Column('overcnt', db.Integer),
    db.Column('overrt', db.Numeric(19, 4)),
    db.Column('netamt1', db.Numeric(19, 4)),
    db.Column('adjamt1', db.Numeric(19, 4)),
    db.Column('rt1', db.Numeric(19, 4)),
    db.Column('netamt2', db.Numeric(19, 4)),
    db.Column('adjamt2', db.Numeric(19, 4)),
    db.Column('rt2', db.Numeric(19, 4)),
    db.Column('netamt3', db.Numeric(19, 4)),
    db.Column('adjamt3', db.Numeric(19, 4)),
    db.Column('rt3', db.Numeric(19, 4)),
    db.Column('netamt4', db.Numeric(19, 4)),
    db.Column('adjamt4', db.Numeric(19, 4)),
    db.Column('rt4', db.Numeric(19, 4)),
    db.Column('netamt5', db.Numeric(19, 4)),
    db.Column('adjamt5', db.Numeric(19, 4)),
    db.Column('rt5', db.Numeric(19, 4)),
    db.Column('netamt6', db.Numeric(19, 4)),
    db.Column('adjamt6', db.Numeric(19, 4)),
    db.Column('rt6', db.Numeric(19, 4)),
    db.Column('netamt7', db.Numeric(19, 4)),
    db.Column('adjamt7', db.Numeric(19, 4)),
    db.Column('rt7', db.Numeric(19, 4)),
    db.Column('netamt8', db.Numeric(19, 4)),
    db.Column('adjamt8', db.Numeric(19, 4)),
    db.Column('rt8', db.Numeric(19, 4)),
    db.Column('netamt9', db.Numeric(19, 4)),
    db.Column('adjamt9', db.Numeric(19, 4)),
    db.Column('rt9', db.Numeric(19, 4)),
    db.Column('netamt10', db.Numeric(19, 4)),
    db.Column('adjamt10', db.Numeric(19, 4)),
    db.Column('rt10', db.Numeric(19, 4)),
    db.Column('netamt11', db.Numeric(19, 4)),
    db.Column('adjamt11', db.Numeric(19, 4)),
    db.Column('rt11', db.Numeric(19, 4)),
    db.Column('netamt12', db.Numeric(19, 4)),
    db.Column('adjamt12', db.Numeric(19, 4)),
    db.Column('rt12', db.Numeric(19, 4)),
    db.Column('netamt13', db.Numeric(19, 4)),
    db.Column('adjamt13', db.Numeric(19, 4)),
    db.Column('rt13', db.Numeric(19, 4)),
    db.Column('netamt14', db.Numeric(19, 4)),
    db.Column('adjamt14', db.Numeric(19, 4)),
    db.Column('rt14', db.Numeric(19, 4)),
    db.Column('netamt15', db.Numeric(19, 4)),
    db.Column('adjamt15', db.Numeric(19, 4)),
    db.Column('rt15', db.Numeric(19, 4)),
    db.Column('netamt16', db.Numeric(19, 4)),
    db.Column('adjamt16', db.Numeric(19, 4)),
    db.Column('rt16', db.Numeric(19, 4)),
    db.Column('netamt17', db.Numeric(19, 4)),
    db.Column('adjamt17', db.Numeric(19, 4)),
    db.Column('rt17', db.Numeric(19, 4)),
    db.Column('netamt18', db.Numeric(19, 4)),
    db.Column('adjamt18', db.Numeric(19, 4)),
    db.Column('rt18', db.Numeric(19, 4)),
    db.Column('netamt19', db.Numeric(19, 4)),
    db.Column('adjamt19', db.Numeric(19, 4)),
    db.Column('rt19', db.Numeric(19, 4)),
    db.Column('netamt20', db.Numeric(19, 4)),
    db.Column('adjamt20', db.Numeric(19, 4)),
    db.Column('rt20', db.Numeric(19, 4)),
    db.Column('netamt21', db.Numeric(19, 4)),
    db.Column('adjamt21', db.Numeric(19, 4)),
    db.Column('rt21', db.Numeric(19, 4)),
    db.Column('netamt22', db.Numeric(19, 4)),
    db.Column('adjamt22', db.Numeric(19, 4)),
    db.Column('rt22', db.Numeric(19, 4)),
    db.Column('netamt23', db.Numeric(19, 4)),
    db.Column('adjamt23', db.Numeric(19, 4)),
    db.Column('rt23', db.Numeric(19, 4)),
    db.Column('netamt24', db.Numeric(19, 4)),
    db.Column('adjamt24', db.Numeric(19, 4)),
    db.Column('rt24', db.Numeric(19, 4)),
    db.Column('netamt25', db.Numeric(19, 4)),
    db.Column('adjamt25', db.Numeric(19, 4)),
    db.Column('rt25', db.Numeric(19, 4)),
    db.Column('netamt26', db.Numeric(19, 4)),
    db.Column('adjamt26', db.Numeric(19, 4)),
    db.Column('rt26', db.Numeric(19, 4)),
    db.Column('netamt27', db.Numeric(19, 4)),
    db.Column('adjamt27', db.Numeric(19, 4)),
    db.Column('rt27', db.Numeric(19, 4)),
    db.Column('netamt28', db.Numeric(19, 4)),
    db.Column('adjamt28', db.Numeric(19, 4)),
    db.Column('rt28', db.Numeric(19, 4)),
    db.Column('netamt29', db.Numeric(19, 4)),
    db.Column('adjamt29', db.Numeric(19, 4)),
    db.Column('rt29', db.Numeric(19, 4)),
    db.Column('netamt30', db.Numeric(19, 4)),
    db.Column('adjamt30', db.Numeric(19, 4)),
    db.Column('rt30', db.Numeric(19, 4)),
    db.Column('netamt31', db.Numeric(19, 4)),
    db.Column('adjamt31', db.Numeric(19, 4)),
    db.Column('rt31', db.Numeric(19, 4)),
    db.Column('upddt', db.DateTime),
    db.Column('flg1', db.Integer),
    db.Column('flg2', db.Integer),
    db.Column('flg3', db.Integer),
    db.Column('flg4', db.Integer),
    db.Column('flg5', db.Integer),
    db.Column('flg6', db.Integer),
    db.Column('flg7', db.Integer),
    db.Column('flg8', db.Integer),
    db.Column('flg9', db.Integer),
    db.Column('flg10', db.Integer),
    db.Column('flg11', db.Integer),
    db.Column('flg12', db.Integer),
    db.Column('flg13', db.Integer),
    db.Column('flg14', db.Integer),
    db.Column('flg15', db.Integer),
    db.Column('flg16', db.Integer),
    db.Column('flg17', db.Integer),
    db.Column('flg18', db.Integer),
    db.Column('flg19', db.Integer),
    db.Column('flg20', db.Integer),
    db.Column('flg21', db.Integer),
    db.Column('flg22', db.Integer),
    db.Column('flg23', db.Integer),
    db.Column('flg24', db.Integer),
    db.Column('flg25', db.Integer),
    db.Column('flg26', db.Integer),
    db.Column('flg27', db.Integer),
    db.Column('flg28', db.Integer),
    db.Column('flg29', db.Integer),
    db.Column('flg30', db.Integer),
    db.Column('flg31', db.Integer)
)


t_rpt_saleadt = db.Table(
    'rpt_saleadt',
    db.Column('bizdt', db.DateTime, nullable=False),
    db.Column('deptid', db.Integer, nullable=False),
    db.Column('tillcd', db.String(20)),
    db.Column('dthour', db.Integer),
    db.Column('adt', db.Integer, server_default=db.FetchedValue()),
    db.Index('idx_rpt_saleadt', 'bizdt', 'deptid')
)


t_rpt_salecat = db.Table(
    'rpt_salecat',
    db.Column('id', db.Integer, nullable=False),
    db.Column('deptid', db.Integer, nullable=False),
    db.Column('bizdt', db.DateTime, nullable=False),
    db.Column('catid', db.Integer, nullable=False),
    db.Column('grossamt', db.Numeric(16, 2), server_default=db.FetchedValue()),
    db.Column('rtnamt', db.Numeric(16, 2), server_default=db.FetchedValue()),
    db.Column('discamt', db.Numeric(16, 2), server_default=db.FetchedValue()),
    db.Column('netamt', db.Numeric(16, 2)),
    db.Column('hqgrossamt', db.Numeric(16, 2)),
    db.Column('hqrtnamt', db.Numeric(16, 2)),
    db.Column('hqdiscamt', db.Numeric(16, 2)),
    db.Column('hqnetamt', db.Numeric(16, 2)),
    db.Column('upddt', db.DateTime),
    db.Column('updby', db.String(20)),
    db.Column('rtndiscamt', db.Numeric(16, 2), server_default=db.FetchedValue()),
    db.Column('yearno', db.Integer),
    db.Column('monthno', db.Integer),
    db.Column('saleqty', db.Numeric(20, 2)),
    db.Index('idx_rpt_salecat1', 'deptid', 'bizdt')
)


t_rpt_saledept = db.Table(
    'rpt_saledept',
    db.Column('deptid', db.Integer, nullable=False),
    db.Column('bizdt', db.DateTime, nullable=False),
    db.Column('grossamt', db.Numeric(19, 4)),
    db.Column('netamt', db.Numeric(19, 4), server_default=db.FetchedValue()),
    db.Column('rtnamt', db.Numeric(19, 4), server_default=db.FetchedValue()),
    db.Column('salecnt', db.Integer, server_default=db.FetchedValue()),
    db.Column('rtncnt', db.Integer, server_default=db.FetchedValue()),
    db.Column('cnlcnt', db.Integer, server_default=db.FetchedValue()),
    db.Column('adt', db.Integer, server_default=db.FetchedValue()),
    db.Column('discamt', db.Numeric(19, 4), server_default=db.FetchedValue()),
    db.Column('rtndiscamt', db.Numeric(19, 4), server_default=db.FetchedValue()),
    db.Column('tillcd', db.String(20)),
    db.Index('idx_rpt_saledept1', 'deptid', 'bizdt')
)


t_rpt_saledisc = db.Table(
    'rpt_saledisc',
    db.Column('deptid', db.Integer, nullable=False),
    db.Column('bizdt', db.DateTime, nullable=False),
    db.Column('disctp', db.String(1)),
    db.Column('discid', db.Integer, nullable=False),
    db.Column('discamt', db.Numeric(16, 4), server_default=db.FetchedValue()),
    db.Column('disccnt', db.Integer, server_default=db.FetchedValue()),
    db.Column('rtndiscamt', db.Numeric(16, 4), server_default=db.FetchedValue()),
    db.Column('pluid', db.Integer),
    db.Column('qty', db.Numeric(16, 4)),
    db.Column('saleprc', db.Numeric(16, 4), server_default=db.FetchedValue()),
    db.Column('hqdiscamt', db.Numeric(16, 4)),
    db.Column('upddt', db.DateTime),
    db.Column('updby', db.String(20)),
    db.Column('id', db.Integer, index=True),
    db.Index('idx_rpt_saledisc', 'deptid', 'bizdt')
)


t_rpt_salemajor = db.Table(
    'rpt_salemajor',
    db.Column('id', db.Integer, nullable=False),
    db.Column('deptid', db.Integer, nullable=False),
    db.Column('bizdt', db.DateTime, nullable=False),
    db.Column('majorcd', db.String(20)),
    db.Column('grossamt', db.Numeric(16, 2), server_default=db.FetchedValue()),
    db.Column('rtnamt', db.Numeric(16, 2), server_default=db.FetchedValue()),
    db.Column('discamt', db.Numeric(16, 2), server_default=db.FetchedValue()),
    db.Column('netamt', db.Numeric(16, 2)),
    db.Column('hqgrossamt', db.Numeric(16, 2)),
    db.Column('hqrtnamt', db.Numeric(16, 2)),
    db.Column('hqdiscamt', db.Numeric(16, 2)),
    db.Column('hqnetamt', db.Numeric(16, 2)),
    db.Column('upddt', db.DateTime),
    db.Column('updby', db.String(20)),
    db.Column('rtndiscamt', db.Numeric(16, 2), server_default=db.FetchedValue()),
    db.Column('yearno', db.Integer),
    db.Column('monthno', db.Integer),
    db.Column('saleqty', db.Numeric(20, 2)),
    db.Index('idx_sale_major_1', 'deptid', 'bizdt')
)


t_rpt_saleplu = db.Table(
    'rpt_saleplu',
    db.Column('deptid', db.Integer, nullable=False),
    db.Column('bizdt', db.DateTime, nullable=False),
    db.Column('pluid', db.Integer, nullable=False),
    db.Column('saleqty', db.Integer, server_default=db.FetchedValue()),
    db.Column('rtnqty', db.Integer, server_default=db.FetchedValue()),
    db.Column('cnlqty', db.Integer, server_default=db.FetchedValue()),
    db.Column('slprc', db.Numeric(19, 4), server_default=db.FetchedValue()),
    db.Column('netamt', db.Numeric(19, 4), server_default=db.FetchedValue()),
    db.Column('rtnamt', db.Numeric(19, 4), server_default=db.FetchedValue()),
    db.Column('discamt', db.Numeric(19, 4), server_default=db.FetchedValue()),
    db.Column('grossamt', db.Numeric(19, 4), server_default=db.FetchedValue()),
    db.Column('rtndiscamt', db.Numeric(19, 4), server_default=db.FetchedValue()),
    db.Column('yearno', db.Integer),
    db.Column('monthno', db.Integer),
    db.Index('idx_rpt_saleplu1', 'deptid', 'bizdt')
)


t_rpt_saleplumth = db.Table(
    'rpt_saleplumth',
    db.Column('deptid', db.Integer, nullable=False),
    db.Column('bizdt', db.DateTime, nullable=False),
    db.Column('pluid', db.Integer, nullable=False),
    db.Column('saleqty', db.Integer, server_default=db.FetchedValue()),
    db.Column('rtnqty', db.Integer, server_default=db.FetchedValue()),
    db.Column('cnlqty', db.Integer, server_default=db.FetchedValue()),
    db.Column('slprc', db.Numeric(19, 4), server_default=db.FetchedValue()),
    db.Column('netamt', db.Numeric(19, 4), server_default=db.FetchedValue()),
    db.Column('rtnamt', db.Numeric(19, 4), server_default=db.FetchedValue()),
    db.Column('discamt', db.Numeric(19, 4), server_default=db.FetchedValue()),
    db.Column('grossamt', db.Numeric(19, 4), server_default=db.FetchedValue()),
    db.Column('rtndiscamt', db.Numeric(19, 4), server_default=db.FetchedValue()),
    db.Column('yearno', db.Integer),
    db.Column('monthno', db.Integer)
)


t_rpt_shift = db.Table(
    'rpt_shift',
    db.Column('deptid', db.Integer, nullable=False),
    db.Column('bizdt', db.DateTime, nullable=False),
    db.Column('userid', db.Integer, nullable=False),
    db.Column('grossamt', db.Numeric(16, 2), server_default=db.FetchedValue()),
    db.Column('salecnt', db.Integer, server_default=db.FetchedValue()),
    db.Column('cnlcnt', db.Integer, server_default=db.FetchedValue()),
    db.Column('rtncnt', db.Integer, server_default=db.FetchedValue()),
    db.Column('rtnamt', db.Numeric(16, 2), server_default=db.FetchedValue()),
    db.Column('shortcnt', db.Integer, server_default=db.FetchedValue()),
    db.Column('shortamt', db.Numeric(16, 2)),
    db.Column('overcnt', db.Integer),
    db.Column('overamt', db.Integer),
    db.Column('netamt', db.Numeric(16, 2)),
    db.Column('shiftid', db.Numeric(12, 0, asdecimal=False), index=True),
    db.Column('calamt', db.Numeric(16, 2)),
    db.Column('ralamt', db.Numeric(16, 2)),
    db.Index('idx_rpt_shift', 'deptid', 'bizdt')
)


t_rpt_userdiscount = db.Table(
    'rpt_userdiscount',
    db.Column('ctrcode', db.Numeric(20, 0, asdecimal=False)),
    db.Column('transno', db.Numeric(20, 0, asdecimal=False)),
    db.Column('deptcd', db.String(20)),
    db.Column('bizdt', db.DateTime),
    db.Column('usercode', db.String(20)),
    db.Column('username', db.String(40)),
    db.Column('disccd', db.String(20)),
    db.Column('discname', db.String(50)),
    db.Column('pluid', db.Integer),
    db.Column('sal_qty', db.Numeric(19, 4)),
    db.Column('discount_amt', db.Numeric(19, 4)),
    db.Column('saldate', db.DateTime),
    db.Column('upddt', db.DateTime),
    db.Index('idx_rpt_userdiscount_bizdept', 'deptcd', 'bizdt')
)


t_sal08_msr_hex = db.Table(
    'sal08_msr_hex',
    db.Column('pid', db.String(50), nullable=False),
    db.Column('bizdt', db.DateTime, index=True),
    db.Column('cardnumber', db.String(50)),
    db.Column('net_no', db.String(20)),
    db.Column('inttransnum', db.Numeric(asdecimal=False)),
    db.Column('usercode', db.String(20)),
    db.Column('username', db.String(26)),
    db.Column('discountcode', db.String(20)),
    db.Column('discountname', db.String(50)),
    db.Column('item_no', db.String(20)),
    db.Column('item_name', db.String(50)),
    db.Column('sal_qty', db.Numeric(asdecimal=False)),
    db.Column('discount_amt', db.Numeric(asdecimal=False)),
    db.Column('saldate', db.DateTime),
    db.Column('processdate', db.DateTime),
    db.Column('update_date', db.DateTime, server_default=db.FetchedValue()),
    db.Index('sal08_idx', 'net_no', 'discountcode')
)


t_sal08_msr_hex_total = db.Table(
    'sal08_msr_hex_total',
    db.Column('bizdt', db.DateTime, index=True),
    db.Column('cardnumber', db.String(50)),
    db.Column('net_no', db.String(20)),
    db.Column('usercode', db.String(20)),
    db.Column('username', db.String(50)),
    db.Column('discountcode', db.String(20)),
    db.Column('discountname', db.String(255)),
    db.Column('hex_qty', db.Numeric(asdecimal=False)),
    db.Column('hexdisc_amt', db.Numeric(asdecimal=False)),
    db.Column('msr_qty', db.Numeric(asdecimal=False)),
    db.Column('gc_qty', db.Numeric(asdecimal=False)),
    db.Column('spcc_qty', db.Numeric(asdecimal=False)),
    db.Column('msrdisc_amt', db.Numeric(asdecimal=False)),
    db.Column('data_type', db.String(3)),
    db.Column('is_deff', db.String(1)),
    db.Column('update_date', db.DateTime, server_default=db.FetchedValue()),
    db.Column('deff_qty', db.Numeric(asdecimal=False))
)


t_sal08_msr_msr = db.Table(
    'sal08_msr_msr',
    db.Column('pid', db.String(50), nullable=False),
    db.Column('bizdt', db.DateTime),
    db.Column('cardnumber', db.String(50)),
    db.Column('net_no', db.String(20)),
    db.Column('transactionid', db.String(100)),
    db.Column('discountcode', db.String(20)),
    db.Column('discountname', db.String(255)),
    db.Column('sal_qty', db.Numeric(asdecimal=False)),
    db.Column('redeemeddatetime', db.DateTime),
    db.Column('earnedarea', db.String(50)),
    db.Column('update_date', db.DateTime, server_default=db.FetchedValue()),
    db.Index('sal08_msr_idx', 'net_no', 'discountcode')
)


t_sdata = db.Table(
    'sdata',
    db.Column('name', db.String(256))
)


t_se_discount_bag = db.Table(
    'se_discount_bag',
    db.Column('transno', db.Numeric(20, 0, asdecimal=False)),
    db.Column('ctrno', db.Numeric(20, 0, asdecimal=False)),
    db.Column('curqty', db.Numeric(20, 0, asdecimal=False))
)


t_se_discount_card = db.Table(
    'se_discount_card',
    db.Column('transno', db.Numeric(20, 0, asdecimal=False)),
    db.Column('ctrno', db.Numeric(20, 0, asdecimal=False))
)


t_se_rpt_salecat = db.Table(
    'se_rpt_salecat',
    db.Column('deptid', db.Numeric(20, 0, asdecimal=False)),
    db.Column('discamt', db.Numeric(20, 0, asdecimal=False)),
    db.Column('rtndiscamt', db.Numeric(20, 0, asdecimal=False))
)


class SfStaffView(db.Model):
    __tablename__ = 'sf_staff_view'

    staffno = db.Column(db.String(10), primary_key=True)
    staffname = db.Column(db.String(30), nullable=False)
    stafftitle = db.Column(db.String(2), nullable=False)
    isenable = db.Column(db.String(1), nullable=False)
    pwd = db.Column(db.String(100))
    updatedate = db.Column(db.DateTime, nullable=False)


class SfStorestaffView(db.Model):
    __tablename__ = 'sf_storestaff_view'

    storeno = db.Column(db.String(10), primary_key=True, nullable=False)
    staffno = db.Column(db.String(10), primary_key=True, nullable=False)
    updatedate = db.Column(db.DateTime, nullable=False)


t_snp_plan_table = db.Table(
    'snp_plan_table',
    db.Column('statement_id', db.String(30)),
    db.Column('plan_id', db.Numeric(asdecimal=False)),
    db.Column('timestamp', db.DateTime),
    db.Column('remarks', db.String(4000)),
    db.Column('operation', db.String(30)),
    db.Column('options', db.String(255)),
    db.Column('object_node', db.String(128)),
    db.Column('object_owner', db.String(30)),
    db.Column('object_name', db.String(30)),
    db.Column('object_alias', db.String(65)),
    db.Column('object_instance', db.Integer),
    db.Column('object_type', db.String(30)),
    db.Column('optimizer', db.String(255)),
    db.Column('search_columns', db.Numeric(asdecimal=False)),
    db.Column('id', db.Integer),
    db.Column('parent_id', db.Integer),
    db.Column('depth', db.Integer),
    db.Column('position', db.Integer),
    db.Column('cost', db.Integer),
    db.Column('cardinality', db.Integer),
    db.Column('bytes', db.Integer),
    db.Column('other_tag', db.String(255)),
    db.Column('partition_start', db.String(255)),
    db.Column('partition_stop', db.String(255)),
    db.Column('partition_id', db.Integer),
    db.Column('other', db.Text),
    db.Column('distribution', db.String(30)),
    db.Column('cpu_cost', db.Integer),
    db.Column('io_cost', db.Integer),
    db.Column('temp_space', db.Integer),
    db.Column('access_predicates', db.String(4000)),
    db.Column('filter_predicates', db.String(4000)),
    db.Column('projection', db.String(4000)),
    db.Column('time', db.Integer),
    db.Column('qblock_name', db.String(30))
)


class SpccShop(db.Model):
    __tablename__ = 'spcc_shop'

    shopno = db.Column(db.Unicode(10), primary_key=True)
    status = db.Column(db.Unicode(10), server_default=db.FetchedValue())


class StStoreareaplanView(db.Model):
    __tablename__ = 'st_storeareaplan_view'

    storeno = db.Column(db.String(10), primary_key=True, nullable=False)
    effdatefrom = db.Column(db.DateTime, primary_key=True, nullable=False)
    areatype = db.Column(db.String(20), nullable=False)
    areano = db.Column(db.String(20), nullable=False)
    newareano = db.Column(db.String(20), nullable=False)
    status = db.Column(db.String(3), primary_key=True, nullable=False)
    updatedate = db.Column(db.DateTime, nullable=False)


class StStoremView(db.Model):
    __tablename__ = 'st_storem_view'

    storeno = db.Column(db.String(10), primary_key=True)
    storename = db.Column(db.String(50), nullable=False)
    opendate = db.Column(db.DateTime, nullable=False)
    closedate = db.Column(db.DateTime, nullable=False)
    marketareano = db.Column(db.String(20), nullable=False)
    manageareano = db.Column(db.String(20), nullable=False)
    updatedate = db.Column(db.DateTime, nullable=False)
    city_code = db.Column(db.String(20))


t_starbuck_store = db.Table(
    'starbuck_store',
    db.Column('store', db.Unicode(255)),
    db.Column('extract_date', db.Unicode(255)),
    db.Column('source', db.Unicode(255))
)


t_stk_bomcostlist = db.Table(
    'stk_bomcostlist',
    db.Column('bomlistid', db.Numeric(14, 0, asdecimal=False)),
    db.Column('deptid', db.Integer, nullable=False),
    db.Column('pluid', db.Integer, nullable=False),
    db.Column('locid', db.Integer, nullable=False),
    db.Column('lotno', db.String(20)),
    db.Column('uomcd', db.String(6)),
    db.Column('qty', db.Numeric(16, 6), nullable=False),
    db.Column('crcd', db.String(3)),
    db.Column('prc', db.Numeric(16, 6), nullable=False),
    db.Column('prc1', db.Numeric(16, 6)),
    db.Column('txrt', db.Numeric(6, 2)),
    db.Column('upddt', db.DateTime)
)


t_stk_bominlist = db.Table(
    'stk_bominlist',
    db.Column('bomlistid', db.Numeric(14, 0, asdecimal=False), index=True),
    db.Column('deptid', db.Integer, nullable=False),
    db.Column('pluid', db.Integer, nullable=False),
    db.Column('locid', db.Integer, nullable=False),
    db.Column('lotno', db.String(20)),
    db.Column('uomcd', db.String(6)),
    db.Column('qty', db.Numeric(16, 6), nullable=False),
    db.Column('crcd', db.String(3)),
    db.Column('prc', db.Numeric(16, 6), nullable=False),
    db.Column('prc1', db.Numeric(16, 6)),
    db.Column('txrt', db.Numeric(6, 2)),
    db.Column('upddt', db.DateTime)
)


class StkBomlist(db.Model):
    __tablename__ = 'stk_bomlist'
    __table_args__ = (
        db.Index('idx_stk_bombd', 'stkdt', 'pluid'),
    )

    id = db.Column(db.Numeric(14, 0, asdecimal=False), primary_key=True)
    stktp = db.Column(db.String(3), nullable=False)
    stkdt = db.Column(db.DateTime)
    actdt = db.Column(db.DateTime)
    billid = db.Column(db.Numeric(14, 0, asdecimal=False), nullable=False)
    billdtlid = db.Column(db.Numeric(14, 0, asdecimal=False), nullable=False)
    billtp = db.Column(db.String(10), nullable=False)
    deptid = db.Column(db.Integer, nullable=False)
    opplktp = db.Column(db.String(1))
    opplkid = db.Column(db.Integer)
    pluid = db.Column(db.Integer, nullable=False, index=True)
    locid = db.Column(db.Integer, nullable=False)
    lotno = db.Column(db.String(20))
    uomcd = db.Column(db.String(6))
    qty = db.Column(db.Numeric(16, 6), nullable=False)
    crcd = db.Column(db.String(3))
    prc = db.Column(db.Numeric(16, 6), nullable=False)
    prc1 = db.Column(db.Numeric(16, 6))
    txrt = db.Column(db.Numeric(6, 2))
    upddt = db.Column(db.DateTime)
    sta = db.Column(db.String(3), nullable=False)
    billrsn = db.Column(db.String(20))


t_stk_chk13log = db.Table(
    'stk_chk13log',
    db.Column('deptid', db.Integer),
    db.Column('deptcd', db.String(20)),
    db.Column('deptnm', db.String(100)),
    db.Column('pluid', db.Integer),
    db.Column('plucd', db.String(20)),
    db.Column('plunm', db.String(100)),
    db.Column('bizdt', db.DateTime),
    db.Column('h1endqty', db.Numeric(16, 6)),
    db.Column('h1inqty', db.Numeric(16, 6)),
    db.Column('h1outqty', db.Numeric(16, 6)),
    db.Column('h3endqty', db.Numeric(16, 6)),
    db.Column('logtp', db.String(10), server_default=db.FetchedValue()),
    db.Column('stktp', db.String(10), server_default=db.FetchedValue())
)


t_stk_chkstk = db.Table(
    'stk_chkstk',
    db.Column('stkdt', db.DateTime, nullable=False),
    db.Column('stktp', db.String(6), nullable=False),
    db.Column('billtp', db.String(10)),
    db.Column('billid', db.Numeric(14, 0, asdecimal=False)),
    db.Column('deptid', db.Integer, nullable=False),
    db.Column('pluid', db.Integer),
    db.Column('locid', db.Integer),
    db.Column('lotno', db.String(20)),
    db.Column('uomcd', db.String(6)),
    db.Column('listqty', db.Numeric(18, 6)),
    db.Column('stkqty', db.Numeric(18, 6)),
    db.Column('upddt', db.DateTime),
    db.Column('rmk', db.String(255))
)


t_stk_chkstk_bak = db.Table(
    'stk_chkstk_bak',
    db.Column('stkdt', db.DateTime, nullable=False),
    db.Column('stktp', db.String(6), nullable=False),
    db.Column('billtp', db.String(10)),
    db.Column('billid', db.Numeric(14, 0, asdecimal=False)),
    db.Column('deptid', db.Integer, nullable=False),
    db.Column('pluid', db.Integer),
    db.Column('locid', db.Integer),
    db.Column('lotno', db.String(20)),
    db.Column('uomcd', db.String(6)),
    db.Column('listqty', db.Numeric(18, 6)),
    db.Column('stkqty', db.Numeric(18, 6)),
    db.Column('upddt', db.DateTime),
    db.Column('rmk', db.String(255))
)


t_stk_list = db.Table(
    'stk_list',
    db.Column('billdtlid', db.Numeric(14, 0, asdecimal=False), nullable=False),
    db.Column('stktp', db.String(3), nullable=False),
    db.Column('stkdt', db.DateTime, index=True),
    db.Column('actdt', db.DateTime),
    db.Column('billid', db.Numeric(14, 0, asdecimal=False), nullable=False),
    db.Column('billtp', db.String(10), nullable=False),
    db.Column('deptid', db.Integer, nullable=False),
    db.Column('opplktp', db.String(1)),
    db.Column('opplkid', db.Integer),
    db.Column('pluid', db.Integer, nullable=False),
    db.Column('locid', db.Integer, nullable=False),
    db.Column('lotno', db.String(20)),
    db.Column('uomcd', db.String(6)),
    db.Column('qty', db.Numeric(16, 6), nullable=False),
    db.Column('crcd', db.String(3)),
    db.Column('prc', db.Numeric(16, 6), nullable=False),
    db.Column('prc1', db.Numeric(16, 6)),
    db.Column('txrt', db.Numeric(6, 2)),
    db.Column('upddt', db.DateTime),
    db.Column('billrsn', db.String(20)),
    db.Index('idx_stklist1', 'deptid', 'stkdt')
)


t_stk_list_tmp = db.Table(
    'stk_list_tmp',
    db.Column('billdtlid', db.Numeric(14, 0, asdecimal=False), nullable=False),
    db.Column('stktp', db.String(3), nullable=False),
    db.Column('stkdt', db.DateTime),
    db.Column('actdt', db.DateTime),
    db.Column('billid', db.Numeric(14, 0, asdecimal=False), nullable=False),
    db.Column('billtp', db.String(10), nullable=False),
    db.Column('deptid', db.Integer, nullable=False),
    db.Column('opplktp', db.String(1)),
    db.Column('opplkid', db.Integer),
    db.Column('pluid', db.Integer, nullable=False),
    db.Column('locid', db.Integer, nullable=False),
    db.Column('lotno', db.String(20)),
    db.Column('uomcd', db.String(6)),
    db.Column('qty', db.Numeric(16, 6), nullable=False),
    db.Column('crcd', db.String(3)),
    db.Column('prc', db.Numeric(16, 6), nullable=False),
    db.Column('prc1', db.Numeric(16, 6)),
    db.Column('txrt', db.Numeric(6, 2)),
    db.Column('upddt', db.DateTime),
    db.Column('billrsn', db.String(20))
)


t_stk_month_fch01 = db.Table(
    'stk_month_fch01',
    db.Column('net_no', db.String(20), nullable=False),
    db.Column('net_name', db.String(250)),
    db.Column('work_area_fm', db.String(10)),
    db.Column('businessdate', db.DateTime),
    db.Column('itemcode', db.String(50)),
    db.Column('itemname', db.String(250)),
    db.Column('stk_name', db.String(50)),
    db.Column('qty', db.Float)
)


t_stk_month_fch02 = db.Table(
    'stk_month_fch02',
    db.Column('net_no', db.String(20), nullable=False),
    db.Column('net_name', db.String(50)),
    db.Column('work_area_fm', db.String(10)),
    db.Column('plu_no', db.String(10)),
    db.Column('sbi_code', db.String(20)),
    db.Column('plu_namechs', db.String(150)),
    db.Column('lock_qty', db.Numeric(18, 6)),
    db.Column('input_qty', db.Numeric(18, 6)),
    db.Column('end_qty', db.Numeric(18, 6)),
    db.Column('businessmonth', db.String(20), index=True)
)


t_stk_orderitem = db.Table(
    'stk_orderitem',
    db.Column('net_id', db.Integer),
    db.Column('plu_id', db.Integer),
    db.Column('business_date', db.DateTime),
    db.Column('radvord_qty', db.Numeric(14, 4), server_default=db.FetchedValue()),
    db.Column('radvmax_qty', db.Numeric(14, 4), server_default=db.FetchedValue()),
    db.Column('est_tp', db.String(1)),
    db.Column('update_date', db.DateTime, server_default=db.FetchedValue()),
    db.Index('idx_stk_orderitem', 'net_id', 'business_date')
)


t_stk_period = db.Table(
    'stk_period',
    db.Column('yearno', db.Integer, nullable=False),
    db.Column('monthno', db.Integer, nullable=False),
    db.Column('deptid', db.Integer, nullable=False),
    db.Column('pluid', db.Integer, nullable=False),
    db.Column('bgnqty', db.Numeric(16, 6)),
    db.Column('endqty', db.Numeric(16, 6)),
    db.Column('lqty1', db.Numeric(16, 6)),
    db.Column('lqty2', db.Numeric(16, 6)),
    db.Column('lqty3', db.Numeric(16, 6)),
    db.Column('lqty4', db.Numeric(16, 6)),
    db.Column('lqty5', db.Numeric(16, 6)),
    db.Column('lqty6', db.Numeric(16, 6)),
    db.Column('lqty7', db.Numeric(16, 6)),
    db.Column('lqty8', db.Numeric(16, 6)),
    db.Column('lqty9', db.Numeric(16, 6)),
    db.Column('lqty10', db.Numeric(16, 6)),
    db.Column('lqty11', db.Numeric(16, 6)),
    db.Column('lqty12', db.Numeric(16, 6)),
    db.Column('lqty13', db.Numeric(16, 6)),
    db.Column('lqty14', db.Numeric(16, 6)),
    db.Column('lqty15', db.Numeric(16, 6)),
    db.Column('lqty16', db.Numeric(16, 6)),
    db.Column('ptid', db.Integer),
    db.Index('idx_stk_period', 'ptid', 'deptid')
)


class StkPluqty(db.Model):
    __tablename__ = 'stk_pluqty'

    deptid = db.Column(db.Integer, primary_key=True, nullable=False, index=True)
    pluid = db.Column(db.Integer, primary_key=True, nullable=False)
    uomcd = db.Column(db.String(6))
    qty = db.Column(db.Numeric(16, 6), nullable=False)
    upddt = db.Column(db.DateTime)


t_stk_sallist = db.Table(
    'stk_sallist',
    db.Column('billdtlid', db.Numeric(14, 0, asdecimal=False), nullable=False),
    db.Column('stktp', db.String(3), nullable=False),
    db.Column('stkdt', db.DateTime),
    db.Column('actdt', db.DateTime),
    db.Column('billid', db.Numeric(14, 0, asdecimal=False), nullable=False),
    db.Column('billtp', db.String(10), nullable=False),
    db.Column('deptid', db.Integer, nullable=False),
    db.Column('opplktp', db.String(1)),
    db.Column('opplkid', db.Integer),
    db.Column('pluid', db.Integer, nullable=False),
    db.Column('locid', db.Integer, nullable=False),
    db.Column('lotno', db.String(20)),
    db.Column('uomcd', db.String(6)),
    db.Column('qty', db.Numeric(16, 6), nullable=False),
    db.Column('crcd', db.String(3)),
    db.Column('prc', db.Numeric(16, 6), nullable=False),
    db.Column('prc1', db.Numeric(16, 6)),
    db.Column('txrt', db.Numeric(6, 2)),
    db.Column('upddt', db.DateTime),
    db.Index('idx_deptpluid', 'deptid', 'pluid')
)


class StkSlouse(db.Model):
    __tablename__ = 'stk_slice'
    __table_args__ = (
        db.Index('idx_slice1', 'yearno', 'monthno', 'deptid'),
    )

    yearno = db.Column(db.Integer, primary_key=True, nullable=False)
    monthno = db.Column(db.Integer, primary_key=True, nullable=False)
    slicetp = db.Column(db.String(10), primary_key=True, nullable=False)
    deptid = db.Column(db.Integer, primary_key=True, nullable=False)
    pluid = db.Column(db.Integer, primary_key=True, nullable=False)
    locid = db.Column(db.Integer, primary_key=True, nullable=False)
    lotno = db.Column(db.String(20), primary_key=True, nullable=False)
    uomcd = db.Column(db.String(6))
    qty = db.Column(db.Numeric(16, 6), nullable=False)
    crcd = db.Column(db.String(3))
    prc = db.Column(db.Numeric(16, 6), nullable=False)
    txrt = db.Column(db.Numeric(6, 2))
    upddt = db.Column(db.DateTime)
    slicedt = db.Column(db.DateTime)


t_stk_slice_sun2018 = db.Table(
    'stk_slice_sun2018',
    db.Column('yearno', db.Integer, nullable=False),
    db.Column('monthno', db.Integer, nullable=False),
    db.Column('slicetp', db.String(10), nullable=False),
    db.Column('deptid', db.Integer, nullable=False),
    db.Column('pluid', db.Integer, nullable=False),
    db.Column('locid', db.Integer, nullable=False),
    db.Column('lotno', db.String(20), nullable=False),
    db.Column('uomcd', db.String(6)),
    db.Column('qty', db.Numeric(16, 6), nullable=False),
    db.Column('crcd', db.String(3)),
    db.Column('prc', db.Numeric(16, 6), nullable=False),
    db.Column('txrt', db.Numeric(6, 2)),
    db.Column('upddt', db.DateTime),
    db.Column('slicedt', db.DateTime)
)


t_stk_slice_suntest = db.Table(
    'stk_slice_suntest',
    db.Column('yearno', db.Integer, nullable=False),
    db.Column('monthno', db.Integer, nullable=False),
    db.Column('slicetp', db.String(10), nullable=False),
    db.Column('deptid', db.Integer, nullable=False),
    db.Column('pluid', db.Integer, nullable=False),
    db.Column('locid', db.Integer, nullable=False),
    db.Column('lotno', db.String(20), nullable=False),
    db.Column('uomcd', db.String(6)),
    db.Column('qty', db.Numeric(16, 6), nullable=False),
    db.Column('crcd', db.String(3)),
    db.Column('prc', db.Numeric(16, 6), nullable=False),
    db.Column('txrt', db.Numeric(6, 2)),
    db.Column('upddt', db.DateTime),
    db.Column('slicedt', db.DateTime)
)


t_stk_snapshotqty = db.Table(
    'stk_snapshotqty',
    db.Column('deptid', db.Integer, nullable=False),
    db.Column('pluid', db.Integer, nullable=False),
    db.Column('uomcd', db.String(6)),
    db.Column('totalqty', db.Numeric(16, 6), nullable=False),
    db.Column('lockqty', db.Numeric(16, 6), nullable=False),
    db.Column('qty', db.Numeric(16, 6), nullable=False),
    db.Column('upddt', db.DateTime)
)


t_stmp_fincostmp_sun2018 = db.Table(
    'stmp_fincostmp_sun2018',
    db.Column('ptid', db.Integer),
    db.Column('yearno', db.Integer),
    db.Column('monthno', db.Integer),
    db.Column('deptlktp', db.String(10)),
    db.Column('deptlkid', db.Integer),
    db.Column('pluid', db.Integer),
    db.Column('bgnqty', db.Numeric(18, 6)),
    db.Column('bgncost', db.Numeric(18, 6)),
    db.Column('bgnamt', db.Numeric(18, 6)),
    db.Column('purqty', db.Numeric(18, 6)),
    db.Column('puramt', db.Numeric(18, 6)),
    db.Column('feeamt', db.Numeric(18, 6)),
    db.Column('invadjamt', db.Numeric(18, 6)),
    db.Column('puradjamt', db.Numeric(18, 6)),
    db.Column('txoqty', db.Numeric(18, 6)),
    db.Column('txiqty', db.Numeric(18, 6)),
    db.Column('adjqty', db.Numeric(18, 6)),
    db.Column('bomoutqty', db.Numeric(18, 6)),
    db.Column('bomcsamt', db.Numeric(20, 6)),
    db.Column('bomprcinqty', db.Numeric(18, 6)),
    db.Column('saleqty', db.Numeric(18, 6)),
    db.Column('dlvqty', db.Numeric(18, 6)),
    db.Column('rcvqty', db.Numeric(18, 6)),
    db.Column('invqty', db.Numeric(18, 6)),
    db.Column('endqty', db.Numeric(18, 6)),
    db.Column('endcost', db.Numeric(18, 6)),
    db.Column('endamt', db.Numeric(18, 6)),
    db.Column('enddtqty', db.Numeric(18, 6)),
    db.Column('enddtamt', db.Numeric(18, 6)),
    db.Column('defqty', db.Numeric(18, 6)),
    db.Column('defamt', db.Numeric(18, 6)),
    db.Column('estprc', db.Numeric(20, 6)),
    db.Column('accendamt', db.Numeric(18, 6)),
    db.Column('sta', db.String(3)),
    db.Column('bomadjinqty', db.Numeric(18, 6)),
    db.Column('bomsaleinqty', db.Numeric(18, 6))
)


t_stmp_slicestk_sun2018 = db.Table(
    'stmp_slicestk_sun2018',
    db.Column('deptid', db.Integer, nullable=False),
    db.Column('pluid', db.Integer, nullable=False),
    db.Column('locid', db.Integer, nullable=False),
    db.Column('lotno', db.String(20)),
    db.Column('qty', db.Numeric(16, 6))
)


t_stp_userdept = db.Table(
    'stp_userdept',
    db.Column('userid', db.Integer, nullable=False, index=True),
    db.Column('deptid', db.Integer),
    db.Column('pid', db.Integer),
    db.Column('lvl', db.Integer),
    db.Column('pth', db.String(100)),
    db.Column('flag', db.String(1)),
    db.Column('upddt', db.DateTime)
)


t_syn_accmaping = db.Table(
    'syn_accmaping',
    db.Column('hex1cd', db.String(20)),
    db.Column('hex1name', db.String(100)),
    db.Column('hex3cd', db.String(20)),
    db.Column('hex3name', db.String(1000))
)


t_syn_accmaping3t1 = db.Table(
    'syn_accmaping3t1',
    db.Column('hex1cd', db.String(20)),
    db.Column('hex1name', db.String(100)),
    db.Column('hex3cd', db.String(20)),
    db.Column('hex3name', db.String(1000))
)


t_syn_adj = db.Table(
    'syn_adj',
    db.Column('adjgid', db.String(50)),
    db.Column('adjid', db.Numeric(12, 0, asdecimal=False), index=True),
    db.Column('sta', db.String(1), index=True),
    db.Column('syndate', db.DateTime)
)


t_syn_dal = db.Table(
    'syn_dal',
    db.Column('dalid', db.Numeric(12, 0, asdecimal=False), index=True),
    db.Column('syndate', db.DateTime),
    db.Column('sta', db.String(1), index=True)
)


t_syn_dalhq = db.Table(
    'syn_dalhq',
    db.Column('dalid', db.Numeric(12, 0, asdecimal=False), index=True),
    db.Column('syndate', db.DateTime),
    db.Column('sta', db.String(3)),
    db.Column('upddate', db.DateTime, index=True)
)


t_syn_hq_pur = db.Table(
    'syn_hq_pur',
    db.Column('id', db.Numeric(13, 0, asdecimal=False), index=True),
    db.Column('gid', db.String(50), index=True),
    db.Column('hex3update', db.DateTime),
    db.Column('synflg', db.String(1)),
    db.Column('syndata', db.DateTime),
    db.Column('he1upddt', db.DateTime, index=True),
    db.Column('tp', db.String(1), server_default=db.FetchedValue()),
    db.Column('sta', db.String(1)),
    db.Column('status', db.String(1)),
    db.Column('upddt', db.DateTime)
)


t_syn_hqdlv = db.Table(
    'syn_hqdlv',
    db.Column('gid', db.String(50), index=True),
    db.Column('id', db.Integer, index=True),
    db.Column('sta', db.String(1), index=True),
    db.Column('syndate', db.DateTime),
    db.Column('billtp', db.String(10))
)


t_syn_inv = db.Table(
    'syn_inv',
    db.Column('stocktakecode', db.String(20)),
    db.Column('tohex3', db.String(1)),
    db.Column('tohex3dt', db.DateTime),
    db.Column('tohex1', db.String(1)),
    db.Column('tohex1dt', db.DateTime),
    db.Column('invid', db.Numeric(20, 0, asdecimal=False)),
    db.Column('sta1', db.String(3)),
    db.Column('sta30', db.String(3)),
    db.Column('synflg', db.String(1)),
    db.Column('gid', db.String(50)),
    db.Column('sta31', db.String(3), server_default=db.FetchedValue()),
    db.Index('idx_syn_inv_syndt', 'tohex3dt', 'tohex1dt')
)


t_syn_invoice = db.Table(
    'syn_invoice',
    db.Column('pid', db.String(50)),
    db.Column('invoicecd', db.Numeric(12, 0, asdecimal=False)),
    db.Column('syndate', db.DateTime),
    db.Column('synflg', db.String(1))
)


t_syn_ord = db.Table(
    'syn_ord',
    db.Column('bizdt', db.DateTime),
    db.Column('syndt', db.DateTime),
    db.Column('typ', db.String(1))
)


t_syn_rcv = db.Table(
    'syn_rcv',
    db.Column('goodrev_no', db.String(20), index=True),
    db.Column('bizdt', db.DateTime, index=True),
    db.Column('ven_cd', db.String(20)),
    db.Column('dept_cd', db.String(20)),
    db.Column('rcvid', db.Numeric(12, 0, asdecimal=False)),
    db.Column('sta', db.String(1), index=True),
    db.Column('orddt', db.DateTime),
    db.Column('syn_date', db.DateTime),
    db.Column('dc_cd', db.String(20)),
    db.Column('so', db.String(20)),
    db.Column('dstp', db.String(1)),
    db.Column('status', db.String(1)),
    db.Column('pid', db.String(50)),
    db.Column('upddt', db.DateTime),
    db.Column('po', db.String(20))
)


t_syn_rcv1 = db.Table(
    'syn_rcv1',
    db.Column('goodrev_no', db.String(20), index=True),
    db.Column('bizdt', db.DateTime, index=True),
    db.Column('ven_cd', db.String(20)),
    db.Column('dept_cd', db.String(20)),
    db.Column('rcvid', db.Numeric(12, 0, asdecimal=False)),
    db.Column('sta', db.String(1), index=True),
    db.Column('orddt', db.DateTime),
    db.Column('syn_date', db.DateTime),
    db.Column('dc_cd', db.String(20)),
    db.Column('so', db.String(20)),
    db.Column('dstp', db.String(1)),
    db.Column('status', db.String(1)),
    db.Column('pid', db.String(50)),
    db.Column('upddt', db.DateTime)
)


t_syn_rvr = db.Table(
    'syn_rvr',
    db.Column('purid', db.Numeric(12, 0, asdecimal=False), index=True),
    db.Column('plucd', db.String(20)),
    db.Column('rvrguid', db.String(50), index=True),
    db.Column('syndate', db.DateTime),
    db.Column('sta', db.String(1), index=True),
    db.Column('realqty', db.Numeric(20, 4)),
    db.Column('stkqty', db.Numeric(20, 4)),
    db.Column('dtlid', db.Numeric(12, 0, asdecimal=False), index=True),
    db.Column('typ', db.String(1)),
    db.Column('vencd', db.String(20)),
    db.Column('deptcd', db.String(20)),
    db.Column('bizdt', db.DateTime),
    db.Column('rzncd', db.String(50)),
    db.Column('rcvid', db.Numeric(12, 0, asdecimal=False)),
    db.Column('so', db.String(20)),
    db.Column('sta2', db.String(1), index=True, server_default=db.FetchedValue()),
    db.Column('syndate2', db.DateTime),
    db.Column('rmk', db.String(100)),
    db.Column('sta3', db.String(3))
)


t_syn_rvr1 = db.Table(
    'syn_rvr1',
    db.Column('purid', db.Numeric(12, 0, asdecimal=False)),
    db.Column('plucd', db.String(20)),
    db.Column('rvrguid', db.String(50)),
    db.Column('syndate', db.DateTime),
    db.Column('sta', db.String(1)),
    db.Column('realqty', db.Numeric(20, 4)),
    db.Column('stkqty', db.Numeric(20, 4)),
    db.Column('dtlid', db.Numeric(12, 0, asdecimal=False)),
    db.Column('typ', db.String(1)),
    db.Column('vencd', db.String(20)),
    db.Column('deptcd', db.String(20)),
    db.Column('bizdt', db.DateTime),
    db.Column('rzncd', db.String(50)),
    db.Column('rcvid', db.Numeric(12, 0, asdecimal=False)),
    db.Column('so', db.String(20)),
    db.Column('sta2', db.String(1), server_default=db.FetchedValue()),
    db.Column('syndate2', db.DateTime),
    db.Column('rmk', db.String(100)),
    db.Column('sta3', db.String(3))
)


t_syn_rvrin = db.Table(
    'syn_rvrin',
    db.Column('pid', db.String(50), index=True),
    db.Column('rvr_no', db.Integer),
    db.Column('bizdt', db.DateTime),
    db.Column('deptcd', db.String(10)),
    db.Column('plucd', db.String(10)),
    db.Column('sqty', db.Numeric(20, 4)),
    db.Column('rqt', db.Numeric(20, 4)),
    db.Column('status', db.String(1)),
    db.Column('rvrrsn', db.String(10)),
    db.Column('rcvid', db.Numeric(11, 0, asdecimal=False)),
    db.Column('venno', db.String(20)),
    db.Column('upddt', db.DateTime, index=True),
    db.Column('synfg', db.String(1), server_default=db.FetchedValue())
)


t_syn_sopo = db.Table(
    'syn_sopo',
    db.Column('purid', db.Numeric(13, 0, asdecimal=False)),
    db.Column('po', db.String(50)),
    db.Column('so', db.String(50)),
    db.Column('tp', db.String(1)),
    db.Column('pid', db.String(100))
)


t_syn_sopo1 = db.Table(
    'syn_sopo1',
    db.Column('purid', db.Numeric(13, 0, asdecimal=False)),
    db.Column('po', db.String(50)),
    db.Column('so', db.String(50)),
    db.Column('tp', db.String(1), index=True),
    db.Column('pid', db.String(150))
)


t_syn_stk = db.Table(
    'syn_stk',
    db.Column('deptcd', db.String(20)),
    db.Column('plucd', db.String(20)),
    db.Column('stkqty', db.Numeric(14, 2)),
    db.Column('bizdt', db.DateTime)
)


t_syn_transfer = db.Table(
    'syn_transfer',
    db.Column('transgid', db.String(50)),
    db.Column('transno', db.Numeric(20, 0, asdecimal=False)),
    db.Column('transtyp', db.String(1)),
    db.Column('syndate', db.DateTime, index=True),
    db.Column('isaccept', db.String(1))
)


class SysBatchcfg(db.Model):
    __tablename__ = 'sys_batchcfg'

    batchcfgcd = db.Column(db.String(20), primary_key=True)
    batchcfgdsc = db.Column(db.String(50))
    batchtp = db.Column(db.String(20))
    batchno = db.Column(db.Integer)
    bizdt = db.Column(db.DateTime)
    stdtpoint = db.Column(db.Integer)
    sttmpoint = db.Column(db.String(8))
    eddtpoint = db.Column(db.Integer)
    edtmpoint = db.Column(db.String(8))
    batchsta = db.Column(db.String(3))
    updby = db.Column(db.String(20))
    upddt = db.Column(db.DateTime)
    rmk = db.Column(db.String(100))
    sta = db.Column(db.String(3))


class SysBillidcfg(db.Model):
    __tablename__ = 'sys_billidcfg'

    id = db.Column(db.Integer, primary_key=True)
    tbnm = db.Column(db.String(30), nullable=False)
    buildrule = db.Column(db.String(10), server_default=db.FetchedValue())
    funcnm = db.Column(db.String(30))
    fmtflg = db.Column(db.String(1), server_default=db.FetchedValue())
    dtfmprefix = db.Column(db.String(10))
    seqlen = db.Column(db.Integer, server_default=db.FetchedValue())
    curseq = db.Column(db.Numeric(10, 0, asdecimal=False), server_default=db.FetchedValue())
    curdtfmt = db.Column(db.String(10))
    rmk = db.Column(db.String(255))
    updby = db.Column(db.String(20))
    upddt = db.Column(db.DateTime)
    sta = db.Column(db.String(3), nullable=False)


class SysCachecfg(db.Model):
    __tablename__ = 'sys_cachecfg'

    id = db.Column(db.Integer, primary_key=True)
    tp = db.Column(db.String(10))
    cd = db.Column(db.String(20))
    nm_l_zh = db.Column(db.Unicode(50), nullable=False)
    nm_l_en = db.Column(db.Unicode(50))
    nm_l_ja = db.Column(db.Unicode(50))
    cacheflg = db.Column(db.String(1), server_default=db.FetchedValue())
    rmk = db.Column(db.Unicode(255))
    updby = db.Column(db.String(20))
    upddt = db.Column(db.DateTime)
    sta = db.Column(db.String(3), nullable=False)


t_sys_cachelog = db.Table(
    'sys_cachelog',
    db.Column('apnm', db.String(50)),
    db.Column('cfgid', db.Integer),
    db.Column('updby', db.String(20)),
    db.Column('upddt', db.DateTime),
    db.Column('sta', db.String(3), nullable=False)
)


t_sys_check_log = db.Table(
    'sys_check_log',
    db.Column('logcd', db.String(100)),
    db.Column('logdsc', db.String(100)),
    db.Column('logrmk', db.String(400)),
    db.Column('sta', db.String(3), index=True, server_default=db.FetchedValue()),
    db.Column('upddt', db.DateTime, index=True),
    db.Column('lkcd', db.String(100))
)


class SysCompany(db.Model):
    __tablename__ = 'sys_company'

    id = db.Column(db.Integer, primary_key=True)
    cd = db.Column(db.String(20))
    secondcd = db.Column(db.String(20), nullable=False)
    nm_l_zh = db.Column(db.Unicode(50), nullable=False)
    nm_l_en = db.Column(db.Unicode(50))
    nm_l_ja = db.Column(db.Unicode(50))
    fjstdt = db.Column(db.DateTime, nullable=False)
    pnc = db.Column(db.Integer)
    arfjstdt = db.Column(db.DateTime)
    arpnc = db.Column(db.Integer)
    apfjstdt = db.Column(db.DateTime)
    appnc = db.Column(db.Integer)
    taxcd = db.Column(db.String(30))
    bizcd = db.Column(db.String(20))
    cp = db.Column(db.Unicode(30))
    lr = db.Column(db.Unicode(30))
    invaddr = db.Column(db.Unicode(100))
    invzipcd = db.Column(db.String(20))
    coaddr = db.Column(db.Unicode(100))
    cozipcd = db.Column(db.Unicode(20))
    country = db.Column(db.Unicode(20))
    province = db.Column(db.Unicode(20))
    city = db.Column(db.Unicode(20))
    officetel = db.Column(db.String(30))
    officefax = db.Column(db.String(30))
    crcd = db.Column(db.String(3))
    taxa = db.Column(db.String(20))
    taxrt = db.Column(db.Numeric(6, 2))
    banknm = db.Column(db.Unicode(50))
    bankaccount = db.Column(db.String(30))
    rmk = db.Column(db.Unicode(255))
    updby = db.Column(db.String(20))
    upddt = db.Column(db.DateTime)
    sta = db.Column(db.String(3), nullable=False)
    bankid = db.Column(db.Integer)


class SysCompcfg(db.Model):
    __tablename__ = 'sys_compcfg'

    id = db.Column(db.Integer, primary_key=True)
    moduleid = db.Column(db.Integer)
    ctrlid = db.Column(db.String(80))
    ctrltp = db.Column(db.String(20))
    nm_l_zh = db.Column(db.Unicode(50))
    nm_l_en = db.Column(db.Unicode(50))
    nm_l_ja = db.Column(db.Unicode(50))
    hidemode = db.Column(db.String(10))
    cols = db.Column(db.String(40))
    usernm = db.Column(db.String(20))
    meta1 = db.Column(db.String(50))
    meta2 = db.Column(db.String(50))
    meta3 = db.Column(db.String(50))
    updby = db.Column(db.String(20))
    upddt = db.Column(db.DateTime)
    sta = db.Column(db.String(3), nullable=False)


class SysCompcfgmbr(db.Model):
    __tablename__ = 'sys_compcfgmbr'

    id = db.Column(db.Integer, primary_key=True)
    compcfgid = db.Column(db.Integer)
    ctrlnm = db.Column(db.Unicode(30))
    ctrltp = db.Column(db.Unicode(20))
    ordseq = db.Column(db.Integer)
    pctrlnm = db.Column(db.Unicode(30))
    attrcaption = db.Column(db.Unicode(50))
    attrwidth = db.Column(db.Unicode(10))
    attrcolspan = db.Column(db.Integer)
    attrrowspan = db.Column(db.Integer)
    attrvisible = db.Column(db.Unicode(2))
    updby = db.Column(db.String(20))
    upddt = db.Column(db.DateTime)
    sta = db.Column(db.String(3), nullable=False)


class SysCompre(db.Model):
    __tablename__ = 'sys_compres'

    id = db.Column(db.Integer, primary_key=True)
    menuid = db.Column(db.Integer)
    moduleid = db.Column(db.Integer)
    comptp = db.Column(db.String(20), nullable=False)
    chgnmflg = db.Column(db.String(1), server_default=db.FetchedValue())
    nm_l_zh = db.Column(db.Unicode(50))
    nm_l_en = db.Column(db.Unicode(50))
    nm_l_ja = db.Column(db.Unicode(50))
    param = db.Column(db.String(50))
    url = db.Column(db.String(100))
    updby = db.Column(db.String(20))
    upddt = db.Column(db.DateTime)
    sta = db.Column(db.String(3))


class SysCustomsearch(db.Model):
    __tablename__ = 'sys_customsearch'

    id = db.Column(db.Integer, primary_key=True)
    moduleid = db.Column(db.Integer)
    gridid = db.Column(db.String(100))
    ordseq = db.Column(db.Integer)
    fieldnm = db.Column(db.String(50))
    lb_l_zh = db.Column(db.Unicode(50))
    lb_l_en = db.Column(db.Unicode(50))
    lb_l_ja = db.Column(db.Unicode(50))
    tp = db.Column(db.String(50))
    opr = db.Column(db.String(10))
    reqflg = db.Column(db.String(1), server_default=db.FetchedValue())
    dftval = db.Column(db.String(50))
    dftsort = db.Column(db.String(10))
    trgid = db.Column(db.String(50))
    usernm = db.Column(db.String(20))
    updby = db.Column(db.String(20))
    upddt = db.Column(db.DateTime)
    sta = db.Column(db.String(3), nullable=False)


t_sys_data_move_cfg = db.Table(
    'sys_data_move_cfg',
    db.Column('pid', db.String(50), server_default=db.FetchedValue()),
    db.Column('mst_table', db.String(50)),
    db.Column('dtl_table', db.String(50)),
    db.Column('his_table_typ', db.String(1)),
    db.Column('dtl_fk', db.String(50)),
    db.Column('mst_pk', db.String(50)),
    db.Column('save_days', db.Integer),
    db.Column('step', db.Integer),
    db.Column('businessdate', db.DateTime),
    db.Column('task_name', db.String(50)),
    db.Column('date_field', db.String(50)),
    db.Column('where_df', db.String(150)),
    db.Column('is_delete', db.String(1), server_default=db.FetchedValue()),
    db.Column('update_date', db.DateTime),
    db.Column('db_user', db.String(50)),
    db.Column('group_dsc', db.String(50)),
    db.Column('is_varchar', db.String(1), server_default=db.FetchedValue()),
    db.Column('where_df_mst_insert', db.String(100)),
    db.Column('where_df_dtl_insert', db.String(100)),
    db.Column('sn', db.Integer),
    db.Column('excesqltxt', db.String(2000)),
    db.Column('dtl_only', db.String(1), server_default=db.FetchedValue())
)


t_sys_data_move_lg = db.Table(
    'sys_data_move_lg',
    db.Column('pid', db.String(100), server_default=db.FetchedValue()),
    db.Column('task_pid', db.String(100)),
    db.Column('businessdate', db.DateTime),
    db.Column('bcreate_date', db.DateTime, server_default=db.FetchedValue()),
    db.Column('dsc', db.String(200)),
    db.Column('is_err', db.String(2), server_default=db.FetchedValue()),
    db.Column('ecreate_date', db.DateTime, server_default=db.FetchedValue()),
    db.Column('dsc_sql', db.String(1000))
)


class SysDataauth(db.Model):
    __tablename__ = 'sys_dataauth'

    id = db.Column(db.Integer, primary_key=True)
    domainnm = db.Column(db.String(200))
    fieldnm = db.Column(db.String(200), nullable=False)
    condexp = db.Column(db.String(5), nullable=False)
    value = db.Column(db.String(250), nullable=False)
    rmk = db.Column(db.String(200))
    updby = db.Column(db.String(20))
    upddt = db.Column(db.DateTime)
    sta = db.Column(db.String(3))


class SysDataitem(db.Model):
    __tablename__ = 'sys_dataitem'

    id = db.Column(db.Integer, primary_key=True)
    dsid = db.Column(db.Integer, nullable=False)
    colnm = db.Column(db.String(30), nullable=False)
    condnm = db.Column(db.String(30))
    lb_l_zh = db.Column(db.Unicode(50))
    lb_l_en = db.Column(db.Unicode(50))
    lb_l_ja = db.Column(db.Unicode(50))
    datatp = db.Column(db.String(20))
    disfmt = db.Column(db.String(30))
    ordseq = db.Column(db.Integer, server_default=db.FetchedValue())
    disflg = db.Column(db.String(1), server_default=db.FetchedValue())
    qryflg = db.Column(db.String(1))
    condmark = db.Column(db.String(30))
    colwidth = db.Column(db.Integer, server_default=db.FetchedValue())
    mappingtp = db.Column(db.String(10))
    mappingcd = db.Column(db.String(30))
    updby = db.Column(db.String(20))
    upddt = db.Column(db.DateTime)
    sta = db.Column(db.String(3), nullable=False)


class SysDataset(db.Model):
    __tablename__ = 'sys_dataset'

    id = db.Column(db.Integer, primary_key=True)
    lktp = db.Column(db.String(1))
    lkid = db.Column(db.Integer)
    cd = db.Column(db.String(50))
    tp = db.Column(db.String(10))
    pid = db.Column(db.Integer)
    fknm = db.Column(db.String(100))
    lvl = db.Column(db.Integer)
    pth = db.Column(db.String(200))
    leafflg = db.Column(db.String(1), server_default=db.FetchedValue())
    nm_l_zh = db.Column(db.Unicode(50), nullable=False)
    nm_l_en = db.Column(db.Unicode(50))
    nm_l_ja = db.Column(db.Unicode(50))
    queryby = db.Column(db.String(2000))
    filterby = db.Column(db.String(1000))
    groupby = db.Column(db.String(500))
    orderby = db.Column(db.String(500))
    lazyflg = db.Column(db.String(1), server_default=db.FetchedValue())
    ordseq = db.Column(db.Integer)
    pageflg = db.Column(db.String(1), server_default=db.FetchedValue())
    updby = db.Column(db.String(20))
    upddt = db.Column(db.DateTime)
    sta = db.Column(db.String(3), nullable=False)


class SysDept(db.Model):
    __tablename__ = 'sys_dept'
    __table_args__ = (
        db.Index('idx_sys_dept_02', 'cd', 'adminby', 'id'),
    )

    id = db.Column(db.Integer, primary_key=True)
    cd = db.Column(db.String(20), nullable=False)
    nm_l_zh = db.Column(db.Unicode(50), nullable=False)
    nm_l_en = db.Column(db.Unicode(50))
    nm_l_ja = db.Column(db.Unicode(50))
    coid = db.Column(db.Integer, nullable=False)
    adminby = db.Column(db.String(50))
    pid = db.Column(db.Integer)
    secondcd = db.Column(db.String(20))
    tp = db.Column(db.String(20))
    subtp = db.Column(db.String(20))
    roundtp = db.Column(db.String(20))
    brand = db.Column(db.String(20))
    lvl = db.Column(db.Integer)
    pth = db.Column(db.String(200), index=True)
    leafflg = db.Column(db.String(1), server_default=db.FetchedValue())
    plutplid = db.Column(db.Integer)
    potplid = db.Column(db.Integer)
    bomtplid = db.Column(db.Integer)
    costtplid = db.Column(db.Integer)
    mkttplid = db.Column(db.Integer)
    istplid = db.Column(db.Integer)
    dlvtplid = db.Column(db.Integer)
    accttplid = db.Column(db.Integer)
    svrtplid = db.Column(db.Integer)
    prntplid = db.Column(db.Integer)
    tdrtplid = db.Column(db.Integer)
    scrtplid = db.Column(db.Integer)
    prtplid = db.Column(db.Integer)
    shoptp1 = db.Column(db.String(10))
    shoptp2 = db.Column(db.String(10))
    cbdtp1 = db.Column(db.String(10))
    cbdtp2 = db.Column(db.String(10))
    area = db.Column(db.Numeric(8, 2))
    tablecnt = db.Column(db.Integer)
    renttp = db.Column(db.String(20))
    rentfee = db.Column(db.Numeric(14, 2))
    stdt = db.Column(db.DateTime)
    eddt = db.Column(db.DateTime)
    menutp = db.Column(db.String(10))
    ordcldflg = db.Column(db.String(1), server_default=db.FetchedValue())
    locflg = db.Column(db.String(1), server_default=db.FetchedValue())
    lotflg = db.Column(db.String(1), server_default=db.FetchedValue())
    saftamt = db.Column(db.Numeric(16, 2))
    taxcd = db.Column(db.String(30))
    bizcd = db.Column(db.Unicode(20))
    cp = db.Column(db.Unicode(30))
    lr = db.Column(db.Unicode(30))
    invaddr = db.Column(db.Unicode(100))
    invzipcd = db.Column(db.String(20))
    coaddr = db.Column(db.Unicode(100))
    cozipcd = db.Column(db.String(20))
    country = db.Column(db.Unicode(20))
    province = db.Column(db.Unicode(20))
    city = db.Column(db.Unicode(20))
    officetel = db.Column(db.String(30))
    officefax = db.Column(db.String(30))
    email = db.Column(db.String(32))
    crcd = db.Column(db.String(3))
    taxa = db.Column(db.String(20))
    taxrt = db.Column(db.Numeric(6, 2))
    bankid = db.Column(db.Integer)
    banknm = db.Column(db.Unicode(50))
    bankaccount = db.Column(db.String(30))
    exattr1 = db.Column(db.String(100))
    exattr2 = db.Column(db.String(100))
    exattr3 = db.Column(db.String(100))
    exattr4 = db.Column(db.String(100))
    exattr5 = db.Column(db.String(100))
    exattr6 = db.Column(db.String(100))
    exattr7 = db.Column(db.String(100))
    exattr8 = db.Column(db.String(100))
    exattr9 = db.Column(db.String(100))
    exattr10 = db.Column(db.String(100))
    exattr11 = db.Column(db.String(100))
    exattr12 = db.Column(db.String(100))
    exattr13 = db.Column(db.String(100))
    exattr14 = db.Column(db.String(100))
    exattr15 = db.Column(db.String(100))
    exattr16 = db.Column(db.String(100))
    exattr17 = db.Column(db.String(100))
    exattr18 = db.Column(db.String(100))
    exattr19 = db.Column(db.String(100))
    exattr20 = db.Column(db.String(100))
    exattr21 = db.Column(db.String(100))
    exattr22 = db.Column(db.String(100))
    exattr23 = db.Column(db.String(100))
    exattr24 = db.Column(db.String(100))
    exattr25 = db.Column(db.String(100))
    exattr26 = db.Column(db.String(100))
    exattr27 = db.Column(db.String(100))
    exattr28 = db.Column(db.String(100))
    exattr29 = db.Column(db.String(100))
    exattr30 = db.Column(db.String(100))
    rmk = db.Column(db.Unicode(200))
    updby = db.Column(db.String(20))
    upddt = db.Column(db.DateTime)
    sta = db.Column(db.String(3), nullable=False)
    execflg = db.Column(db.String(1), server_default=db.FetchedValue())
    nxtsta = db.Column(db.String(3))
    exattr31 = db.Column(db.String(100))
    exattr32 = db.Column(db.String(100))
    exattr33 = db.Column(db.String(100))
    exattr34 = db.Column(db.String(100))
    exattr35 = db.Column(db.String(100))
    exattr36 = db.Column(db.String(100))
    exattr37 = db.Column(db.String(100))
    exattr38 = db.Column(db.String(100))
    exattr39 = db.Column(db.String(100))
    exattr40 = db.Column(db.String(100))
    exattr41 = db.Column(db.String(100))
    exattr42 = db.Column(db.String(100))
    exattr43 = db.Column(db.String(100))
    exattr44 = db.Column(db.String(100))
    exattr45 = db.Column(db.String(100))
    exattr46 = db.Column(db.String(100))
    exattr47 = db.Column(db.String(100))
    exattr48 = db.Column(db.String(100))
    exattr49 = db.Column(db.String(100))
    exattr50 = db.Column(db.String(100))
    exattr51 = db.Column(db.String(100))
    exattr52 = db.Column(db.String(100))
    exattr53 = db.Column(db.String(100))
    exattr54 = db.Column(db.String(100))
    exattr55 = db.Column(db.String(100))
    exattr56 = db.Column(db.String(100))
    exattr57 = db.Column(db.String(100))
    exattr58 = db.Column(db.String(100))
    exattr59 = db.Column(db.String(100))
    exattr60 = db.Column(db.String(100))
    ctzn = db.Column(db.String(20))
    stocksz = db.Column(db.Numeric(8, 2))
    pcdt = db.Column(db.DateTime)
    ordstdt = db.Column(db.DateTime)
    posstdt = db.Column(db.DateTime)
    invflg = db.Column(db.String(1), server_default=db.FetchedValue())


t_sys_dept_lyl = db.Table(
    'sys_dept_lyl',
    db.Column('id', db.Integer, nullable=False),
    db.Column('cd', db.String(20), nullable=False),
    db.Column('nm_l_zh', db.Unicode(50), nullable=False),
    db.Column('nm_l_en', db.Unicode(50)),
    db.Column('nm_l_ja', db.Unicode(50)),
    db.Column('coid', db.Integer, nullable=False),
    db.Column('adminby', db.String(50)),
    db.Column('pid', db.Integer),
    db.Column('secondcd', db.String(20)),
    db.Column('tp', db.String(20)),
    db.Column('subtp', db.String(20)),
    db.Column('roundtp', db.String(20)),
    db.Column('brand', db.String(20)),
    db.Column('lvl', db.Integer),
    db.Column('pth', db.String(200)),
    db.Column('leafflg', db.String(1)),
    db.Column('plutplid', db.Integer),
    db.Column('potplid', db.Integer),
    db.Column('bomtplid', db.Integer),
    db.Column('costtplid', db.Integer),
    db.Column('mkttplid', db.Integer),
    db.Column('istplid', db.Integer),
    db.Column('dlvtplid', db.Integer),
    db.Column('accttplid', db.Integer),
    db.Column('svrtplid', db.Integer),
    db.Column('prntplid', db.Integer),
    db.Column('tdrtplid', db.Integer),
    db.Column('scrtplid', db.Integer),
    db.Column('prtplid', db.Integer),
    db.Column('shoptp1', db.String(10)),
    db.Column('shoptp2', db.String(10)),
    db.Column('cbdtp1', db.String(10)),
    db.Column('cbdtp2', db.String(10)),
    db.Column('area', db.Numeric(8, 2)),
    db.Column('tablecnt', db.Integer),
    db.Column('renttp', db.String(20)),
    db.Column('rentfee', db.Numeric(14, 2)),
    db.Column('stdt', db.DateTime),
    db.Column('eddt', db.DateTime),
    db.Column('menutp', db.String(10)),
    db.Column('ordcldflg', db.String(1)),
    db.Column('locflg', db.String(1)),
    db.Column('lotflg', db.String(1)),
    db.Column('saftamt', db.Numeric(16, 2)),
    db.Column('taxcd', db.String(30)),
    db.Column('bizcd', db.Unicode(20)),
    db.Column('cp', db.Unicode(30)),
    db.Column('lr', db.Unicode(30)),
    db.Column('invaddr', db.Unicode(100)),
    db.Column('invzipcd', db.String(20)),
    db.Column('coaddr', db.Unicode(100)),
    db.Column('cozipcd', db.String(20)),
    db.Column('country', db.Unicode(20)),
    db.Column('province', db.Unicode(20)),
    db.Column('city', db.Unicode(20)),
    db.Column('officetel', db.String(30)),
    db.Column('officefax', db.String(30)),
    db.Column('email', db.String(32)),
    db.Column('crcd', db.String(3)),
    db.Column('taxa', db.String(20)),
    db.Column('taxrt', db.Numeric(6, 2)),
    db.Column('bankid', db.Integer),
    db.Column('banknm', db.Unicode(50)),
    db.Column('bankaccount', db.String(30)),
    db.Column('exattr1', db.String(100)),
    db.Column('exattr2', db.String(100)),
    db.Column('exattr3', db.String(100)),
    db.Column('exattr4', db.String(100)),
    db.Column('exattr5', db.String(100)),
    db.Column('exattr6', db.String(100)),
    db.Column('exattr7', db.String(100)),
    db.Column('exattr8', db.String(100)),
    db.Column('exattr9', db.String(100)),
    db.Column('exattr10', db.String(100)),
    db.Column('exattr11', db.String(100)),
    db.Column('exattr12', db.String(100)),
    db.Column('exattr13', db.String(100)),
    db.Column('exattr14', db.String(100)),
    db.Column('exattr15', db.String(100)),
    db.Column('exattr16', db.String(100)),
    db.Column('exattr17', db.String(100)),
    db.Column('exattr18', db.String(100)),
    db.Column('exattr19', db.String(100)),
    db.Column('exattr20', db.String(100)),
    db.Column('exattr21', db.String(100)),
    db.Column('exattr22', db.String(100)),
    db.Column('exattr23', db.String(100)),
    db.Column('exattr24', db.String(100)),
    db.Column('exattr25', db.String(100)),
    db.Column('exattr26', db.String(100)),
    db.Column('exattr27', db.String(100)),
    db.Column('exattr28', db.String(100)),
    db.Column('exattr29', db.String(100)),
    db.Column('exattr30', db.String(100)),
    db.Column('rmk', db.Unicode(200)),
    db.Column('updby', db.String(20)),
    db.Column('upddt', db.DateTime),
    db.Column('sta', db.String(3), nullable=False),
    db.Column('execflg', db.String(1)),
    db.Column('nxtsta', db.String(3)),
    db.Column('exattr31', db.String(100)),
    db.Column('exattr32', db.String(100)),
    db.Column('exattr33', db.String(100)),
    db.Column('exattr34', db.String(100)),
    db.Column('exattr35', db.String(100)),
    db.Column('exattr36', db.String(100)),
    db.Column('exattr37', db.String(100)),
    db.Column('exattr38', db.String(100)),
    db.Column('exattr39', db.String(100)),
    db.Column('exattr40', db.String(100)),
    db.Column('exattr41', db.String(100)),
    db.Column('exattr42', db.String(100)),
    db.Column('exattr43', db.String(100)),
    db.Column('exattr44', db.String(100)),
    db.Column('exattr45', db.String(100)),
    db.Column('exattr46', db.String(100)),
    db.Column('exattr47', db.String(100)),
    db.Column('exattr48', db.String(100)),
    db.Column('exattr49', db.String(100)),
    db.Column('exattr50', db.String(100)),
    db.Column('exattr51', db.String(100)),
    db.Column('exattr52', db.String(100)),
    db.Column('exattr53', db.String(100)),
    db.Column('exattr54', db.String(100)),
    db.Column('exattr55', db.String(100)),
    db.Column('exattr56', db.String(100)),
    db.Column('exattr57', db.String(100)),
    db.Column('exattr58', db.String(100)),
    db.Column('exattr59', db.String(100)),
    db.Column('exattr60', db.String(100)),
    db.Column('ctzn', db.String(20)),
    db.Column('stocksz', db.Numeric(8, 2)),
    db.Column('pcdt', db.DateTime),
    db.Column('ordstdt', db.DateTime),
    db.Column('posstdt', db.DateTime),
    db.Column('invflg', db.String(1))
)


t_sys_dept_syn = db.Table(
    'sys_dept_syn',
    db.Column('deptid', db.Integer),
    db.Column('upddt', db.DateTime)
)


t_sys_dept_temp = db.Table(
    'sys_dept_temp',
    db.Column('id', db.Integer),
    db.Column('cd', db.String(20)),
    db.Column('nm_l_zh', db.Unicode(50)),
    db.Column('nm_l_en', db.Unicode(50)),
    db.Column('nm_l_ja', db.Unicode(50)),
    db.Column('coid', db.Integer),
    db.Column('adminby', db.String(50)),
    db.Column('pid', db.Integer),
    db.Column('secondcd', db.String(20)),
    db.Column('tp', db.String(20)),
    db.Column('subtp', db.String(20)),
    db.Column('roundtp', db.String(20)),
    db.Column('brand', db.String(20)),
    db.Column('lvl', db.Integer),
    db.Column('pth', db.String(200)),
    db.Column('leafflg', db.String(1)),
    db.Column('plutplid', db.Integer),
    db.Column('potplid', db.Integer),
    db.Column('bomtplid', db.Integer),
    db.Column('costtplid', db.Integer),
    db.Column('mkttplid', db.Integer),
    db.Column('istplid', db.Integer),
    db.Column('dlvtplid', db.Integer),
    db.Column('accttplid', db.Integer),
    db.Column('svrtplid', db.Integer),
    db.Column('prntplid', db.Integer),
    db.Column('tdrtplid', db.Integer),
    db.Column('scrtplid', db.Integer),
    db.Column('prtplid', db.Integer),
    db.Column('shoptp1', db.String(10)),
    db.Column('shoptp2', db.String(10)),
    db.Column('cbdtp1', db.String(10)),
    db.Column('cbdtp2', db.String(10)),
    db.Column('area', db.Numeric(8, 2)),
    db.Column('tablecnt', db.Integer),
    db.Column('renttp', db.String(20)),
    db.Column('rentfee', db.Numeric(14, 2)),
    db.Column('stdt', db.DateTime),
    db.Column('eddt', db.DateTime),
    db.Column('menutp', db.String(10)),
    db.Column('ordcldflg', db.String(1)),
    db.Column('locflg', db.String(1)),
    db.Column('lotflg', db.String(1)),
    db.Column('saftamt', db.Numeric(16, 2)),
    db.Column('taxcd', db.String(30)),
    db.Column('bizcd', db.Unicode(20)),
    db.Column('cp', db.Unicode(30)),
    db.Column('lr', db.Unicode(30)),
    db.Column('invaddr', db.Unicode(100)),
    db.Column('invzipcd', db.String(20)),
    db.Column('coaddr', db.Unicode(100)),
    db.Column('cozipcd', db.String(20)),
    db.Column('country', db.Unicode(20)),
    db.Column('province', db.Unicode(20)),
    db.Column('city', db.Unicode(20)),
    db.Column('officetel', db.String(30)),
    db.Column('officefax', db.String(30)),
    db.Column('email', db.String(32)),
    db.Column('crcd', db.String(3)),
    db.Column('taxa', db.String(20)),
    db.Column('taxrt', db.Numeric(6, 2)),
    db.Column('bankid', db.Integer),
    db.Column('banknm', db.Unicode(50)),
    db.Column('bankaccount', db.String(30)),
    db.Column('exattr1', db.String(100)),
    db.Column('exattr2', db.String(100)),
    db.Column('exattr3', db.String(100)),
    db.Column('exattr4', db.String(100)),
    db.Column('exattr5', db.String(100)),
    db.Column('exattr6', db.String(100)),
    db.Column('exattr7', db.String(100)),
    db.Column('exattr8', db.String(100)),
    db.Column('exattr9', db.String(100)),
    db.Column('exattr10', db.String(100)),
    db.Column('exattr11', db.String(100)),
    db.Column('exattr12', db.String(100)),
    db.Column('exattr13', db.String(100)),
    db.Column('exattr14', db.String(100)),
    db.Column('exattr15', db.String(100)),
    db.Column('exattr16', db.String(100)),
    db.Column('exattr17', db.String(100)),
    db.Column('exattr18', db.String(100)),
    db.Column('exattr19', db.String(100)),
    db.Column('exattr20', db.String(100)),
    db.Column('exattr21', db.String(100)),
    db.Column('exattr22', db.String(100)),
    db.Column('exattr23', db.String(100)),
    db.Column('exattr24', db.String(100)),
    db.Column('exattr25', db.String(100)),
    db.Column('exattr26', db.String(100)),
    db.Column('exattr27', db.String(100)),
    db.Column('exattr28', db.String(100)),
    db.Column('exattr29', db.String(100)),
    db.Column('exattr30', db.String(100)),
    db.Column('rmk', db.Unicode(200)),
    db.Column('updby', db.String(20)),
    db.Column('upddt', db.DateTime),
    db.Column('sta', db.String(3)),
    db.Column('execflg', db.String(1)),
    db.Column('nxtsta', db.String(3)),
    db.Column('exattr31', db.String(100)),
    db.Column('exattr32', db.String(100)),
    db.Column('exattr33', db.String(100)),
    db.Column('exattr34', db.String(100)),
    db.Column('exattr35', db.String(100)),
    db.Column('exattr36', db.String(100)),
    db.Column('exattr37', db.String(100)),
    db.Column('exattr38', db.String(100)),
    db.Column('exattr39', db.String(100)),
    db.Column('exattr40', db.String(100)),
    db.Column('exattr41', db.String(100)),
    db.Column('exattr42', db.String(100)),
    db.Column('exattr43', db.String(100)),
    db.Column('exattr44', db.String(100)),
    db.Column('exattr45', db.String(100)),
    db.Column('exattr46', db.String(100)),
    db.Column('exattr47', db.String(100)),
    db.Column('exattr48', db.String(100)),
    db.Column('exattr49', db.String(100)),
    db.Column('exattr50', db.String(100)),
    db.Column('exattr51', db.String(100)),
    db.Column('exattr52', db.String(100)),
    db.Column('exattr53', db.String(100)),
    db.Column('exattr54', db.String(100)),
    db.Column('exattr55', db.String(100)),
    db.Column('exattr56', db.String(100)),
    db.Column('exattr57', db.String(100)),
    db.Column('exattr58', db.String(100)),
    db.Column('exattr59', db.String(100)),
    db.Column('exattr60', db.String(100)),
    db.Column('ctzn', db.String(20)),
    db.Column('stocksz', db.Numeric(8, 2)),
    db.Column('pcdt', db.DateTime),
    db.Column('ordstdt', db.DateTime),
    db.Column('posstdt', db.DateTime),
    db.Column('invflg', db.String(1))
)


class SysExcelmodel(db.Model):
    __tablename__ = 'sys_excelmodel'

    id = db.Column(db.Integer, primary_key=True)
    cd = db.Column(db.String(20))
    nm_l_zh = db.Column(db.Unicode(50))
    nm_l_en = db.Column(db.Unicode(50))
    nm_l_ja = db.Column(db.Unicode(50))
    dsnm = db.Column(db.String(100), nullable=False)
    coid = db.Column(db.Integer, nullable=False)
    sheetnm = db.Column(db.String(50))
    tbnm = db.Column(db.String(50))
    keynm = db.Column(db.String(50))
    keytp = db.Column(db.String(50))
    seqnm = db.Column(db.String(100))
    dbtp = db.Column(db.String(50))
    strow = db.Column(db.Integer)
    edrow = db.Column(db.Integer)
    stcol = db.Column(db.Integer)
    edcol = db.Column(db.Integer)
    proctp = db.Column(db.String(10))
    procnm = db.Column(db.String(100))
    helpdoc = db.Column(db.String(100))
    hdrcols = db.Column(db.String(500))
    rmk = db.Column(db.Unicode(255))
    updby = db.Column(db.String(20))
    upddt = db.Column(db.DateTime)
    sta = db.Column(db.String(3))


class SysExcelmodeldtl(db.Model):
    __tablename__ = 'sys_excelmodeldtl'

    id = db.Column(db.Integer, primary_key=True)
    excelmodelid = db.Column(db.Integer, nullable=False)
    excelcol = db.Column(db.Integer, nullable=False)
    tbcol = db.Column(db.String(50), nullable=False)
    expdgcol = db.Column(db.String(50))
    dftval = db.Column(db.String(50))
    uniqueflg = db.Column(db.String(1))
    lktp = db.Column(db.String(100))
    lknm = db.Column(db.String(50))
    lksql = db.Column(db.String(500))
    srccolnm = db.Column(db.String(30))
    trgcolnm = db.Column(db.String(30))
    updateflg = db.Column(db.String(1))
    insertflg = db.Column(db.String(1))
    updby = db.Column(db.String(20))
    upddt = db.Column(db.DateTime)
    sta = db.Column(db.String(3))
    dttp = db.Column(db.String(20))
    dtlnm = db.Column(db.String(50))
    fkey = db.Column(db.String(30))
    dgid = db.Column(db.String(30))
    nm_l_zh = db.Column(db.String(50))
    nm_l_en = db.Column(db.String(50))
    nm_l_ja = db.Column(db.String(50))


t_sys_execlog = db.Table(
    'sys_execlog',
    db.Column('procid', db.String(50)),
    db.Column('seqid', db.Integer),
    db.Column('logtp', db.String(1)),
    db.Column('logcd', db.String(20)),
    db.Column('logdsc', db.String(4000)),
    db.Column('logloc', db.String(255)),
    db.Column('logstdt', db.DateTime),
    db.Column('logeddt', db.DateTime),
    db.Column('upddt', db.DateTime, server_default=db.FetchedValue())
)


t_sys_hhslog = db.Table(
    'sys_hhslog',
    db.Column('step', db.String(20)),
    db.Column('upddt', db.DateTime)
)


class SysMenucomp(db.Model):
    __tablename__ = 'sys_menucomp'

    id = db.Column(db.Integer, primary_key=True)
    menuid = db.Column(db.Integer, nullable=False)
    compid = db.Column(db.Integer, nullable=False)
    updby = db.Column(db.String(20))
    upddt = db.Column(db.DateTime)
    sta = db.Column(db.String(3))


class SysMenure(db.Model):
    __tablename__ = 'sys_menures'

    id = db.Column(db.Integer, primary_key=True)
    coid = db.Column(db.Integer, nullable=False)
    cd = db.Column(db.String(20))
    nm_l_zh = db.Column(db.Unicode(50), nullable=False)
    nm_l_en = db.Column(db.Unicode(50))
    nm_l_ja = db.Column(db.Unicode(50))
    moduleid = db.Column(db.Integer)
    icon = db.Column(db.String(100))
    bigicon = db.Column(db.String(100))
    leafflg = db.Column(db.String(1), server_default=db.FetchedValue())
    pid = db.Column(db.Integer)
    lvl = db.Column(db.Integer)
    pth = db.Column(db.String(100))
    navflg = db.Column(db.String(1), nullable=False, server_default=db.FetchedValue())
    seqord = db.Column(db.Integer)
    updby = db.Column(db.String(20))
    upddt = db.Column(db.DateTime)
    sta = db.Column(db.String(3))


class SysModulere(db.Model):
    __tablename__ = 'sys_moduleres'

    id = db.Column(db.String(50), primary_key=True)
    coid = db.Column(db.Integer)
    tp = db.Column(db.String(10))
    cd = db.Column(db.String(50), nullable=False)
    nm_l_zh = db.Column(db.Unicode(50), nullable=False)
    nm_l_en = db.Column(db.Unicode(50))
    nm_l_ja = db.Column(db.Unicode(50))
    url = db.Column(db.String(300), nullable=False)
    icon = db.Column(db.String(100))
    bigicon = db.Column(db.String(100))
    adminby = db.Column(db.String(50))
    accflg = db.Column(db.String(1), nullable=False, server_default=db.FetchedValue())
    rmk = db.Column(db.String(100))
    updby = db.Column(db.String(20))
    upddt = db.Column(db.DateTime)
    sta = db.Column(db.String(3))
    logflg = db.Column(db.String(1), server_default=db.FetchedValue())
    murl = db.Column(db.String(300))


t_sys_optlog = db.Table(
    'sys_optlog',
    db.Column('moduleid', db.Integer),
    db.Column('acttp', db.String(10)),
    db.Column('tbnm', db.Unicode(30)),
    db.Column('keyid', db.Numeric(14, 0, asdecimal=False)),
    db.Column('updby', db.String(20)),
    db.Column('upddt', db.DateTime)
)


class SysParameter(db.Model):
    __tablename__ = 'sys_parameter'

    id = db.Column(db.Integer)
    title = db.Column(db.String(50), primary_key=True)
    param_name = db.Column(db.String(100))
    default_value = db.Column(db.String(250))
    current_value = db.Column(db.String(250))
    last_value = db.Column(db.String(250))
    remark = db.Column(db.String(255))
    updby = db.Column(db.String(20))
    upddt = db.Column(db.DateTime)
    sta = db.Column(db.String(3))


class SysPgtpl(db.Model):
    __tablename__ = 'sys_pgtpl'

    id = db.Column(db.Integer, primary_key=True)
    tp = db.Column(db.String(10))
    cd = db.Column(db.String(20))
    nm_l_zh = db.Column(db.Unicode(50))
    nm_l_en = db.Column(db.Unicode(50))
    nm_l_ja = db.Column(db.Unicode(50))
    tbnm = db.Column(db.String(100))
    d1tbnm = db.Column(db.String(100))
    d1fknm = db.Column(db.String(100))
    d2tbnm = db.Column(db.String(30))
    d2fknm = db.Column(db.String(30))
    pkgcd = db.Column(db.String(30))
    rmk = db.Column(db.Unicode(255))
    updby = db.Column(db.String(20))
    upddt = db.Column(db.DateTime)
    sta = db.Column(db.String(3), nullable=False)


class SysPgtplcfg(db.Model):
    __tablename__ = 'sys_pgtplcfg'

    id = db.Column(db.Integer, primary_key=True)
    pgtplid = db.Column(db.Integer)
    cd = db.Column(db.String(20))
    nm_l_zh = db.Column(db.Unicode(50))
    nm_l_en = db.Column(db.Unicode(50))
    nm_l_ja = db.Column(db.Unicode(50))
    ordseq = db.Column(db.Integer)
    rmk = db.Column(db.Unicode(355))
    updby = db.Column(db.String(20))
    upddt = db.Column(db.DateTime)
    sta = db.Column(db.String(3), nullable=False)


class SysPgtplexa(db.Model):
    __tablename__ = 'sys_pgtplexa'

    id = db.Column(db.Integer, primary_key=True)
    pgtplid = db.Column(db.Integer)
    tp = db.Column(db.String(10))
    cd = db.Column(db.String(50))
    nm_l_zh = db.Column(db.Unicode(100))
    nm_l_en = db.Column(db.Unicode(100))
    nm_l_ja = db.Column(db.Unicode(100))
    ordseq = db.Column(db.Integer)
    rmk = db.Column(db.Unicode(255))
    updby = db.Column(db.String(20))
    upddt = db.Column(db.DateTime)
    sta = db.Column(db.String(3), nullable=False)


class SysPgtplrsn(db.Model):
    __tablename__ = 'sys_pgtplrsn'

    id = db.Column(db.Integer, primary_key=True)
    pgtplid = db.Column(db.Integer, nullable=False)
    tbnm = db.Column(db.String(30), nullable=False)
    pgtplrsn = db.Column(db.String(10), nullable=False)
    nm_l_zh = db.Column(db.Unicode(30))
    nm_l_en = db.Column(db.Unicode(30))
    nm_l_ja = db.Column(db.Unicode(30))
    rmk = db.Column(db.Unicode(255))
    updby = db.Column(db.String(20))
    upddt = db.Column(db.DateTime)
    sta = db.Column(db.String(3), nullable=False)


class SysPgtplsta(db.Model):
    __tablename__ = 'sys_pgtplsta'

    id = db.Column(db.Integer, primary_key=True)
    pgtplid = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    tbnm = db.Column(db.String(30), nullable=False)
    pgtplsta = db.Column(db.String(3), nullable=False)
    nm_l_zh = db.Column(db.Unicode(30))
    nm_l_en = db.Column(db.Unicode(30))
    nm_l_ja = db.Column(db.Unicode(30))
    seq = db.Column(db.Integer)
    rmk = db.Column(db.Unicode(255))
    updby = db.Column(db.String(20))
    upddt = db.Column(db.DateTime)
    sta = db.Column(db.String(3), nullable=False)


class SysPgtpltp(db.Model):
    __tablename__ = 'sys_pgtpltp'

    id = db.Column(db.Integer, primary_key=True)
    pgtplid = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    tbnm = db.Column(db.String(30), nullable=False)
    billtp = db.Column(db.String(10))
    nm_l_zh = db.Column(db.Unicode(50))
    nm_l_en = db.Column(db.Unicode(50))
    nm_l_ja = db.Column(db.Unicode(50))
    rmk = db.Column(db.Unicode(255))
    updby = db.Column(db.String(20))
    upddt = db.Column(db.DateTime)
    sta = db.Column(db.String(3), nullable=False)
    pgtpltp = db.Column(db.String(10))


class SysPgver(db.Model):
    __tablename__ = 'sys_pgver'

    id = db.Column(db.Integer, primary_key=True)
    pgtplid = db.Column(db.Integer)
    cd = db.Column(db.String(20))
    nm_l_zh = db.Column(db.Unicode(50))
    nm_l_en = db.Column(db.Unicode(50))
    nm_l_ja = db.Column(db.Unicode(50))
    dftflg = db.Column(db.String(1), server_default=db.FetchedValue())
    rmk = db.Column(db.Unicode(255))
    updby = db.Column(db.String(20))
    upddt = db.Column(db.DateTime)
    sta = db.Column(db.String(3), nullable=False)


class SysPgvercfg(db.Model):
    __tablename__ = 'sys_pgvercfg'

    id = db.Column(db.Integer, primary_key=True)
    pgverid = db.Column(db.Integer)
    pgtplcfgid = db.Column(db.Integer)
    val = db.Column(db.String(500))
    updby = db.Column(db.String(20))
    upddt = db.Column(db.DateTime)
    sta = db.Column(db.String(3), nullable=False)


class SysPgverexa(db.Model):
    __tablename__ = 'sys_pgverexa'

    id = db.Column(db.Integer, primary_key=True)
    pgverid = db.Column(db.Integer)
    pgtplexaid = db.Column(db.Integer)
    nm_l_zh = db.Column(db.Unicode(50))
    nm_l_en = db.Column(db.Unicode(50))
    nm_l_ja = db.Column(db.Unicode(50))
    disflg = db.Column(db.String(1), server_default=db.FetchedValue())
    reqflg = db.Column(db.String(1), server_default=db.FetchedValue())
    uniqueflg = db.Column(db.String(1), server_default=db.FetchedValue())
    readflg = db.Column(db.String(1), server_default=db.FetchedValue())
    chkflg = db.Column(db.String(1), server_default=db.FetchedValue())
    alwista = db.Column(db.String(30))
    alwdefcnd = db.Column(db.String(100))
    lkreqcnd = db.Column(db.String(400))
    datatp = db.Column(db.String(20))
    defval = db.Column(db.String(100))
    defsort = db.Column(db.String(10))
    disfmt = db.Column(db.String(30))
    chkmin = db.Column(db.String(20))
    chkmax = db.Column(db.String(20))
    regrule = db.Column(db.String(100))
    lktp = db.Column(db.String(100))
    lknm = db.Column(db.String(50))
    lksql = db.Column(db.String(500))
    ordseq = db.Column(db.Integer)
    rmk = db.Column(db.Unicode(255))
    updby = db.Column(db.String(20))
    upddt = db.Column(db.DateTime)
    sta = db.Column(db.String(3), nullable=False)
    cfgflg = db.Column(db.String(1), server_default=db.FetchedValue())


class SysPgverrsn(db.Model):
    __tablename__ = 'sys_pgverrsn'

    id = db.Column(db.Integer, primary_key=True)
    pgverid = db.Column(db.Integer, nullable=False)
    pgtplrsnid = db.Column(db.Integer)
    updby = db.Column(db.String(20))
    upddt = db.Column(db.DateTime)
    sta = db.Column(db.String(3), nullable=False)


class SysPgversta(db.Model):
    __tablename__ = 'sys_pgversta'

    id = db.Column(db.Integer, primary_key=True)
    pgverid = db.Column(db.Integer, nullable=False, index=True, server_default=db.FetchedValue())
    cstaid = db.Column(db.Integer, nullable=False)
    pstaid = db.Column(db.Integer)
    nstaid = db.Column(db.Integer)
    seq = db.Column(db.Integer)
    pacttp = db.Column(db.String(10))
    exec1 = db.Column(db.String(20))
    exec2 = db.Column(db.String(10))
    exec3 = db.Column(db.String(10))
    rmk = db.Column(db.Unicode(255))
    updby = db.Column(db.String(20))
    upddt = db.Column(db.DateTime)
    sta = db.Column(db.String(3), nullable=False)
    nacttp = db.Column(db.String(10))
    alwista = db.Column(db.String(30))


class SysPgvertp(db.Model):
    __tablename__ = 'sys_pgvertp'

    id = db.Column(db.Integer, primary_key=True)
    pgverid = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    pgtplid = db.Column(db.Integer, nullable=False)
    updby = db.Column(db.String(20))
    upddt = db.Column(db.DateTime)
    sta = db.Column(db.String(3), nullable=False)


class SysPreference(db.Model):
    __tablename__ = 'sys_preference'

    id = db.Column(db.Integer, primary_key=True)
    keynm = db.Column(db.String(50), nullable=False)
    value = db.Column(db.String(50))
    rmk = db.Column(db.String(200))
    updby = db.Column(db.String(20))
    upddt = db.Column(db.DateTime)
    sta = db.Column(db.String(3))


class SysQuery(db.Model):
    __tablename__ = 'sys_query'

    id = db.Column(db.Integer, primary_key=True)
    tp = db.Column(db.String(10))
    cd = db.Column(db.String(20))
    nm_l_zh = db.Column(db.Unicode(50), nullable=False)
    nm_l_en = db.Column(db.Unicode(50))
    nm_l_ja = db.Column(db.Unicode(50))
    updby = db.Column(db.String(20))
    upddt = db.Column(db.DateTime)
    sta = db.Column(db.String(3), nullable=False)


t_sys_queryds = db.Table(
    'sys_queryds',
    db.Column('id', db.Integer, nullable=False),
    db.Column('queryid', db.Integer),
    db.Column('dsid', db.Integer),
    db.Column('pdsid', db.Integer),
    db.Column('lvl', db.Integer),
    db.Column('ordseq', db.Integer),
    db.Column('pageflg', db.String(1), server_default=db.FetchedValue()),
    db.Column('upddt', db.DateTime),
    db.Column('updby', db.String(30)),
    db.Column('sta', db.String(3))
)


class SysReg(db.Model):
    __tablename__ = 'sys_reg'

    id = db.Column(db.Integer, primary_key=True)
    regnm = db.Column(db.String(100))
    apnm = db.Column(db.String(100))
    regcd = db.Column(db.String(100))
    bldcd = db.Column(db.String(100))
    updby = db.Column(db.String(20))
    upddt = db.Column(db.DateTime)
    rmk = db.Column(db.String(255))
    sta = db.Column(db.String(3))
    prdver = db.Column(db.String(50))
    updver = db.Column(db.String(50))
    runmod = db.Column(db.String(50))
    authcnt = db.Column(db.String(50))
    stdt = db.Column(db.DateTime)
    eddt = db.Column(db.DateTime)


class SysReport(db.Model):
    __tablename__ = 'sys_report'

    id = db.Column(db.Integer, primary_key=True)
    cd = db.Column(db.String(20))
    tp = db.Column(db.String(10))
    jaspernm = db.Column(db.String(50))
    ename = db.Column(db.Unicode(50))
    dsnm = db.Column(db.String(50))
    upldfilenm = db.Column(db.String(100))
    coid = db.Column(db.Integer)
    rmk = db.Column(db.Unicode(255))
    updby = db.Column(db.String(20))
    upddt = db.Column(db.DateTime)
    sta = db.Column(db.String(3))


class SysResrole(db.Model):
    __tablename__ = 'sys_resrole'

    id = db.Column(db.Integer, primary_key=True)
    restp = db.Column(db.String(1), nullable=False)
    resid = db.Column(db.Integer, nullable=False)
    roleid = db.Column(db.Integer, nullable=False)
    updby = db.Column(db.String(20))
    upddt = db.Column(db.DateTime)
    sta = db.Column(db.String(3))


class SysRole(db.Model):
    __tablename__ = 'sys_role'

    id = db.Column(db.Integer, primary_key=True)
    coid = db.Column(db.Integer, nullable=False)
    cd = db.Column(db.String(20))
    secondcd = db.Column(db.String(20))
    nm_l_zh = db.Column(db.String(50), nullable=False)
    nm_l_en = db.Column(db.Unicode(50))
    nm_l_ja = db.Column(db.Unicode(50))
    pid = db.Column(db.Integer)
    lvl = db.Column(db.Integer)
    pth = db.Column(db.String(100))
    leafflg = db.Column(db.String(1))
    posflg = db.Column(db.String(1))
    rmk = db.Column(db.String(200))
    updby = db.Column(db.String(20))
    upddt = db.Column(db.DateTime)
    sta = db.Column(db.String(3))


class SysRolembr(db.Model):
    __tablename__ = 'sys_rolembr'

    id = db.Column(db.Integer, primary_key=True)
    roleid = db.Column(db.Integer, nullable=False)
    mbrtp = db.Column(db.String(1), nullable=False)
    mbrid = db.Column(db.Integer, nullable=False)
    grantflg = db.Column(db.String(1))
    updby = db.Column(db.String(20))
    upddt = db.Column(db.DateTime)
    sta = db.Column(db.String(3))


class SysRptmbr(db.Model):
    __tablename__ = 'sys_rptmbr'

    id = db.Column(db.Integer, primary_key=True)
    mstid = db.Column(db.String(50))
    tp = db.Column(db.String(1), nullable=False)
    mbrid = db.Column(db.Integer, nullable=False)
    updby = db.Column(db.String(20))
    upddt = db.Column(db.DateTime)
    sta = db.Column(db.String(3))


class SysRptpmt(db.Model):
    __tablename__ = 'sys_rptpmt'

    id = db.Column(db.Integer, primary_key=True)
    rptid = db.Column(db.Integer)
    tp = db.Column(db.Unicode(10))
    nm = db.Column(db.Unicode(50))
    dttp = db.Column(db.Unicode(20))
    value = db.Column(db.Unicode(100))
    meta1 = db.Column(db.Unicode(100))
    meta2 = db.Column(db.Unicode(100))
    updby = db.Column(db.String(20))
    upddt = db.Column(db.DateTime)
    sta = db.Column(db.String(3))


class SysTable(db.Model):
    __tablename__ = 'sys_table'

    id = db.Column(db.Integer, primary_key=True)
    nm = db.Column(db.String(30))
    classnm = db.Column(db.String(50))
    managernm = db.Column(db.String(100))
    rmk = db.Column(db.Unicode(255))
    updby = db.Column(db.String(20))
    upddt = db.Column(db.DateTime)
    sta = db.Column(db.String(3), nullable=False)


t_sys_tablerows = db.Table(
    'sys_tablerows',
    db.Column('table_name', db.Unicode(50)),
    db.Column('table_rows', db.Numeric(10, 0, asdecimal=False)),
    db.Column('table_user', db.Unicode(50))
)


t_sys_time = db.Table(
    'sys_time',
    db.Column('timeid', db.Integer, nullable=False),
    db.Column('t1', db.String(20)),
    db.Column('t2', db.String(20)),
    db.Column('btime', db.String(8)),
    db.Column('etime', db.String(8))
)


class SysUdc(db.Model):
    __tablename__ = 'sys_udc'

    id = db.Column(db.Integer, primary_key=True)
    ucatid = db.Column(db.Integer, nullable=False, index=True)
    cd = db.Column(db.String(50), nullable=False)
    nm_l_zh = db.Column(db.Unicode(50), nullable=False)
    nm_l_en = db.Column(db.Unicode(50))
    nm_l_ja = db.Column(db.Unicode(50))
    val1 = db.Column(db.String(100))
    val2 = db.Column(db.String(100))
    val3 = db.Column(db.String(100))
    pid = db.Column(db.Integer)
    lvl = db.Column(db.Integer)
    pth = db.Column(db.String(100))
    leafflg = db.Column(db.String(1), server_default=db.FetchedValue())
    seq = db.Column(db.Integer)
    rmk = db.Column(db.Unicode(255))
    updby = db.Column(db.String(20), nullable=False)
    upddt = db.Column(db.DateTime, nullable=False)
    sta = db.Column(db.String(3), nullable=False)


t_sys_udc_temp_min = db.Table(
    'sys_udc_temp_min',
    db.Column('id', db.Integer),
    db.Column('ucatid', db.Integer),
    db.Column('cd', db.String(50)),
    db.Column('nm_l_zh', db.Unicode(50)),
    db.Column('nm_l_en', db.Unicode(50)),
    db.Column('nm_l_ja', db.Unicode(50)),
    db.Column('val1', db.String(100)),
    db.Column('val2', db.String(100)),
    db.Column('val3', db.String(100)),
    db.Column('pid', db.Integer),
    db.Column('lvl', db.Integer),
    db.Column('pth', db.String(100)),
    db.Column('leafflg', db.String(1)),
    db.Column('seq', db.Integer),
    db.Column('rmk', db.Unicode(255)),
    db.Column('updby', db.String(20)),
    db.Column('upddt', db.DateTime),
    db.Column('sta', db.String(3))
)


class SysUdccat(db.Model):
    __tablename__ = 'sys_udccat'

    id = db.Column(db.Integer, primary_key=True)
    cd = db.Column(db.String(20), nullable=False, unique=True)
    nm_l_zh = db.Column(db.Unicode(50), nullable=False)
    nm_l_en = db.Column(db.Unicode(50))
    nm_l_ja = db.Column(db.Unicode(50))
    tp = db.Column(db.String(10), nullable=False)
    dtdp = db.Column(db.String(10))
    dtlen = db.Column(db.Integer)
    dtpre = db.Column(db.Integer)
    lvltp = db.Column(db.String(10))
    rmk = db.Column(db.Unicode(255))
    upddt = db.Column(db.DateTime, nullable=False)
    updby = db.Column(db.String(20), nullable=False)
    sta = db.Column(db.String(3), nullable=False)


class SysUpgver(db.Model):
    __tablename__ = 'sys_upgver'

    id = db.Column(db.Integer, primary_key=True)
    upgsys = db.Column(db.String(20))
    verno = db.Column(db.String(20))
    rmk = db.Column(db.Unicode(200))
    updby = db.Column(db.String(20))
    upddt = db.Column(db.DateTime)
    sta = db.Column(db.String(3), nullable=False)
    execflg = db.Column(db.String(1))
    nxtsta = db.Column(db.String(3))


class SysUpgverfile(db.Model):
    __tablename__ = 'sys_upgverfile'

    id = db.Column(db.Integer, primary_key=True)
    upgverid = db.Column(db.String(20))
    filenm = db.Column(db.String(20))
    linkpth = db.Column(db.String(100))
    filedt = db.Column(db.DateTime)
    rmk = db.Column(db.Unicode(200))
    updby = db.Column(db.String(20))
    upddt = db.Column(db.DateTime)
    sta = db.Column(db.String(3), nullable=False)
    execflg = db.Column(db.String(1))
    nxtsta = db.Column(db.String(3))


class SysUpgverlog(db.Model):
    __tablename__ = 'sys_upgverlog'

    id = db.Column(db.Integer, primary_key=True)
    upgvertaskid = db.Column(db.String(20))
    rmk = db.Column(db.Unicode(200))
    logtp = db.Column(db.String(1))
    logcd = db.Column(db.String(20))
    logdsc = db.Column(db.String(500))
    logdt = db.Column(db.DateTime)


class SysUpgvertask(db.Model):
    __tablename__ = 'sys_upgvertask'

    id = db.Column(db.Integer, primary_key=True)
    upgverid = db.Column(db.String(20))
    lktp = db.Column(db.String(10))
    lkid = db.Column(db.Integer)
    plvaldt = db.Column(db.DateTime)
    rlvaldt = db.Column(db.DateTime)
    rmk = db.Column(db.Unicode(200))
    updby = db.Column(db.String(20))
    upddt = db.Column(db.DateTime)
    sta = db.Column(db.String(3), nullable=False)
    execflg = db.Column(db.String(1))
    nxtsta = db.Column(db.String(3))


class SysUpldinfo(db.Model):
    __tablename__ = 'sys_upldinfo'

    id = db.Column(db.String(50), primary_key=True)
    filenm = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(200), nullable=False)
    sz = db.Column(db.Integer, nullable=False)
    contenttp = db.Column(db.String(50), nullable=False)
    upldtime = db.Column(db.DateTime, nullable=False)
    upldby = db.Column(db.String(50), nullable=False)
    updby = db.Column(db.String(20))
    upddt = db.Column(db.DateTime)
    sta = db.Column(db.String(3))


class SysUser(db.Model):
    __tablename__ = 'sys_user'

    id = db.Column(db.Integer, primary_key=True)
    cd = db.Column(db.String(20), index=True)
    coid = db.Column(db.Integer)
    deptid = db.Column(db.Integer, nullable=False)
    nm_l_zh = db.Column(db.Unicode(50), nullable=False)
    nm_l_en = db.Column(db.Unicode(50))
    nm_l_ja = db.Column(db.Unicode(50))
    pwd = db.Column(db.String(50))
    salt = db.Column(db.String(10))
    stdt = db.Column(db.DateTime)
    eddt = db.Column(db.DateTime)
    valided = db.Column(db.String(1), server_default=db.FetchedValue())
    locked = db.Column(db.String(1), server_default=db.FetchedValue())
    fpflg = db.Column(db.String(1), server_default=db.FetchedValue())
    hiretp = db.Column(db.String(10))
    langdft = db.Column(db.String(10))
    gender = db.Column(db.String(1), server_default=db.FetchedValue())
    birthday = db.Column(db.DateTime)
    nation = db.Column(db.Unicode(20))
    origin = db.Column(db.Unicode(200))
    edu = db.Column(db.Unicode(50))
    party = db.Column(db.Unicode(50))
    marriage = db.Column(db.String(1), server_default=db.FetchedValue())
    graduate = db.Column(db.Unicode(80))
    hobby = db.Column(db.Unicode(255))
    idcd = db.Column(db.String(20))
    htel = db.Column(db.String(20))
    mtel = db.Column(db.String(20))
    otel = db.Column(db.String(32))
    email = db.Column(db.String(32))
    haddr = db.Column(db.Unicode(255))
    hpostcd = db.Column(db.String(10))
    headship = db.Column(db.Unicode(32))
    salary = db.Column(db.Numeric(12, 2))
    bankcd = db.Column(db.String(30))
    banknm = db.Column(db.Unicode(50))
    gradingdt = db.Column(db.DateTime)
    boarddt = db.Column(db.DateTime)
    dimissiondt = db.Column(db.DateTime)
    issta = db.Column(db.String(10), server_default=db.FetchedValue())
    indt = db.Column(db.DateTime)
    inrmk = db.Column(db.Unicode(255))
    outdt = db.Column(db.DateTime)
    outrmk = db.Column(db.Unicode(255))
    photo = db.Column(db.String(50))
    locktime = db.Column(db.DateTime)
    errcnt = db.Column(db.Integer)
    lastpwddt = db.Column(db.DateTime)
    lastlogindt = db.Column(db.DateTime)
    lastloginarea = db.Column(db.String(80))
    logindt = db.Column(db.DateTime)
    loginarea = db.Column(db.String(80))
    logincnt = db.Column(db.Integer)
    isonline = db.Column(db.String(1), server_default=db.FetchedValue())
    posflg = db.Column(db.String(1), server_default=db.FetchedValue())
    poscd = db.Column(db.String(20), index=True)
    pospwd = db.Column(db.String(30))
    secondflg = db.Column(db.String(1), server_default=db.FetchedValue())
    secondcd = db.Column(db.String(20))
    secondpwd = db.Column(db.String(50))
    exattr1 = db.Column(db.String(100))
    exattr2 = db.Column(db.String(100))
    exattr3 = db.Column(db.String(100))
    exattr4 = db.Column(db.String(100))
    exattr5 = db.Column(db.String(100))
    exattr6 = db.Column(db.String(100))
    exattr7 = db.Column(db.String(100))
    exattr8 = db.Column(db.String(100))
    exattr9 = db.Column(db.String(100))
    exattr10 = db.Column(db.String(100))
    exattr11 = db.Column(db.String(100))
    exattr12 = db.Column(db.String(100))
    exattr13 = db.Column(db.String(100))
    exattr14 = db.Column(db.String(100))
    exattr15 = db.Column(db.String(100))
    rmk = db.Column(db.Unicode(255))
    upddt = db.Column(db.DateTime)
    updby = db.Column(db.String(30))
    sta = db.Column(db.String(3))
    execflg = db.Column(db.String(1), server_default=db.FetchedValue())
    nxtsta = db.Column(db.String(3))


class SysUserdept(db.Model):
    __tablename__ = 'sys_userdept'

    id = db.Column(db.Integer, primary_key=True)
    userid = db.Column(db.Integer, index=True)
    deptid = db.Column(db.Integer)
    updby = db.Column(db.String(20))
    upddt = db.Column(db.DateTime)
    sta = db.Column(db.String(3), nullable=False)
    nxtsta = db.Column(db.String(3))
    execflg = db.Column(db.String(1))
    lktp = db.Column(db.String(10))
    lkcd = db.Column(db.String(20))


class SysUserfav(db.Model):
    __tablename__ = 'sys_userfav'

    id = db.Column(db.Integer, primary_key=True)
    userid = db.Column(db.Integer)
    menuid = db.Column(db.Integer)
    ordseq = db.Column(db.Integer)
    updby = db.Column(db.String(20))
    upddt = db.Column(db.DateTime)
    sta = db.Column(db.String(3), nullable=False)


t_t = db.Table(
    't',
    db.Column('id', db.Numeric(asdecimal=False))
)


t_t_outbound_ap = db.Table(
    't_outbound_ap',
    db.Column('mdextractdate_batch', db.Unicode(25)),
    db.Column('mdgroupcount_batch', db.Numeric(3, 0, asdecimal=False)),
    db.Column('mdgroupid_batch', db.Unicode(20)),
    db.Column('batchamount_batch', db.Numeric(38, 2)),
    db.Column('batchlinecount_batch', db.Unicode(20)),
    db.Column('globalregioncode_batch', db.Unicode(40)),
    db.Column('organizationid_batch', db.Unicode(15)),
    db.Column('organizationname_batch', db.Unicode(140)),
    db.Column('source_batch', db.Unicode(10)),
    db.Column('mdextractid_invoice', db.Unicode(30)),
    db.Column('mdtxlinecount_invoice', db.Numeric(5, 0, asdecimal=False)),
    db.Column('accountingdate_invoice', db.Unicode(25)),
    db.Column('currencycode_invoice', db.Unicode(15)),
    db.Column('date_invoice', db.Unicode(25)),
    db.Column('description_invoice', db.Unicode(200)),
    db.Column('number_invoice', db.Unicode(50)),
    db.Column('organizationid_invoice', db.Numeric(15, 0, asdecimal=False)),
    db.Column('organizationname_invoice', db.Unicode(140)),
    db.Column('requester_invoice', db.Unicode(50)),
    db.Column('sourceinvoiceid_invoice', db.Unicode(150)),
    db.Column('totalamount_invoice', db.Numeric(38, 2)),
    db.Column('vendornumber_invoice', db.Unicode(30)),
    db.Column('vendorsitecode_invoice', db.Unicode(15)),
    db.Column('mdextractid_line', db.Unicode(30)),
    db.Column('accountnumber_line', db.Unicode(128)),
    db.Column('amount_line', db.Numeric(38, 2)),
    db.Column('description_line', db.Unicode(240)),
    db.Column('includestaxind_line', db.Unicode(1)),
    db.Column('linetypelookupcode_line', db.Unicode(25)),
    db.Column('productservicecode_line', db.Unicode(100)),
    db.Column('projectnumber_line', db.Unicode(160)),
    db.Column('reasoncode_line', db.Unicode(150)),
    db.Column('shiptolocationcode_line', db.Unicode(60)),
    db.Column('storenumber_line', db.Unicode(20)),
    db.Column('tasknumber_line', db.Unicode(160)),
    db.Column('taxcode_line', db.Unicode(15)),
    db.Column('status', db.Unicode(1)),
    db.Column('creation_date', db.DateTime),
    db.Column('update_date', db.DateTime),
    db.Column('creation_user', db.Unicode(10)),
    db.Column('update_user', db.Unicode(10))
)


t_t_outbound_gl = db.Table(
    't_outbound_gl',
    db.Column('mdextractdate_batch', db.Unicode(25)),
    db.Column('mdgroupcount_batch', db.Numeric(20, 0, asdecimal=False)),
    db.Column('mdgroupid_batch', db.Unicode(20)),
    db.Column('source_batch', db.Unicode(10)),
    db.Column('mdextractid_batch', db.Unicode(32)),
    db.Column('accountnumber_line', db.Unicode(6)),
    db.Column('batchid_line', db.Unicode(32), index=True),
    db.Column('category_line', db.Unicode(30)),
    db.Column('creditamount_line', db.Numeric(11, 2)),
    db.Column('currencycode_line', db.Unicode(10)),
    db.Column('debitamount_line', db.Numeric(11, 2)),
    db.Column('entrydate_line', db.Unicode(25)),
    db.Column('entrydescription_line', db.Unicode(30)),
    db.Column('entrylinedescription_line', db.Unicode(512), index=True),
    db.Column('fiscalperiod_line', db.Unicode(2)),
    db.Column('fiscalyear_line', db.Numeric(4, 0, asdecimal=False)),
    db.Column('future_line', db.Unicode(4)),
    db.Column('globalregioncode_line', db.Unicode(6)),
    db.Column('intercompany_line', db.Unicode(3)),
    db.Column('companycode_line', db.Unicode(3)),
    db.Column('responsibilitycenter_line', db.Unicode(6)),
    db.Column('status', db.Unicode(1), index=True),
    db.Column('creation_date', db.DateTime),
    db.Column('update_date', db.DateTime),
    db.Column('creation_user', db.Unicode(10)),
    db.Column('update_user', db.Unicode(10))
)


class TOutboundLog(db.Model):
    __tablename__ = 't_outbound_log'

    log_id = db.Column(db.Numeric(11, 0, asdecimal=False), primary_key=True)
    source = db.Column(db.Unicode(50))
    type = db.Column(db.Unicode(50))
    scan_time = db.Column(db.Unicode(50))
    groupid = db.Column(db.Unicode(50))
    send_time = db.Column(db.Unicode(50))
    status = db.Column(db.Unicode(50))


t_t_sun = db.Table(
    't_sun',
    db.Column('deptid', db.Integer),
    db.Column('pid', db.Integer),
    db.Column('lvl', db.Integer),
    db.Column('pth', db.String(200)),
    db.Column('flag', db.String(1))
)


t_temp_deptlist = db.Table(
    'temp_deptlist',
    db.Column('area', db.String(50)),
    db.Column('deptcd', db.String(50)),
    db.Column('deptdsc', db.String(50)),
    db.Column('tel', db.String(50)),
    db.Column('bdate', db.String(50)),
    db.Column('bizdt', db.DateTime)
)


t_test4 = db.Table(
    'test4',
    db.Column('id', db.Integer, nullable=False),
    db.Column('cd', db.String(20)),
    db.Column('secondcd', db.String(50)),
    db.Column('nm_l_zh', db.Unicode(100), nullable=False),
    db.Column('nm_l_ja', db.Unicode(100)),
    db.Column('nm_l_en', db.Unicode(100)),
    db.Column('snm_l_zh', db.Unicode(100), nullable=False),
    db.Column('snm_l_en', db.Unicode(100)),
    db.Column('snm_l_ja', db.Unicode(100)),
    db.Column('lnm_l_zh', db.Unicode(100)),
    db.Column('lnm_l_en', db.Unicode(100)),
    db.Column('lnm_l_ja', db.Unicode(100)),
    db.Column('spec', db.Unicode(30)),
    db.Column('plutp', db.String(10)),
    db.Column('bomtp', db.String(10)),
    db.Column('stkflg', db.String(1)),
    db.Column('storetp', db.Unicode(10), nullable=False),
    db.Column('plucatid', db.Integer),
    db.Column('pickcatid', db.Integer),
    db.Column('ordcatid', db.Integer),
    db.Column('salecatid', db.Integer),
    db.Column('catcd', db.String(20)),
    db.Column('cat1cd', db.String(20)),
    db.Column('cat2cd', db.String(20)),
    db.Column('cat3cd', db.String(20)),
    db.Column('cat4cd', db.String(20)),
    db.Column('pkuomcd', db.String(6), nullable=False),
    db.Column('lntp', db.String(2), nullable=False),
    db.Column('daypart', db.String(50)),
    db.Column('tastetp', db.String(10)),
    db.Column('plusize', db.String(20)),
    db.Column('smtscrcd', db.String(20)),
    db.Column('disseq', db.Integer),
    db.Column('agrillflg', db.String(1)),
    db.Column('grillflg', db.String(1)),
    db.Column('nprngrillflg', db.String(1)),
    db.Column('kvsmfyflg', db.String(1)),
    db.Column('kvssumflg', db.String(1)),
    db.Column('kvsndvmflg', db.String(1)),
    db.Column('kvsmainflg', db.String(1)),
    db.Column('pkvsc', db.String(20)),
    db.Column('pdc', db.String(20)),
    db.Column('pbgn', db.String(20)),
    db.Column('pbgp', db.String(20)),
    db.Column('pfgn', db.String(20)),
    db.Column('pfgp', db.String(20)),
    db.Column('ptitle', db.Unicode(50)),
    db.Column('rmdprio', db.String(10)),
    db.Column('rmdtitle', db.String(50)),
    db.Column('imgfilenm', db.String(100)),
    db.Column('diswflg', db.String(1)),
    db.Column('mdfflg', db.String(1)),
    db.Column('purflg', db.String(1)),
    db.Column('saleflg', db.String(1)),
    db.Column('saleolflg', db.String(1)),
    db.Column('presaleflg', db.String(1)),
    db.Column('discflg', db.String(1)),
    db.Column('ordflg', db.String(1)),
    db.Column('ordrqflg', db.String(1)),
    db.Column('ordmxflg', db.String(1)),
    db.Column('dlvflg', db.String(1)),
    db.Column('adjflg', db.String(1)),
    db.Column('invflg', db.String(1)),
    db.Column('dscflg', db.String(1)),
    db.Column('upkflg', db.String(1)),
    db.Column('cpngcflg', db.String(1)),
    db.Column('chkqtyflg', db.String(1)),
    db.Column('ivtcyctp', db.String(10)),
    db.Column('advordrule', db.String(10)),
    db.Column('tucyc', db.String(10)),
    db.Column('saftqtyrule', db.String(10)),
    db.Column('minsaftqty', db.Numeric(16, 6)),
    db.Column('maxsaftqty', db.Numeric(16, 6)),
    db.Column('lottp', db.String(10)),
    db.Column('lotsta', db.String(2)),
    db.Column('lotrule', db.String(2)),
    db.Column('lotiorule', db.String(2)),
    db.Column('lotexprule', db.String(2)),
    db.Column('sld', db.Integer),
    db.Column('expd', db.Integer),
    db.Column('defd', db.Integer),
    db.Column('mld', db.Integer),
    db.Column('pld', db.Integer),
    db.Column('bld1', db.Integer),
    db.Column('bld2', db.Integer),
    db.Column('bld3', db.Integer),
    db.Column('bld4', db.Integer),
    db.Column('bld5', db.Integer),
    db.Column('cpncrtp', db.String(10)),
    db.Column('cpnmd', db.String(10)),
    db.Column('cpntp', db.String(10)),
    db.Column('exattr1', db.String(100)),
    db.Column('exattr2', db.String(100)),
    db.Column('exattr3', db.String(100)),
    db.Column('exattr4', db.String(100)),
    db.Column('exattr5', db.String(100)),
    db.Column('exattr6', db.String(100)),
    db.Column('exattr7', db.String(100)),
    db.Column('exattr8', db.String(100)),
    db.Column('exattr9', db.String(100)),
    db.Column('exattr10', db.String(100)),
    db.Column('exattr11', db.String(100)),
    db.Column('exattr12', db.String(100)),
    db.Column('exattr13', db.String(100)),
    db.Column('exattr14', db.String(100)),
    db.Column('exattr15', db.String(100)),
    db.Column('exattr16', db.String(100)),
    db.Column('exattr17', db.String(100)),
    db.Column('exattr18', db.String(100)),
    db.Column('exattr19', db.String(100)),
    db.Column('exattr20', db.String(100)),
    db.Column('exattr21', db.String(100)),
    db.Column('exattr22', db.String(100)),
    db.Column('exattr23', db.String(100)),
    db.Column('exattr24', db.String(100)),
    db.Column('exattr25', db.String(100)),
    db.Column('exattr26', db.String(100)),
    db.Column('exattr27', db.String(100)),
    db.Column('exattr28', db.String(100)),
    db.Column('exattr29', db.String(100)),
    db.Column('exattr30', db.String(100)),
    db.Column('rmk', db.Unicode(255)),
    db.Column('updby', db.String(20)),
    db.Column('upddt', db.DateTime),
    db.Column('sta', db.String(3), nullable=False),
    db.Column('execflg', db.String(1)),
    db.Column('nxtsta', db.String(3)),
    db.Column('brand', db.String(20)),
    db.Column('matflg', db.String(1)),
    db.Column('plugrd', db.String(20)),
    db.Column('taxtp', db.String(10)),
    db.Column('addtxflg', db.String(1)),
    db.Column('cpncat', db.String(20)),
    db.Column('cacctcd', db.String(20))
)


t_tmp_2016 = db.Table(
    'tmp_2016',
    db.Column('col1', db.String(50)),
    db.Column('col2', db.String(50)),
    db.Column('col3', db.String(50))
)


t_tmp_20180530 = db.Table(
    'tmp_20180530',
    db.Column('transno', db.Numeric(20, 0, asdecimal=False), nullable=False, index=True)
)


t_tmp_advqty = db.Table(
    'tmp_advqty',
    db.Column('id', db.Numeric(12, 0, asdecimal=False)),
    db.Column('orddt', db.DateTime),
    db.Column('deptid', db.Integer),
    db.Column('pluid', db.Integer),
    db.Column('advordrule', db.String(10)),
    db.Column('tucyc', db.String(10)),
    db.Column('saleamt', db.Numeric(16, 2)),
    db.Column('useqty', db.Numeric(16, 6)),
    db.Column('qofkqty', db.Numeric(16, 6)),
    db.Column('arvdays', db.Integer),
    db.Column('narvdays', db.Integer),
    db.Column('saftrule', db.String(10)),
    db.Column('saftamt', db.Numeric(16, 2)),
    db.Column('arvamt', db.Numeric(16, 2)),
    db.Column('narvamt', db.Numeric(16, 2)),
    db.Column('dmdqty', db.Numeric(16, 6)),
    db.Column('stkqty', db.Numeric(16, 6)),
    db.Column('dlvqty', db.Numeric(16, 6)),
    db.Column('reqqty', db.Numeric(16, 6)),
    db.Column('uomcd', db.String(6)),
    db.Column('incqty', db.Numeric(16, 6)),
    db.Column('minqty', db.Numeric(16, 6)),
    db.Column('maxqty', db.Numeric(16, 6)),
    db.Column('advqty', db.Numeric(16, 6)),
    db.Column('updby', db.String(20)),
    db.Column('upddt', db.DateTime),
    db.Column('sta', db.String(3)),
    db.Column('execflg', db.String(1)),
    db.Column('nxtsta', db.String(3))
)


t_tmp_bas_plupotpl = db.Table(
    'tmp_bas_plupotpl',
    db.Column('vencd', db.String(50)),
    db.Column('plucd', db.String(50)),
    db.Column('taxrt', db.Numeric(6, 2)),
    db.Column('prc', db.Numeric(18, 6)),
    db.Column('taxtp', db.String(1))
)


t_tmp_billdtlmsg = db.Table(
    'tmp_billdtlmsg',
    db.Column('tbnm', db.String(30), nullable=False),
    db.Column('billid', db.Numeric(14, 0, asdecimal=False), nullable=False),
    db.Column('billdtlid', db.Numeric(14, 0, asdecimal=False), nullable=False),
    db.Column('lktp', db.String(10), nullable=False),
    db.Column('lkid', db.Integer, nullable=False),
    db.Column('msgcd', db.String(20), nullable=False),
    db.Column('exattr1', db.String(100)),
    db.Column('exattr2', db.String(100)),
    db.Column('exattr3', db.String(100)),
    db.Column('exattr4', db.String(100)),
    db.Column('exattr5', db.String(100)),
    db.Column('updby', db.String(20)),
    db.Column('upddt', db.DateTime),
    db.Index('idx_tmp_billdtlmsg', 'tbnm', 'billid')
)


t_tmp_bomimport = db.Table(
    'tmp_bomimport',
    db.Column('deptlktp', db.String(10)),
    db.Column('deptlkid', db.Integer),
    db.Column('bompluid', db.Integer),
    db.Column('stdt', db.DateTime),
    db.Column('eddt', db.DateTime),
    db.Column('bomtp', db.String(10)),
    db.Column('uomcd', db.String(6)),
    db.Column('inpluid', db.Integer),
    db.Column('inuomcd', db.String(6)),
    db.Column('qty', db.Numeric(16, 6)),
    db.Column('rmk', db.Unicode(255)),
    db.Column('updby', db.String(20)),
    db.Column('upddt', db.DateTime),
    db.Column('execflg', db.String(1))
)


t_tmp_cost_monthreport = db.Table(
    'tmp_cost_monthreport',
    db.Column('account_term', db.String(40)),
    db.Column('cost_id', db.String(50)),
    db.Column('net_no', db.String(10)),
    db.Column('net_name', db.String(100)),
    db.Column('net_type', db.String(2)),
    db.Column('plu_no', db.String(10)),
    db.Column('plu_name', db.String(100)),
    db.Column('item_type', db.String(20)),
    db.Column('begin_qty', db.Float),
    db.Column('last_cost', db.Float),
    db.Column('begin_amt', db.Float),
    db.Column('rev_qty', db.Float),
    db.Column('rev_amt', db.Float),
    db.Column('transferin_qty', db.Float),
    db.Column('adjustin_qty', db.Float),
    db.Column('sales_qty', db.Float),
    db.Column('transferout_qty', db.Float),
    db.Column('adjust_qty', db.Float),
    db.Column('end_qty', db.Float),
    db.Column('end_cost', db.Float),
    db.Column('end_amt', db.Float),
    db.Column('dtp_no', db.String(10)),
    db.Column('dtp_name', db.String(50)),
    db.Column('cat_no', db.String(10)),
    db.Column('cat_name', db.String(50)),
    db.Column('group_no', db.String(10)),
    db.Column('group_name', db.String(50)),
    db.Column('plu_type', db.String(50)),
    db.Column('transfer_cost', db.Float),
    db.Column('other_amt', db.Float),
    db.Column('enddate_qty', db.Float),
    db.Column('enddate_amt', db.Float),
    db.Column('deff_qty', db.Float),
    db.Column('deff_amt', db.Float)
)


t_tmp_deladj = db.Table(
    'tmp_deladj',
    db.Column('adjid', db.Numeric(12, 0, asdecimal=False)),
    db.Column('stkdt', db.DateTime)
)


t_tmp_dept = db.Table(
    'tmp_dept',
    db.Column('stcd', db.String(50)),
    db.Column('stnm', db.String(50)),
    db.Column('iscd1', db.String(50)),
    db.Column('isnm1', db.String(50)),
    db.Column('iscd2', db.String(50)),
    db.Column('isnm2', db.String(50)),
    db.Column('iscd3', db.String(50)),
    db.Column('isnm3', db.String(50))
)


t_tmp_district = db.Table(
    'tmp_district',
    db.Column('district_cd', db.String(50)),
    db.Column('district_name', db.String(50)),
    db.Column('district_pcd', db.String(50))
)


t_tmp_docreqimp = db.Table(
    'tmp_docreqimp',
    db.Column('billtp', db.String(10)),
    db.Column('psdt', db.DateTime),
    db.Column('deptid', db.Integer),
    db.Column('deptcd', db.String(20)),
    db.Column('deptnm', db.String(50)),
    db.Column('pluid', db.Integer),
    db.Column('plucd', db.String(20)),
    db.Column('plunm', db.String(50)),
    db.Column('qty', db.Numeric(16, 6)),
    db.Column('updby', db.String(20)),
    db.Column('upddt', db.DateTime),
    db.Column('flg', db.String(1))
)


class TmpEstOrderitem(db.Model):
    __tablename__ = 'tmp_est_orderitem'
    __table_args__ = (
        db.Index('idx_tmp_net_id', 'deptid', 'pluid', 'bizdt'),
    )

    id = db.Column(db.Integer, primary_key=True)
    deptid = db.Column(db.Integer)
    dcid = db.Column(db.Integer)
    pluid = db.Column(db.Integer)
    bizdt = db.Column(db.DateTime)
    advord_qty = db.Column(db.Numeric(14, 4), server_default=db.FetchedValue())
    radvord_qty = db.Column(db.Numeric(14, 4), server_default=db.FetchedValue())
    advmax_qty = db.Column(db.Numeric(14, 4), server_default=db.FetchedValue())
    radvmax_qty = db.Column(db.Numeric(14, 4), server_default=db.FetchedValue())
    minord_qty = db.Column(db.Numeric(14, 4), server_default=db.FetchedValue())
    maxord_qty = db.Column(db.Numeric(14, 4), server_default=db.FetchedValue())
    incord_qty = db.Column(db.Numeric(14, 4), server_default=db.FetchedValue())
    dlvstk_qty = db.Column(db.Numeric(14, 4), server_default=db.FetchedValue())
    ref_qty = db.Column(db.Numeric(14, 4), server_default=db.FetchedValue())
    planpdc_rate = db.Column(db.Numeric(14, 4), server_default=db.FetchedValue())
    lwk_qty = db.Column(db.Numeric(14, 4), server_default=db.FetchedValue())
    lday_qty = db.Column(db.Numeric(14, 4), server_default=db.FetchedValue())
    cday_qty = db.Column(db.Numeric(14, 4), server_default=db.FetchedValue())
    lwkrcv_qty = db.Column(db.Numeric(14, 4), server_default=db.FetchedValue())
    lwkti_qty = db.Column(db.Numeric(14, 4), server_default=db.FetchedValue())
    lwkto_qty = db.Column(db.Numeric(14, 4), server_default=db.FetchedValue())
    lmthsal_qty = db.Column(db.Numeric(14, 4), server_default=db.FetchedValue())
    lmthede_qty = db.Column(db.Numeric(14, 4), server_default=db.FetchedValue())
    lmthbgn_qty = db.Column(db.Numeric(14, 4), server_default=db.FetchedValue())
    lmthend_qty = db.Column(db.Numeric(14, 4), server_default=db.FetchedValue())
    lmthrcv_qty = db.Column(db.Numeric(14, 4), server_default=db.FetchedValue())
    lmthti_qty = db.Column(db.Numeric(14, 4), server_default=db.FetchedValue())
    lmthto_qty = db.Column(db.Numeric(14, 4), server_default=db.FetchedValue())
    splanpdc_rate = db.Column(db.Numeric(14, 4), server_default=db.FetchedValue())
    slwkepd_qty = db.Column(db.Numeric(14, 4), server_default=db.FetchedValue())
    slmthinv_qty = db.Column(db.Numeric(14, 4), server_default=db.FetchedValue())
    stermrcv_qty = db.Column(db.Numeric(14, 4), server_default=db.FetchedValue())
    slmthinv_date = db.Column(db.DateTime)
    thismthsal_qty = db.Column(db.Numeric(14, 4), server_default=db.FetchedValue())
    thismthede_qty = db.Column(db.Numeric(14, 4), server_default=db.FetchedValue())
    cal_no = db.Column(db.String(20))
    is_cal = db.Column(db.String(1), server_default=db.FetchedValue())
    sta = db.Column(db.String(1), server_default=db.FetchedValue())
    update_date = db.Column(db.DateTime, server_default=db.FetchedValue())
    update_by = db.Column(db.String(50))
    is_delete = db.Column(db.String(1), server_default=db.FetchedValue())
    max_a = db.Column(db.Numeric(14, 4), server_default=db.FetchedValue())
    onway_qty = db.Column(db.Numeric(14, 4), server_default=db.FetchedValue())


t_tmp_est_orderonway = db.Table(
    'tmp_est_orderonway',
    db.Column('deptid', db.Integer),
    db.Column('pluid', db.Integer),
    db.Column('lockqty', db.Numeric(16, 6))
)


t_tmp_explog = db.Table(
    'tmp_explog',
    db.Column('strcode', db.String(2000)),
    db.Column('rmk', db.String(2000)),
    db.Column('strstep', db.String(20))
)


class TmpFinCostmphi(db.Model):
    __tablename__ = 'tmp_fin_costmphis'

    ptid = db.Column(db.Integer)
    yearno = db.Column(db.Integer, primary_key=True, nullable=False)
    monthno = db.Column(db.Integer, primary_key=True, nullable=False)
    deptlktp = db.Column(db.String(10), primary_key=True, nullable=False)
    deptlkid = db.Column(db.Integer, primary_key=True, nullable=False)
    pluid = db.Column(db.Integer, primary_key=True, nullable=False)
    lotno = db.Column(db.String(20), nullable=False, server_default=db.FetchedValue())
    bgnqty = db.Column(db.Numeric(18, 6))
    bgncost = db.Column(db.Numeric(18, 6))
    bgnamt = db.Column(db.Numeric(18, 6))
    purqty = db.Column(db.Numeric(18, 6))
    puramt = db.Column(db.Numeric(18, 6))
    feeamt = db.Column(db.Numeric(18, 6))
    invadjamt = db.Column(db.Numeric(18, 6))
    puradjamt = db.Column(db.Numeric(18, 6))
    txoqty = db.Column(db.Numeric(18, 6))
    txiqty = db.Column(db.Numeric(18, 6))
    adjqty = db.Column(db.Numeric(18, 6))
    bomoutqty = db.Column(db.Numeric(18, 6))
    bomcsamt = db.Column(db.Numeric(20, 6))
    bomprcinqty = db.Column(db.Numeric(18, 6))
    saleqty = db.Column(db.Numeric(18, 6))
    dlvqty = db.Column(db.Numeric(18, 6))
    rcvqty = db.Column(db.Numeric(18, 6))
    invqty = db.Column(db.Numeric(18, 6))
    endqty = db.Column(db.Numeric(18, 6))
    endcost = db.Column(db.Numeric(18, 6))
    endamt = db.Column(db.Numeric(18, 6))
    enddtqty = db.Column(db.Numeric(18, 6))
    enddtamt = db.Column(db.Numeric(18, 6))
    defqty = db.Column(db.Numeric(18, 6))
    defamt = db.Column(db.Numeric(18, 6))
    estprc = db.Column(db.Numeric(20, 6))
    accendamt = db.Column(db.Numeric(18, 6))
    upddt = db.Column(db.DateTime)
    crcd = db.Column(db.String(3), server_default=db.FetchedValue())
    sta = db.Column(db.String(3))
    bomadjinqty = db.Column(db.Numeric(18, 6), server_default=db.FetchedValue())
    bomsaleinqty = db.Column(db.Numeric(18, 6), server_default=db.FetchedValue())


t_tmp_fin_purpt = db.Table(
    'tmp_fin_purpt',
    db.Column('ptid', db.Integer),
    db.Column('yearno', db.Integer, nullable=False),
    db.Column('monthno', db.Integer, nullable=False),
    db.Column('deptlktp', db.String(10), nullable=False),
    db.Column('deptlkid', db.Integer, nullable=False),
    db.Column('venid', db.Integer),
    db.Column('pluid', db.Integer),
    db.Column('amt', db.Numeric(20, 6)),
    db.Column('taxamt', db.Numeric(20, 6)),
    db.Column('crcd', db.String(3), server_default=db.FetchedValue()),
    db.Column('upddt', db.DateTime)
)


t_tmp_h1stk = db.Table(
    'tmp_h1stk',
    db.Column('plucd', db.String(20)),
    db.Column('qty', db.Numeric(18, 6)),
    db.Column('stktp', db.String(20)),
    db.Column('pt', db.String(20)),
    db.Column('qty1', db.Numeric(18, 6)),
    db.Column('qty2', db.Numeric(18, 6)),
    db.Column('prc', db.Numeric(18, 6)),
    db.Column('deptcd', db.String(20)),
    db.Column('stkdt', db.DateTime)
)


class TmpH1stkend(db.Model):
    __tablename__ = 'tmp_h1stkend'

    deptcd = db.Column(db.String(20), primary_key=True, nullable=False)
    plucd = db.Column(db.String(20), primary_key=True, nullable=False)
    bizdt = db.Column(db.DateTime, primary_key=True, nullable=False)
    endqty = db.Column(db.Numeric(18, 6))


t_tmp_hr = db.Table(
    'tmp_hr',
    db.Column('personid', db.String(50)),
    db.Column('usercode', db.String(20)),
    db.Column('username', db.String(50)),
    db.Column('gender', db.String(20)),
    db.Column('iswage', db.String(20)),
    db.Column('isfulltime', db.String(20)),
    db.Column('levelcode', db.String(20)),
    db.Column('levelname', db.String(50)),
    db.Column('status', db.String(20)),
    db.Column('regname', db.String(20)),
    db.Column('groupname', db.String(50)),
    db.Column('detid', db.String(20)),
    db.Column('detname', db.String(50)),
    db.Column('positioncode', db.String(20)),
    db.Column('positionname', db.String(50)),
    db.Column('joindate', db.String(20)),
    db.Column('resigndate', db.String(50)),
    db.Column('updatedate', db.String(50)),
    db.Column('gongzhong', db.String(50)),
    db.Column('inipositionname', db.String(50))
)


class TmpImp(db.Model):
    __tablename__ = 'tmp_imp'

    id = db.Column(db.Numeric(14, 0, asdecimal=False), primary_key=True)
    coid = db.Column(db.Integer)
    deptid = db.Column(db.Integer)
    orddt = db.Column(db.DateTime)
    billtp = db.Column(db.String(10), nullable=False)
    filenm = db.Column(db.String(100))
    imptitle = db.Column(db.String(200), server_default=db.FetchedValue())
    rmk = db.Column(db.String(255))
    updby = db.Column(db.String(20))
    upddt = db.Column(db.DateTime)
    sta = db.Column(db.String(3), nullable=False)
    execflg = db.Column(db.String(1))
    nxtsta = db.Column(db.String(3))
    stdt = db.Column(db.DateTime)
    eddt = db.Column(db.DateTime)


class TmpImpdtl(db.Model):
    __tablename__ = 'tmp_impdtl'

    id = db.Column(db.Numeric(14, 0, asdecimal=False), primary_key=True)
    impid = db.Column(db.Numeric(14, 0, asdecimal=False), nullable=False, index=True)
    impdttp = db.Column(db.String(30))
    col1 = db.Column(db.String(100))
    col2 = db.Column(db.String(100))
    col3 = db.Column(db.String(100))
    col4 = db.Column(db.String(100))
    col5 = db.Column(db.String(100))
    col6 = db.Column(db.String(100))
    col7 = db.Column(db.String(100))
    col8 = db.Column(db.String(100))
    col9 = db.Column(db.String(100))
    col10 = db.Column(db.String(100))
    col11 = db.Column(db.String(100))
    col12 = db.Column(db.String(100))
    col13 = db.Column(db.String(100))
    col14 = db.Column(db.String(100))
    col15 = db.Column(db.String(100))
    col16 = db.Column(db.String(100))
    col17 = db.Column(db.String(100))
    col18 = db.Column(db.String(100))
    col19 = db.Column(db.String(100))
    col20 = db.Column(db.String(100))
    col21 = db.Column(db.String(100))
    col22 = db.Column(db.String(100))
    col23 = db.Column(db.String(100))
    col24 = db.Column(db.String(100))
    col25 = db.Column(db.String(100))
    col26 = db.Column(db.String(100))
    col27 = db.Column(db.String(100))
    col28 = db.Column(db.String(100))
    col29 = db.Column(db.String(100))
    col30 = db.Column(db.String(100))
    col31 = db.Column(db.String(100))
    col32 = db.Column(db.String(100))
    col33 = db.Column(db.String(100))
    col34 = db.Column(db.String(100))
    col35 = db.Column(db.String(100))
    col36 = db.Column(db.String(100))
    col37 = db.Column(db.String(100))
    col38 = db.Column(db.String(100))
    col39 = db.Column(db.String(100))
    col40 = db.Column(db.String(100))
    rmk = db.Column(db.String(255))
    updby = db.Column(db.String(20))
    upddt = db.Column(db.DateTime)
    sta = db.Column(db.String(3), server_default=db.FetchedValue())
    rid = db.Column(db.Numeric(16, 0, asdecimal=False))


t_tmp_lockqty = db.Table(
    'tmp_lockqty',
    db.Column('bizdt', db.DateTime),
    db.Column('deptid', db.Integer),
    db.Column('pluid', db.Integer),
    db.Column('uomcd', db.String(6)),
    db.Column('lockqty', db.Numeric(16, 6))
)


t_tmp_logmonitor = db.Table(
    'tmp_logmonitor',
    db.Column('pid', db.Integer),
    db.Column('storecode', db.String(50)),
    db.Column('net_name', db.Unicode(50), nullable=False),
    db.Column('wy_type', db.Unicode(50), nullable=False),
    db.Column('cur_value', db.String(200)),
    db.Column('bizdt', db.DateTime),
    db.Column('net_rmk', db.String(1000)),
    db.Column('wy_desc', db.String(200)),
    db.Column('rmk', db.String(1000)),
    db.Column('update_date', db.DateTime),
    db.Column('flag', db.String(1))
)


t_tmp_monthamt = db.Table(
    'tmp_monthamt',
    db.Column('ptid', db.Integer),
    db.Column('pluid', db.Integer),
    db.Column('amt', db.Numeric(18, 2)),
    db.Column('tp', db.String(10)),
    db.Column('taxamt', db.Numeric(18, 2))
)


t_tmp_ordplu = db.Table(
    'tmp_ordplu',
    db.Column('plucd', db.String(50))
)


t_tmp_plu = db.Table(
    'tmp_plu',
    db.Column('plucd', db.String(50)),
    db.Column('pluname', db.String(200))
)


t_tmp_plureqqty = db.Table(
    'tmp_plureqqty',
    db.Column('systp', db.String(10)),
    db.Column('pluid', db.Integer),
    db.Column('qty', db.Numeric(20, 6))
)


t_tmp_stk_bominlist = db.Table(
    'tmp_stk_bominlist',
    db.Column('bomlistid', db.Numeric(14, 0, asdecimal=False)),
    db.Column('deptid', db.Integer, nullable=False),
    db.Column('pluid', db.Integer, nullable=False),
    db.Column('locid', db.Integer, nullable=False),
    db.Column('lotno', db.String(20)),
    db.Column('uomcd', db.String(6)),
    db.Column('qty', db.Numeric(16, 6), nullable=False),
    db.Column('crcd', db.String(3)),
    db.Column('prc', db.Numeric(16, 6), nullable=False),
    db.Column('prc1', db.Numeric(16, 6)),
    db.Column('txrt', db.Numeric(6, 2)),
    db.Column('upddt', db.DateTime)
)


t_tmp_stk_bomlist = db.Table(
    'tmp_stk_bomlist',
    db.Column('id', db.Numeric(14, 0, asdecimal=False), nullable=False),
    db.Column('stktp', db.String(3), nullable=False),
    db.Column('stkdt', db.DateTime),
    db.Column('actdt', db.DateTime),
    db.Column('billid', db.Numeric(14, 0, asdecimal=False), nullable=False),
    db.Column('billdtlid', db.Numeric(14, 0, asdecimal=False), nullable=False),
    db.Column('billtp', db.String(10), nullable=False),
    db.Column('deptid', db.Integer, nullable=False),
    db.Column('opplktp', db.String(1)),
    db.Column('opplkid', db.Integer),
    db.Column('pluid', db.Integer, nullable=False),
    db.Column('locid', db.Integer, nullable=False),
    db.Column('lotno', db.String(20)),
    db.Column('uomcd', db.String(6)),
    db.Column('qty', db.Numeric(16, 6), nullable=False),
    db.Column('crcd', db.String(3)),
    db.Column('prc', db.Numeric(16, 6), nullable=False),
    db.Column('prc1', db.Numeric(16, 6)),
    db.Column('txrt', db.Numeric(6, 2)),
    db.Column('upddt', db.DateTime),
    db.Column('sta', db.String(3), nullable=False),
    db.Column('billrsn', db.String(20))
)


t_tmp_stk_list = db.Table(
    'tmp_stk_list',
    db.Column('billdtlid', db.Numeric(14, 0, asdecimal=False), nullable=False),
    db.Column('stktp', db.String(3), nullable=False),
    db.Column('stkdt', db.DateTime),
    db.Column('actdt', db.DateTime),
    db.Column('billid', db.Numeric(14, 0, asdecimal=False), nullable=False),
    db.Column('billtp', db.String(10), nullable=False),
    db.Column('deptid', db.Integer, nullable=False),
    db.Column('opplktp', db.String(1)),
    db.Column('opplkid', db.Integer),
    db.Column('pluid', db.Integer, nullable=False),
    db.Column('locid', db.Integer, nullable=False),
    db.Column('lotno', db.String(20)),
    db.Column('uomcd', db.String(6)),
    db.Column('qty', db.Numeric(16, 6), nullable=False),
    db.Column('crcd', db.String(3)),
    db.Column('prc', db.Numeric(16, 6), nullable=False),
    db.Column('prc1', db.Numeric(16, 6)),
    db.Column('txrt', db.Numeric(6, 2)),
    db.Column('upddt', db.DateTime),
    db.Column('billrsn', db.String(20))
)


t_tmp_stk_storage = db.Table(
    'tmp_stk_storage',
    db.Column('deptid', db.Integer),
    db.Column('pluid', db.Integer),
    db.Column('locid', db.Integer),
    db.Column('lotno', db.String(20)),
    db.Column('uomcd', db.String(6)),
    db.Column('bookqty', db.Numeric(16, 6)),
    db.Column('lockqty', db.Numeric(16, 6)),
    db.Column('avlqty', db.Numeric(16, 6)),
    db.Column('reqqty', db.Numeric(16, 6)),
    db.Column('reqavlqty', db.Numeric(16, 6)),
    db.Column('dlviqty', db.Numeric(16, 6)),
    db.Column('dlvoqty', db.Numeric(16, 6)),
    db.Column('csprc', db.Numeric(16, 4)),
    db.Column('crcd', db.String(3)),
    db.Column('sta', db.String(3))
)


t_tmp_sys_dept = db.Table(
    'tmp_sys_dept',
    db.Column('id', db.Integer, nullable=False),
    db.Column('cd', db.String(20), nullable=False),
    db.Column('nm_l_zh', db.Unicode(50), nullable=False),
    db.Column('secondcd', db.String(20))
)


t_tmp_t = db.Table(
    'tmp_t',
    db.Column('transno', db.String(20))
)


t_tmp_t_outbound_gl_dtl = db.Table(
    'tmp_t_outbound_gl_dtl',
    db.Column('voucher_batch_id', db.String(20)),
    db.Column('voucher_code', db.String(20)),
    db.Column('ptid', db.Integer, index=True),
    db.Column('deptcd', db.String(20)),
    db.Column('vencd', db.String(20)),
    db.Column('bizdt', db.String(20)),
    db.Column('actdt', db.String(20)),
    db.Column('plucd', db.String(50)),
    db.Column('qty', db.Numeric(20, 6)),
    db.Column('amount_line', db.Numeric(20, 6)),
    db.Column('amount2_line', db.Numeric(20, 6)),
    db.Column('fee_line', db.Numeric(20, 6)),
    db.Column('fee2_line', db.Numeric(20, 6)),
    db.Column('category_l1', db.String(10)),
    db.Column('category_l2', db.String(10)),
    db.Column('category_l3', db.String(10)),
    db.Column('plu_type', db.String(1)),
    db.Column('reason_type', db.String(100)),
    db.Column('remark1', db.String(50)),
    db.Column('remark2', db.String(50)),
    db.Column('page_no', db.Integer),
    db.Column('page_row_no', db.Integer),
    db.Column('page_group_count', db.Integer),
    db.Column('rn', db.Integer),
    db.Column('acccd', db.String(10)),
    db.Column('created', db.DateTime, server_default=db.FetchedValue()),
    db.Column('status', db.Integer, server_default=db.FetchedValue()),
    db.Column('dacccd', db.String(10)),
    db.Column('cacccd', db.String(10)),
    db.Column('major_group_no', db.String(30)),
    db.Index('tmp_t_outboud_gl_dtl_index_1', 'voucher_batch_id', 'voucher_code')
)


t_tmp_test = db.Table(
    'tmp_test',
    db.Column('pluid', db.String(200)),
    db.Column('data2', db.String(200)),
    db.Column('data3', db.String(200)),
    db.Column('data4', db.String(200)),
    db.Column('data5', db.String(200)),
    db.Column('data6', db.String(200)),
    db.Column('data7', db.String(200)),
    db.Column('data8', db.String(200)),
    db.Column('data9', db.String(200))
)


t_tmp_transop = db.Table(
    'tmp_transop',
    db.Column('transno', db.Numeric(20, 0, asdecimal=False)),
    db.Column('newctrno', db.Numeric(20, 0, asdecimal=False)),
    db.Column('oldctrno', db.Numeric(20, 0, asdecimal=False)),
    db.Column('id', db.Integer),
    db.Column('cnt', db.Integer, server_default=db.FetchedValue())
)


t_tmp_yulei01 = db.Table(
    'tmp_yulei01',
    db.Column('businessday', db.String(10)),
    db.Column('salesamount', db.Numeric(19, 4)),
    db.Column('salesqty', db.Integer),
    db.Column('globalstorenumber', db.String(20)),
    db.Column('store', db.Unicode(102)),
    db.Column('itemcode', db.String(20)),
    db.Column('itemdesc', db.Unicode(201)),
    db.Column('majorgroup', db.Unicode(50), nullable=False),
    db.Column('familygroup', db.Unicode(50), nullable=False),
    db.Column('salescost', db.Numeric(asdecimal=False)),
    db.Column('city', db.Unicode(50))
)


t_tmp_yulei02 = db.Table(
    'tmp_yulei02',
    db.Column('businessday', db.String(10)),
    db.Column('salesamount', db.Numeric(19, 4)),
    db.Column('salesqty', db.Integer),
    db.Column('globalstorenumber', db.String(20)),
    db.Column('store', db.Unicode(102)),
    db.Column('itemcode', db.String(20)),
    db.Column('itemdesc', db.Unicode(201)),
    db.Column('majorgroup', db.Unicode(50), nullable=False),
    db.Column('familygroup', db.Unicode(50), nullable=False),
    db.Column('salescost', db.Numeric(asdecimal=False)),
    db.Column('city', db.Unicode(50))
)


t_tmp_yulei03 = db.Table(
    'tmp_yulei03',
    db.Column('businessday', db.String(10)),
    db.Column('salesamount', db.Numeric(19, 4)),
    db.Column('salesqty', db.Integer),
    db.Column('globalstorenumber', db.String(20)),
    db.Column('store', db.Unicode(102)),
    db.Column('itemcode', db.String(20)),
    db.Column('itemdesc', db.Unicode(201)),
    db.Column('majorgroup', db.Unicode(50), nullable=False),
    db.Column('familygroup', db.Unicode(50), nullable=False),
    db.Column('salescost', db.Numeric(asdecimal=False)),
    db.Column('city', db.Unicode(50))
)


t_tmp_yulei04 = db.Table(
    'tmp_yulei04',
    db.Column('businessday', db.String(10)),
    db.Column('salesamount', db.Numeric(19, 4)),
    db.Column('salesqty', db.Integer),
    db.Column('globalstorenumber', db.String(20)),
    db.Column('store', db.Unicode(102)),
    db.Column('itemcode', db.String(20)),
    db.Column('itemdesc', db.Unicode(201)),
    db.Column('majorgroup', db.Unicode(50), nullable=False),
    db.Column('familygroup', db.Unicode(50), nullable=False),
    db.Column('salescost', db.Numeric(asdecimal=False)),
    db.Column('city', db.Unicode(50))
)


t_tmp_yulei1 = db.Table(
    'tmp_yulei1',
    db.Column('tillcd', db.Numeric(asdecimal=False)),
    db.Column('saleid', db.Numeric(asdecimal=False)),
    db.Column('deptcd', db.Numeric(asdecimal=False)),
    db.Column('tradedt', db.DateTime)
)


t_tmp_yulei2 = db.Table(
    'tmp_yulei2',
    db.Column('id', db.Numeric(12, 0, asdecimal=False), nullable=False)
)


t_tmp_yulei3 = db.Table(
    'tmp_yulei3',
    db.Column('businessday', db.String(10)),
    db.Column('salesamount', db.Numeric(19, 4)),
    db.Column('salesqty', db.Integer),
    db.Column('globalstorenumber', db.String(20)),
    db.Column('store', db.Unicode(102)),
    db.Column('itemcode', db.String(20)),
    db.Column('itemdesc', db.Unicode(201)),
    db.Column('majorgroup', db.Unicode(50), nullable=False),
    db.Column('familygroup', db.Unicode(50), nullable=False)
)


t_tmp_yulei_itemlist = db.Table(
    'tmp_yulei_itemlist',
    db.Column('itemcode', db.String(6))
)


t_tmp_yulei_yinye = db.Table(
    'tmp_yulei_yinye',
    db.Column('itemcode', db.String(20)),
    db.Column('itemname', db.String(100)),
    db.Column('storecode', db.String(20)),
    db.Column('storename', db.String(100)),
    db.Column('stockquantity', db.String(20)),
    db.Column('att', db.String(20)),
    db.Column('rdo', db.String(50)),
    db.Column('om', db.String(50)),
    db.Column('dm', db.String(50)),
    db.Column('rdo_code', db.String(20)),
    db.Column('om_code', db.String(20)),
    db.Column('dm_code', db.String(20))
)


t_tmp_yulei_yinye_itemlist = db.Table(
    'tmp_yulei_yinye_itemlist',
    db.Column('item', db.String(20)),
    db.Column('att1', db.String(20))
)


t_ty = db.Table(
    'ty',
    db.Column('transno', db.Numeric(20, 0, asdecimal=False), nullable=False),
    db.Column('bizdt', db.DateTime),
    db.Column('ctrno', db.Numeric(20, 0, asdecimal=False)),
    db.Column('disctp', db.String(1)),
    db.Column('disccd', db.String(4)),
    db.Column('discamt', db.Numeric(asdecimal=False))
)


t_ty2 = db.Table(
    'ty2',
    db.Column('transno', db.Numeric(20, 0, asdecimal=False), nullable=False),
    db.Column('bizdt', db.DateTime),
    db.Column('tradedt', db.DateTime),
    db.Column('ctrno', db.Numeric(20, 0, asdecimal=False)),
    db.Column('plucd', db.String(20)),
    db.Column('pluid', db.Integer),
    db.Column('pluprc', db.Numeric(19, 4)),
    db.Column('grossamt', db.Numeric(19, 4)),
    db.Column('netamt', db.Numeric(asdecimal=False)),
    db.Column('discamt', db.Numeric(asdecimal=False)),
    db.Column('curqty', db.Numeric(19, 4)),
    db.Column('billuom', db.Integer),
    db.Column('convrate', db.Numeric(16, 6)),
    db.Column('pkuom', db.Integer),
    db.Column('transtp', db.String(10)),
    db.Column('strcomment', db.String(100)),
    db.Column('msr', db.Numeric(19, 4)),
    db.Column('giftno', db.String(30))
)


t_v_bas_hareainfo = db.Table(
    'v_bas_hareainfo',
    db.Column('pid', db.String(1)),
    db.Column('areacode', db.String(100)),
    db.Column('areaname', db.Unicode(50), nullable=False),
    db.Column('areaid', db.String(100)),
    db.Column('dp_code', db.String(100)),
    db.Column('dp_name', db.Unicode(50), nullable=False)
)


t_v_bas_recruit_user = db.Table(
    'v_bas_recruit_user',
    db.Column('pid', db.String(1)),
    db.Column('usercode', db.String(20)),
    db.Column('username', db.Unicode(50), nullable=False),
    db.Column('email', db.String(32)),
    db.Column('is_delete', db.Numeric(asdecimal=False)),
    db.Column('remark', db.Unicode(255)),
    db.Column('create_date', db.DateTime),
    db.Column('create_by', db.String(30)),
    db.Column('update_date', db.DateTime),
    db.Column('update_by', db.String(30)),
    db.Column('node_code', db.String(0))
)


t_v_bas_uom = db.Table(
    'v_bas_uom',
    db.Column('cd', db.String(50), nullable=False),
    db.Column('nm_l_zh', db.Unicode(50), nullable=False)
)


t_v_doc_rvrformail = db.Table(
    'v_doc_rvrformail',
    db.Column('rvr_no', db.Numeric(12, 0, asdecimal=False)),
    db.Column('dhlso', db.String(20)),
    db.Column('????', db.String(6)),
    db.Column('RVR??', db.Unicode(50)),
    db.Column('?????', db.Unicode(50)),
    db.Column('SBI??', db.String(100)),
    db.Column('??', db.String(100)),
    db.Column('???', db.Numeric(asdecimal=False)),
    db.Column('??????', db.DateTime)
)


t_v_doc_rvrformail1 = db.Table(
    'v_doc_rvrformail1',
    db.Column('rvr_no', db.Numeric(12, 0, asdecimal=False)),
    db.Column('dhlso', db.String(20)),
    db.Column('????', db.String(6)),
    db.Column('RVR??', db.Unicode(50)),
    db.Column('?????', db.Unicode(50)),
    db.Column('SBI??', db.String(100)),
    db.Column('??', db.String(100)),
    db.Column('???', db.Numeric(asdecimal=False)),
    db.Column('??????', db.DateTime)
)


t_v_dw_depinfo = db.Table(
    'v_dw_depinfo',
    db.Column('word_no', db.String(40)),
    db.Column('word_name', db.Unicode(50), nullable=False)
)


t_v_dw_itemmaster = db.Table(
    'v_dw_itemmaster',
    db.Column('plu_no', db.String(20)),
    db.Column('sbi_code', db.String(100)),
    db.Column('plu_namechs', db.Unicode(100), nullable=False),
    db.Column('plu_nameeng', db.Unicode(100)),
    db.Column('cat_no_1', db.String(20)),
    db.Column('cat_name_1', db.Unicode(50), nullable=False),
    db.Column('cat_no_2', db.String(20)),
    db.Column('cat_name_2', db.Unicode(50), nullable=False),
    db.Column('cat_no_3', db.String(20)),
    db.Column('cat_name_3', db.Unicode(50), nullable=False),
    db.Column('order_unit', db.String(6), nullable=False),
    db.Column('order_unit_name', db.Unicode(50), nullable=False),
    db.Column('pk_unit', db.String(6), nullable=False),
    db.Column('pk_unit_name', db.Unicode(50), nullable=False),
    db.Column('isadd', db.String(1)),
    db.Column('word_no', db.String(0)),
    db.Column('word_name', db.String(0)),
    db.Column('create_date', db.DateTime),
    db.Column('update_date', db.DateTime)
)


t_v_dw_miscellaneous = db.Table(
    'v_dw_miscellaneous',
    db.Column('net_no', db.String(20), nullable=False),
    db.Column('net_name', db.String(250)),
    db.Column('work_area_fm', db.String(10)),
    db.Column('businessdate', db.DateTime),
    db.Column('itemcode', db.String(50)),
    db.Column('itemname', db.String(250)),
    db.Column('stk_name', db.String(50)),
    db.Column('qty', db.Float)
)


t_v_dw_netinfo = db.Table(
    'v_dw_netinfo',
    db.Column('net_no', db.String(20)),
    db.Column('net_name', db.Unicode(50)),
    db.Column('work_area_zone', db.Unicode(250)),
    db.Column('word_name_city', db.Unicode(50)),
    db.Column('work_area_do', db.String(100)),
    db.Column('word_name_district', db.Unicode(50)),
    db.Column('work_area_fm', db.String(50)),
    db.Column('dm_code', db.String(100)),
    db.Column('word_name_area', db.Unicode(50)),
    db.Column('om_area', db.String(50)),
    db.Column('om_code', db.String(100)),
    db.Column('net_address', db.Unicode(100)),
    db.Column('net_zipcode', db.String(20)),
    db.Column('status', db.String(3)),
    db.Column('net_name_eng', db.Unicode(50)),
    db.Column('telphone', db.String(30)),
    db.Column('fax', db.String(30)),
    db.Column('busi_size', db.Numeric(asdecimal=False)),
    db.Column('stock_size', db.Numeric(asdecimal=False)),
    db.Column('seat_qty', db.Numeric(asdecimal=False)),
    db.Column('opendate', db.DateTime),
    db.Column('state', db.Unicode(50))
)


t_v_dw_ominfo = db.Table(
    'v_dw_ominfo',
    db.Column('areacode', db.String(100)),
    db.Column('areaname', db.Unicode(50), nullable=False),
    db.Column('dp_code', db.String(100)),
    db.Column('dp_name', db.Unicode(50), nullable=False)
)


t_v_dw_stockdiff = db.Table(
    'v_dw_stockdiff',
    db.Column('businessmonth', db.String(20)),
    db.Column('net_no', db.String(20), nullable=False),
    db.Column('net_name', db.String(50)),
    db.Column('work_area_fm', db.String(10)),
    db.Column('plu_no', db.String(10)),
    db.Column('sbi_code', db.String(20)),
    db.Column('plu_namechs', db.String(150)),
    db.Column('lock_qty', db.Numeric(18, 6)),
    db.Column('input_qty', db.Numeric(18, 6)),
    db.Column('end_qty', db.Numeric(18, 6))
)


t_v_fd_netinfo = db.Table(
    'v_fd_netinfo',
    db.Column('net_no', db.String(20), nullable=False),
    db.Column('net_name', db.Unicode(50), nullable=False),
    db.Column('word_no', db.String(50)),
    db.Column('dm_code', db.String(100)),
    db.Column('word_name_area', db.Unicode(50)),
    db.Column('om_area', db.String(50)),
    db.Column('areaname', db.Unicode(50)),
    db.Column('net_address', db.Unicode(100)),
    db.Column('status', db.String(3))
)


t_v_if_msr_disc = db.Table(
    'v_if_msr_disc',
    db.Column('discounttypeid', db.String(10)),
    db.Column('nm_l_zh', db.String(50), nullable=False),
    db.Column('quantity', db.Numeric(19, 4)),
    db.Column('amount', db.Numeric(19, 4)),
    db.Column('tax', db.Numeric(asdecimal=False)),
    db.Column('inttransnum', db.Numeric(20, 0, asdecimal=False), nullable=False),
    db.Column('ctrcode', db.Numeric(20, 0, asdecimal=False))
)


t_v_if_msr_tender = db.Table(
    'v_if_msr_tender',
    db.Column('tendartypeid', db.String(10)),
    db.Column('tdramt', db.Numeric(asdecimal=False)),
    db.Column('description', db.String(50), nullable=False),
    db.Column('inttransnum', db.Numeric(20, 0, asdecimal=False))
)


t_v_if_msr_trans = db.Table(
    'v_if_msr_trans',
    db.Column('inttransnum', db.Numeric(20, 0, asdecimal=False)),
    db.Column('strtradecode', db.String(10)),
    db.Column('dtmsaledatetime', db.DateTime),
    db.Column('strtillcode', db.String(20)),
    db.Column('intsaleid', db.Integer),
    db.Column('strnotes', db.String(20)),
    db.Column('cursales', db.Numeric(asdecimal=False)),
    db.Column('intoperatorid', db.String(10)),
    db.Column('strusername', db.Unicode(50)),
    db.Column('stranswer2', db.String(0)),
    db.Column('strordercode', db.String(20)),
    db.Column('dblqtysold', db.Numeric(asdecimal=False)),
    db.Column('ctrcode', db.Numeric(20, 0, asdecimal=False)),
    db.Column('strsaletype', db.String(10)),
    db.Column('strcomment', db.String(100)),
    db.Column('strtype', db.String(10)),
    db.Column('lg', db.Numeric(asdecimal=False)),
    db.Column('cardnotransferinttransnum', db.Numeric(20, 0, asdecimal=False)),
    db.Column('intdiscountcode', db.Numeric(asdecimal=False)),
    db.Column('salesstandinctax', db.Numeric(asdecimal=False))
)


t_v_if_msr_trans_hhs = db.Table(
    'v_if_msr_trans_hhs',
    db.Column('inttransnum', db.Numeric(20, 0, asdecimal=False)),
    db.Column('strtradecode', db.String(10)),
    db.Column('dtmsaledatetime', db.DateTime),
    db.Column('strtillcode', db.String(20)),
    db.Column('intsaleid', db.Integer),
    db.Column('strnotes', db.String(20)),
    db.Column('cursales', db.Numeric(asdecimal=False)),
    db.Column('intoperatorid', db.String(10)),
    db.Column('strusername', db.Unicode(50)),
    db.Column('stranswer2', db.String(0)),
    db.Column('strordercode', db.String(20)),
    db.Column('dblqtysold', db.Numeric(asdecimal=False)),
    db.Column('ctrcode', db.Numeric(20, 0, asdecimal=False)),
    db.Column('strsaletype', db.String(10)),
    db.Column('strcomment', db.String(100)),
    db.Column('strtype', db.String(10)),
    db.Column('lg', db.Numeric(asdecimal=False)),
    db.Column('cardnotransferinttransnum', db.Numeric(20, 0, asdecimal=False)),
    db.Column('intdiscountcode', db.Numeric(asdecimal=False)),
    db.Column('salesstandinctax', db.Numeric(asdecimal=False))
)


t_v_pic_deposithdr = db.Table(
    'v_pic_deposithdr',
    db.Column('deptcd', db.String(10)),
    db.Column('deptname', db.Unicode(50)),
    db.Column('bizdt', db.DateTime),
    db.Column('depositno', db.String(20)),
    db.Column('tp', db.String(8)),
    db.Column('amt', db.Numeric(asdecimal=False)),
    db.Column('applydt', db.DateTime),
    db.Column('plandt', db.DateTime),
    db.Column('tendercd', db.String(20)),
    db.Column('tendername', db.String(50)),
    db.Column('sta', db.String(18))
)


t_v_pluquotasel = db.Table(
    'v_pluquotasel',
    db.Column('id', db.Integer, nullable=False),
    db.Column('cd', db.String(20)),
    db.Column('nm', db.Unicode(100), nullable=False),
    db.Column('uomcd', db.String(6), nullable=False),
    db.Column('uomnm', db.Unicode(50)),
    db.Column('catid', db.Integer),
    db.Column('catcd', db.String(20)),
    db.Column('catnm', db.Unicode(50)),
    db.Column('exattr30', db.String(100))
)


t_v_recruit_netinfo = db.Table(
    'v_recruit_netinfo',
    db.Column('net_no', db.String(20), nullable=False),
    db.Column('net_name', db.Unicode(50), nullable=False),
    db.Column('work_area_fm', db.String(53)),
    db.Column('dm_code', db.String(100)),
    db.Column('work_name_area', db.Unicode(50)),
    db.Column('om_area', db.String(53)),
    db.Column('om_code', db.String(100)),
    db.Column('net_address', db.Unicode(100)),
    db.Column('status', db.String(3))
)


t_v_recruit_user = db.Table(
    'v_recruit_user',
    db.Column('usercode', db.String(20)),
    db.Column('username', db.Unicode(50), nullable=False),
    db.Column('email', db.String(32))
)


t_v_rms_netamt_daily = db.Table(
    'v_rms_netamt_daily',
    db.Column('business_date', db.DateTime),
    db.Column('net_no', db.String(20), nullable=False),
    db.Column('net_name', db.Unicode(50), nullable=False),
    db.Column('subject_no', db.String(20)),
    db.Column('subject_name', db.Unicode(50), nullable=False),
    db.Column('real_value', db.Numeric(18, 2)),
    db.Column('status', db.String(1)),
    db.Column('update_date', db.DateTime)
)


t_v_rms_netamt_daily_jeffrey = db.Table(
    'v_rms_netamt_daily_jeffrey',
    db.Column('business_date', db.DateTime),
    db.Column('net_no', db.String(20), nullable=False),
    db.Column('net_name', db.Unicode(50), nullable=False),
    db.Column('subject_no', db.String(20)),
    db.Column('subject_name', db.Unicode(50), nullable=False),
    db.Column('real_value', db.Numeric(18, 2)),
    db.Column('status', db.String(1)),
    db.Column('update_date', db.DateTime),
    db.Column('vat', db.Numeric(asdecimal=False))
)


t_v_rms_netinfo = db.Table(
    'v_rms_netinfo',
    db.Column('net_no', db.String(20)),
    db.Column('net_name', db.String(100)),
    db.Column('dm_area', db.String(50)),
    db.Column('dm_code', db.String(100)),
    db.Column('dm_name', db.Unicode(50)),
    db.Column('om_area', db.String(50)),
    db.Column('om_code', db.String(100)),
    db.Column('om_name', db.Unicode(50)),
    db.Column('net_address', db.Unicode(100)),
    db.Column('province_code', db.String(2500)),
    db.Column('city_code', db.String(2500)),
    db.Column('district_code', db.String(100)),
    db.Column('status', db.String(3)),
    db.Column('globalid', db.String(20)),
    db.Column('rc', db.String(12))
)


t_v_rms_ominfo = db.Table(
    'v_rms_ominfo',
    db.Column('areaid', db.String(10)),
    db.Column('areacode', db.String(10)),
    db.Column('areaname', db.String(100), nullable=False)
)


t_v_rms_ominfo1 = db.Table(
    'v_rms_ominfo1',
    db.Column('areaid', db.String(100)),
    db.Column('areacode', db.String(100)),
    db.Column('areaname', db.Unicode(50), nullable=False)
)


t_v_rms_region = db.Table(
    'v_rms_region',
    db.Column('province_code', db.String(50), nullable=False),
    db.Column('province_name', db.Unicode(50), nullable=False),
    db.Column('city_code', db.String(100)),
    db.Column('city_name', db.Unicode(50), nullable=False),
    db.Column('district_code', db.String(100)),
    db.Column('district_name', db.Unicode(50), nullable=False)
)


t_v_rms_region1 = db.Table(
    'v_rms_region1',
    db.Column('province_code', db.String(50), nullable=False),
    db.Column('province_name', db.Unicode(50), nullable=False),
    db.Column('city_code', db.String(100)),
    db.Column('city_name', db.Unicode(50), nullable=False),
    db.Column('district_code', db.String(100)),
    db.Column('district_name', db.Unicode(50), nullable=False)
)


t_v_voucdlk = db.Table(
    'v_voucdlk',
    db.Column('lktp', db.String(1)),
    db.Column('lkcd', db.String(50)),
    db.Column('lknm', db.Unicode(50))
)


t_v_voudeptlk = db.Table(
    'v_voudeptlk',
    db.Column('lktp', db.String(1)),
    db.Column('lkcd', db.String(20)),
    db.Column('lknm', db.Unicode(50))
)


t_v_voulk = db.Table(
    'v_voulk',
    db.Column('lktp', db.String(1)),
    db.Column('lkcd', db.String(50)),
    db.Column('lknm', db.Unicode(50))
)


t_v_wxpay_chk_pos2 = db.Table(
    'v_wxpay_chk_pos2',
    db.Column('tran_date', db.DateTime),
    db.Column('tran_time', db.String(8)),
    db.Column('order_no', db.String(50)),
    db.Column('trade_code', db.String(10)),
    db.Column('till_code', db.String(20)),
    db.Column('sale_id', db.Integer),
    db.Column('sale_type', db.String(1)),
    db.Column('tender_amt', db.Numeric(18, 4)),
    db.Column('tender_discount', db.Numeric(asdecimal=False)),
    db.Column('tender_type', db.String(8)),
    db.Column('tr_code', db.Numeric(20, 0, asdecimal=False))
)


t_v_wxpay_dal_dtl = db.Table(
    'v_wxpay_dal_dtl',
    db.Column('trade_code', db.String(20), nullable=False),
    db.Column('dal_id', db.Numeric(12, 0, asdecimal=False), nullable=False),
    db.Column('tran_date', db.DateTime),
    db.Column('dal_status', db.String(3), nullable=False),
    db.Column('dal_sta', db.String(0)),
    db.Column('dal_stval', db.Numeric(18, 2)),
    db.Column('dal_hqval', db.Numeric(18, 2))
)


t_vi_dal_dtl = db.Table(
    'vi_dal_dtl',
    db.Column('trade_code', db.String(20), nullable=False),
    db.Column('dal_id', db.Numeric(12, 0, asdecimal=False), nullable=False),
    db.Column('tran_date', db.DateTime),
    db.Column('dal_status', db.String(3), nullable=False),
    db.Column('dal_sta', db.String(0)),
    db.Column('acid', db.Integer),
    db.Column('dal_stval', db.Numeric(18, 2)),
    db.Column('dal_hqval', db.Numeric(18, 2)),
    db.Column('pk1', db.Numeric(asdecimal=False))
)


t_vi_pos_sand_trans = db.Table(
    'vi_pos_sand_trans',
    db.Column('store_no', db.String(10), nullable=False),
    db.Column('pos_no', db.String(10), nullable=False),
    db.Column('busi_date', db.DateTime, nullable=False),
    db.Column('card_no', db.String(50)),
    db.Column('pos_amt', db.Numeric(10, 2)),
    db.Column('flow_no', db.String(20)),
    db.Column('busi_no', db.String(30)),
    db.Column('eternal_no', db.String(30)),
    db.Column('batch_no', db.String(30)),
    db.Column('card_type', db.String(30)),
    db.Column('issue_no', db.String(30)),
    db.Column('sys_no', db.String(30)),
    db.Column('pk1', db.String(36), nullable=False),
    db.Column('pk2', db.Integer, nullable=False)
)


t_view_gcbi_dd_refresh = db.Table(
    'view_gcbi_dd_refresh',
    db.Column('deptcd', db.String(10)),
    db.Column('bizdt', db.DateTime),
    db.Column('dd_type', db.Numeric(asdecimal=False)),
    db.Column('dd_netamt', db.Numeric(asdecimal=False)),
    db.Column('dd_curqty', db.Numeric(asdecimal=False))
)


t_view_gcbi_fact_payment = db.Table(
    'view_gcbi_fact_payment',
    db.Column('deptcd', db.Numeric(asdecimal=False)),
    db.Column('dateid', db.DateTime),
    db.Column('timeid', db.Numeric(asdecimal=False)),
    db.Column('storeid', db.Numeric(asdecimal=False)),
    db.Column('tdrcd', db.String(10)),
    db.Column('tdramt', db.Numeric(asdecimal=False)),
    db.Column('tdrat', db.Numeric(asdecimal=False)),
    db.Column('tdramt_60', db.Numeric(asdecimal=False)),
    db.Column('tdrat_60', db.Numeric(asdecimal=False))
)


t_view_gcbi_fact_payment_raw = db.Table(
    'view_gcbi_fact_payment_raw',
    db.Column('deptcd', db.Numeric(asdecimal=False)),
    db.Column('dateid', db.DateTime),
    db.Column('timeid', db.Numeric(asdecimal=False)),
    db.Column('storeid', db.Numeric(asdecimal=False)),
    db.Column('tdrcd', db.String(10)),
    db.Column('tdrat', db.Numeric(20, 0, asdecimal=False)),
    db.Column('tdramt', db.Numeric(asdecimal=False)),
    db.Column('at_amt', db.Numeric(asdecimal=False)),
    db.Column('tdr_60_amt', db.Numeric(asdecimal=False)),
    db.Column('at_60_amt', db.Numeric(asdecimal=False))
)


t_view_gcbi_fact_saleitem = db.Table(
    'view_gcbi_fact_saleitem',
    db.Column('DateID', db.DateTime),
    db.Column('TimeID', db.Numeric(asdecimal=False)),
    db.Column('StoreID', db.Numeric(asdecimal=False)),
    db.Column('RevenueCentreID', db.Numeric(asdecimal=False)),
    db.Column('CashierID', db.String(10)),
    db.Column('SaleItemID', db.String(20)),
    db.Column('BusinessDay', db.DateTime),
    db.Column('Item_GrossSales', db.Numeric(scale=2)),
    db.Column('Item_NetSales', db.Numeric(scale=2)),
    db.Column('Item_Tax', db.Numeric(scale=2)),
    db.Column('Item_Quantity', db.Numeric(asdecimal=False)),
    db.Column('SalesCost', db.Numeric(asdecimal=False))
)


t_view_gcbi_fact_sales = db.Table(
    'view_gcbi_fact_sales',
    db.Column('DateID', db.DateTime),
    db.Column('TimeID', db.Numeric(asdecimal=False)),
    db.Column('StoreID', db.Numeric(asdecimal=False)),
    db.Column('RevenueCentreID', db.Numeric(asdecimal=False)),
    db.Column('posid', db.String(20)),
    db.Column('CashierID', db.String(10)),
    db.Column('GlobalNumber', db.String(20)),
    db.Column('TransactionCount', db.Numeric(asdecimal=False)),
    db.Column('StoreSales', db.Numeric(scale=2)),
    db.Column('NetStoreSales', db.Numeric(scale=2)),
    db.Column('NonSales', db.String(100)),
    db.Column('Tax', db.Numeric(scale=2)),
    db.Column('SalesQty', db.Numeric(asdecimal=False)),
    db.Column('DiscountAmount', db.Numeric(asdecimal=False)),
    db.Column('DiscountQuantity', db.Numeric(asdecimal=False))
)


t_view_gcbi_fact_sales_his = db.Table(
    'view_gcbi_fact_sales_his',
    db.Column('DateID', db.DateTime),
    db.Column('TimeID', db.Numeric(asdecimal=False)),
    db.Column('StoreID', db.Numeric(asdecimal=False)),
    db.Column('RevenueCentreID', db.Numeric(asdecimal=False)),
    db.Column('posid', db.String(20)),
    db.Column('CashierID', db.String(10)),
    db.Column('GlobalNumber', db.String(20)),
    db.Column('TransactionCount', db.Numeric(asdecimal=False)),
    db.Column('StoreSales', db.Numeric(scale=2)),
    db.Column('NetStoreSales', db.Numeric(scale=2)),
    db.Column('NonSales', db.String(100)),
    db.Column('Tax', db.Numeric(scale=2)),
    db.Column('SalesQty', db.Numeric(asdecimal=False)),
    db.Column('DiscountAmount', db.Numeric(asdecimal=False)),
    db.Column('DiscountQuantity', db.Numeric(asdecimal=False))
)


t_view_gcbi_fact_sales_itemlt = db.Table(
    'view_gcbi_fact_sales_itemlt',
    db.Column('plucd', db.String(20)),
    db.Column('plu_name', db.Unicode(100), nullable=False),
    db.Column('deptcd', db.String(10)),
    db.Column('sale_qty', db.Numeric(asdecimal=False)),
    db.Column('tradedt', db.DateTime)
)


t_view_gcbi_itemtype_flash = db.Table(
    'view_gcbi_itemtype_flash',
    db.Column('deptcd', db.String(10)),
    db.Column('bizdt', db.DateTime),
    db.Column('d_type', db.String(50)),
    db.Column('curqty', db.Numeric(asdecimal=False))
)


t_voucher_io_po = db.Table(
    'voucher_io_po',
    db.Column('sno', db.String(20)),
    db.Column('bizdt', db.DateTime),
    db.Column('po_type', db.String(1)),
    db.Column('rev_date', db.DateTime),
    db.Column('net_no', db.String(20)),
    db.Column('plu_no', db.String(20)),
    db.Column('qty', db.Numeric(14, 2)),
    db.Column('rmk', db.String(100)),
    db.Column('createdate', db.DateTime),
    db.Column('old_net_no', db.String(20)),
    db.Column('old_plu_no', db.String(20)),
    db.Index('voucher_io_po_1', 'sno', 'bizdt')
)


t_voucher_io_po_tmp = db.Table(
    'voucher_io_po_tmp',
    db.Column('sno', db.String(20)),
    db.Column('bizdt', db.String(8)),
    db.Column('po_type', db.String(1)),
    db.Column('rev_date', db.String(8)),
    db.Column('net_no', db.String(20)),
    db.Column('plu_no', db.String(20)),
    db.Column('qty', db.Numeric(14, 2)),
    db.Column('rmk', db.String(100)),
    db.Column('createdate', db.DateTime, server_default=db.FetchedValue()),
    db.Column('old_net_no', db.String(20)),
    db.Column('old_plu_no', db.String(20))
)


t_vw_pluchk = db.Table(
    'vw_pluchk',
    db.Column('pluid', db.Integer),
    db.Column('msgcd', db.String(7))
)


t_yinglian = db.Table(
    'yinglian',
    db.Column('inttransnum', db.Numeric(20, 0, asdecimal=False)),
    db.Column('strcreditcardnum', db.String(20))
)


t_yinglian0426 = db.Table(
    'yinglian0426',
    db.Column('inttransnum', db.Numeric(20, 0, asdecimal=False)),
    db.Column('strcreditcardnum', db.String(20))
)


t_yingliandata_0419 = db.Table(
    'yingliandata_0419',
    db.Column('net_no', db.String(10)),
    db.Column('biz_date', db.String(8)),
    db.Column('strcreditcardnum', db.String(20)),
    db.Column('curtenderamt', db.Numeric(19, 4))
)


t_yingliandata_0426 = db.Table(
    'yingliandata_0426',
    db.Column('net_no', db.String(10)),
    db.Column('biz_date', db.String(8)),
    db.Column('curtenderamt', db.Numeric(19, 4)),
    db.Column('strcreditcardnum', db.String(20))
)


t_yulei_itembomprc = db.Table(
    'yulei_itembomprc',
    db.Column('pluid', db.Integer, nullable=False),
    db.Column('nm_l_zh', db.Unicode(100), nullable=False),
    db.Column('pnotax', db.Numeric(asdecimal=False))
)


t_yulei_itemcost = db.Table(
    'yulei_itemcost',
    db.Column('cd', db.String(20)),
    db.Column('nm_l_zh', db.Unicode(100), nullable=False),
    db.Column('prc', db.Numeric(asdecimal=False))
)


t_yulei_itemcosthistory_view = db.Table(
    'yulei_itemcosthistory_view',
    db.Column('ptdsc', db.String(50)),
    db.Column('pluid', db.Integer, nullable=False),
    db.Column('csprc', db.Numeric(20, 6))
)


t_yulei_itemdefaultprc = db.Table(
    'yulei_itemdefaultprc',
    db.Column('pluid', db.Integer, nullable=False),
    db.Column('venid', db.Integer),
    db.Column('prc', db.Numeric(18, 6)),
    db.Column('taxrt', db.Numeric(6, 2)),
    db.Column('pnotax', db.Numeric(asdecimal=False))
)


t_yulei_lastpt = db.Table(
    'yulei_lastpt',
    db.Column('id', db.Integer, nullable=False),
    db.Column('coid', db.Integer),
    db.Column('yearno', db.Integer),
    db.Column('monthno', db.Integer),
    db.Column('ptdsc', db.String(50)),
    db.Column('finstdt', db.DateTime),
    db.Column('fineddt', db.DateTime),
    db.Column('stkstdt', db.DateTime),
    db.Column('stkeddt', db.DateTime),
    db.Column('exattr1', db.String(100)),
    db.Column('exattr2', db.String(100)),
    db.Column('exattr3', db.String(100)),
    db.Column('exattr4', db.String(100)),
    db.Column('exattr5', db.String(100)),
    db.Column('exattr6', db.String(100)),
    db.Column('rmk', db.String(100)),
    db.Column('updby', db.String(20)),
    db.Column('upddt', db.DateTime),
    db.Column('sta', db.String(3)),
    db.Column('nxtsta', db.String(3)),
    db.Column('execflg', db.String(1)),
    db.Column('costdt', db.DateTime)
)


t_yulei_netinfo = db.Table(
    'yulei_netinfo',
    db.Column('net_no', db.String(20), nullable=False),
    db.Column('net_name', db.Unicode(50), nullable=False),
    db.Column('word_no', db.String(50)),
    db.Column('dm_code', db.String(50)),
    db.Column('dm_owner', db.String(100)),
    db.Column('word_name_area', db.Unicode(50)),
    db.Column('om_old', db.String(50)),
    db.Column('om_area', db.String(100)),
    db.Column('om_owner', db.String(100)),
    db.Column('areaname', db.Unicode(50)),
    db.Column('areaen', db.Unicode(50)),
    db.Column('rdo_code', db.String(50)),
    db.Column('rdoname', db.Unicode(50)),
    db.Column('rdoen', db.Unicode(50)),
    db.Column('rdo_owner', db.String(100)),
    db.Column('net_address', db.Unicode(100)),
    db.Column('status', db.String(3))
)


t_yulei_simphonyposlist = db.Table(
    'yulei_simphonyposlist',
    db.Column('cd', db.String(20), nullable=False)
)
