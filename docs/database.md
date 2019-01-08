## 数据库的使用

URI统一资源标识符(Uniform Resource Identifier)是一个用于标识某一互联网资源名称的字符串。

URI = Universal Resource Identifier 统一资源标识符

URL = Universal Resource Locator 容易资源定位符

URN = Universal Resource Name 统一资源名称

这三者的关系如下图：

[URI组成](imgs/uri.png)

URI 分为三种，URL、URN或者(URL和URN)

URI标记一个网络资源，URL标记了一个www互联网资源的访问地址，URN标记了资源的名字。

类型这个术语表示程序使用的持久化实体。在ORM中，模型一般是一个python类，类中的属性对应数据库表中的列。

类变量__tablename__定义在数据库中使用的表名。如果没有定义__tablename__,会使用一个默认名字，最好自己指定。其余变量都是该模型的属性，被定义为db.Column类的实例。

### python SQLAlchemy mysql使用

```
#!/usr/bin/env python3
#coding = utf-8

from flask_sqlalchemy import SQLAlchemy
from flask import Flask

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 
```
