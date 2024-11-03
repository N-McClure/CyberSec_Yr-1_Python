def randomFunc():
    import random
    randomNum = random.randint(0,100)
    print("random number is: ", randomNum)

def aboutRandom():
    import random

    for n in range(10):
        r = random.randint(1,100)
        print(r , end=" ")