import random
def face1():
    x = random.randrange(1, 7)
    return x
def face2():
    y = random.randrange(1, 7)
    return y
for roll in range(1,11):
    f1 = face1()
    f2 = face2()
    if roll == 1 and (f1 + f2 in [7,11]):
        print(f1 , f2)
        print(f'You win')
        break
    elif roll == 1 and (f1 + f2 in [2,3,12]):
        print(f1, f2)
        print(f'craps, You Lose!!!')
        break
    elif roll == 1 and (f1 + f2 in [4,5,6,8,9,10]):
        print(f1, f2)
        print(f'You made a point of {f1 + f2}')
        meet = f1 + f2
        continue
    elif roll > 1 and (f1 + f2 == 7):
        print(f1, f2)
        print(f'You lose')
        break
    elif roll > 1 and (f1 + f2 == meet):
        print(f1, f2)
        print(f'You Win')
        break

        
    