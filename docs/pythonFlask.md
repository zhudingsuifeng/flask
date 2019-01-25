## flask

### response

http 响应的三个基本组成部分，即数据或正文、状态码和标头。

flask的应用实例拥有一个make_response函数，可以接受路由函数的返回值(可以是单个值，也可以是有1-3个值的元组),并将其填入响应对象(Response object)中。

```
>>> from flask import Flask
>>> app = Flask(__name__)
>>> app.make_response('hello, world')
<Response 12 bytes [200 OK]>
>>> app.make_response(('hello, world', 222))
<Response 12 bytes [222 UNKNOWN]>
```

flask在创建了代表路由函数返回值的响应对象(Response object)之后，还会做一些处理。包括将响应对象传入自定义的after_request处理程序(handlers)，在这一步，应用还有机会插入或修改标头、更改正文或状态码，如果愿意的话，甚至是启用崭新的响应对象取而代之。最后，flask会获取最终的响应对象，渲染成http响应，并发送给客户端。

### flask-script

```
```

### bootstrap

```
```

### sqlalchemy

```
```

### flask-sqlalchemy

```
```

### sqlacodegen

```

```



### tablib

```
# 安装tablib
(venv)pip install tablib

import tablib

# 设置表头
headers = (u"姓名", u"性别", u"年龄")

# 数据
info = [(), ()]

# 构建数据对象
data = tablib.Dataset(*info, header=headers)

# 支持的数据格式
data.xlsx
data.xls
data.ods
data.json
data.yaml
data.csv
data.tsv
data.html

# 使用xls格式的话，最大行数为65536，如果要取消这个限制，导出文件为book.xlsx即可。

# 增加行
data.append([])

# 增加列
data.append_col([], header=u'')

# 删除行
del data[1:3]

# 删除列
del data[u'年龄']

# 多个sheet的execl表
book = tablib.Databook((data1,data2))
book.xls
```

### pip freeze

```
pip freeze > requirements.txt      # 导出项目依赖包到requirements.txt
pip install -r requirements.txt    # 从requirements.txt导入依赖
```
