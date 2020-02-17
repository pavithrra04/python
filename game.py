import random
def yes():
    n=int(input('enter the no'))
    r=random.randint(1,6)
    print(r)
    if n==r:
        print('you win')
    else:
        print('try again')
def no():
    print('game over')
def data():
    a=['YES','yes','Yes','y','Y']
    b=['NO','no','No','n','N']
    i=1
    while i<100:
       x=input('enter yes or no')
       if x in a:
           yes()
           i=i+1
       if x in b:
           no()
           break
data()
            
