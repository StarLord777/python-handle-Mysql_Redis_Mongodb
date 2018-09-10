# MySQL 最流行的关系型数据库

- 数据库: 数据库是一些关联表的集合。
- 数据表: 表是数据的矩阵。在一个数据库中的表看起来像一个简单的电子表格。
- 列: 一列(数据元素) 包含了相同的数据, 例如邮政编码的数据。
- 行：一行（=元组，或记录）是一组相关的数据，例如一条用户订阅的数据。
- 冗余：存储两倍数据，冗余降低了性能，但提高了数据的安全性。
- 主键：主键是唯一的。一个数据表中只能包含一个主键。你可以使用主键来查询数据。
- 外键：外键用于关联两个表。
- 复合键：复合键（组合键）将多个列作为一个索引键，一般用于复合索引。
- 索引：使用索引可快速访问数据库表中的特定信息。索引是对数据库表中一列或多列的值进行排序的一种结构。类似于书籍的目录。
- 参照完整性: 参照的完整性要求关系中不允许引用不存在的实体。与实体完整性是关系模型必须满足的完整性约束条件，目的是保证数据的一致性。


---

### MySQL管理（win下）
- 开启服务  net start mysql

- 关闭服务  net stop mysql

- 连接数据库  mysql -u root -p

- 关于用户设置
  - 添加用户只需在mysql user表中添加数据即可
  - 还可以使用 grant命令

- 操作数据库
  - 使用数据库 use 数据库名;
  - 列出所有数据库列表 show databases;
  - 显示指定数据库所有表  show tables;
  - 显示指定表所有属性    desc 表名;


---

# SQL语法

### select语句：
- 用于查询数据

- 语法：SELECT column_name,column_name
FROM table_name;

- SELECT * FROM table_name;

### select distinct语句：
- SELECT DISTINCT 语句用于返回唯一不同的值。

      +----+--------------+---------------------------+-------+---------+
      | id | name         | url                       | alexa | country |
      +----+--------------+---------------------------+-------+---------+
      | 1  | Google       | https://www.google.cm/    | 1     | USA     |
      | 2  | 淘宝          | https://www.taobao.com/   | 13    | CN      |
      | 3  | 菜鸟教程      | http://www.runoob.com/    | 4689  | CN      |
      | 4  | 微博          | http://weibo.com/         | 20    | CN      |
      | 5  | Facebook     | https://www.facebook.com/ | 3     | USA     |
      +----+--------------+---------------------------+-------+---------+

- SELECT DISTINCT country FROM Websites;

- 只会返回USA和CN，如果查询多列，除非两行全部相同，否则dictinct无效

### where子句：
- WHERE 子句用于过滤记录。

- SELECT column_name,column_name
FROM table_name
WHERE column_name operator value;

- 例子
  - SELECT * FROM Websites WHERE country='CN';
  - SELECT * FROM Websites WHERE id=1;

- 用到的运算符：= ，！=，>，<，>=，<=，
  - between 在某个范围内
  - like   搜索某种模式
  - in  指定针对某个列的多个可能值，跟python一样

### and 和 or 运算符
- AND & OR 运算符用于基于一个以上的条件对记录进行过滤。

- 如果第一个条件和第二个条件都成立，则 AND 运算符显示一条记录。

- 如果第一个条件和第二个条件中只要有一个成立，则 OR 运算符显示一条记录。

- 从 "Websites" 表中选取国家为 "CN" 且alexa排名大于 "50" 的所有网站：
  - SELECT * FROM Websites
WHERE country='CN'
AND alexa > 50;

- 从 "Websites" 表中选取国家为 "USA" 或者 "CN" 的所有客户：
  - SELECT * FROM Websites
WHERE country='USA'
OR country='CN';

- 从 "Websites" 表中选取 alexa 排名大于 "15" 且国家为 "CN" 或 "USA" 的所有网站：
  - SELECT * FROM Websites
WHERE alexa > 15
AND (country='CN' OR country='USA');


### ORDER BY 关键字
- ORDER BY 关键字用于对结果集按照一个列或者多个列进行排序。

- ORDER BY 关键字默认按照升序对记录进行排序。如果需要按照降序对记录进行排序，可以使用 DESC 关键字。

- 例子：
  - 从 "Websites" 表中选取所有网站，并按照 "alexa" 列排序：
    - SELECT * FROM Websites
ORDER BY alexa;
  - 降序排序
    - SELECT * FROM Websites
ORDER BY alexa DESC;
  - 从 "Websites" 表中选取所有网站，并按照 "country" 和 "alexa" 列排序：
    - SELECT * FROM Websites
ORDER BY country,alexa;

### INSERT INTO 语句
- 用于插入新记录

- INSERT INTO table_name
VALUES (value1,value2,value3,...);

- INSERT INTO table_name (column1,column2,column3,...)
VALUES (value1,value2,value3,...);

- 向 "Websites" 表中插入一个新行：
  - INSERT INTO Websites (name, url, alexa, country)
VALUES ('百度','https://www.baidu.com/','4','CN');

- 在指定的列插入数据：
  - INSERT INTO Websites (name, url, country)
VALUES ('stackoverflow', 'http://stackoverflow.com/', 'IND');


### UPDATE 语句
- 用于更新表中的记录

- UPDATE table_name
SET column1=value1,column2=value2,...
WHERE some_column=some_value;

- 假设我们要把 "菜鸟教程" 的 alexa 排名更新为 5000，country 改为 USA
  - UPDATE Websites
SET alexa='5000', country='USA'
WHERE name='菜鸟教程';

##### Update 警告！
- 在更新记录时要格外小心！在上面的实例中，如果我们省略了 WHERE 子句

- 执行以上代码会将 Websites 表中所有数据的 alexa 改为 5000，country 改为 USA。


### DELETE 语句
- DELETE 语句用于删除表中的记录。

- DELETE FROM table_name
WHERE some_column=some_value;

- 从 "Websites" 表中删除网站名为 "百度" 且国家为 CN 的网站 :
  - DELETE FROM Websites
WHERE name='百度' AND country='CN';

- 删除所有数据:
  - DELETE FROM table_name;
  - DELETE * FROM table_name;
