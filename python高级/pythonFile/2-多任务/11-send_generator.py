def create_num(all_num):
    a, b = 0, 1
    current_num = 0
    while current_num < all_num:
        res = yield af
        print(">>>res>>>", res)
        a, b = b, a+b
        current_num += 1


obj = create_num(10)

ret = next(obj)
print(ret)

# send中的参数作为yield的返回值，可以修改参考值；但第一次传入时会出现问题（传入的值没人接收）
# 可以通过next或者参数为None来解决
ret = obj.send("lalala")
print(ret)

