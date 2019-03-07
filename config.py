#coding = utf-8
# dialect+driver://username:password@host:port/database
# mysql+pymysql://username:password@host:port/databasename      # mysql连接方式
# oracle+cx_oracle://username:password@host:port/databaseSID    # oracle连接方式

import os

class BaseConfig:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'flask')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

# 数据库连接配置
class DevelopmentConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = 'oracle+cx_oracle://HEX_SPCC:HEX_SPCC@frps.hexcloud.cn:31733/HEXDB'
    SQLALCHEMY_BINDS = {
        'oracle': 'oracle+cx_oracle://HEX_SPCC:HEX_SPCC@frps.hexcloud.cn:31733/HEXDB',
        'mysql': 'mysql+pymysql://fly:huangzongwen_123@localhost/works'
    }

config = {
    'development': DevelopmentConfig
}