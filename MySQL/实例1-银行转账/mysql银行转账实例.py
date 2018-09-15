# 账户A给账户B转账100元，该操作是要么成功，要么失败
'''
流程：
开始一个事务，检查账户AB是否可用，账户A是否有100，没问题的话，给B转100，提交事务
            若出现异常，则回滚操作
'''
import pymysql
conn = pymysql.connect(host='localhost',port=3306,user='root',passwd='root',db='qq')
cursor = conn.cursor()

#首先创建表，填入数据
#该数据库默认引擎为INNODB，支持事务
#sql = '''
#create table bank(
#id int not null primary key comment '账户ID',
#money int not null comment '账户余额'
#);
#'''
#cursor.execute(sql)

class TransferMoney():
    def __init__(self,conn,cursor,A,B,money):
        self.conn = conn
        self.cursor = cursor
        self.A = A
        self.B = B
        self.num = money
    def transfer(self):
        try:
            #检查AB账户余额并存入变量，如果账户不存在则会报错，进入except
            self.cursor.execute('select money from bank where id={}'.format(self.A))
            a = int(self.cursor.fetchone()[0])
            self.cursor.execute('select money from bank where id={}'.format(self.B))
            b = int(self.cursor.fetchone()[0])
            print(a,b)      #打印AB账户的金额，供测试用
            if a<self.num:
                print('余额不足，转账失败')      #若余额不足，属于正常执行，没有i,u,d语句，不用回滚
            else:
                #此为转账操作，将A的钱减去转账金额，B的钱加上转账金额
                #这里如果出错则进入except执行数据回滚
                #体现了事务的原子性，事务操作要么都做，要么都不做，如果其中一条语句错误，则全部回滚
                self.cursor.execute('update bank set money={} where id={}'.format(a-self.num,self.A))
                self.cursor.execute('update bank set money={} where id={}'.format(b + self.num, self.B))
                self.conn.commit()      #提交后数据库才会改变
                print('转账成功')
        except Exception as e:
            print('转账失败，事务回滚,请检查是否输入错误，放心，您的钱还在！')
            self.conn.rollback()

if __name__ == '__main__':
    A = int(input('请输入您的账户：'))
    B = int(input('请输入对方账户：'))
    money = int(input('请输入要转账的金额：'))

    tm = TransferMoney(conn,cursor,A,B,money)
    tm.transfer()

