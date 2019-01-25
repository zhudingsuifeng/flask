## Flask

### 项目结构

```
app
├── __init__.py        # app工厂函数，blueprint注册
├── models.py          # 数据库orm文件
├── sales
│   ├── __init__.py    # sales蓝图创建
│   └── views.py       # 功能视图文件，主要功能在这里面实现
├── static
│   └── favicon.ico
└── templates          # 模板文件
    ├── 404.html
    ├── 500.html
    ├── base.html
    └── index.html
config.py    # 配置文件，数据库的连接配置
manage.py    # 程序入口文件 (venv)python manage.py runserver
```

**支持指定门店号，日期，json格式查询。**

**和指定日期，格式，页面显示或导出为文件。**

请求oracle数据库中的数据，指定门店号和日期，不导出为文件

```
http://127.0.0.1:5000/sales/oracle?store_id=131101&date=2018-01-03&format=json&export=false
```

请求mysql数据库中的数据，指定门店号和日期，不导出为文件

```
http://127.0.0.1:5000/sales/mysql?store_id=131101&date=2018-01-03&format=json&export=false
```

请求oracle数据库中的数据，指定日期，不导出为文件

```
http://127.0.0.1:5000/sales/oracle?date=2018-01-03&format=json&export=false
```

请求oracle数据库中的数据，指定日期，导出为文件

```
http://127.0.0.1:5000/sales/oracle?date=2018-01-03&format=json&export=True
```

mysql数据库的数据类似

同时请求mysql和oracle数据库的数据，指定门店号和日期，指定导出格式json，是否导出false

```
http://127.0.0.1:5000/sales/both?store_id=131101&date=2018-01-03&format=json&export=false
```

同时请求mysql和oracle数据库的数据，指定门店号和日期，指定导出格式csv，是否导出True

```
http://127.0.0.1:5000/sales/both?store_id=131101&date=2018-01-03&format=csv&export=True
```