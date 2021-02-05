class Parent(object):
    # *arg（元组）, **kwargs（字典） 不定长参数
    def __init__(self, name, *arg, **kwargs) -> None:
        print('parent的init开始被调用')
        self.name = name 
        print('parent的init结束被调用')


class Son1(Parent):
    def __init__(self, name, *arg, **kwargs) -> None:
        print('Son1的init开始被调用')
        super().__init__(name, *arg, **kwargs)
        print('Son1的init开始被调用')


class Son2(Parent):
    def __init__(self, name, *arg, **kwargs) -> None:
        print('Son2的init开始被调用')
        super().__init__(name, *arg, **kwargs)
        print('Son2的init开始被调用')


class Grandson(Son1, Son2):
    def __init__(self, name, *arg, **kwargs) -> None:
        print('Grandson的init开始被调用')
        super().__init__(name, *arg, **kwargs)
        print('Grandson的init开始被调用')


print(Grandson.__mro__)