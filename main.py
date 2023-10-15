import random
import time
import teams
from game import Game

# started on 02/24

def main():
    print('Welcome to the World Cup!')
    g = Game()
    g.set_difficulty()
    g.play_group_games()
    if g.user_in:
        g.play_knockouts()
    else:
        print('You have lost!')

    print()
    print('Thank you for playing!')

if __name__ == '__main__':
    main()
