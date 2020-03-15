
"""
by : islam abdelmoumen

"""
import random
def OneLine():
    l,ns = [[]],list('123456789')
    while len(l[-1]) != 9:
        l[-1] += ns.pop(random.randint(0,len(ns)-1))
    return l
def GetLen(l):
    L = []
    for _ in range(len(l)-1):
        L.append(l[_][len(l[-1])])
    return L
def Box(l):
    x ,y,L = len(l), len(l[-1]) ,[]
    if x <= 3:x = 0
    elif 4<= x <=6:x = 3
    else:x = 6

    if y < 3:y = [0,3]
    elif 3<= y <6:y = [3,6]
    else :y = [6,9]

    for _ in range(x,len(l)):
        L.extend(l[_][y[0]:y[1]])
    return L

def Check(l,n):
    if n not in l[-1] and n not in GetLen(l) and n not in Box(l):
        return True
    return False

def Create():
    l,y = OneLine(),0
    while len(l) != 9:
        ns,l,x = list('123456789'),l+[[]],0
        while len(l[-1]) != 9:
            x,n = x+1,ns.pop(random.randint(0,len(ns)-1))
            if x == 40:
                y += 1
                del l[-1]
                break
            if y == 10:
                del l[-1],l[-1]
                y = 0
                break
            if Check(l,n):l[-1]+=n
            else:ns.append(n)
    return l
def UnderLine(l):
    print(' +---------+---------+---------+')
    for _ in range(9):
        l[_].insert(0,' | ')
        l[_].insert(4,' | ')
        l[_].insert(8,' | ')
        l[_].insert(13,' | ')
        print(' '.join(l[_]))
        if (_+1)%3==0:
            print(' +---------+---------+---------+')
x = set()
while 1:
    l = Create()
    x.add(str(l))
    print(len(x))
    UnderLine(l)
    print('\n')
