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