# Tank Battle
#### This is a tank game including:
* A Tank which fires bullets with varying hitpoints.
* enemy blocks with different powers
* Booster stone to power up the hitpoints

#### How to play:
* Clone the repository.
* Firstly install the latest version of python in your device from https://www.python.org/downloads/.
* Run the command `pip install pygame` or `pip3 install pygame`. This will download the pygame library. 
* Now, run `python TankBattle.py`, you will see a pop-up window coming, which is the game.

#### Rules:
* Each stone has it's power and you have to destroy the stone by decreasing it power to zero.
* Your initial hitpoint is 1, which means that if a bullet hits a stone it will decrease it's health by 1.
* The stones will bounce up and down if their power is non-zero and you have to dodge the tank from them, if a stone collides with the tank then the game ends.

#### Power-Ups:
* The yellow stones are the booster stones and they increase hitpoints of the bullets being fired from the tank.
* Randomly white stones will appear with unknown power and once they are destroyed they reduce the speed of all stones and upcoming stones by half for 5 sec. and restore the original speed after 5 sec.

#### Controls:
* `Space`: for firing bullets.
* `Left key`: for moving left.
* `Right key`: for moving right.

File `TankBattle.py` is the updated file.
