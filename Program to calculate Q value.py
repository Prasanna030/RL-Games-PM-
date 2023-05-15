import random
import math

# Define the states and actions
states = [0, 1, 2, 3, 4]
actions = [1, 2, 3, 4]
t = 0.9

# Define the rewards and probabilities
rewards = {
    0: {1: 6, 2: -1, 3: 10, 4: 7},
    1: {1: 6},
    2: {1: -1},
    3: {1: 15},
    4: {1: 6}
}
probabilities = {
    0: {1: 0.1, 2: 0.4, 3: 0.2, 4: 0.3},
    1: {},
    2: {},
    3: {},
    4: {}
}

# Initialize the Q-values
Q = {}
for state in states:
    for action in actions:
        Q[state, action] = 0

# Calculate the Q-values
for state in states:
    for action in actions:
        # Calculate the expected reward
        if action in rewards[state]:
            expected_reward = rewards[state][action]
        else:
            expected_reward = rewards[state][1]
        if state == 0:
            for next_state in states:
                expected_reward += probabilities[state][action] * Q[next_state, random.choice(actions)]

        # Update the Q-value
        Q[state, action] = expected_reward * math.exp(-t)

# Print the Q-values
for action in actions:
    print(0, action, Q[0, action])

for state in states[1:4]:
    print(state, 1, Q[state, 1])
