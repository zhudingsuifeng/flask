## flask web 构建过程

### http请求发送与响应过程

1. 通信双方遵从HTTP协议进行连接。通过ip地址和端口，三次握手建立一个tcp连接。

2. 请求：连接成功建立后，开始向web服务器发送HTTP请求。flask通过wsgi协议传递请求。

3. 响应：接到请求后，交给相应路由处理，根据地址转发给相应的控制器(函数)处理。

后端大部分工作就是写这些处理过程。处理完成后将最终的response返回给用户。这其中request与response都是由python的wsgi工具包werkzeug提供。

4. 关闭连接：通讯双方均可关闭socket结束tcp/ip会话。

### 项目结构

```
.
├── app
│   ├── admin
│   │   ├── errors.py
│   │   ├── forms.py
│   │   ├── __init__.py
│   │   └── views.py
│   ├── __init__.py
│   ├── main
│   │   ├── forms.py
│   │   ├── __init__.py
│   │   └── views.py
│   ├── models.py
│   ├── static
│   └── templates
│       ├── 404.html
│       ├── 500.html
│       ├── admin
│       │   ├── login.html
│       │   └── register.html
│       ├── base.html
│       ├── index.html
│       └── user.html
├── config.py
├── manage.py
```

- flask程序一般都保存在名为app的包中。

- config.py 保存着配置。

- manage.py 用于启动项目。

###

如果执行命令时使用绝对路径，__file__就是脚本的绝对路径。
如果执行命令时使用绝对路径，__file__就是脚本的绝对路径。

```
import os

print(__file__)           # 可执行文件名

print(os.path.dirname(__file__))   # 相对路径名

print(os.path.abspath(os.path.dirname(__file__))) # 绝对路径名

PROJECT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), 'application'))
sys.path.insert(0, PROJECT_PATH)
# sys.path.append(path) 和 sys.path.insert(0, path) 效果一致
sys.path.append(PROJECT_PATH)
# 将模块路径暂时添加到当前模块扫描的路径里，脚本运行后失效。
```

### flask-script

flask-script是一个flask扩展，为flask程序添加了一个命令行解析器。flask-script自带了一组常用选项，而且还支持自定义命令。

```
(venv)$pip install flask-script
from flask_script import Manager
manager = Manager(app)

if __name__ == "__main__":
    manager.run()

$python hello.py
```

老版的 from flask.ext.script import Manager 更新为from flask_script import Manager.

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

### flask模板

```
<!--{% extends "bootstrap/base.html"%} 模板继承,这个注释好像不能屏蔽语句，加上就出错-->
```

### python class中的__all__属性

__all__是一个字符串list,用来定义模块中对于from XXX import * 时要对外导出的符号，即要暴露的接口，但它只对import * 起作用，对from XXX import XXX不起作用。

函数  <function XX at 0x000000>

类方法 <unbound method X.x>

实例方法  <bound method X.x of <__main__.X object at 0x.....>