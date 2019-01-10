## Flask

### flask环境搭建

```
mkdir flask
cd flask
which python3
virtualenv -p /usr/bin/python3 venv
source venv/bin/activate
(venv)$pip install flask
(venv)$pip install flask-script     # 扩展插件,支持命令行选项
(venv)$pip install flask-moment     # 时间插件
(venv)$pip install flask-wtf        # web表单验证
(venv)$pip install jinja2           # 模板渲染
(venv)$pip install flask-bootstrap  # 模板插件
(venv)$pip install flask-sqlalchemy # python orm包
(venv)$pip list                     # 查看当前pip安装的python包
```
[python 数据库支持](https://github.com/zhudingsuifeng/flask/blob/works/docs/pythonDB.md)
### git delete remote file

```
git rm -r --cached targetfile
git commit -m 'delete targetfile'
git push origin works
```

### 报错E1101:Instance of ‘SQLAlchemy’ has no ‘Column’ member

这个错误不影响程序的执行，但是编辑器总是报错，影响心情，并且容易引发误解，浪费时间检查程序。

解决方案：code ——>首选项——>设置——>搜索‘pylintArgs’

将“ “python.linting.pylintArgs”: [] ”添加到用户设置，

如： "python.linting.pylintArgs": ["--load-plugins", "pylint_flask"]

### oracle数据库

```
select * from v$version;  #查看oracle版本信息

Oracle Database 11g Enterprise Edition Release 11.2.0.4.0 - 64bit Production
PL/SQL Release 11.2.0.4.0 - Production
"CORE	11.2.0.4.0	Production"
TNS for Linux: Version 11.2.0.4.0 - Production
NLSRTL Version 11.2.0.4.0 - Production
```

### sqlalchemy

### flask-sqlalchemy