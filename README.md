# World Cup Game -- Python-based Game
This game was created in Python and it allows the player to simulate playing in the world cup, selecting a team that participated in the 2022 World Cup and versing the computer in matches based off of penatly shootouts with the goal of winning the tournament. After an amazing world cup where Argentina managed to beat France in the final to win, I wanted to create a game which allowed me to choose different teams and see how the outcome could've have been different. The game is played in the terminal. 

Created by [Luis Rivas](https://github.com/Rivas142)

## Content

### `main.py`
`main.py` is the Python script that introduces the player to the game and calls `game.py` and `teams.py`, performing the functions in `game.py`. The script also checks to see if the player has lost the game or not, seeing if the class attribute of the player's game "user_in" is True (still in the game) or False (player has lost the game).

### `game.py`
`game.py` is the Python script that contains most of the functions used for the game.


The game is the same tournament style that the world cup was based off of, so the player will start in a group with three other random teams. There will be 8 groups in total and the results for the other groups, that does not include the player's team, will be simulated as well. The player will have one match against each of the three teams, with points awarded based on win, loss, or draw (3, 0, and 1 respectively). Each match will be a penalty shoot-out in both group stage and knockout stage games, with draws being allowed in the group stages. Once passing the group stages, the player will progress by versing teams in the round of 16, quarter-final, semi-final, and final. 

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

After selecting the 

### `teams.py`


## How To Use
 1. Install all required dependencies.
 3. Open `configmain.json` and enter desired values (see `configmain.json` content section).
 4. Open `configbot.json` and enter desired values (see `configbot.json` content section). For `"chromedriver_path"` make sure to include the chromedriver itself. This means for Windows the path should end in "chromedriver.exe" and for Linux/MacOS the path should end in "chromedriver".
 6. Run `main.py` in the command line.
 5. The resulting CSV files will appear in the corresponding `folder_path` variable/

## Known Issues
- Crawler will get caught when initially collecting pictures especially if told to collect a lot. If caught restart the crawler or request fewer pictures. The largets successful crawl so far is 10,000 pictures but it is recommended to keep it under 3,000. Note that this crawl was done using a proxy service.
- Running crawler for extended period results in some failure to collect some profile address (about 10 per 1000 pictures). It is speculated that this is Instagram rejecting the requests so take a break and crawl again later.
- Running crawler with too many threads results in a slowdown. This is believed to be a hardware-based problem and so one should test optimal number of threads on a per machine basis. Somewhere between 5 and 8 seems to work best.
