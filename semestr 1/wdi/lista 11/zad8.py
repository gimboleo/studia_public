class TreeItem:
    def __init__(self,value):
        self.val = value
        self.left = None
        self.right = None

def wstaw(root, nkey):
    if root == None: return TreeItem(nkey)
    if nkey < root.val: root.left = wstaw(root.left, nkey)
    elif nkey > root.val: root.right = wstaw(root.right, nkey)
    return root

def wypisz(root):
    if root != None:
        wypisz(root.left)
        print(root.val,end=' ')
        wypisz(root.right)

def wypisz2(root):
    if root != None:
        print('l:',root.left.val,end=' ') if root.left else print('      ',end='')
        print('v:',root.val,end=' ')
        print('r:',root.right.val,end=' ') if root.right else print('      ',end='')
        print()
        wypisz2(root.left)
        wypisz2(root.right)

def szukaj(root, skey):
    if root == None: return None
    if root.val == skey: return root
    if root.val > skey: return szukaj(root.left, skey)
    else: return szukaj(root.right, skey)

def szukajpoprz(root, skey, poprz):
    if root == None: return None
    if root.val == skey: return poprz
    if root.val > skey: return szukajpoprz(root.left, skey, root)
    else: return szukajpoprz(root.right, skey, root)

def zamiana(root,w,d):
    u = szukaj(root,w)
    poprz = szukajpoprz(root,w,None)
    if not u: return 0

    if d == 'l':
        if not u.left: return 0

        v = u.left
        temp = v.right

        if poprz.right == u: poprz.right = v
        else: poprz.left = v
        v.right = u
        u.left = temp
        return root

    if d == 'r':
        if not u.right: return 0

        v = u.right
        temp = v.left
        
        if poprz.right == u: poprz.right = v
        else: poprz.left = v
        v.left = u
        u.right = temp
        return root

    return 0


t = wstaw(None,44)
wstaw(t,27)
wstaw(t,20)
wstaw(t,82)
wstaw(t,47)
wstaw(t,45)
wstaw(t,80)
wstaw(t,62)
wstaw(t,83)


wypisz2(t)

print()
print()

if zamiana(t,82,'l'): wypisz2(t)
else: print('Nie dało się :c')

print()
print()

if zamiana(t,47,'r'): wypisz2(t)
else: print('Nie dało się :c')

