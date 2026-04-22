import random
def rps(main,comp):
    if main==comp:
        return 'draw'
    elif (main=='rock' and comp=='scissor') or \
         (main=='paper' and comp=='rock') or \
         (main=='scissor' and comp=='paper'):
         return 'win'
    else:
        return 'lose'
user_score=0
comp_score=0
choices=['rock','paper','scissor']
print("Lets play rock paper scissor Game:")
while True:
    main=input("enter rock, paper,scissor or 'quit':").strip().lower()
    if main=='quit':
        print('Game End')
        print(f"your score {user_score} computer score {comp_score}")
        break
    if main not in choices:
        print('invalid input')
        continue
    comp=random.randint(0,2)
    comp=choices[comp]
    game=rps(main,comp)
    print(f"you chose {main}")
    print(f"computer chose {comp}")
    if game=='win':
        user_score+=1
        print("you win")
    elif game=='draw':
        print('draw')
    else:
        print("you lose")
        comp_score+=1
