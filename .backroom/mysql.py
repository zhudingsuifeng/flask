# coding: utf-8
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, distinct, func
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

    # __str__() 方法在打印对象的时候，不在打印对象的没存地址，而是打印__str__方法的返回值。
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

# mysql 连接字符串
DB_CONNECT_STRING = 'mysql+pymysql://fly:huangzongwen_123@localhost/web?charset=utf8'

# 初始化数据库连接，创建引擎，echo=True 输出引擎执行的语句
engine = create_engine(DB_CONNECT_STRING)    # , echo=True)

# 创建DB_Session类型
DB_Session = sessionmaker(bind=engine)

# 创建session对象
session = DB_Session()

# 返回结果集的第一项
# data = session.query(student).get(1)

# 返回结果的第2-3项
# datas = session.query(student)[1:3]

# 条件查询
# data = session.query(student).filter(student.id < 3).first()

# 排序
# data = session.query(student).order_by(student.history).all()

# 给结果集的列取别名
# data = session.query(student.name.label('student_name')).all()

# 去重查询(需要导入distinct方法)
# data = session.query(distinct(student.name)).all()

# 统计查询
# data = session.query(student.name).order_by(student.name).count()

# 平均值
# data = session.query(func.avg(student.math)).first()

# 求和
# data = session.query(func.sum(student.math)).first()

# 分组查询统计 
data = session.query(student.teacher, func.count(student.history).label('count')).group_by(student.teacher).all()
print(data)

# print(data.id, data.name, data.age)