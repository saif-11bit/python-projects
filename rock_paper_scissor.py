import random


def is_win(player, opponent):
    # r > s, s > p, p > r 
    if (player=='r' and  opponent=='s') or (player=='s' and opponent == 'p') \
        or (player=='p' and opponent=='r'):
        return True
    
    return False

def play(rounds):
    points = 0
    pc_points = 0
    ties = 0
    while rounds > 0:
        pc_choice = random.choice(['r','p', 's'])

        user_choice = input("Choose ROCK(r) OR PAPER(p) OR SCISSOR(s): ")
        
        if user_choice==pc_choice:
            ties += 1
            print('Tie!!')
        else:
            user_won = is_win(user_choice, pc_choice)

            if user_won:
                points += 1
                print('You Won!!')
            else:
                pc_points += 1
                print('You Lost!!!')

        rounds -= 1

    if points > pc_points:
        print(f'HURRAYYY!!\nYOU WON!!!\nFinal Scores:\nYour Points:{points}\nPC points:{pc_points}\nTies:{ties}')
    elif points < pc_points:
        print(f'OPPSSS!!\nYOU LOST!!!\nFinal Scores:\nYour Points:{points}\nPC points:{pc_points}\nTies:{ties}')
    else:
        print(f'MATCH TIE\nFinal Scores:\nYour Points:{points}\nPC points:{pc_points}\nTies:{ties}')


if __name__=='__main__':
    rounds = int(input("Enter how many rounds you wanna play: "))
    play(rounds)
