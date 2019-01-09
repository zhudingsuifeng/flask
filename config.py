#coding = utf-8
# dialect+driver://username:password@host:port/database
# mysql+pymysql://username:password@host:port/databasename      # mysql连接方式
# oracle+cx_oracle://username:password@host:port/databaseSID    # oracle连接方式

DIALECT = 'oralce'
DRIVER = 'cx_oracle'
USERNAME = 'HEX_SPCC'
PASSWORD = 'HEX_SPCC'
HOST = 'frps.hexcloud.cn'
PORT = '31733'
SID = 'HEXDB'

# 连接字符串变量名
SQLALCHEMY_DATABASE_URI = '{}+{}://{}:{}@{}:{}/{}?charset=utf8'.format(DIALECT, DRIVER, USERNAME, PASSWORD, HOST, PORT, SID)

TABLENAME = 'POS_TRANSMST'