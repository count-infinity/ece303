import random
import statistics

# 100, 200, 400, 500 dollar prizes are hidden behind 4 doors. 
# You choose a door, and a host then opens the door with the median amount.
# For example, if you chose the $200 door, the host would unveil the $400 door since it is 
# the median of the 100,400, 500 doors that are left.
#  You are then given an option to change to any of the other unveiled doors.

reward=[]

def rel_freq(x):
    freqs = [(value, x.count(value) / len(x)) for value in set(x)] 
    return freqs


for i in range(10000):
    rewards = [100,200, 400, 500]

    picked_door = rewards.pop(random.randint(0,len(rewards)-1))
    shown_door = statistics.median(rewards)
    rewards.remove(shown_door)

    picked_door = rewards.pop(random.randint(0,len(rewards)-1))
    reward.append(picked_door)

print(rel_freq(reward))
print(statistics.mean(reward))

