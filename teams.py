wc_teams = ['Netherlands', 'Senegal', 'Ecuador', 'Qatar',
            'England', 'Iran', 'USA', 'Wales',
            'Argentina', 'Mexico', 'Poland', 'Saudi Arabia',
            'Australia', 'Denmark', 'France', 'Tunisia',
            'Costa Rica', 'Germany', 'Japan', 'Spain',
            'Belgium', 'Canada', 'Croatia', 'Morocco',
            'Brazil', 'Cameroon', 'Serbia', 'Switzerland',
            'Ghana', 'Portugal', 'South Korea', 'Uruguay'
            ]

class Team:
    def __init__(self, country):
        # points for the group stage
        self.points = 0
        # boolean to check if the team is still in the tournament
        self.in_tournament = True
        # setting which turn the team is on: defending or attacking
        self.side = ''
        # name of team
        self.country = country

    # adding points to team depending on the result
    def add_points(self, result):
        if result == 'W':
            self.points += 3
        elif result == 'L':
            self.points += 0
        elif result == 'D':
            self.points += 1

    def change_side(self):
        if self.side == 'A':
            self.side = 'D'
        elif self.side == 'D':
            self.side = 'A'




