## python 连接操作数据库

URI统一资源标识符(Uniform Resource Identifier)是一个用于标识某一互联网资源名称的字符串。

URI = Universal Resource Identifier 统一资源标识符

URL = Universal Resource Locator 容易资源定位符

URN = Universal Resource Name 统一资源名称

这三者的关系如下图：

<img src="../imgs/uri.png" width = "200" />

URI 分为三种，URL、URN或者(URL和URN)

URI标记一个网络资源，URL标记了一个www互联网资源的访问地址，URN标记了资源的名字。

类型这个术语表示程序使用的持久化实体。在ORM中，模型一般是一个python类，类中的属性对应数据库表中的列。

抽象层，也称为对象关系映射(Object-Relational Mapper, ORM)或对象文档映射(Object-Document Mapper, ODM),在用户不知觉的情况下把高层的面向对象操作转换成低层的数据库命令。

类变量__tablename__定义在数据库中使用的表名。如果没有定义__tablename__,会使用一个默认名字，最好自己指定。其余变量都是该模型的属性，被定义为db.Column类的实例。

### mysql

```
$virtualenv -p /usr/bin/python3 venv
$source venv/bin/activate
(venv)$pip install pymysql            # python3 mysql 支持
(venv)$pip install flask-sqlalchemy   # flask sqlalchemy支持
```

### python SQLAlchemy mysql使用

```
#!/usr/bin/env python3
#coding = utf-8

from flask_sqlalchemy import SQLAlchemy  # 引入sqlalchemy插件
from flask import Flask

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://fly:password@localhost/web?charset=utf8'
# SQLALCHEMY_DATBASE_URI 指定所要操作的数据库
# mysql+pymysql指定配置数据库类型为mysql,fly为用户名，password是用户密码(根据自己情况)
# @localhost是数据库ip地址(本地数据库),web?charset=utf8指定数据库名和编码格式。
# 需要确定mysql中有web数据库，以及后面要使用的user表。

db = SQLAlchemy(app)  # 生成SQLAlchemy实例。

class user(db.Model):
    __tablename__ = 'user'     # 指定表名
    id = db.Column('id', db.Integer, Primary_key=True)
    name = db.Column(db.String(20), unique=True)

    def __init__(self, id=None, name='fly'):
        self.id = id
        self.name = name

    # __str__,__repr__当执行print对象user时，显示的内容，__str__()显示给用户，__repr__()显示给开发人员。
    def __repr__(self):
        return '<User %r>' % self.name

# insert 用户信息
test_user = user(1, 'sky')
db.session.add(test_user)
db.session.commit()

# select 信息
db.session.query(user).filter_by(id=1).first()
# or
db.session.query(user).filter(user.id == 1).first()
db.session.query(user).all()
# 查询返回值是一个list,可以通过list[i].attr访问对象i的attr属性。

# update 数据
user = db.session.query(user).filter_by(id=1).first()
user.name = 'fly'
db.session.commit()

# delete 数据
user = db.session.query(user).filter_by(id=1).first()
db.session.delete(user)
db.session.commit()
```

### mongodb

### oracle

SQLAlchemy并不是数据库驱动，python访问oracle数据库的驱动是cx_Oracle,但是这个驱动依赖于Oracle instant client.

所以python如果想通过SQLAlchemy库访问oracle数据库，那么需要先安装Oracle instant client,再安装cx_Oracle和SQLAlchemy.

去官网下载安装包，注意版本对应。

https://www.oracle.com/technetwork/topics/linuxx86-64soft-092277.html

支持cx_Oracle需要下载
oracle-instantclient12.1-basic-12.1.0.2.0-1.x86_64.rpm 
oracle-instantclient12.1-devel-12.1.0.2.0-1.x86_64.rpm
两个包，注意自己的版本。

在dataGrip查看oracle 版本：

```
select * from v$version;
# oracle 版本信息
Oracle Database 11g Enterprise Edition Release 11.2.0.4.0 - 64bit Production
PL/SQL Release 11.2.0.4.0 - Production
"CORE	11.2.0.4.0	Production"
TNS for Linux: Version 11.2.0.4.0 - Production
NLSRTL Version 11.2.0.4.0 - Production
```

basic包含所有的oracle client lib/bin文件。

devel包含oracle client 外部接口的头文件。

```
# 通过zip文件安装basic
cp instantclient-basic-linux.x64.zip /opt/oracle
cd /opt/oracle
unzip instantclient-basic-linux.x64.zip
cd /opt/oracle/instantclient_11_2
ln -s libclntsh.so.11.1 libclntsh.so
ln -s libocci.so.11.1 libocci.so

apt install 
```

```
(venv)$pip install cx_Oracle
```