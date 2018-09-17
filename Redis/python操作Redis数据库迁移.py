from redis import Redis
A = Redis(host='127.0.0.1',db=7)
B = Redis(host='192.168.1.10',db=7)
#测试连接是否成功
print(A,B)
#--------------------------------------------------------------------------
def copydb():
    for key in A.keys():
        # 转成字符串形式
        key = str(key)[2:-1]
        key_type = str(A.type(key))[2:-1]
        print('*' * 30)
        print('A:', 'key='+key, '---------type='+key_type)
        #对字符串类型的键值对执行操作------------------------------------------
        if key_type == 'string':
            print(A.get(key))
            B.set(key,str(A.get(key))[2:-1])
            print('写入到数据库B成功，{}'.format(B.get(key)))
        #对哈希字典类型的键值对执行操作-----------------------------------------
        elif key_type == 'hash':
            print(A.hgetall(key))
            for son_key in A.hkeys(key):
                son_key = str(son_key)[2:-1]
                son_value = str(A.hget(key,son_key))[2:-1]
                B.hset(key,son_key,son_value)
            print('写入到数据库B成功，{}'.format(B.hgetall(key)))
        #对列表类型的键值对执行操作---------------------------------------------
        elif key_type == 'list':
            print('A:',A.lrange(key, 0, A.llen(key)))
            for value in A.lrange(key, 0, A.llen(key)):
                v1 = str(value)[2:-1]
                B.rpush(key, v1)
            print('写入到数据库B成功，{}'.format(B.llen(key)))
        #对集合类型的键值对执行操作---------------------------------------------
        elif key_type == 'set':
            print('A:',key, A.scard(key))
            for value in A.smembers(key):
                value = str(value)[2:-1]
                B.sadd(key,value)
            print('写入到数据库B成功，{}'.format(B.scard(key)))
        #对有序集合类型的键值对执行操作------------------------------------------
        elif key_type == 'zset':
            print('A:',key,A.zcard(key))
            for value in A.zrangebyscore(key,0,100):
                value = str(value)[2:-1]
                score = A.zscore(key,value)
                print(value,score,end='----')
                B.zadd(key,value,score)
            print('\n写入到数据库B成功，{}'.format(B.zcard(key)))

copydb()

def testdata():
    A.set('str_test','redis')
    A.rpush('list_test','redis'),A.rpush('list_test','python')
    A.sadd('set_test','redis'),A.sadd('set_test','python')
    A.zadd('zset_test','python',66),A.zadd('zset_test','redis',99)
    A.hset('hash_test','db','redis'),A.hset('hash_test','qq','1694')

#testdata()
