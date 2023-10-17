# World Cup Game -- Python-based Game
This game was created in Python and it allows the player to simulate playing in the world cup, selecting a team that participated in the 2022 World Cup and versing the computer in matches based off of penatly shootouts with the goal of winning the tournament. After an amazing World Cup where Argentina managed to beat France in the final to win and a soccer super fan, I wanted to create a game which allowed me to choose different teams and see how the outcome could've have been different. The game is played in the terminal. 

Created by [Luis Rivas](https://github.com/Rivas142)

## Content

### `main.py`
`main.py` is the Python script that introduces the player to the game and calls `game.py` and `teams.py`, performing the functions in `game.py`. The script also checks to see if the player has lost the game or not, seeing if the class attribute of the player's game "user_in" is True (still in the game) or False (player has lost the game).

### `game.py`
`game.py` is the Python script that contains most of the functions used for the game.


The game is the same tournament style that the world cup was based off of, so the player will start in a group with three other random teams. There will be 8 groups in total and the results for the other groups, that does not include the player's team, will be simulated as well. The player will have 3 matches, one against each of the three teams, with points awarded based on win, loss, or draw (3, 0, and 1 respectively). Each match will be a penalty shoot-out in both group stage and knockout stage games, with draws being allowed in the group stages. Once passing the group stages, the player will progress by versing teams in the round of 16, quarter-final, semi-final, and final. 

**Note that the game is based off the teams that played in the tournament and the style of tournament, but the rest will have modifications. 


The player is first greeted with the message below:

![image](https://github.com/Rivas142/WorldCupGame/assets/44100453/558ecdd9-af51-48f5-bfcb-74948c1bd106)

The player will first select the difficulty that would like to play at. The difficulty is based off of probabilities set in the `"set_difficulty"` function. The probabilities are set as:

`"probability"` : variable used to store the probability that the the computer player will block the player's shot 

`"probability_2"` : variable used to store the probability that the player will block the computer player's shot

`Difficulties:`

`Easy`

`"probability"` : 20%

`"probability_2"` : 80%

`Medium`

`"probability"` : 50%

`"probability_2"` : 50%

`Hard`

`"probability"` : 80%

`"probability_2"` : 20%

After selecting the difficulty, the player then gets prompted to select the team they want to use (must be a team that participated in the 2022 World Cup). Once selecting the team, the player's group as well as the groups for every other team in the tournament will be created. An example group can be seen below (For this example the player has selected Spain as their team, but the game will give the option to see every group for the tournament): 

![image](https://github.com/Rivas142/WorldCupGame/assets/44100453/f727ff66-8da4-4210-8043-51ff62b6434c)

The player is then ready to start the matches! To advance to the knockout games, the player's team must be top 2 in the group in terms of number of points. If the player's team is 3rd or 4th in the group, they will be eliminated and the game will end. 

Before starting any match in the tournament, the game will prompt the start of a head's or tail's game. This will decide if the player or the computer will choose to attack first (shoot first) or defend first (block first). This process is the same when starting a penatly shootout in real life. The first message will be like this:

![image](https://github.com/Rivas142/WorldCupGame/assets/44100453/dee2710c-23cb-4a0f-9ad6-34abb43e8634)

Whatever the player chooses, the computer is left with the other option. So for example, the player in the example below has chosen heads so the computer had to choose tails. The player ended up winning the coin toss, so they get to choose their option of attacking or defending first. 

![image](https://github.com/Rivas142/WorldCupGame/assets/44100453/2e97b7fe-3694-4d93-8dcf-9db39b2356e4)

The player for the example chooses to attack first. Once the decision has been made, the match starts. Once the match starts, a scoreboard of how many penalties each team scores appear. Since the game just started, all the 5 spots for each team (Since each team will take 5 penalties) will be dashes (empty). Once the teams start taking their penalties, the dash for the turn will turn to either an "o" (scored) or "x" (shot got saved). The scoreboard empty will look like:

![image](https://github.com/Rivas142/WorldCupGame/assets/44100453/2c00a097-f774-43e9-837f-01c58df790f8)

The player will then choose what what direction they want to shoot/dive (depends on if they are attacking or defending) and the 1st dash will be replaced with an "x" or "o" depending on the outcome. If the player decides to shoot left, for example, and they score, it will show as:

![image](https://github.com/Rivas142/WorldCupGame/assets/44100453/23f274c6-463b-4e01-b5bf-21faa6c43045)

In the case of a miss, as shown by the opponent/computer missing, it will show as:

![image](https://github.com/Rivas142/WorldCupGame/assets/44100453/0fc3f734-1f29-4c8a-9843-92b47b4f1df9)

The process will continue for each penalty shot, until the match is finished. The final scoreboard will be shown and the winner is announced, the points will be assigned to the respective team depending on the outcome as well. In the case for below, Spain (player's team) has scored all five penalties while Netherlands (computer's team) has only scored one penalty on their second go. 

![image](https://github.com/Rivas142/WorldCupGame/assets/44100453/03d8852d-bace-41bf-80d6-cbeadb5f7087)

The next match will start immediately and continue to the last match until the group stage matches are finished, playing three matches in total. The final results of the group will be shown:

![image](https://github.com/Rivas142/WorldCupGame/assets/44100453/50b4ace4-b8e1-441a-b4b4-dd1bb64493de)

The player will have the choice to see the results from the other groups as well, so you can see group D for example:

![image](https://github.com/Rivas142/WorldCupGame/assets/44100453/fc7ad7f6-1475-409f-bb0a-aba6ab1b0306)

If the player's team was one of the bottom two teams of the group, they are eliminated. However, if they are one of the top two teams, they advance to the knockout stages! Once they advance, the player will have the choice to see the matchups for both their side as well as the side their team is not on:

![image](https://github.com/Rivas142/WorldCupGame/assets/44100453/843ad270-8aca-4c6e-a8d7-b274f409f444)

![image](https://github.com/Rivas142/WorldCupGame/assets/44100453/629484f6-4ba0-4616-acb5-4f978a8dcc17)

TBD (to be determined) is used as placeholders until the winner is decided for each match. The TBD connected to the match will be updated with the winner of the round. Note that all matches that do not include the player's team will be simulated as well, including the teams on the other side of matchups. 

The title that corresponds to the round is changed (RO16, Quarter-Finals, Semi-Finals, Final) as shown below:

![image](https://github.com/Rivas142/WorldCupGame/assets/44100453/bea1b700-e12f-42b0-b943-ddf17b737c10)

![image](https://github.com/Rivas142/WorldCupGame/assets/44100453/f9fcce37-9a80-49e5-9380-c3b5e4d73f8c)

![image](https://github.com/Rivas142/WorldCupGame/assets/44100453/ae1aff06-ca74-4d86-8393-05b7e0f2bc16)

![image](https://github.com/Rivas142/WorldCupGame/assets/44100453/e8396ef1-42f2-4502-995f-8e107a2d02c0)

The other aspect of matches that is changed ties are not allowed for knockout stages. In the case that the teams are tied in amount of penalties scored at the end of the match, they enter a sudden death. So the teams will take turns in taking penalties until one scores and the other doesn't. The match will keep going until this result happens. Other than sudden death/ties not being allowed, the matches are played the same until the final. Of course if the player loses a match leading up the final, they will be eliminated and the game will end. 

If the player manages to win every match, including the final, they have won the tournament! They will presented with the message below:

![image](https://github.com/Rivas142/WorldCupGame/assets/44100453/eb396e02-e77f-4190-974a-c4e10e0d61d0)


### `teams.py`

`teams.py` is the Python script that contains the variable "wc_teams" that lists all the teams included in the tournament. It also contains the class "Team" that allows teams in the tournament to be stored as "Team" objects, to allow the game to keep track of the amount of points the team has, whether they are still in the tournament or not, if the team is attacking or defending in the match, and the name of the team. 

If the user of the game would like to change the teams that are included in the tournament, they would change the teams in the "wc_teams" variable but the total number of teams must be 32. 

## How To Use

Run the `main.py` script, this starts the game. Use the terminal to enter the inputs needed to play the game when prompted. 

## Known Issues / Improvements 
- When finishing the group stages, there is the possibility of 2nd and 3rd place teams to tie in terms of points, in that case it is whoever is listed as second in the table that advances. There could be a functionality added that can determine which of the two teams go through through either luck (such as coin toss) or through matchmaking, which would be between the two teams who scored the most penalties or who won between them when they versed in their match.
- There could be a factor of randomness added to see if the person shooting misses the goal entirely, which occurs in real life games as well. This would add more engagement and excitement to the game.
- A UI could be created for the game, which would make it more aesthetically pleasing as well as more functional for the user to play the game. 
