import random as r
def calling():
    for i in range(0,3):
        print(l[i],end=' ')
def game(l):
    o=r.randint(0,2)
    print(l[o])
def choice():
    choice=input("Are you willing to play rock paper scissor?").lower()
    if choice=='yes':
        return True
    else:
        print('ok')
        return False
def out():
    out=input('Are you out or not?').lower()
    if out=='yes':
        print('you are out.....')
        return False
    else:
        return True
l=('rock','paper','scissor')
ch=True
while choice():
    while ch:
        calling()
        print('...')
        game(l)
        ch=out()








