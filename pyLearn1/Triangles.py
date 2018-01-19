"""
杨辉三角
"""
def triangles(layer):
    ll = [1]
    for i in range(layer + 1):
        l = ll[:]
        for j in range(i+1):
            if j == 0:
                ll[0] = 1
                continue
            elif j == i:
                ll.append(1)
            else:
                ll[j] = l[j-1] + l[j]
        yield ll
if __name__ == "__main__":
    a = triangles(10)
    for i in a:
        print(i)
