# python操作MySQL数据库

- python2的驱动 mysqldb

- python3的驱动 pymysql

### python DB API：python访问数据库的统一接口规范
- 数据库连接对象 connection

- 数据库交互对象 cursor

- 数据库异常类 exception

##### 流程：开始-创建connection-获取cursor-(执行查询，命令，获取，处理数据)-关闭cursor-关闭connection-结束



### 安装pymysql模块
- pip install pymysql

- 引入该模块
  - import pymysql

  - print(pymysql.__version__)


---

## 数据库连接对象connection
- pymysql.connect(参数):
  - host
  - port
  - user
  - passwd
  - db
  - charset

- 该对象支持的方法：
  - cursor() 使用该连接创建并返回游标
  - commit() 提交当前事务

  - rollback() 回滚当前事务
  - close() 关闭连接

- pymysql.connect(host='localhost',port=3306,user='root',passwd='root',db='mysql',charset='utf8')



## 数据库交互对象cursor
- 该对象支持的方法：
  - execute(op[args]) 执行一个数据库查询或命令
  - fetchone() 取的结果集的下一行

  - fetchmany(size) 取的结果集的下n行
  - fetchall() 获取结果集中剩下的所有行

  - rowcount() 最近一次execute返回数据的行数或影响行数
  - close()  关闭对象

- 注意：调用execute方法后数据存在缓冲区内，调用fetch方法获取数据


## 实例演示

- 执行命令，查询：
      cursor.execute('select * from myapp_student')
      print(cursor.rowcount)
      for i in cursor.fetchall():
          print(i)

- 插入，更新，删除
  - 语句没什么问题

#### 注意！这些操作需要提交，conn.commit()

#### 过程：使用cursor.execute()执行i,u,d操作，如果出现异常，进行conn.rollback()进行事务回滚，如果没有出现异常，则conn.commit()提交事务


## 事务的概念：访问和更新数据库的一个程序执行单元
- 原子性：事务中的操作要么都做，要么都不做

- 一致性：事务必须保证数据库从一个一致性状态变到另一个一致性状态

- 持久性：事务一旦提交，对数据库的改变就是永久的

- 隔离性：一个事务的执行不能被其他事务干扰

## 开发过程中一般设置自动提交为失效！！！！
- 关闭自动commit ,conn.autocommit(False)

- 正常结束：conn.commit()

- 异常结束：conn.rollback()

- 经试验，pymysql模块中默认为FALSE

        try:
            cursor.execute('insert into myapp_student values (11,"test",20,1,"haha",1)')
            cursor.execute('insert into myapp_student values (13,"test",20,1,"haha",1)')
            cursor.execute('delete from myapp_student where qid=1000')
            conn.commit()
        except:
            print('SQL语句执行出错，执行回滚操作')
            conn.rollback()
