# coding = utf-8

import os, datetime
from flask import request, jsonify, make_response
from flask_bootstrap import Bootstrap
import mimetypes   # 用于设置响应headers['Content-Type']
import pandas as pd
import tablib      # 用于导出各种格式的文件
from sqlalchemy import func   # 用于func.count()统计行数

# 导入orm文件
from app.models import PosTransmst, PtmTrade
from app import db

# 导入blueprint
from . import sales

# 前端请求URL为：http://127.0.0.1:5000/sales/oracle?store_id=131101&date=2018-01-03&format=json&export=false
# 给出门店的号码(DEPTCD)和时间(BIZDT)返回门店对应时间交易量
@sales.route('/oracle', methods=['GET'])
def oracle():
    info = {"id" : request.args.get('store_id'),
            "date" : ' '.join([request.args.get('date'), '00:00:00']),
            "format" : request.args.get('format'),
            "export" : request.args.get('export')}
    # 对数据格式进行一个统一，方便后面mysql的查询
    if info['date']:
        if info['id']:
            # 查询单一门店某一天的销售数据
            sale = PosTransmst.query.filter_by(
                deptcd = info["id"],
                bizdt = datetime.datetime.strptime(info["date"], "%Y-%m-%d %H:%M:%S"),
                saletp = 'SALE'
                ).count()

            res = {"ID": info["id"], "DATE": request.args.get('date'), "SALE": sale}
            return jsonify(res)  # 向前端返回json格式数据
        else:
            # 查询某一天所有门店的交易数据
            tem = db.session.query(PosTransmst.deptcd, func.count()).filter_by(
                bizdt = datetime.datetime.strptime(info["date"], "%Y-%m-%d %H:%M:%S"),
                saletp = 'SALE'
                ).group_by(PosTransmst.deptcd).all()
            # 按门店号分组group by，并统计每个门店指定日期的交易量
            # datetime.datetime.strptime(res["BIZDT"], "%Y-%m-%d %H:%M:%S") 将字符串转换为数据库可以识别的datetime格式
            if info['export'] == str(True):

                def str2list():
                    for dept, sale in tem:
                        yield [dept, request.args.get('date'), sale]

                res = str2list()   # res 数据list,tablib 导入的格式
                data = tablib.Dataset(*res, headers = ["ID", "DATE", "SALE"])

                if info['format'] == 'json':
                    resp = make_response(data.json)                    # 创建相应对象
                    filename = ''.join(['oracle', request.args.get('date'), '.json'])         # 响应下载的文件名
                    mime_type = mimetypes.guess_type(filename)[0]      # 响应类型
                    resp.headers['Content-Type'] = mime_type           # 设置响应头
                    resp.headers['Content-Disposition'] = 'attachment; filename={}'.format(filename)
                    return resp

                elif info['format'] == 'csv':
                    resp = make_response(data.csv)
                    filename = ''.join(['oracle', request.args.get('date'), '.csv'])
                    mime_type = mimetypes.guess_type(filename)[0]
                    resp.headers['Content-Type'] = mime_type
                    resp.headers['Content-Disposition'] = 'attachment; filename={}'.format(filename)
                    return resp

                else:
                    return "请输入正确的数据格式"
            else:
                # 将字符格式的数据转换成json格式
                def str2json():
                    for dept, sale in tem:
                        yield {"ID": dept, "DATE": info["date"], "SALE": sale}
                # 在网页显示
                return jsonify(list(str2json()))    

    else:
        return "请输入正确的URL"


# 前端请求URL为：http://127.0.0.1:5000/sales/mysql?store_id=131101&date=2018-01-03&format=json&export=false
@sales.route('/mysql', methods=['GET'])
def mysql():
    info = {"id" : request.args.get('store_id'),
            "date" : request.args.get('date'),
            "format" : request.args.get('format'),
            "export" : request.args.get('export')}
    
    if info['date']:
        if info['id']:
            # 查询单一门店某一天的销售数据
            sale = PtmTrade.query.filter_by(
                global_storeid = info["id"],
                business_day = datetime.datetime.strptime(info["date"], "%Y-%m-%d")
                ).count()
            # 日期的格式和oracle 数据库不同

            res = {"ID": info["id"], "DATE": info["date"], "SALE": sale}
            return jsonify(res)  # 向前端返回json格式数据

        else:
            # 查询某一天所有门店的交易数据
            tem = db.session.query(PtmTrade.global_storeid, func.count()).filter_by(
                business_day = datetime.datetime.strptime(info["date"], "%Y-%m-%d")
                ).group_by(PtmTrade.global_storeid).all()
            # 按门店号分组group by，并统计每个门店指定日期的交易量

            if info['export'] == str(True):

                def str2list():
                    for dept, sale in tem:
                        yield [dept, info["date"], sale]

                res = str2list()   # res 数据list,tablib 导入的格式
                data = tablib.Dataset(*res, headers = ["ID", "DATE", "SALE"])

                if info['format'] == 'json':
                    resp = make_response(data.json)                    # 创建相应对象
                    filename = ''.join(['mysql', info['date'], '.json'])         # 响应下载的文件名
                    mime_type = mimetypes.guess_type(filename)[0]      # 响应类型
                    resp.headers['Content-Type'] = mime_type           # 设置响应头
                    resp.headers['Content-Disposition'] = 'attachment; filename={}'.format(filename)
                    return resp

                elif info['format'] == 'csv':
                    resp = make_response(data.csv)
                    filename = ''.join(['mysql', info["date"], '.csv'])
                    mime_type = mimetypes.guess_type(filename)[0]
                    resp.headers['Content-Type'] = mime_type
                    resp.headers['Content-Disposition'] = 'attachment; filename={}'.format(filename)
                    return resp

                else:
                    return "请输入正确的数据格式"
            else:
                # 将字符格式的数据转换成json格式
                def str2json():
                    for dept, sale in tem:
                        yield {"ID": dept, "DATE": info["date"], "SALE": sale}
                # 在网页显示
                return jsonify(list(str2json()))    

    else:
        return "请输入正确的URL"


