## sqlalchemy学习笔记

SQLAlchemy是python的一个数据库ORM工具，提供了强大的对象模型间的转换，支持多种数据库引擎，以下是基本用法和笔记。

使用orm将python类与数据库的table映射，通过对类对象的操作来操作数据库。这种方法免去了写sql语句，但是写类也是个麻烦事(使用sqlacodegen能大大减少这部分的工作量)，而且复杂的sql语言依靠orm比较难实现。

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
DB_CONNECT_STRING = 'mysql+pymysql://fly:huangzongwen_123@127.0.0.1:3306/web'

# 创建数据库引擎，echo=True，会打印所有的sql语句
# engine = create_engine(DB_CONNECT_STRING, echo=True)
engine = create_engine(DB_CONNECT_STRING)

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
DB_CONNECT_STRING = 'mysql+pymysql://fly:huangzongwen_123@127.0.0.1:3306/web?charset=utf8'

# 创建数据库引擎
engin = create_engin(DB_CONNECT_STRING)

# 创建会话类
DB_Session = sessionmaker(bind=engin)

# 创建会话对象
session = DB_Session()

# execute() 里面直接执行sql语句
session.execute('select * from user')
session.execute("insert into user(name, age) values('bomo', 13)")

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
# mysql.py
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, func, distinct
from sqlalchemy.orm import sessionmaker

# 创建对象的基类
Base = declarative_base()

# mysql web数据库student表 orm类
class student(Base):
    __tablename__ = 'student'
    id = Column('id', Integer, primary_key=True)
    name = Column(String(20))
    age = Column(Integer)
    math = Column(Integer)
    english = Column(Integer)
    history = Column(Integer)
    teacher = Column(String(20))

    # __str__() 方法在打印对象的时候，不在打印对象的内存地址，而是打印__str__方法的返回值。
    # __str__ 方法只能在打印单一对象的时候调用，打印多个对象时还是会返回内存地址
    def __str__(self):
        res = {}
        res['id'] = self.id
        res['name'] = self.name
        res['age'] = self.age
        res['math'] = self.math
        res['english'] = self.english
        res['history'] = self.history
        res['teacher'] = self.teacher
        return str(res)   # __str__ 方法只能返回string类型
```

Column构造函数相关设置

- name: 名称，指定orm模型中某个属性映射到表中的字段。如果不指定，那么会使用这个属性的名字作为字段名。
- type_: 列类型
- autoincrement: 自增
- default: 默认值
- index: 索引
- nullable: 可空
- primary_key: 外键

### 通过session进行增删改

```
# mysql.py # 接着上面的

# 1. 创建表(如果表已经存在，则不会创建)
Base.metadata.create_all(engine)

# 2. 插入数据
r = Role(name = 'user')

# 如果add 已经存在，会报错
session.add(r)
session.commit()

# 3. 修改数据
# 3.1 使用merge方法，如果存在则修改，如果不存在则插入（只判断主键，不判断unique列）
r.name = 'admin'
session.merge(r)

# 3.2 也可以通过这种方式修改
session.query(Role).filter(Role.id == 1).update({'name': 'admin'})

# 4. 删除数据
session.query(Role).filter(Role.id == 1).delete()
```

### 数据的查询

```
# 5. 查询数据
# 5.1 返回结果集的第一项
user = session.query(student).get(1)

# <__main__.student object at 0x7f48f3846f60>
{'id': 1, 'name': 'fly', 'age': 24, 'math': 80, 'english': 68, 'history': 100, 'teacher': 'liu'}

# 5.2 返回结果集中的第2-3项
users = session.query(student)[1:3]

# [<__main__.student object at 0x7fcb50c2c080>, <__main__.student object at 0x7fcb50c2c0f0>]

# 5.3 查询条件
user = session.query(student).filter(student.id < 3).first()

# <__main__.student object at 0x7fdc10d84128>

# 5.4 排序
users = session.query(student).order_by(student.name)
# 获取排序结果需要后缀.all() 或者指定数量
data = session.query(student).order_by(student.history).all()

# 5.5 降序（需要导入desc方法）
from sqlalchemy import desc
users = session.query(student).order_by(desc(student.name))

# 5.6 只查询部分属性
users = session.query(User.name).order_by(desc(User.name))
for user in users:
    print user.name

# 5.7 给结果集的列取别名
users = session.query(student).name.label('student_name')).all()
# [('fly',), ('test',), ('sky',), ('snow',), ('flasky',), ('kaow',), ('trigger',)]

# 5.8 去重查询（需要导入distinct方法）
from sqlalchemy import distinct
users = session.query(distinct(student.name).label('name')).all()
# [('fly',), ('test',), ('sky',), ('snow',), ('flasky',), ('kaow',), ('trigger',)]

# 5.9 统计查询
user_count = session.query(User.name).order_by(User.name).count()

# 平均值
age_avg = session.query(func.avg(student.math)).first()
# (Decimal('79.8571'),)

# 求和
age_sum = session.query(func.sum(student.math)).first()
# (Decimal('559'),)

# 5.10 分组查询
# 分组查询统计 
data = session.query(func.count(student.history).label('count')).group_by(student.teacher).all()
# [(2,), (3,), (2,)]

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

### 返回

```
all() 返回一个列表
first() 返回至多一个结果，而且以单项形式，而不是只有一个元素的tuple形式返回结果。
one() 返回且仅返回一个查询结果。当结果的数量不足一个或者多于一个时会报错。
```

### SQL Expression layer

```
from sqlalchemy import select, func, Integer, Table, Column, MetaData

metadata = MetaData()

table = Table("table", metadata,
              Column('primary_key', Integer),
              Column('other_column', Integer)
              )
print(select([func.count()]).select_from(table))
```

### ORM layer

```
from sqlalchemy import create_engine, distinct, func
from sqlalchemy.orm import sessionmaker

# mysql 连接字符串
DB_CONNECT_STRING = 'mysql+pymysql://fly:huangzongwen_123@localhost/web?charset=utf8'

# 初始化数据库连接，创建引擎，echo=True 输出引擎执行的语句
engine = create_engine(DB_CONNECT_STRING)    # , echo=True)

# 创建DB_Session类型
DB_Session = sessionmaker(bind=engine)

# 创建session对象
session = DB_Session()

session.query(table.col).count()
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