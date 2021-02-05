class Province(object):
    con = "sjtu"

    def enroll(self, name):
        """
        docstring
        """
        self.stu = name

    @classmethod
    def cls_mthd(cls,nam):
        cls.con = nam

    @staticmethod
    def stc_mthd():
        print("lalala")


ltt = Province()

ltt.enroll("ltt")

print(ltt.stu)

Province.cls_mthd("ji")

print(ltt.con)
