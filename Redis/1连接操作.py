#连接Redis数据库,需要安装Redispy库
from redis import Redis
#连接需指定IP，端口（默认6379），数据库（默认0）
redis = Redis(host='127.0.0.1',port=6379,db=6)

print(redis)