#模块导入
from _struct import pack
from re import match
#基本语句
print ("hello world")
L = [1,2,[1,2],'hello']
print(L[1:2])
print(L[3])
context = """hello world!
hello china
do you like me ?
wangxin"""
#文件操作 序列化
myfile = open('myfile.txt','w')
myfile.write(context)
myfile.close()
import pickle
D = {'a' : 1, 'b' : 2}
F = open('datafile.pkl', 'wb')
pickle.dump(D,F)
F.close()
F = open('datafile.pkl','rb')
E = pickle.load(F)
print(E)
"""F = open('data.bin','wb')
import struct
data = struct.pack('>i4sh', 7, 8,10)
print(data)
F.write(data)
F.close()"""
x = 'samp'
#判断语句
while x:
    print(x)
    x = x[1:]
x = ...
print(x)
y = 53
x = y // 2
while x > 1:
    if y % x == 0:
        print("%2d 是个合数\n" % (y))
        print(x)
        break
    x -= 1
else:
    print("%2d 是个质数" % (y))
found = False
x = [1,2,3,4,5,10]

"""while x and not found:
    if match(x[0]):
        print("Yes")
        found = not found
    else:
        x = x[1:]
else:
    print("Not found")"""
sep1 = "spam"
sep2 = "scam"
res = []
for x in sep1:
    if x in sep2:
        print(x,end = " ")
    else:
        continue
for line in open('myfile.txt'):
    print(line,end = '')
tem = sep1[0:len(sep1):2]
print(tem)
for i in range(len(sep1)):
    print(i)
    print(sep1[i])
if 's' in sep2:
    print(True)
else:
    print(False)
print(tuple(map(ord,"a")))
keys = [1,2,3]
vales = ["one","two","three"]
D = {}
for (k,v) in zip(keys,vales):D[k] = v
print(D)
D1 = dict(zip(keys,vales))
print(D1)
for (i,dic) in enumerate(D1):
    print(i,D1[dic],sep = "->")
for x in open('myfile.txt'):
    print(x,end ="")
f = open('myfile.txt')
print("\n"+next(f),end = '')
L = range(0,100)
I = iter(L)
while True:
    try:
        X = next(I)
    except StopIteration:
        break
    print("%-4d" % (X**2),end = ' ')
print()
for keys in D:#for keys in D.keys():
    print(keys,D[keys])
C = enumerate('samp')
print(C)
I = iter(C)
print(next(I))
for (index ,c) in C:
    print(index,c)
print("".join([x + y for x in "abc" for y in "123"]))
print(list(map(str.upper,open('myfile.txt'))))
print(max(open('myfile.txt')),end = ' ')
print(min(open('myfile.txt')),end = '')
[a,b,*c] = open('myfile.txt')
print(a,b,c)
print({index:value for index ,value in enumerate(open('myfile.txt'))})
def f(a,b,c,d): print(a,b,c,d,sep = " ")
f( *(open('myfile.txt')))
L = [];
s = 'hello world'
sum1 = 0;
for s1 in s:
    sum1 = sum1 + ord(s1)
    L.append(ord(s1))
    print(ord(s1),sum1,L,end = '\n')
for i in range(50):
    print('hello %d\a' % i)
D = {1:"one",5:'five',2:'two',4:'four'}
for d in sorted(D):
    print('%d : %s' % (d,D[d]))
for d in sorted(D.keys()):
    print(d,D[d])
def maker(x):
    def action(y):
       return y ** x
    return action

f = maker(4)
print(f(2))
def makerAction():
    acts = []
    for i in range(5):
        acts.append(lambda x , i = i: i ** x)#acts.append(lambda x: i ** x)
    return acts
acts = makerAction()
print(acts[4](2))
print(acts[0](2))
#gl = 1;
def f():
    global gl
    gl = 3
    print(gl)
f()
print(gl)
def tester(start):
    def nested(label):
        print(label,nested.state)
        nested.state += 1
    nested.state = start
    return nested
F = tester(0)
F('wang')
print(F.state)
def multiple(x,y):
    x = 2
    y = [3,4]
    return x, y
x = 1
y = [1,2]
x,y = multiple(x, y)
T = (x,y)
print(T)
print(x,y,sep = "#")
def func(a:'samp',b,c:99,d):
    return a + b + c + d
def tracer(func,*pargs,**kargs):
    print('calling','func')
    return func(*pargs,**kargs)

print(tracer(func,1,2,d = 3,c = 4))
def intersect(*args):
    res = []
    for x in args[0]:
        for last in args[0:]:
            if x not in last: break;
        else:
            res.append(x)
    return res
def union(*args):
    res = []
    for x in args:
        for i in x:
            if i not in res:
                res.append(i)
            else:
                continue
    return res
s1,s2,s3 = 'wang','cang','anxy'
print(intersect(s1,s2,s3))
print(union(s1,s2,s3))
import sys
def print30(*args,**kargs):
    sep = kargs.pop('sep',' ')
    end = kargs.pop('end','\n')
    file = kargs.pop("file",sys.stdout)
    if kargs: raise TypeError('错误: %s'.format(kargs))
    output = ""
    first = True
    for arg in args:
        output += ("" if first else sep) + str(arg)
        first = False
    file.write(output + end)
print30(1,2,3,4,sep = '*')
from tkinter import *
widgt = Button(text = 'press me',command = print30)
def echo(context:'input') -> None:
    print(context)
Dic = [(echo,'hello')]
for (func,arg) in Dic:
    func(arg);
