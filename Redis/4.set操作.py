from redis import Redis
r = Redis()

#sadd   srem     spop
print(r.sadd('sql','mysql'))
print(r.sadd('sql','oracle'))
print(r.spop('sql'))
print(r.srem('sql','mysql'))

#scard
print(r.scard('sql'))

#smembers,sismember
r.sadd('sql','redis','mongodb')
print(r.smembers('sql'))
print(r.sismember('sql','mysql'))