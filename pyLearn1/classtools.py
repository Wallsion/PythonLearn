class AttrDisplay:
    def gatherAttrs(self):
        attrs = []
        for key in sorted(self.__dict__):
            attrs.append('%s=%s' % (key,getattr(self,key)))
        return ','.join(attrs)
    def __str__(self):
        return '[%s:%s]' % (self.__class__.__name__,self.gatherAttrs())
if __name__ == "__main__":
    class Toptest(AttrDisplay):
        count = 0
        def __init__(self):
            self.att1 = Toptest.count
            self.att2 = Toptest.count + 1
            Toptest.count += 2
    class Subtest(Toptest):
        pass
    X,Y = Toptest(),Subtest()
    print(X)
    print(Y)
    def test():#函数会搜索嵌套域，类中的方法不会搜类中的属性
        coun = 1;
        def ll():
            print(coun)
        return ll()
    test()