func.__name__
dir(func)
func.__code__
print(func.__code__.co_varnames)
print(func.__code__.co_argcount)
func.description = "print input"
print(func.__annotations__)
import sys
"""from tkinter import Button,mainloop
x = Button(text = 'Press me',command = (lambda:sys.stdout.write('wang\n')))
x.pack();
mainloop();"""
print(list(range(-5,5)))
print(list(filter(lambda x: x > 0,range(-5,5))))
from functools import reduce
print(reduce(lambda x,y: x + y,[1,2,3,4]))
def myreduce(function,sequence):
    tem = sequence[0]
    for sequ in sequence[1:]:
        tem = function(tem,sequ)
    return tem
myreduce(lambda x,y: x + y,[1,2,3,4])
#列表解析
print([x for x in range(5) if x % 2 == 0])
print([(x + y) for x in range(-5,0) for y in range(5)])#嵌套循环
print([{x:y} for x in range(5) if x % 2 == 0 for y in range(5) if y % 2 == 1])
M =[[1,2],
    [3,4],
    [5,6]]
N = [[1,2,3],
     [4,5,6]]
N_ = [ N[i][j] for j in range(len(N[0])) for i in range(len(N))]
N_reverse = []
i = 0
while i < len(N_):
    N_reverse.append(N_[i:i+len(N)])
    i += len(N)
print(N_reverse)
MN = [[M[i][0]*N[0][j]+M[i][1]*N[1][j] for i in range(len(M))] for j in range(len(N[0]))]
MN1 = [[reduce((lambda x, y: x+y),list(map(lambda m,n: m*n,M[i],N_reverse[j]))) for i in range(len(M))] for j in range(len(N_reverse))]
print(MN,MN1,sep = "\n")
#矩阵相乘,列表表示的矩阵
def matrxmulti(M,N):
    if len(M[0]) != len(N):
        print('无法计算')
        return None
    else:
        N_reverse = []
        i = 0
        N_ = [ N[i][j] for j in range(len(N[0])) for i in range(len(N))]
        while i < len(N_):
            N_reverse.append(N_[i:i+len(N)])
            i += len(N)
        MN = [[reduce((lambda x, y: x+y),list(map(lambda m,n: m*n,M[i],N_reverse[j]))) for i in range(len(M))] for j in range(len(N_reverse))]
        return MN
print(matrxmulti(M,N))
def gensquares(N):
    for i in range(N):
        yield i**2
I = gensquares(5)
print(I.__next__())
print(list((x**2) for x in range(4)))
def mymap(func,*seqs):
    res = []
    for args in zip(*seqs):
        res.append(func(*args))
    return res
def mypadmap(*seqs,pad = None):
    args = [list(seq) for seq in seqs]
    while any(args):
        yield tuple((s.pop(0) if s else pad) for s in args)
def mypadmap1(pad = None,*seqs):
    maxlen = max(len(s) for s in seqs)
    index = range(maxlen)
    return [tuple((s[i] if len(s) > i else pad)for s in seqs) for i in index]
print(mymap(pow,[1,2,3],[1,2,3]))
print(list(mypadmap((1,2,3),(2,3,4,5))))
print(mypadmap1(None,[1,2,3],('one','two','three','four')))
"""import time
reps = 1000
reps1 = 1000
replist = range(reps)
replist1 = range(reps1)
def timer(func,*args,**kargs):
    start = time.clock()
    for i in replist1:
        ret = func(*args,**kargs)
    elapsed = time.clock() - start
    return (elapsed,ret)
def forloop():
    res = []
    for i in replist:
        res.append(abs(i))
    return res
def listcmp():
   return [abs(i) for i in replist]
def mapcmp():
    return list(map(abs,replist))
def genExpr():
    return list((abs(i) for i in replist))
def genFunc():
    def gen():
        for i in replist:
            yield abs(i)
    return list(gen())
print(sys.version)
for test in (forloop,listcmp,mapcmp,genExpr,genFunc):
    inteval,result = timer(test)
    print(' '*33)
    print('%-9s: %.5f => [%s....%s]' % (test.__name__,inteval,result[0],result[-1]))"""
print(list(sys.modules.keys()))
print(sys.path)
dir(sys)
print(sys.path)
import dir1.dir2.mod
from imp import reload
reload(dir1)
reload(dir1.dir2)
print(dir)
print(dir1.dir2)
print(dir1.dir2.mod)
print(dir1.x,dir1.dir2.y,dir1.dir2.mod.z)
class c2:
    def printc2(self):
        print("c2")
class c3:
    def printc3(self):
        print("c3")
class c1(c2,c3):
    def printc1(self):
        print('c1')
    def setname(self,name):
        self.name = name
    def __init__(self, who):
        self.name = who
I1 = c1("wang xin")
I1.printc1()
I1.printc2()
#c1.printc1()
I1.printc3()
#I1.setname('wang xin')
print(I1.name)
#I2 = c2()
#I3 = c3()
class firstclass:
    def setdata(self,value):
        self.data = value
    def display(self):
        print(self.data)

class secondclass(firstclass):
    def display(self):
        print('current value = "%s"' % self.data)
z = secondclass()
z.setdata(42)
z.display()
class Thirdclass(secondclass):
    def __init__(self,value):
        self.data = value
    def __add__(self,other):
        return Thirdclass(self.data + other)
    def __str__(self):
        return '[Thirdclass: %s]' % self.data
    def mul(self,other):
        self.data *= other
a = Thirdclass('abc')
a.display()
print(a + 'de')
a.mul(3)
print(a)

