# Q-Learning Algorithm

This is my code for Q-Learning in simple environment with Python.

## Environment Definition
- There is a 1-D path that goes from 0 to 9 (10 blocks).
- In block 0, there is a hole. In block 9, there is an apple (the prize).
- A player starts from block 2 and can move to the left and right.
- If the player falls to the hole (block 0), the player is punished for -100. If the player gets the prize, the player receive +100. If the player is on the other block (1-8), the player gets -1.
- If the player arrive at 0 or 9, the player will be teleported to block 3.
- Player loses when cumulative score is -200 and win if the score is +500.

## How to Run

To run the program, simply type 

```cmd
python src/main.py
```

in your command prompt.

If you are interested in understanding what is Q-learning algorithm, please see this very awesome tutorial [here!](https://huggingface.co/blog/deep-rl-q-part1) :D

