## Flask

- 后续操作步骤将会以脚本的形式呈现

```
$which python3
$/usr/bin/python3
$virtualenv -p /usr/bin/python3 venv
$source venv/vin/activate
(venv)$pip install flask
(venv)$pip install flask-script
(venv)$pip install flask-bootstrap
(venv)$pip install flask-moment
(venv)$python hello.py runserver
(venv)$pip install flask-wtf
<!--{% extends "bootstrap/base.html"%} 模板继承,这个注释好像不能屏蔽语句，加上就出错-->
```
