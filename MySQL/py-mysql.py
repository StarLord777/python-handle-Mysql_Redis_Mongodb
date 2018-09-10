#python操作mysql数据库，使用pymysql模块
import pymysql
pymysql.install_as_MySQLdb()

#创建连接
conn = pymysql.connect(host='localhost',port=3306,user='root',passwd='root',db='myapp',charset='utf8')
#获取游标
cursor = conn.cursor()

#执行SQL语句
cursor.execute('show tables')
print(cursor.fetchall())

cursor.execute('desc myapp_student')
print(cursor.fetchall())

cursor.execute('select * from myapp_student')
print(cursor.rowcount)      #返回受影响的行数
for i in cursor.fetchall():     #返回结果集
    print(i)

try:
    cursor.execute('insert into myapp_student values (11,"test",20,1,"haha",1)')
    cursor.execute('insert into myapp_student values (13,"test",20,1,"haha",1)')
    cursor.execute('delete from myapp_student where qid=1000')      #该表中无此列qid
    conn.commit()
except:
    print('SQL语句执行出错，执行回滚操作')
    conn.rollback()

