import os
"""fp = open('context.txt',encoding = 'utf-8')
L = fp.read().split('\n')
fp.close()
fp = open('context1.txt','w',encoding = 'utf-8')
for i in L:
    s = ''
    for j in range(0,len(i)):
        if j != len(i) - 1:
            if ((i[j] == '.' or i[j] == ';') and (i[j + 1] == ' ' or i[j + 1] == '\"' or (ord(i[j + 1]) > 64 and ord(i[j + 1]) < 91))) or i[j] == '\t':
                s = s + i[j] + '\n'
            else:
                s = s + i[j]
        else:
            s = s + i[j] + '\n'
    fp.write(s)
fp.close()
"""
fp = open('context1.txt',encoding = 'utf-8')
L = fp.read().split('\n')
fp.close()
print('***********begin************')
fp = open('context1.txt','w',encoding = 'utf-8')
for i in L:
    s = ''
    if i == '\n':
        continue
    if len(i) < 5 or len(i) == 0:
        continue
    if i[0] == '\t' or i[0] == ' ':
        s = i[1:len(i)] +'\n'
    else:
        s = i + '\n'
    fp.write(s)
fp.close()
os._exit(0)