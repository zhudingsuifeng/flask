## Flask

### flask环境搭建

```
mkdir flask
cd flask
which python3
virtualenv -p /usr/bin/python3 venv
source venv/bin/activate
(venv)$pip install flask
(venv)$pip install flask-script     # 扩展插件,支持命令行选项
(venv)$pip install flask-moment     # 时间插件
(venv)$pip install flask-wtf        # web表单验证
(venv)$pip install jinja2           # 模板渲染
(venv)$pip install flask-bootstrap  # 模板插件
(venv)$pip install flask-sqlalchemy # python orm包
(venv)$pip list                     # 查看当前pip安装的python包
```
[python 数据库支持](https://github.com/zhudingsuifeng/flask/blob/works/docs/pythonDB.md)
### git delete remote file

```
git rm -r --cached targetfile
git commit -m 'delete targetfile'
git push origin works
```

### 报错E1101:Instance of ‘SQLAlchemy’ has no ‘Column’ member

这个错误不影响程序的执行，但是编辑器总是报错，影响心情，并且容易引发误解，浪费时间检查程序。

解决方案：code ——>首选项——>设置——>搜索‘pylintArgs’

将“ “python.linting.pylintArgs”: [] ”添加到用户设置，

如： "python.linting.pylintArgs": ["--load-plugins", "pylint_flask"]

### oracle数据库

```
select * from v$version;  #查看oracle版本信息

Oracle Database 11g Enterprise Edition Release 11.2.0.4.0 - 64bit Production
PL/SQL Release 11.2.0.4.0 - Production
"CORE	11.2.0.4.0	Production"
TNS for Linux: Version 11.2.0.4.0 - Production
NLSRTL Version 11.2.0.4.0 - Production
```

### sqlalchemy

### flask-sqlalchemy

### sqlacodegen

利用sqlacodegen自动生成已有数据表的orm实体类

```
(venv)pip install sqlacodegen
(venv)pip install flask-sqlacodegen
(venv)sqlacodegen --help
usage: sqlacodegen [-h] [--version] [--schema SCHEMA] [--tables TABLES]
                   [--noviews] [--noindexes] [--noconstraints] [--nojoined]
                   [--noinflect] [--noclasses] [--outfile OUTFILE]
                   [--nobackrefs] [--flask] [--ignore-cols IGNORE_COLS]
                   [url]

Generates SQLAlchemy model code from an existing database.

positional arguments:
  url                   SQLAlchemy url to the database

optional arguments:
  -h, --help            show this help message and exit
  --version             print the version number and exit
  --schema SCHEMA       load tables from an alternate schema
  --tables TABLES       tables to process (comma-separated, default: all)
  --noviews             ignore views
  --noindexes           ignore indexes
  --noconstraints       ignore constraints
  --nojoined            don't autodetect joined table inheritance
  --noinflect           don't try to convert tables names to singular form
  --noclasses           don't generate classes, only tables
  --outfile OUTFILE     file to write output to (default: stdout)
  --nobackrefs          don't include backrefs
  --flask               use Flask-SQLAlchemy columns
  --ignore-cols IGNORE_COLS
                        Don't check foreign key constraints on specified
                        columns (comma-separated)

# oracle生成orm实体类
sqlacodegen --flask --tables pos_transmst oracle+cx_oracle://HEX_SPCC:HEX_SPCC@frps.hexcloud.cn:31733/HEXDB > temp.py
# --flask use Flask-SQLAlchemy columns
# --tables 指定数据库中的表，注意后面跟着的表名的大小写
# > 后面指定python文件名，用来存储orm类

# 查看mysql的端口号
mysql> show global variables like 'port';
+---------------+-------+
| Variable_name | Value |
+---------------+-------+
| port          | 3306  |
+---------------+-------+
1 row in set (0.00 sec)

# mysql生成orm实体类
sqlacodegen --tables student mysql+pymysql://fly:password@localhost：3306/web > temp.py
# 如果数据库中的表不是通过sqlalchemy创建的表，并不能完全逆向生成orm类，需要手动做些小修改

mysql> desc student;
+---------+-------------+------+-----+---------+-------+
| Field   | Type        | Null | Key | Default | Extra |
+---------+-------------+------+-----+---------+-------+
| id      | int(11)     | YES  |     | NULL    |       |
| name    | varchar(20) | YES  |     | NULL    |       |
| age     | int(11)     | YES  |     | NULL    |       |
| math    | int(11)     | YES  |     | NULL    |       |
| english | int(11)     | YES  |     | NULL    |       |
| history | int(11)     | YES  |     | NULL    |       |
| teacher | varchar(20) | YES  |     | NULL    |       |
+---------+-------------+------+-----+---------+-------+
7 rows in set (0.01 sec)

# 为表添加primary key
mysql> alter table student add primary key(id);
Query OK, 0 rows affected (0.15 sec)
Records: 0  Duplicates: 0  Warnings: 0

mysql> desc student;
+---------+-------------+------+-----+---------+-------+
| Field   | Type        | Null | Key | Default | Extra |
+---------+-------------+------+-----+---------+-------+
| id      | int(11)     | NO   | PRI | NULL    |       |
| name    | varchar(20) | YES  |     | NULL    |       |
| age     | int(11)     | YES  |     | NULL    |       |
| math    | int(11)     | YES  |     | NULL    |       |
| english | int(11)     | YES  |     | NULL    |       |
| history | int(11)     | YES  |     | NULL    |       |
| teacher | varchar(20) | YES  |     | NULL    |       |
+---------+-------------+------+-----+---------+-------+
7 rows in set (0.00 sec)
```