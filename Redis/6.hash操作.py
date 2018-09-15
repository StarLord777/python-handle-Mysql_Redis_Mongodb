from redis import Redis
r = Redis()

#hash操作，值为字典类型，方便查找

#添加，hset   hmset
r.hset('redis','cake',6)
r.hset('redis','mysql','666')
print(r.hgetall('redis'))

#  hget   hmget获取一个或多个
print(r.hget('redis','cake'))

#判断是否存在键
print(r.hexists('redis','mysql'))

#删除键
print(r.hdel('redis','1'))

print(r.hlen('redis'))

#---  hkeys   hvals      从key为name的hash中获取所有键名，映射的值
print(r.hkeys('redis'))
print(r.hvals('redis'))