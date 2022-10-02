import random
YourScore = 0
ComputerScore = 0

chekedPicked = ['paper',  'stone', 'seissor', 'quite']
for i in range(5):
    user_picked = input(
        "press p for paper/ s for stone/ x for seissor/and q for quit?  ")
    if (user_picked == 'quit'):
        print("ok game over")
        break
    if (user_picked not in chekedPicked):
        break

    randompicked = random.randint(0, 2)
    computerpicked = chekedPicked[randompicked]
    if computerpicked == 'paper' and user_picked == 'seissor':
        print(f'Computer picked {computerpicked} and you picked {user_picked}')
        print("you won")
        YourScore += 1
    elif computerpicked == 'seissor' and user_picked == 'stone':
        print(f'Computer picked {computerpicked} and you picked {user_picked}')
        YourScore += 1
        print("you won")
    elif computerpicked == 'stone' and user_picked == 'paper':
        print(f'Computer picked {computerpicked} and you picked {user_picked}')
        print("you won")
        YourScore += 1
    elif computerpicked == user_picked:
        print(f'Computer picked {computerpicked} and you picked {user_picked}')
        print('drawn')
    else:
        print(
            f" Computer picked {computerpicked} and you picked {user_picked}")
        print('you lose')
        ComputerScore += 1
print(f'your scor is {YourScore} and Computer score is {ComputerScore}')
