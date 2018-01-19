"""
class operator_overload1:
    def __init__(self):
        self.L = [5,6,7,8,9]
    def __getitem__(self,index):
        print('getitem',index)
        return self.L[index]
    def __setitem__(self,index,value):
        print('setitem',index)
        self.L[index] = value
operator1 = operator_overload1()
print(operator1[3])
L = [5,6,7,8,9]
print(L[::2],L[0:],L[2:4],L[-5:])
print(operator1[::2],operator1[0:],operator1[2:4],operator1[-5:])
operator1[1] = 100
print(operator1[1])
"""
"""
class operator_overload2:
    def __init__(self,start,stop):
        self.value = start - 1
        self.stop = stop
    def __iter__(self):
        return self
    def __next__(self):
        if self.value == self.stop:
            raise StopIteration
        self.value += 1
        return self.value ** 2
for i in operator_overload2(1,5):
    print(i,end = ' ')
"""
class SkipIterator:
    def __init__(self,wrapped):
        self.wrapped = wrapped
        self.offset = 0
    def __next__(self):
        if self.offset >= len(self.wrapped):
            raise StopIteration
        else:
            self.item = self.wrapped[self.offset]
            self.offset += 2
            return self.item
"""class SkipObject:
    def __init__(self,wrapped):
        self.wrapped = wrapped
    def __iter__(self):
        return SkipIterator(self.wrapped)
if __name__ == '__main__':
    l = ['1','2','3','4']
    x = SkipObject(l)
    I = iter(x)
    i = next(I)
    print(i,next(I),next(I))
    for i in x:
        print(i)
"""
"""
class Iters:
    def __init__(self,value):#调用顺序__contains__,__iter__,__getitem__
        self.data = value;
    def __getitem__(self,i):
        print('get[%s]' % i,end = '')
        return self.data[i]
    def __iter__(self):
        print('iter => ',end = '')
        self.ix = 0
        return self
    def __next__(self):
        print('next:',end = '')
        if self.ix == len(self.data):
            raise StopIteration
        item = self.data[self.ix]
        self.ix += 1
        return item
    def __contains__(self,x):
        print('contains:', end = '')
        return x in self.data
x =Iters([1,2,3,4,5])
print(3 in x)
for i in x:
    print(i,end = '|')
print([i ** 2 for i in x])
print(list(map(bin,x)))
I = iter(x)
while True:
    try:
        print(next(I),end  = '@')
    except StopIteration:
        break
class get_set_attribute:
    def __getatrr__(self,attname):
        if attname == 'age':
            return 40
        else:
            raise AttributeError
    def __setattr__(self,attr,value):
        if attr == 'age':
            self.__dict__[attr] = value
        else:
            raise AttributeError
test = get_set_attribute()
#test.name = 'wang'
test.age = 25
print(test.age)
"""
"""
class test:
    def te(self,value):
        if self.private == 1:
            self.wang = value
a  = test()
a.private = 1
b = test()
#print(b.private)
a.te(2)
print(a.wang)
"""
class adder:
    def __init__(self,value = 0):
        self.data = value
    def __add__(self,other):
        self.data += other
class addboth(adder):
    def __str__(self):
        return '[value：%d]' % (self.data)
    def __repr__(self):
        return 'addboth(%s)' % self.data
x = addboth(1)
print(x)
class Commuter:
    def __init__(self,value):
        self.val = value
    def __add__(self,other):
        print('add', self.val, other)
        return self.val + other
    def __radd__(self,other):
        print('radd', other, self.val )
        return other + self.val
    def __iadd__(self,other):
        self.val += other
        return self
x = Commuter(1)
y = Commuter(2)
print(1 + x, x + 1, x + y )
class C:
    data = 'spam'
    def __gt__(self,other):
        return self.data > other
    def __lt__(self,other):
        return self.data < other
    def __del__(self):
        print('delete myself')
x = C()
y = C()
C.data = 'a'
print(C.__name__)
print( x < 'a')
print( x > 'a')
print('a' < x )
print('a' > x )
print( y < 'a')
print( y > 'a')
print('a' < y )
print('a' > y )
C.data = 'b'
print( x < 'a')
print( x > 'a')
print('a' < x )
print('a' > x )
x = 1
import lister
class testtree(Commuter,C,lister.ListerTree):
    pass
x = testtree(1)
print(x)