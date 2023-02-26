import click
def nawias(strn):
    import re
    print(strn)
    nowy = re.sub('\(.*?\)','',strn)  #.* - jakiekolwiek znaki; ? - mniej agresywne
    print(nowy)
    print()

def nawias2(strn):
    nowy = ''
    x = False
    for i in strn:
        if i == '(' and x == False:
            x = True
        if not x:
            nowy += i
        if i == ')' and x:
            x = False
    print(strn)
    print(nowy)
    print()

test1 = "Si(e)ma (en)iu"
test2 = "(s)he (be)li(ev)ed"
test3 = "Pa jak (znika)"

nawias(test1)
nawias(test2)
nawias(test3)

if click.confirm('Custom?', default=False):
    a = input("Napis z nawiasami do usunięcia: ")
    print()
    nawias(a)
    
print("Druga wersja: ")
print()

nawias2(test1)
nawias2(test2)
nawias2(test3)

if click.confirm('Custom?', default=False):
    a = input("Napis z nawiasami do usunięcia: ")
    print()
    nawias2(a)