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

def wypisz(root):
    if root != None:
        print(root.val,end=' ')
        wypisz(root.left)
        wypisz(root.right)

def wypisz2(root):
    if root != None:
        wypisz2(root.left)
        print(root.val,end=' ')
        wypisz2(root.right)


t = TreeItem(3)
t.left = TreeItem(8)
t.right = TreeItem(2)
t.left.left = TreeItem(1)
t.left.right = TreeItem(0)

bst = wstaw(None,4)
wstaw(bst,2)
wstaw(bst,6)
wstaw(bst,1)
wstaw(bst,3)
wstaw(bst,5)
wstaw(bst,7)

wypisz(t)           #1
print()
wypisz(bst)
print()

print()

wypisz2(t)           #2
print()
wypisz2(bst)        
print()