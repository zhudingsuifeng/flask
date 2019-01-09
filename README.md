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

### oracle数据库

```
select * from v$version;  #查看oracle版本信息

Oracle Database 11g Enterprise Edition Release 11.2.0.4.0 - 64bit Production
PL/SQL Release 11.2.0.4.0 - Production
"CORE	11.2.0.4.0	Production"
TNS for Linux: Version 11.2.0.4.0 - Production
NLSRTL Version 11.2.0.4.0 - Production

```