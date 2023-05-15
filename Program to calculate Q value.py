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
    2: {1:-1},
    3: {1:15},
    4: {1: 0}
}
probabilities = {
    0: {1: 0.1, 2: 0.4, 3: 0.2, 4: 0.3},
    1: {},
    2: {},
    3: {},
    4: {}
}

# Define the discount factors
discount_factors = [(lambda x: math.exp(-x), "e^-t"),
                    (lambda x: math.pow(0.3, abs(x - 2)), "(0.3)^|t-2|"),
                    (lambda x: math.pow(0.3, abs(x)), "(0.3)^|t|")]

# Initialize the Q-values
Q = {}
for state in states:
    for action in actions:
        Q[state, action] = 0

# Calculate and print the Q-values for each discount factor
for discount_factor_func, discount_factor_name in discount_factors:
    print(f"Discount Factor Function: {discount_factor_name}")
    print("---------------------------")

    discount_factor = discount_factor_func(t)

    for state in states:
        if state == 0:
            for action in actions:
                # Calculate the expected reward
                if action in rewards[state]:
                    expected_reward = rewards[state][action]
                else:
                    expected_reward = rewards[state].get(1, 0)  # Use default action reward of 0 if action 1 is not present
                for next_state in states:
                    expected_reward += probabilities[state].get(action, 0) * Q[next_state, random.choice(actions)]

                # Update the Q-value with the corresponding discount factor
                Q[state, action] = expected_reward * discount_factor
        else:
            default_action = 1
            if default_action in rewards[state]:
                Q[state, default_action] = rewards[state][default_action] * discount_factor

    # Print the Q-values
    for state in states:
        if state == 0:
            for action in actions:
                print(state, action, Q[state, action])
        else:
            default_action = 1
            print(state, default_action, Q[state, default_action])

    print("\n")
