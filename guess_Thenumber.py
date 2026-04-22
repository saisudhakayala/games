import random
number=random.randint(1,100)
guess=int(input("guess the number between 1 to 100: "))
attempt=0
while True:
    if number<guess:
        guess=int(input("guess another number, this one is big: "))
        attempt+=1
    elif number>guess:
        guess=int(input("guess another number, this one is low: "))
        attempt+=1
    else:
        print(f"you won after {attempt} attempts")
        break
