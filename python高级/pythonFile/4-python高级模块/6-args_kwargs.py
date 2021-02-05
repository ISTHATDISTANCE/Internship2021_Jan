def test(a, b, *arg, **kwargs):
    """*arg用于接受多余的参数（以元组的形式储存），**kwargs用于接受的多余的带名参数（以字典方式储存）"""
    print(a)
    print(b)
    print(arg)
    print(kwargs)


def test2(a, b, *arg, **kwargs):
    print(a)
    print(b)
    print(arg)
    print(kwargs)
    # test(a, b, arg, kwargs) 此时arg和kwargs以元组(args, kwargs)的形式传入
    # test(a, b, arg=arg, kwargs=kwargs) 此时等价于{'arg': arg, 'kwargs': kwargs}
    test(a, b, *arg, **kwargs) # 此时以完全不变的形式传入


test2(11, 22, 33, 44, 55, 66, name="ltt", age=18)