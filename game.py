import random
import time
from teams import Team, wc_teams


class Game:
    def __init__(self):
        # boolean to see if there is a winner of the tournament, default at False
        self.winner = False
        # string of user's team name
        self.user_team_name = ''
        # teams that are still in the tournament
        self.teams_in = {}
        # checks if user still in tournament
        self.user_in = True
        # setting difficulty of tournament, one for scoring probability and blocking probability
        self.shoot_prob = None
        self.block_prob = None

    # creates the random groups for the tournament when provided a team list
    @staticmethod
    def create_groups(tournament_teams):
        group_list = []

        # loop continues to create groups of 4 until there are no teams left in list
        while len(tournament_teams) > 0:
            rand_group = random.sample(tournament_teams, k=4)
            group_list.append(rand_group)
            tournament_teams = [x for x in tournament_teams if x not in rand_group]
        return group_list

    # returns the letter of the selected group based on index
    @staticmethod
    def group_letter(group_index):
        group_letters_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
        group_letter = group_letters_list[group_index]
        return group_letter

    # returns the index of the selected group
    @staticmethod
    def group_index(chosen_team, tournament_groups):
        return [i for i, lst in enumerate(tournament_groups) if chosen_team in lst]

    # returns the group of the selected team of the user
    def team_group(self, chosen_team, tournament_groups):
        index_list = self.group_index(chosen_team, tournament_groups)
        return tournament_groups[index_list[0]]

    # keeps asking user to choose a team until they choose a valid team
    def choose_team(self, team_list):
        while True:
            team_select = input('\nPlease select a team: ').capitalize()
            if team_select in team_list:
                break
            else:
                print('Please choose a valid team from the list!')
        self.user_team_name = team_select
        return team_select

    # prints all the groups of the tournament
    def show_groups(self, group_list):
        for i in group_list:
            group_letter = self.group_letter(group_list.index(i))
            print(f'\nGroup {group_letter}:')
            for team in i:
                print(team)
        print()
        print()

    # set difficulty of game
    def set_difficulty(self):
        # Set the difficulty level
        probability = 0.0
        while True:
            difficulty = input("Choose your difficulty level (easy, medium, hard): ")

            # Set the probability of guessing correctly based on difficulty
            if difficulty == "easy":
                probability = 0.2  # 20% chance of computer guessing user's guess
                probability_2 = 0.8  # 80% chance of blocking computer's shot
                break
            elif difficulty == "medium":
                probability = 0.5  # 50% chance of computer guessing user's guess
                probability_2 = 0.5  # 50% chance of blocking computer's shot
                break
            elif difficulty == "hard":
                probability = 0.8  # 80% chance of computer guessing user's guess
                probability_2 = 0.2  # 20% chance of blocking computer's shot
                break
            else:
                print("Invalid difficulty level.")

        self.shoot_prob = probability
        self.block_prob = probability_2

    # user makes choice on which side to go (based if user is attacking or defending)
    def make_choice(self, team, team_side):
        choice = ''
        # choice if the user is defending ('D')
        if team_side == 'D':
            if team.country == self.user_team_name:
                while True:
                    print()
                    choice = input('Which side would you like '
                                   f'the goalkeeper to dive to?\n1. Left\n2. Middle\n3. Right\n')
                    if choice == '1' or choice == 'Left':
                        choice = 'Left'
                        break
                    elif choice == '2' or choice == 'Middle':
                        choice = 'Middle'
                        break
                    elif choice == '3' or choice == 'Right':
                        choice = 'Right'
                        break
                    else:
                        print('Please choose a valid direction!')
            else:
                print()
                random_choice = random.randint(1, 3)
                if random_choice == 1:
                    choice = 'Left'
                elif random_choice == 2:
                    choice = 'Middle'
                elif random_choice == 3:
                    choice = 'Right'
        # choice if user is attacking
        elif team_side == 'A':
            if team.country == self.user_team_name:
                while True:
                    print()
                    choice = input('Which side would you like to shoot?\n1. Left\n2. Middle\n3. Right\n')
                    if choice == '1' or choice == 'Left':
                        choice = 'Left'
                        break
                    elif choice == '2' or choice == 'Middle':
                        choice = 'Middle'
                        break
                    elif choice == '3' or choice == 'Right':
                        choice = 'Right'
                        break
                    else:
                        print('Please choose a valid direction!')
            else:
                print()
                random_choice = random.randint(1, 3)
                if random_choice == 1:
                    choice = 'Left'
                elif random_choice == 2:
                    choice = 'Middle'
                elif random_choice == 3:
                    choice = 'Right'
        return choice

    # starts a heads of tails game
    @staticmethod
    def heads_or_tails(team_1, team_2, game_num):
        coins = random.randint(0, 1)

        # initialize the result of the coin toss
        result = ''
        # initialize second player choice: **always depends on user choice
        ht2_choice = ''

        user_winner = False

        # random choice to simulate coin flip
        if coins == 0:
            result = 'heads'
        elif coins == 1:
            result = 'tails'

        # prints the teams going against each other
        if isinstance(game_num, int):
            print(f'Game {game_num}: {team_1.country} vs {team_2.country}')
            print('------------------------------------------------')
            print()
        else:
            print(f'{game_num}: {team_1.country} vs {team_2.country}')
            print('------------------------------------------------')
            print()

        # loop to make sure user picks either heads or tails
        while True:
            ht1_choice = input(f'{team_1.country}, would you like to choose heads or tails?: ').lower()
            if ht1_choice not in ['heads', 'tails']:
                print('Please choose either heads or tails!')
            else:
                break

        # opponents choice always the opposite of the user's choice
        if ht1_choice == 'heads':
            ht2_choice = 'tails'
        elif ht1_choice == 'tails':
            ht2_choice = 'heads'

        print(f'{team_1.country} has chosen {ht1_choice} so {team_2.country} is {ht2_choice}')

        print('The coin is now flipping...')
        time.sleep(1)
        print('.....')
        time.sleep(1)
        print('.....')
        time.sleep(1)
        print(f'The coin has landed on {result}!')
        time.sleep(1)

        # if the user wins the coin toss, user has decision to attack or defend
        if result == ht1_choice:
            user_winner = True
            while True:
                t1_decision = input(f'{team_1.country} would you like to attack first (A) '
                                    f'or defend first (D)?: ').upper()
                # user decides to attack
                if t1_decision == 'A':
                    print(f'{team_1.country} is attacking first and {team_2.country} is defending first.')
                    team_1.side = 'A'
                    team_2.side = 'D'
                    break
                # user decides to defend
                elif t1_decision == 'D':
                    print(f'{team_1.country} is defending first and {team_2.country} is attacking first.')
                    team_1.side = 'D'
                    team_2.side = 'A'
                    break
                # if the user does not type 'A' or 'D'
                else:
                    print('Please type in "A" or "D" to attack or defend respectively!')
        # if the user loses the coin toss, opponent has decision to attack or defend
        else:
            t2_decision = random.choice(['A', 'D'])
            # opponent decides to attack
            if t2_decision == 'A':
                print(f'{team_2.country} has chosen to attack first!')
                time.sleep(1)
                print(f'{team_2.country} is attacking first and {team_1.country} is defending first.')
                time.sleep(1)
                team_2.side = 'A'
                team_1.side = 'D'
            # opponent decides to defend
            elif t2_decision == 'D':
                print(f'{team_2.country} has chosen to defend first!')
                time.sleep(1)
                print(f'{team_2.country} is defending first and {team_1.country} is attacking first.')
                time.sleep(1)
                team_2.side = 'D'
                team_1.side = 'A'
        return user_winner

    # returns true or false if shooter scored or missed respectively
    @staticmethod
    def shooter_scored(t1_decision, t2_decision):
        if t1_decision == t2_decision:
            return False
        else:
            return True

    # check winner of match in the group stages
    @staticmethod
    def check_winner(team_1, team_2, t1_points, t2_points):
        if t1_points > t2_points:
            print()
            print(f'{team_1.country} has won!')
            print()
            team_1.points += 3
            return team_1.country
        elif t2_points > t1_points:
            print()
            print(f'{team_2.country} has won!')
            print()
            team_2.points += 3
            return team_2.country
        else:
            print()
            print('It\'s a tie!')
            print()
            team_1.points += 1
            team_2.points += 1

    # begins match between two teams
    def start_match(self, team_1, team_2, ko=False):
        winner = False
        t1_turn = 0
        t2_turn = 0

        # initializing the scoreboard
        t1_scoreboard = ['-', '-', '-', '-', '-']
        t2_scoreboard = ['-', '-', '-', '-', '-']

        t1_side = team_1.side
        t2_side = team_2.side

        t1_points = 0
        t2_points = 0

        while not winner:
            print()
            print(f'{team_1.country}: ', end='')
            [print(x, end=' ') for x in t1_scoreboard]
            print()
            print(f'{team_2.country}: ', end='')
            [print(x, end=' ') for x in t2_scoreboard]
            print()

            t1_choice = self.make_choice(team_1, t1_side)
            t2_choice = self.make_choice(team_2, t2_side)

            # probability to compare to shooting/blocking probability
            prob = random.random()

            if t1_side == 'A':
                if team_1.country == self.user_team_name:
                    # if probability is less than shooting probability then your shot is saved
                    if prob < self.shoot_prob:
                        t2_choice = t1_choice
                        print(f'You decided to shoot {t1_choice.lower()}!')
                        print(f'The opponent decided to dive {t2_choice.lower()}!')
                        print('The shot was saved!!!')
                    # else the computer picks a random choice that is not the user's choice
                    else:
                        new_choices = ['Left', 'Middle', 'Right']

                        # eliminates the user's choice from the list
                        new_choices = [x for x in new_choices if x != t1_choice]

                        t2_choice = random.choice(new_choices)
                        print(f'You decided to shoot {t1_choice.lower()}!')
                        print(f'The opponent decided to dive {t2_choice.lower()}!')
                        print('GOAL!!!')
                if self.shooter_scored(t1_choice, t2_choice):
                    t1_scoreboard[t1_turn] = 'o'
                    t1_points += 1
                    t1_turn += 1
                elif not self.shooter_scored(t1_choice, t2_choice):
                    t1_scoreboard[t1_turn] = 'x'
                    t1_turn += 1

                t1_side = 'D'
                t2_side = 'A'

            elif t1_side == 'D':
                if team_1.country == self.user_team_name:
                    # if probability is less than blocking probability then computer's shot is saved
                    if prob < self.block_prob:
                        t1_choice = t2_choice
                        print(f'You decided to dive {t1_choice.lower()}!')
                        print(f'The opponent decided to shoot {t2_choice.lower()}!')
                        print('The shot was saved!!!')
                    # else the computer picks a random choice that is not the user's choice
                    else:
                        new_choices = ['Left', 'Middle', 'Right']
                        new_choices = [x for x in new_choices if x != t1_choice]
                        t2_choice = random.choice(new_choices)
                        print(f'You decided to dive {t1_choice.lower()}!')
                        print(f'The opponent decided to shoot {t2_choice.lower()}!')
                        print('The opponent scored!!!')
                if self.shooter_scored(t1_choice, t2_choice):
                    t2_scoreboard[t2_turn] = 'o'
                    t2_points += 1
                    t2_turn += 1
                elif not self.shooter_scored(t1_choice, t2_choice):
                    t2_scoreboard[t2_turn] = 'x'
                    t2_turn += 1

                t1_side = 'A'
                t2_side = 'D'

            # checks if both teams have taken 5 shots
            if '-' not in t1_scoreboard and '-' not in t2_scoreboard:
                # starts sudden death if it is a ko match and the score is tied
                if t1_points == t2_points and ko:
                    print()
                    print('SCORE:')
                    print('----------------------')
                    print(f'{team_1.country}: ', end='')
                    [print(x, end=' ') for x in t1_scoreboard]
                    print()
                    print(f'{team_2.country}: ', end='')
                    [print(x, end=' ') for x in t2_scoreboard]
                    print()
                    return self.sudden_death(team_1, team_2)
                # else prints final scoreboard
                else:
                    print()
                    print('FINAL SCORE:')
                    print('----------------------')
                    print(f'{team_1.country}: ', end='')
                    [print(x, end=' ') for x in t1_scoreboard]
                    print()
                    print(f'{team_2.country}: ', end='')
                    [print(x, end=' ') for x in t2_scoreboard]
                    print()
                    return self.check_winner(team_1, team_2, t1_points, t2_points)
                # winner = True

    # sudden death match when knockout games end in tie
    def sudden_death(self, user_team, opp_team):
        print()
        print('SUDDEN DEATH!!!')
        winner = False
        team_winner = ''
        user_turn = 0
        opp_turn = 0

        # initializes the scoreboard for both teams
        t1_scoreboard = ['-']
        t2_scoreboard = ['-']

        user_side = user_team.side
        opp_side = opp_team.side

        while not winner:
            print()
            print(f'{user_team.country}: ', end='')
            [print(x, end=' ') for x in t1_scoreboard]
            print()
            print(f'{opp_team.country}: ', end='')
            [print(x, end=' ') for x in t2_scoreboard]
            print()

            t1_choice = self.make_choice(user_team, user_side)
            t2_choice = self.make_choice(opp_team, opp_side)

            prob = random.random()

            if user_side == 'A':
                if user_team.country == self.user_team_name:
                    if prob < self.shoot_prob:
                        t2_choice = t1_choice
                        print(f'You decided to shoot {t1_choice.lower()}!')
                        print(f'The opponent decided to dive {t2_choice.lower()}!')
                        print('The shot was saved!!!')
                    else:
                        new_choices = ['Left', 'Middle', 'Right']
                        new_choices = [x for x in new_choices if x != t1_choice]
                        t2_choice = random.choice(new_choices)
                        print(f'You decided to shoot {t1_choice.lower()}!')
                        print(f'The opponent decided to dive {t2_choice.lower()}!')
                        print('GOAL!!!')
                if self.shooter_scored(t1_choice, t2_choice):
                    t1_scoreboard[user_turn] = 'o'
                    t1_scoreboard.append('-')
                    user_turn += 1
                elif not self.shooter_scored(t1_choice, t2_choice):
                    t1_scoreboard[user_turn] = 'x'
                    t1_scoreboard.append('-')
                    user_turn += 1

                user_side = 'D'
                opp_side = 'A'

            elif user_side == 'D':
                if user_team.country == self.user_team_name:
                    if prob < self.block_prob:
                        t1_choice = t2_choice
                        print(f'You decided to dive {t1_choice.lower()}!')
                        print(f'The opponent decided to shoot {t2_choice.lower()}!')
                        print('The shot was saved!!!')
                    else:
                        new_choices = ['Left', 'Middle', 'Right']
                        new_choices = [x for x in new_choices if x != t1_choice]
                        t2_choice = random.choice(new_choices)
                        print(f'You decided to dive {t1_choice.lower()}!')
                        print(f'The opponent decided to shoot {t2_choice.lower()}!')
                        print('The opponent scored!!!')
                if self.shooter_scored(t1_choice, t2_choice):
                    t2_scoreboard[opp_turn] = 'o'
                    t2_scoreboard.append('-')
                    opp_turn += 1
                elif not self.shooter_scored(t1_choice, t2_choice):
                    t2_scoreboard[opp_turn] = 'x'
                    t2_scoreboard.append('-')
                    opp_turn += 1

                user_side = 'A'
                opp_side = 'D'

            # t1_scoreboard[user_turn - 1] = 'o'
            # t2_scoreboard[opp_turn - 1] = 'o'

            if t1_scoreboard[user_turn - 1] != t2_scoreboard[opp_turn - 1] and user_turn == opp_turn:
                t1_scoreboard = [x for x in t1_scoreboard if x != '-']
                t2_scoreboard = [x for x in t2_scoreboard if x != '-']

                print()
                print('FINAL SCORE:')
                print('----------------------')
                print(f'{user_team.country}: ', end='')
                [print(x, end=' ') for x in t1_scoreboard]
                print()
                print(f'{opp_team.country}: ', end='')
                [print(x, end=' ') for x in t2_scoreboard]
                print()

                if t1_scoreboard[user_turn - 1] == 'o':
                    print()
                    print(f'{user_team.country} has won!')
                    team_winner = user_team.country
                else:
                    print()
                    print(f'{opp_team.country} has won!')
                    team_winner = opp_team.country
                winner = True
        return team_winner

    # simulate opponents playing their games by giving points based on random results
    @staticmethod
    def point_sim(team_1, team_2, t1_points, t2_points):
        if t1_points > t2_points:
            team_1.points += 3
        elif t2_points > t1_points:
            team_2.points += 3
        else:
            team_1.points += 1
            team_2.points += 1

    # simulate group games
    def sim_group_games(self, group, group_list, y):
        # creating Team objects for the teams in the group
        g_t1 = Team(group[0])
        g_t2 = Team(group[1])
        g_t3 = Team(group[2])
        g_t4 = Team(group[3])

        # index of user's group
        group_index = int(self.group_index(group[0], group_list)[0])
        # letter of the user's group
        group_letter = self.group_letter(group_index)

        # simulate all the games in the group (each team plays each other once)
        self.point_sim(g_t1, g_t2, random.randint(0, 5), random.randint(0, 5))
        self.point_sim(g_t1, g_t3, random.randint(0, 5), random.randint(0, 5))
        self.point_sim(g_t1, g_t4, random.randint(0, 5), random.randint(0, 5))
        self.point_sim(g_t2, g_t3, random.randint(0, 5), random.randint(0, 5))
        self.point_sim(g_t3, g_t4, random.randint(0, 5), random.randint(0, 5))
        self.point_sim(g_t2, g_t4, random.randint(0, 5), random.randint(0, 5))

        # sort the leaderboard of the group by most to least points
        sorted_by_points = {g_t1.country: g_t1.points,
                            g_t2.country: g_t2.points,
                            g_t3.country: g_t3.points,
                            g_t4.country: g_t4.points}

        sorted_by_points = dict(sorted(sorted_by_points.items(), key=lambda x: x[1], reverse=True))

        if y == 'y':
            print()
            print(f'Group {group_letter} Results:\n'
                  f'--------------------------------')
            for team, points in sorted_by_points.items():
                print(f'{team}: {points}')

        # names of the teams sorted by points
        teams_keys = list(sorted_by_points.keys())
        # add the top 2 teams from the group into the teams that are still in the tournament
        self.teams_in.update({group_letter: [teams_keys[0], teams_keys[1]]})

        return sorted_by_points

    # sim the games from the side that is not side the user's team is on
    def sim_ko_side(self, side_matchups):
        # teams that made into the next round
        teams_in = []
        for i in side_matchups:
            teams_in.append(self.sim_knockout_game(i[0], i[1]))
        return teams_in

    # return the team that won
    @staticmethod
    def sim_knockout_game(team_1, team_2):
        t1_points = 0
        t2_points = 0
        # In the knockout games teams cannot tie
        while t1_points == t2_points:
            t1_points = random.randint(0, 5)
            t2_points = random.randint(0, 5)
        if t1_points > t2_points:
            return team_1
        else:
            return team_2

    # starts the tournament
    def play_group_games(self):
        # keeps asking user to choose a team until they choose a valid team
        team_list = wc_teams
        # user's team
        chosen_team = self.choose_team(team_list)
        # list of all groups
        group_list = self.create_groups(team_list)
        # group that the user's team is in
        group = self.team_group(chosen_team, group_list)
        # index of user's group
        group_index = int(self.group_index(chosen_team, group_list)[0])
        # letter of the user's group
        group_letter = self.group_letter(group_index)
        # user team as a Team object
        user_team = Team(chosen_team)
        # list user team's opponents
        opponents = [x for x in group if x != chosen_team]

        # creating Team objects for all the opponents of user's team
        comp_team1 = Team(opponents[0])
        comp_team2 = Team(opponents[1])
        comp_team3 = Team(opponents[2])

        print(f'Your selected team is in Group {group_letter}.')

        show_input = input('Would you like to see all groups? (y/n): ').lower()
        print()

        # if the user types in 'y' then all the groups are shown
        if show_input == 'y':
            self.show_groups(group_list)

        input('Type in anything to start group games: ')

        time.sleep(1)
        print('starting group games...')
        time.sleep(1)
        print()

        c = [comp_team1, comp_team2, comp_team3]
        for x in c:
            # keeps track of the game number
            game_number = c.index(x) + 1
            # starts game of heads and tails to decide who chooses to attack and defend
            self.heads_or_tails(user_team, x, game_number)
            # starts match
            self.start_match(user_team, x)

        # simulate points to opponents
        self.point_sim(comp_team1, comp_team2, random.randint(0, 5), random.randint(0, 5))
        self.point_sim(comp_team1, comp_team3, random.randint(0, 5), random.randint(0, 5))
        self.point_sim(comp_team2, comp_team3, random.randint(0, 5), random.randint(0, 5))

        # dictionary of every team in the group with their final points
        sorted_by_points = {user_team.country: user_team.points,
                            comp_team1.country: comp_team1.points,
                            comp_team2.country: comp_team2.points,
                            comp_team3.country: comp_team3.points}
        # sorted by most to least points in the group
        sorted_by_points = dict(sorted(sorted_by_points.items(), key=lambda x: x[1], reverse=True))
        print(f'Group {group_letter} Results:\n'
              f'--------------------------------')
        for team, points in sorted_by_points.items():
            print(f'{team}: {points}')
        # names of the teams sorted by points
        teams_keys = list(sorted_by_points.keys())
        # add the top 2 teams from the group into the teams that are still in the tournament
        self.teams_in.update({group_letter: [teams_keys[0], teams_keys[1]]})
        # top 2 teams in the group
        group_winners = [teams_keys[0], teams_keys[1]]

        print()
        print(f'The teams that went through are {teams_keys[0]} & {teams_keys[1]}!')

        # if user's team not in the top 2 they are eliminated
        if self.user_team_name not in group_winners:
            self.user_in = False

        while True:
            y = input('Would you like to see the results of the other groups? (y/n): ').lower()
            if y == 'y' or y == 'n':
                break
            else:
                print('Please type in either y or n!')

        # simulate games for the groups that does not include the user's team
        for i in group_list:
            if i != group:
                self.sim_group_games(i, group_list, y)

        self.teams_in = dict(sorted(self.teams_in.items()))
        # print(self.teams_in)
        print()

    # create the knockout tree
    @staticmethod
    def print_ko_tree(s_teams, s_quarter=['TBD', 'TBD', 'TBD', 'TBD'], s_semi=['TBD', 'TBD'],
                      final=['TBD', 'TBD']):
        print()
        print(f'{s_teams[0]}        \n'
              f'        --------------   {s_quarter[0]}      \n'
              f'{s_teams[3]}                         \n'
              f'                                ------------------ {s_semi[0]}\n'
              f'{s_teams[1]}                                                     \n'
              f'        --------------   {s_quarter[1]}                            \n'
              f'{s_teams[2]}\n'
              f'                                                        -------------- {final[0]}\n'
              f'                                                        -------------- {final[1]}\n'
              f'{s_teams[4]}\n'
              f'        --------------   {s_quarter[2]}                            \n'
              f'{s_teams[7]}                                                   \n'
              f'                                ------------------ {s_semi[1]}\n'
              f'{s_teams[5]}                           \n'
              f'        --------------   {s_quarter[3]}\n'
              f'{s_teams[6]}\n')

    # show the initial knockout tree
    def show_ko_tree(self, user_side, other_side):
        x = input('Would you like to see the matchups for your side? (y/n): ').lower()
        if x == 'y':
            print()
            print('Your side:')
            self.print_ko_tree(user_side)
        y = input('Would you like to see the matchups for the other side? (y/n): ').lower()
        if y == 'y':
            print()
            print('The other side:')
            self.print_ko_tree(other_side)

    # starts knockout depending on what side the user team is on
    def knockout(self, user_side_teams, opp_teams, user_matchups, opp_matchups):
        winner = True
        user_team = Team(self.user_team_name)
        self.show_ko_tree(user_side_teams, opp_teams)

        quarters = []
        semis = []
        final = []

        opp_quarters = self.sim_ko_side(opp_matchups)

        input('Type in anything to start R016: ')

        print()
        print('Starting KOs!!')
        time.sleep(.5)
        print()

        for i in user_matchups:
            if self.user_team_name in i:
                user_index = i.index(self.user_team_name)
                if user_index == 0:
                    opp_index = 1
                else:
                    opp_index = 0
                opp_team = Team(i[opp_index])
                self.heads_or_tails(user_team, opp_team, 'RO16')
                quarters.append(self.start_match(user_team, opp_team, True))
            else:
                quarters.append(self.sim_knockout_game(i[0], i[1]))

        print(f'The teams that made the quarters are: {quarters[0]}, {quarters[1]}, {quarters[2]}, {quarters[3]}')
        if input('Would you like to see the matchups for the quarters? (y/n): ').lower() == 'y':
            self.print_ko_tree(user_side_teams, quarters)
        if input('Would you like to see the matchups for the quarters for the other side? (y/n): ').lower() == 'y':
            self.print_ko_tree(opp_teams, opp_quarters)

        if self.user_team_name in quarters:
            print()
            print('You made it to the quarter finals!')
        else:
            print()
            print('You have been eliminated!')
            winner = False

        if winner:
            input('Type in anything to start your quarter-final game: ')
            time.sleep(1)
            print('starting quarter finals...')
            time.sleep(1)
            print()

            user_quarter_matchups = [[quarters[0], quarters[1]], [quarters[2], quarters[3]]]
            opp_quarter_matchups = [[opp_quarters[0], opp_quarters[1]], [opp_quarters[2], opp_quarters[3]]]

            opp_semis = self.sim_ko_side(opp_quarter_matchups)

            for i in user_quarter_matchups:
                if self.user_team_name in i:
                    user_index2 = i.index(self.user_team_name)
                    if user_index2 == 0:
                        opp_index = 1
                    else:
                        opp_index = 0
                    q_opp_team = Team(i[opp_index])
                    self.heads_or_tails(user_team, q_opp_team, 'QUARTER FINAL')
                    semis.append(self.start_match(user_team, q_opp_team, True))
                else:
                    semis.append(self.sim_knockout_game(i[0], i[1]))

            print(f'The teams that made it from your side are {semis[0]} & {semis[1]}!')

            if input('Would you like to see the matchups for the semis? (y/n): ').lower() == 'y':
                self.print_ko_tree(user_side_teams, quarters, semis)
            if input('Would you like to see the matchups for the semis for the other side? (y/n): ').lower() == 'y':
                self.print_ko_tree(opp_teams, opp_quarters, opp_semis)

            if self.user_team_name in semis:
                print()
                print('You made it to the semi finals!')
            else:
                print()
                print('You have been eliminated!')
                winner = False

            if winner:
                input('Type in anything to start your semi-final game: ')
                time.sleep(1)
                print('starting semi finals...')
                time.sleep(1)
                print()

                user_index2 = semis.index(self.user_team_name)
                if user_index2 == 0:
                    opp_index = 1
                else:
                    opp_index = 0
                s_opp_team = Team(semis[opp_index])
                self.heads_or_tails(user_team, s_opp_team, 'SEMI FINAL')
                final.append(self.start_match(user_team, s_opp_team, True))
                final.append(self.sim_knockout_game(opp_semis[0], opp_semis[1]))

                print(f'The teams in the final are {final[0]} & {final[1]}!')

                if self.user_team_name in final:
                    print()
                    print('You made it to the final!')
                else:
                    print()
                    print('You have been eliminated!')
                    winner = False

                if input('Would you like to see the final knockout tree for your side? (y/n): ').lower() == 'y':
                    self.print_ko_tree(user_side_teams, quarters, semis, final)
                if input('Would you like to see the final knockout tree for the other side? (y/n): ').lower() == 'y':
                    self.print_ko_tree(opp_teams, opp_quarters, opp_semis, final)

                if winner:
                    input('Type in anything to start the final: ')
                    print()
                    time.sleep(1)
                    print('starting the final...')
                    time.sleep(1)
                    print()

                    f_opp_team = Team(final[1])

                    self.heads_or_tails(user_team, f_opp_team, 'FINAL')
                    tournament_winner = self.start_match(user_team, f_opp_team, True)

                    if tournament_winner == self.user_team_name:
                        print('CONGRATS! YOU HAVE WON THE TOURNAMENT!!!!!')
                    else:
                        print('You have been eliminated!')

                    print(f'The winner of the tournament is {tournament_winner}!')

    # create matchups for the knockout games
    def play_knockouts(self):
        print('Welcome to the knockout stages!')

        keys = []
        for letter, team in self.teams_in.items():
            keys.append(team)
        side_1 = keys[:4]
        side_2 = keys[4:]

        side_1_teams = []
        side_2_teams = []

        for i in side_1:
            for x in i:
                side_1_teams.append(x)
        for i in side_2:
            for x in i:
                side_2_teams.append(x)

        s1_matchups = []
        s2_matchups = []

        # create matchups -- 1st from one group goes against 2nd of other group
        for i in [0, 4]:
            s1_matchups.append([side_1_teams[i], side_1_teams[i + 3]])
            s2_matchups.append([side_2_teams[i], side_2_teams[i + 3]])
            s1_matchups.append([side_1_teams[i + 1], side_1_teams[i + 2]])
            s2_matchups.append([side_2_teams[i + 1], side_2_teams[i + 2]])

        # starts ko games depending on which side the user team is on
        if self.user_team_name in side_1_teams:
            self.knockout(side_1_teams, side_2_teams, s1_matchups, s2_matchups)
        else:
            self.knockout(side_2_teams, side_1_teams, s2_matchups, s1_matchups)
