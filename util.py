import random as rd

class State:
    def __init__(self):
        self.history_votes = [[0, 0, 0]]
        self.history_rewards = [[0, 0, 0]]

    def update(self, votes):
        self.history_votes.append(votes)

        rewards = [30, 40, 50]
        rewards[votes.index(max(votes))] /= 2
        rewards[votes.index(min(votes))] *= 2        
       
        self.history_rewards.append(rewards) 

def yester(state):
    rewards = state.history_rewards[-1]
    return rewards.index(max(rewards))

def randomer(state):
    return rd.randint(0, 2)

def anti_yester(state):
    rewards =  state.history_rewards[-1]
    return rewards.index(min(rewards))

def rational(state):
    counts = [0, 0, 0]
    for reward in state.history_rewards:
        counts[reward.index(max(reward))] += 1
    return counts.index(max(counts))

def learner(state):
    # TBD
    return 0
