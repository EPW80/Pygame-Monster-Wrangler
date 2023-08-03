# Monster Wrangler

In Monster Wrangler, players assume the role of a knight tasked with capturing specific target monsters from among various colored monsters. As levels advance, players face greater challenges and must act quickly, precisely, and strategically. Catching the designated monster earns points, but beware — capturing the wrong one results in a penalty.

## Features

Four Monster Types: Blue, Green, Purple, Yellow

Player Controls: Use arrow keys to navigate the player.

Special Move: Use space bar to perform a warp that transports the player to a safe zone.

Scoring System: Points are awarded based on the monsters caught. Bonus points are also provided for speedy level completions.

Dynamic Difficulty: As players progress, the number of monsters and the game's complexity increase.

## Installation

Create a virtual environment with

```
python3 -m venv env
```

Activate environment

```
source env/bin/activate
```

Ensure you have pygame installed. If not, you can install it using pip:

```
pip install pygame
```

Clone this repository or download the code.
Navigate to the directory containing the game script and execute:

```
python game_script_name.py
```

## Game Assets

Please ensure the following assets are present in the same directory as your game script:

### Images:

knight.png: Player's sprite

blue_monster.png, green_monster.png, purple_monster.png, yellow_monster.png: Monster sprites

### Sounds:

catch.wav: Sound played when the correct monster is caught

die.wav: Sound played when the wrong monster is caught

warp.wav: Sound played when the player warps

next_level.wav: Sound played when proceeding to the next level

### Fonts:

Abrushow.ttf: Font used for game HUD and other in-game text

## Gameplay

The game presents a target monster image at the screen's top. Players must navigate the arena and capture monsters that match this target.

Each level introduces more monsters. To progress to the subsequent level, players must capture all matching monsters.

Capturing an incorrect monster deducts a life. Depleting all lives ends the game.

Players can deploy the warp function (using the space bar) to teleport to a safety zone. Note: Warp uses are limited.

## Demo

![](demo.gif)

## Contributor

Erik Williams
