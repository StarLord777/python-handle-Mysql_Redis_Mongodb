from redis import Redis
r = Redis()

#list操作
#rpush 在右边传入，lpush在左边传入
r.rpush('qq','star')
print(r.rpush('qq',777))#返回list的大小

print(r.llen('qq'))#返回列表长度

print(r.lrange('qq',0,10))#获取下标从0到10元素
#返回返回key为name的list中index位置的元素
print(r.lindex('qq',5))

#rpop从队尾删除并返回，lpop 从前面删除并返回
print(r.lpop('qq'))



