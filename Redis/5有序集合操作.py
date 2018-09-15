from redis import  Redis
r = Redis()

#添加删除元素    zadd zrem
r.zadd('qq','redis',100,'mysql',50,'oracle',49)
#####我擦，这个分数到后面去了，要记住啊！！！，语法跟Redis不一样
#返回个数
print(r.zcard('qq'))

#返回在分数区间的个数
print(r.zcount('qq',50,100))

#返回元素排名
print(r.zrank('qq','redis'))


