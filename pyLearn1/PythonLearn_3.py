import pickle,shelve
class pickle_shelve_testclass:
    def __init__(self,value):
        self.data = value
    def __repr__(self):
        return 'class = %s, value = %s' % (self.__class__.__name__, self.data)
test = pickle_shelve_testclass(100)
print(test)
fp = open('picklefile.dat','wb')
pickle.dump(test,fp)
fp.close()
fp = open('picklefile.dat','rb')
test1 = pickle.load(fp)
print(test1)
shelvedbase = shelve.open('shelvefile.dat')
shelvedbase['test'] = test
shelvedbase.close()
shelvedbase = shelve.open('shelvefile.dat')
print(shelvedbase['test'])
class A:
    def a(self):
        pass
class wrapper(A):
    def justtest(self):
        print('hello')
    def __init__(self,object):
        self.object = object
    def __getattr__(self,attrname):
        print('Delegate => %s' % self.object.__class__.__name__)
        return getattr(self.object,attrname)
x = wrapper({'1':'one','2':'two'})
print(x.keys())
print(x.clear())
print(x.justtest.__self__.__dict__)