class Environment:
    def __init__(self, rewards, moves, start_pos=0):
        self.rewards = rewards
        self.moves = moves  # [-1, 1]
        self.start_pos = start_pos

    def move_player(self, dest):
        if dest == 0 or dest == 9:
            dest = 3
        return dest

    def is_index_valid(self, idx):
        return 0 <= idx < len(self.rewards)

    def is_episode_complete(self, score):
        return score <= -200 or score >= 500
