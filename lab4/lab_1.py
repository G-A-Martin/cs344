'''
This implements the simulation of a coin flip of two coins that computes the probability

@author: Gavin Martin
@version feb 28, 2020
'''

from probability import JointProbDist, enumerate_joint_ask

# The Joint Probability Distribution Fig. 13.3 (from AIMA Python)
P = JointProbDist(['Coin1', 'Coin2'])
T, F = True, False
# T symbolizes Heads, while False symbolizes Tails
P[T, T] = .25
P[T, F] = .25
P[F, T] = .25
P[F, F] = .25



# Compute P(Coin2|Coin1=T)  # T means heads
PC = enumerate_joint_ask('Coin2', {'Coin1': T}, P)
print(PC.show_approx())



# Answers:
# It did confirm what I thought was true about flipping coins. If one coin is preset to heads / tails,
# it makes sense that the other coin would have a 50/50 shot of being either.

# For the probability done by hand: I took the probability where (Cavity and Catch are true) / P(Catch is true)
# That came out to (.108 + .072) / (.108 + .016 + .072 + .144) or .529 for P(Cavity | Catch)

# I can see why this would be problematic for a bigger function. The more variables you add,
# the longer and more chaotic the problem woudld get. It isn't very scaeable.
