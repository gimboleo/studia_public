from math import inf

class TreeItem:
    def __init__(self,value):
        self.val = value
        self.left = None
        self.right = None

def wstaw(root,nkey):
    if root == None: return TreeItem(nkey)
    if nkey < root.val: root.left = wstaw(root.left, nkey)
    elif nkey > root.val: root.right = wstaw(root.right, nkey)
    return root

def ilosc(root):
    if root == None: return 0
    return 1 + ilosc(root.left) + ilosc(root.right)

def dlugosc(root):
    if root == None: return 0
    return 1 + max(dlugosc(root.left), dlugosc(root.right))

def wypiszdod(root):
    if root != None:
        if root.left and root.left.val > 0: wypiszdod(root.left)
        if root.val > 0: print(root.val,end=' ')
        wypiszdod(root.right)

def bst(root,m,M):
    if not root: return True
    if root.val < m or root.val > M: return False
    return bst(root.left, m, root.val) and bst(root.right, root.val, M)

def polacz(root1,root2):
    temp = root1
    while temp.right: temp = temp.right
    temp.right = root2
    return root1
    
t = wstaw(None,4)
wstaw(t,2)
wstaw(t,6)
wstaw(t,1)
wstaw(t,3)
wstaw(t,5)
wstaw(t,7)

print(ilosc(t))         #2

print(dlugosc(t))       #3

wstaw(t,-5)             #4
wypiszdod(t)            
print()

print()

print(bst(t,-inf,inf))           #5
f = TreeItem(7)
f.right = TreeItem(12)
f.left = TreeItem(3)
temp = f.left
temp.left = TreeItem(2)
temp.right = TreeItem(9)
print(bst(f,-inf,inf))

print()

t2 = wstaw(None,63)     
wstaw(t2,35)
wstaw(t2,65)
wstaw(t2,82)
wstaw(t2,55)

t = polacz(t,t2)        #6
print(ilosc(t))
print(bst(t,-inf,inf))
wypiszdod(t)