from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://fly:huangzongwen_123@localhost/web?charset=utf8'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class user(db.Model):
    __tablename__ = 'user'
    id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True)

    def __init__(self, id=None, name='test'):
        self.id = id
        self.name = name

    def __repr__(self):
        return '<User %r>' % self.name

# test_user = user(4, 'temp')
# db.session.add(test_user)
# db.session.commit()

data = db.session.query(user).all()
print(data[1].id, data[1].name)