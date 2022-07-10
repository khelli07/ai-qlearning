from environment import Environment
from agent import Agent

rewards = [-100, -1, -1, -1, -1, -1, -1, -1, -1, 100]
moves = [-1, 1]

env = Environment(rewards, moves, start_pos=2)
agent = Agent(env)

agent.learn(20)
agent.walk_optimal_moves()
