from environment import Environment
from agent import Agent

moves = [-1, 1]
rewards = [-100, -1, -1, -1, -1, -1, -1, -1, -1, 100]
# index =      0,  1,  2,  3,  4,  5,  6,  7,  8,  9

env = Environment(rewards, moves, start_pos=2)
agent = Agent(env)

agent.learn(30)  # 30 iteration
agent.walk_optimal_moves()

"""
Moves: [2, 3, 4, 5, 6, 7, 8, 3, 4, 5, 6, 7, 8, 3, 4, 5, 6, 7, 8,
3, 4, 5, 6, 7, 8, 3, 4, 5, 6, 7, 8, 3, 4, 5, 6, 7, 8, 3]
Score: 569

- Notice that from 8, the agent moves to 3.
  This is because if the agent gets to 9, it will come back to 3.
"""

print("-" * 35)
for i, table in enumerate(agent.qtables):
    print(f"Block {i}: {table}")

"""
Q-Function
-----------------------------------
Block 0: [0. 0.]
Block 1: [-81.46979811  -2.10323322]
Block 2: [-2.29959937 18.53707329]
Block 3: [-2.24548879 29.38648693]
Block 4: [ 1.98463329 38.00077986]
Block 5: [ 9.3018307  48.75785913]
Block 6: [18.58852254 62.199514  ]
Block 7: [31.97804504 78.99992504]
Block 8: [37.14402926 99.99999411]
Block 9: [0. 0.]
-----------------------------------
"""
