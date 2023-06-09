# TFT Set 9 Composition Generator

This project is a Teamfight Tactics (TFT) Set 9 composition generator. This is not intended to and will not give you any competitive advantage when playing the game.
What this will do is help you find compositions on the fly that maximise your trait synergies.

## How It Works

Essentially, this program will generate around 500,000 compositions that fit your requirements and score them, returning you the composition with the highest score.
It uses a genetic algorithm so it is more efficient than a brute force approach and can realistically be run in a few seconds so you can use it as you play the game.

## Scoring

Compositions are given a point for every trait breakpoint they hit, excluding unique traits. 

For example this (https://imgur.com/a/fflWXMW) would be scored 8 points:
- 1 Wanderer - 0 points
- 4 Rogue - 2 Points
- 3 Noxus - 1 Point
- 2 Shadow Isles - 1 Point
- 2 Zaun - 1 Point
- 2 Challenger - 1 Point
- 2 Juggernaut - 1 Point
- 2 Slayer - 1 Point

If **Built Different** is set to yes, the algorithm will return you the lowest scored composition instead of the highest and
**all units with unique traits will be removed from the pool**.

I've tried to avoid the generation of any compositions that do not satisfy the input parameters, but if a composition is provided with a score of 
-1 (Positive Infinite if **Built Different** is enabled), it is a composition that did not meet your requirements but was somehow the best composition generated.

## Installation

Download `Set 9 Comp Generator.exe` and run. The Python files are not needed to run the application but are there if you would like to see how it works.

## Files

The project consists of three Python files and a standalone application:

1. `Database.py`: This file contains the database of all units and their traits. It also includes the trait breakpoints and unique traits units.

2. `Teambuilder.py`: This file contains the logic for generating a random team, calculating points for a team, performing crossover and mutation operations, and finding the best team composition. It uses a genetic algorithm to optimize the team composition based on the user-defined parameters.

3. `main.py`: This is the main file that you run to start the program. It contains the user interface for entering parameters and displays the best team composition.

4. `Set 9 Comp Generator.exe`: This is the standalone application that makes use of all the Python files. You can run this application directly without needing to run the Python scripts.

## How to Use

To use this program, run the `Set 9 Comp Generator.exe` file. You will be prompted to enter various parameters:

- **Team size**: Enter a number from 2 to 59.
- **Bonus Traits**: Enter your trait bonuses, separated by commas. For example, 'Sorcerer: 1' for Sorcerer+1. If you have multiple bonuses, you can enter 'Noxus: 2, Demacia: 1' for Noxus +2 and Demacia +1.
- **Composition Trait Requirements**: Enter your trait requirements, separated by commas. For example, 'Demacia: 7' for a team with at least 7 Demacia units. 'Yordle: 3, Gunner: 2' for a team with at least 3 Yordles and 2 Gunners.
- **Maximum Unit Cost**: Enter a number from 1 to 5.
- **Included Units**: Enter the units you want to include in your team, separated by commas. For example, 'Senna, Malzahar'.
- **Built Different**: Enter 'y' for yes or 'n' for no.

Unique traits do not work properly with **Bonus Traits** or **Composition Trait Requirements**. If you would like 

After entering the parameters, the program will generate a team composition and display it along with the points calculated for the team.

## Known bugs

If you enable **Built Different** and generate a composition with 55 or more units, the program will crash.

## Requirements

This program requires Python 3.6 or later to run the Python scripts. The standalone application can be run on any Windows machine.