# 前端请求URL为：http://127.0.0.1:5000/sales/both?store_id=131101&date=2018-01-03&format=json&export=false
@sales.route('/both', methods=['GET'])
def both():
    info = {"id" : request.args.get('store_id'),
            "date" : request.args.get('date'),
            "format" : request.args.get('format'),
            "export" : request.args.get('export')}
    
    if info['date']:
        if info['id']:
            # 查询单一门店某一天的销售数据
            mysql_sale = PtmTrade.query.filter_by(
                global_storeid = info["id"],
                business_day = datetime.datetime.strptime(info["date"], "%Y-%m-%d")
                ).count()

            oracle_sale = PosTransmst.query.filter_by(
                deptcd = info["id"],
                bizdt = datetime.datetime.strptime(' '.join([request.args.get('date'), '00:00:00']), "%Y-%m-%d %H:%M:%S"),
                saletp = 'SALE'
                ).count()

            res = {"ID": info["id"], "DATE": info["date"], "SALE_MYSQL": mysql_sale, "SALE_ORACLE": oracle_sale}
            return jsonify(res)  # 向前端返回json格式数据

        # -----------------这之前的已经没问题了-----------------------------------------------
        else:
            # 查询某一天所有门店的交易数据
            tem_mysql = db.session.query(PtmTrade.global_storeid, func.count()).filter_by(
                business_day = datetime.datetime.strptime(info["date"], "%Y-%m-%d")
                ).group_by(PtmTrade.global_storeid).limit(5).all()
            # 按门店号分组group by，并统计每个门店指定日期的交易量

            tem_oracle = db.session.query(PosTransmst.deptcd, func.count()).filter_by(
                bizdt = datetime.datetime.strptime(' '.join([request.args.get('date'), '00:00:00']), "%Y-%m-%d %H:%M:%S"),
                saletp = 'SALE'
                ).group_by(PosTransmst.deptcd).limit(5).all()

            def both2list(tem):
                for dept, sale in tem:
                    yield [dept, sale]

            data_mysql = pd.DataFrame(list(both2list(tem_mysql)), columns=["ID", "SALE_MYSQL"])
            data_oracle = pd.DataFrame(list(both2list(tem_oracle)), columns=["ID", "SALE_ORACLE"])
            data = pd.merge(data_oracle, data_mysql, on='ID', how='outer')

            # DataFrame 转换为list， 不带index 和 header
            # data.values.tolist()

            # DataFrame 转换为json， 不带 index
            # data.to_json(orient='records')

            # DataFrame 转换为csv, 不带 index
            # data.to_csv(index=False)

            if info['export'] == str(True):

                if info['format'] == 'json':
                    resp = make_response(data.to_json(orient='records'))                    # 创建相应对象
                    filename = ''.join(['both', info['date'], '.json'])         # 响应下载的文件名
                    mime_type = mimetypes.guess_type(filename)[0]      # 响应类型
                    resp.headers['Content-Type'] = mime_type           # 设置响应头
                    resp.headers['Content-Disposition'] = 'attachment; filename={}'.format(filename)
                    return resp

                elif info['format'] == 'csv':
                    resp = make_response(data.to_csv(index=False))
                    filename = ''.join(['both', info["date"], '.csv'])
                    mime_type = mimetypes.guess_type(filename)[0]
                    resp.headers['Content-Type'] = mime_type
                    resp.headers['Content-Disposition'] = 'attachment; filename={}'.format(filename)
                    return resp

                else:
                    return "请输入正确的数据格式"
            else:

                # 在网页显示
                return data.to_json(orient='records')

    else:
        return "请输入正确的URL"