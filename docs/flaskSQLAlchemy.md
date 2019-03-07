## flask-sqlalchemy的使用

flask-sqlalchemy是一个为flask应用增加sqlalchemy支持的扩展。他需要sqlalchemy0.6或者更高的版本。它致力于简化在flask中sqlalchemy的使用，提供了有用的默认值和额外的助手来更简单地完成常见任务。

### flask-sqlalchemy中的查询

flask-sqlalchemy在Model类上提供了query属性。在使用all()或者first()发起查询之前可以使用filter()来过滤记录。

```
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()   # 创建SQLAlchemy对象

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))

User.query.filter_by(name='fly').first()
User.query.filter(User.name == 'fly').all()

# 排序
User.query.order_by(User.name)

# 限制返回结果数量
User.query.limit(1).all()

# 用主键查询
User.query.get(1)

# 逻辑非
User.query.filter(User.name != 'fly').all()

from sqlalchemy import not_
User.query.filter(not_(User.name=='fly')).all()

# 逻辑与
from sqlalchemy import and_
User.query.filter(and_(User.name!='fly',User.id = 2)).all()

# 逻辑或
from sqlalchemy import or_
User.query.filter(or_(User.name!='fly',User.id=2)).all()

```
### session

```
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# 创建数据库引擎
some_engine = create_engine('')

# 创建监听数据库引擎的会话类
Session = sessionmaker(bind=some_engine)

session = Session()

# 相等比较==
session.query(User).filter(User.id==1)

# 不相等比较!=
session.query(User).filter(User.name != 'fly')

# 模糊查询'like('% %')'
session.query(User).filter(User.name.like('%ed%'))

# 包含查找in_
session.query(User).filter(User.name.in_(['ed','wendy']))

# 不包含查找~
session.query(User).filter(~User.name.in_(['ed','wendy']))

# 空记录查找
session.query(User).filter(User.name==None)

# 非空记录查找
session.query(User).filter(User.name!=None)

# AND
from sqlalchemy import and_
session.query(User).filter(and_(User.name == 'ed', User.id == 1))
# 可以使用多个filter实现相同的功能
session.query(User).filter(User.name == 'ed').filter(User.id == 1)

# OR
from sqlalchemy import or_
session.query(User).filter(or_(User.name == 'ed', User.id == 1))
```
### flask-sqlalchemy filter和filter_by的区别

filter用类名.属性名,比较用==，filter_by直接用属性名，比较用=。

filter支持><等关系运算符，filter_by不支持。

filter不直接支持组合查询，只能连续调用filter来实现，但是可以通过or_, and_来实现，filter直接支持组合查询。

```
# 前端请求URL为：127.0.0.1:5000/query?deptcd=123&bizdt=123
# 给出门店的号码(DEPTCD)和时间(BIZDT)返回门店对应时间交易量
@app.route('/query')
def query():
    res = {"DEPTCD" : request.args.get('deptcd'),
           "BIZDT" : request.args.get('bizdt')}
    # PosTransmst 在pos_transmst.py文件中定义的PosTransmst类,对应数据库中的POSTRANSMST表
    # and_() 用于支持select 中的and 查询
    '''
    # filter形式查询
    sale = PosTransmst.query.filter(
        and_(PosTransmst.deptcd == res["DEPTCD"], 
        PosTransmst.bizdt == datetime.datetime.strptime(res["BIZDT"], "%Y-%m-%d %H:%M:%S"))
        ).count()
    '''

    # filter_by形式查询
    sale = PosTransmst.query.filter_by(
        deptcd = res["DEPTCD"], 
        bizdt = datetime.datetime.strptime(res["BIZDT"], "%Y-%m-%d %H:%M:%S")
        ).count()
    # datetime.datetime.strptime(res["BIZDT"], "%Y-%m-%d %H:%M:%S")  
    # # 将字符串转换为数据库可以识别的datetime格式
    res["SALE"] = sale

    return jsonify(res)
```