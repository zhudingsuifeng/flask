## flask中的请求对象request的使用

### 在flask 开发中，前端需要发送不同的请求及各种带参数的方式，比如GET方法在URL后面带参数，这时候需要从request提取参数。

```
from flask import request, Flask

app = Flask(__name__)

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

request.headers      # 请求头信息
request.method       # GET
request.url          # 请求url地址:http://127.0.0.1:5000/
request.data         # 请求数据{name:'fly', age:18}

# request.json.get()    # 获取数据

# json.dumps(data)      # 字典转字符串
# json.loads(data)      # 字符串转字典

# request.form.get()    # 获取表单中的数据

# 操作URL(?key=value)中提交的参数可以使用args属性
# request.args.get('key','')    # 获取URL中?之后的参数
# 把?之后的参数看成是字典，通过类似访问字典的方式访问参数

# request.values
# args返回请求中的参数，values返回请求中的参数和form
# request.files.get()   # 获取文件

# 保存文件
# file = request.files.get()
# file.save()

# request.cookies
```