class ListerTree:
    """
    返回类树和它们的属性
    """
    def __str__(self):
        self.__visited = {}
        return "<Instance of {0},address {1}:\n{2}{3}>".format(self.__class__.__name__,id(self),self.__attrnames(self,0),self.__listclass(self.__class__,4))
    def __listclass(self, aClass, indent):
        dots = '.'*indent
        if aClass in self.__visited:
            return '\n{0}<class {1}:, address {2}: (see above)>\n'.format(dots,aClass.__name__,id(aClass))
        else:
            self.__visited[aClass] = True
            genabove = (self.__listclass(c,indent + 4) for c in aClass.__bases__)
            return '\n {0}<class {1}, address {2}:\n{3}{4}{5}>\n'.format(
                dots,
                aClass.__name__,
                id(aClass),
                self.__attrnames(aClass,indent),
                ''.join(genabove),
                dots)
    def __attrnames(self,obj,indent):
        spaces = ' ' * (indent + 4)
        results = ''
        for attr in sorted(obj.__dict__):
            if attr.startswith('__') and attr.endswith('__'):
                results += spaces + '{0}=<>'.format(attr)
            else:
                results += spaces + '{0}={1}'.format(attr,getattr(obj,attr))
        return results
        
