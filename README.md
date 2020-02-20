# ENPM661 Project 1

Brian Bock

ENPM661

Fall 2020

This program solves any 8 puzzle. To run this program, run "main.py". This must be in the same directory as "actions.py", "board_switcher.py", "plot_path.py", "printboard.py", and "verbose.py". Everything was written in Python3. I've tested this for a variety of puzzles on my laptop (2018 Macbook Pro), and it solved every puzzle (or tested all possible boards, for an illegal/unsolvable start) in less than 2 minutes. When it finishes solving, it will print out each board from start to goal. The moves used are also written to a new file ("NodesPath.txt").

If you'd like to toggle more print statements (Verbose mode), open "verbose.py" and change 'verbose=True' in line 4. This additional output will make the program much more informative, but will take considerably longer to complete. For speed, keep 'verbose=False'


Libraries used: numpy, math, datetime, collections