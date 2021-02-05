# Redis 简介

## redis 优势

- 性能极高
- 丰富数据类型
- 原子性
- 丰富特性

# 数据类型

## string

string是redis最基本的类型，是二进制安全的（包含任何数据，如jpg或者序列化对象），类型值最大能储存512MB

```redis
redis 127.0.0.1:6379> SET runoob "菜鸟教程"
OK
redis 127.0.0.1:6379> GET runoob
"菜鸟教程"
```

**(error) WRONGTYPE Operation against a key holding the wrong kind of value** 当重复定义了相同键时会出现该错误。

## hash

redis hash是键值对的集合

```redis
redis 127.0.0.1:6379> DEL runoob
redis 127.0.0.1:6379> HMSET runoob field1 "Hello" field2 "World"
"OK"
redis 127.0.0.1:6379> HGET runoob field1
"Hello"
redis 127.0.0.1:6379> HGET runoob field2
"World"
```

## list

redis list是简单的字符串列表，按照插入顺序排序

```
redis 127.0.0.1:6379> DEL runoob
redis 127.0.0.1:6379> lpush runoob redis
(integer) 1
redis 127.0.0.1:6379> lpush runoob mongodb
(integer) 2
redis 127.0.0.1:6379> lpush runoob rabbitmq
(integer) 3
redis 127.0.0.1:6379> lrange runoob 0 10
1) "rabbitmq"
2) "mongodb"
3) "redis"
```

## set

set是string类型的无序集合，添加、查找、删除的复杂度都是O(1)

### sadd 命令

添加一个 string 元素到 key 对应的 set 集合中，成功返回 1，如果元素已经在集合中返回 0。

```
sadd key member
```

## zset

有序集合，每个成员关联一个分数，以此作为排名

```
zadd key score member
```

## redis 键

管理redis的键

## Redis HyperLogLog

Redis 在 2.8.9 版本添加了 HyperLogLog 结构。

Redis HyperLogLog 是用来做基数统计的算法，HyperLogLog 的优点是，在输入元素的数量或者体积非常非常大时，计算基数所需的空间总是固定 的、并且是很小的。

在 Redis 里面，每个 HyperLogLog 键只需要花费 12 KB 内存，就可以计算接近 2^64 个不同元素的基 数。这和计算基数时，元素越多耗费内存就越多的集合形成鲜明对比。

但是，因为 HyperLogLog 只会根据输入元素来计算基数，而不会储存输入元素本身，所以 HyperLogLog 不能像集合那样，返回输入的各个元素。

## redis 事务

redis可以一次执行多个命令，类似sql，但无法回滚（一条命令出错后不影响其他命令

multi开始，exec执行事务块结束