## flask

```
```

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