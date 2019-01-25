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