class Class_name(object):
    res = 100

    @property
    def val(self):
        return self.res

    @val.setter
    def val(self, value):
        self.res = value

    @val.deleter
    def val(self):
        del self.res


c = Class_name()
print(c.val)
c.val = 200
print(c.val)
del c.val
print(c.val)
del c.val
print(c.val)