## sqlalchemy学习笔记

SQLAlchemy是python的一个数据库ORM工具，提供了强大的对象模型间的转换，支持多种数据库引擎，以下是基本用法和笔记。

### 安装和配置sqlalchemy

```
# pip 安装SQLAlchemy
pip install SQLAlchemy

# 数据库连接参数
# 标准连接URL： dialect+driver://username:password@host:port/database
# dialect,是数据库类型，大概包括：sqlite,mysql,postgresql,oracle,mssql
# driver,是使用的数据库API，驱动，连接包
# username,用户名
# password,密码
# host,网络地址，可以用ip,域名，计算机名，只要是你能访问到的。
# port,数据库端口。
# database,数据库名。

# 连接mysql
'mysql+pymysql://username:password@host:port/database'

# 连接oracle
'oracle+cx_oracle://username:password@host:port/sid'
# oracle最后跟一个SID，SID在oracle中唯一标识一个数据库。
```

1. connection

使用传统的connection的方式连接和操作数据库

```
from sqlalchemy import create_engine

# 数据库连接字符串，根据连接的数据库不同，选择不同的连接字符串
DB_CONNECT_STRING = ''

# 创建数据库引擎，echo=True，会打印所有的sql语句
engine = create_engine(DB_CONNECT_STRING, echo=True)

# 创建一个connection
with engine.connect() as con:
    # 执行sql语句，不需要commit
    rs = con.execute('select 语句')
    data = rs.fetchone()[0]
    print(data)
```

2. connection事务

使用事务可以进行批量提交和回滚

```
with engine.connect() as connection:
    trans = connection.begin()
    try:
        r1 = connection.execute('sql语句')
        r2 = connection.execute('sql语句')
        trans.commit()
    except:
        trans.rollback()
        raise
```

3. session

connection是一般使用数据库的方式，sqlalchemy还提供了另外一种操作数据库的方式，通过session对象，session可以记录和跟踪数据的改变，在适当的时候提交，并且支持强大的orm的功能。

```
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# 数据库连接字符串
DB_CONNECT_STRING = ''

# 创建数据库引擎
engin = create_engin(DB_CONNECT_STRING, echo=True)

# 创建类话
DB_Session = sessionmaker(bind=engin)

# 创建会话对象
session = DB_Session()

session.execute('select * from user')
session.execute("insert into user(name, age) values('bomo', 13)")\

# 参数使用dict，并在sql语句中使用:key占位
session.execute("insert into user(name, age) values(:name, :age)", {'name':'bomo', 'age':12})

# 如果是增删改，需要commit
session.commit()

# 用完关闭session，也可以用with
session.close()
```

4. orm

上面介绍了sql的简单用法，下面介绍orm用法，sqlalchemy的模型类继承自一个由declarative_base()方法生成的类。

```
# Models.py

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# Role.py

from sqlalchemy import Column, Integer, String
from Models import Base

class Role(Base):
    __tablename__ = 'Role'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    name = Column('name', String(50))
```

Column构造函数相关设置

- name: 名称
- type_: 列类型
- autoincrement: 自增
- default: 默认值
- index: 索引
- nullable: 可空
- primary_key: 外键

### 通过session进行增删改查

```
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from User import User
from Models import Base

DB_CONNECT_STRING = ''
engine = create_engine(DB_CONNECT_STRING, echo=True)
DB_Session = sessionmaker(bind=engine)
session = DB_Session()

# 1. 创建表(如果表已经存在，则不会创建)
Base.metadata.create_all(engine)

# 2. 插入数据
r = Role(name = 'user')

# 如果add 已经存在，会报错
session.add(r)

# 3. 修改数据
# 3.1 使用merge方法，如果存在则修改，如果不存在则插入（只判断主键，不判断unique列）
r.name = 'admin'
session.merge(r)

# 3.2 也可以通过这种方式修改
session.query(Role).filter(Role.id == 1).update({'name': 'admin'})

# 4. 删除数据
session.query(Role).filter(Role.id == 1).delete()

# 5. 查询数据
# 5.1 返回结果集的第二项
user = session.query(User).get(2)

# 5.2 返回结果集中的第2-3项
users = session.query(User)[1:3]

# 5.3 查询条件
user = session.query(User).filter(User.id < 6).first()

# 5.4 排序
users = session.query(User).order_by(User.name)

# 5.5 降序（需要导入desc方法）
from sqlalchemy import desc
users = session.query(User).order_by(desc(User.name))

# 5.6 只查询部分属性
users = session.query(User.name).order_by(desc(User.name))
for user in users:
    print user.name

# 5.7 给结果集的列取别名
users = session.query(User.name.label('user_name')).all()
for user in users:
    print user.user_name

# 5.8 去重查询（需要导入distinct方法）
from sqlalchemy import distinct
users = session.query(distinct(User.name).label('name')).all()

# 5.9 统计查询
user_count = session.query(User.name).order_by(User.name).count()
age_avg = session.query(func.avg(User.age)).first()
age_sum = session.query(func.sum(User.age)).first()

# 5.10 分组查询
users = session.query(func.count(User.name).label('count'), User.age).group_by(User.age)
for user in users:
    print 'age:{0}, count:{1}'.format(user.age, user.count)

# 6.1 exists查询(不存在则为~exists())
from sqlalchemy.sql import exists
session.query(User.name).filter(~exists().where(User.role_id == Role.id))
# SELECT name AS users_name FROM users WHERE NOT EXISTS (SELECT * FROM roles WHERE users.role_id = roles.id)

# 6.2 除了exists，any也可以表示EXISTS
session.query(Role).filter(Role.users.any())

# 7 random
from sqlalchemy.sql.functions import random
user = session.query(User).order_by(random()).first()

session.close()
```

5. 多表关系
6. 多表查询

### 数据库迁移

sqlalchemy的数据库迁移/升级有两个库支持alembic和sqlalchemy-migrate

alembic实现了类似git/svn的版本管理的控制，我们可以通过alembic维护每次升级数据库的版本

1. 安装
2. 初始化
3. 配置
4. 创建数据库版本
5. 升级数据库
6. 通过元数据升级数据库