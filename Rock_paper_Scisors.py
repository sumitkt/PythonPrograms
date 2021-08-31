#Lets build a rock paper and scisors game

#name=input("name:")
#print(f"hello {name}....How are you doing")
import random
def play():
    user=input("what's your choice enter 'r' for rock,'s' for scisors and 'p' for papers:")
    computer= random.choice(['r','p','s'])

    if user == computer:
        return 'it\'s a tie'
    elif is_win(user,computer):
        return 'you won'
    else:
        return 'you lost'


def is_win(user,computer):

    if (user== 'r' and computer== 's') or (user== 's' and computer == 'p') or (user == 'p' and computer == 'r'):
        return True
    else:
        return False


if __name__=='__main__':
    print(play())
