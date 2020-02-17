import random
def yes():
    print(random.randint(1,6))
def no():
    print('game over')
def data():
    a=['YES','yes','Yes','y','Y']
    b=['NO','no','No','n','N']
    i=1
    while i<5:
       x=input('enter yes or no')
       if x in a:
           yes()
           i=i+1
       if x in b:
           no()
           break
data()
            
