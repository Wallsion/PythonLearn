#Person 类
from classtools import AttrDisplay
class Person(AttrDisplay):
    """
    创建，操作个人记录
    """
    def __init__(self,name,job = None,pay = 0):
        self.name = name
        self.job = job
        self.pay = pay
    def lastName(self):
        return self.name.split()[-1]
    def giveRaise(self,percent = 0):
        self.pay = int(self.pay * ( 1 + percent ))
    #def __str__(self):
        #return "%s/%s/%d" % (self.name,self.job,self.pay)
class Manager(Person):#继承，定制
   """
   针对person的特殊定制
   """
   def __init__(self,name,pay):
        Person.__init__(self,name,"mgr",pay)
   def giveRaise(self, percent = 0,bonus = 0.1):
        Person.giveRaise(self,percent + bonus)
        #self.pay = int(self.pay * (1 + percent + bonus))
class Manager1:#拦截，委托
    def __init__(self, name,pay):
        self.person = Person(name,'mgr',pay)
    def giveRaise(self,percent,bonus = 0.1):
        self.person.giveRaise(percent + bonus)
    def __getattr__(self,attr):
        return getattr(self.person,attr)
    def __str__(self):
        return str(self.person)
if __name__ == "__main__":
    wang = Person('Willson','Alibaba',400000)
    dai = Person('Dai Huijun','Anhui University',pay = 20000)
    print(wang.name,wang.job,wang.pay)
    print(dai.name,dai.job,dai.pay)
    print(wang.lastName())
    wang.giveRaise(.2)
    print(wang.pay)
    print(wang,dai,sep = '\n')
    xin = Manager('xx',400000)
    print(xin)
    xin.giveRaise(.1)
    print(xin)
    print(wang.__class__,wang.__class__.__name__,sep = '  ')
    print(list(wang.__dict__.keys()),wang.__dict__.values())
    print(getattr(wang,'name'))
    import scrapy
    