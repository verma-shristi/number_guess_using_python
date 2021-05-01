import random
n = random.randrange(1, 101, 1)
guess = 0
num = int(input("Enter your guess: "))
if(n == num):
    print("you guess correctly!!!you won!!!!!")
else:
    print("try again with other number")
while(n != num):

    num = int(input("Enter your guess: "))
    if(n == num):
        print("you guess correctly!!!you won!!!!!")
    elif(n < num):
        print("try a small number")
    else:
        print("try a large number")
    guess += 1
print("you won in ", guess, " chances")
