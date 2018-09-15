from  redis import Redis
r = Redis()

#set方法
print(r.set('nosql','redis'))
print(r.get('nosql'))

#getset方法，为存在的key关联新的value，并返回旧值
print(r.getset('nosql','mongodb'))

#mget返回多个key对应的value,
print(r.mget('qq','pp','yy','star'))
print('*'*40)
#-------------------------------------------------------------
#key 操作
print(r.exists('qq'))
print(r.delete('pp'))
print(r.type('nosql'))
print(r.randomkey())
print(r.rename('yy','star'))
print(r.move('star',7))
#获取当前数据库中的key个数
print(r.dbsize())
#删除当前数据库中所有key
print(r.flushdb())
print(r.dbsize())