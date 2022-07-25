import numpy as np


class Agent:
    def __init__(self, env, epsilon=0.5, lr=0.1, discount=0.8):
        self.env = env
        self.current_pos = env.start_pos
        self.move_length = len(env.moves)

        self.epsilon = epsilon
        self.lr = lr
        self.discount = discount

        self.score = 0
        self.qtables = self.generate_qtables()

    def generate_qtables(self):
        return [
            np.array([0] * self.move_length, dtype=np.float64)
            for _ in range(len(self.env.rewards))
        ]

    def learn(self, iterations):
        for i in range(iterations):
            self.score = 0
            self.current_pos = self.env.start_pos
            while not self.env.is_episode_complete(self.score):
                if np.random.uniform() < self.epsilon:
                    self.explore()
                else:
                    self.exploit()

            self.epsilon *= (iterations - i) / iterations

    def update_qtable(self, move_idx, next_pos):
        value = self.qtables[self.current_pos][move_idx] + self.lr * (
            self.env.rewards[next_pos]
            + self.discount * np.max(self.qtables[next_pos])
            - self.qtables[self.current_pos][move_idx]
        )

        self.qtables[self.current_pos][move_idx] = value

    def explore(self):
        move_idx = np.random.randint(0, self.move_length - 1)
        next_pos = self.current_pos + self.env.moves[move_idx]
        while not self.env.is_index_valid(next_pos):
            move_idx = np.random.randint(0, self.move_length - 1)
            next_pos = self.current_pos + self.env.moves[move_idx]

        self.update_qtable(move_idx, next_pos)

        self.score += self.env.rewards[next_pos]
        self.current_pos = self.env.move_player(next_pos)

    def exploit(self):
        move_idx = np.argmax(self.qtables[self.current_pos])
        next_pos = self.current_pos + self.env.moves[move_idx]

        self.update_qtable(move_idx, next_pos)

        self.score += self.env.rewards[next_pos]
        self.current_pos = self.env.move_player(next_pos)

    def walk_optimal_moves(self):
        score = 0
        current_pos = self.env.start_pos
        all_pos = [current_pos]
        while not self.env.is_episode_complete(score):
            move_idx = np.argmax(self.qtables[current_pos])

            next_pos = current_pos + self.env.moves[move_idx]

            score += self.env.rewards[next_pos]

            current_pos = self.env.move_player(next_pos)
            all_pos.append(current_pos)

        print(all_pos)
        print("Score:", score)

    def print_all_qtables(self):
        for qtable in self.qtables:
            print(qtable)
