## flask-script

flask-script是一个flask扩展，为flask程序添加了一个命令行解析器。flask-script自带了一组常用选项，而且还支持自定义命令。

```
(venv)$pip install flask-script
from flask_script import Manager
manager = Manager(app)

# ...

if __name__ == "__main__":
    manager.run()

$python hello.py
```

老版的 from flask.ext.script import Manager 更新为from flask_script import Manager.

