

from probability import JointProbDist, enumerate_joint_ask

# The Joint Probability Distribution Fig. 13.3 (from AIMA Python)
P = JointProbDist(['Toothache', 'Cavity', 'Catch', 'Rain'])
T, F = True, False
P[T, T, T, T] = 0.054; P[T, T, F, T] = 0.006
P[F, T, T, T] = 0.036; P[F, T, F, T] = 0.004
P[T, F, T, T] = 0.008; P[T, F, F, T] = 0.032
P[F, F, T, T] = 0.072; P[F, F, F, T] = 0.288

P[T, T, T, F] = 0.054; P[T, T, F, F] = 0.006
P[F, T, T, F] = 0.036; P[F, T, F, F] = 0.004
P[T, F, T, F] = 0.008; P[T, F, F, F] = 0.032
P[F, F, T, F] = 0.072; P[F, F, F, F] = 0.288

# Compute P(Cavity|Toothache=T)  (see the text, page 493).
PC = enumerate_joint_ask('Toothache', {'Rain': T}, P)
print(PC.show_approx())


#Answers:
'''
How many entries does your full joint probability distribution contain now?
    - Double; it contains 16 instead of 8. 
    
Do the probabilities sum up to 1.0? Should they? Explain why or why not.
    - Yes they do, they must add up to one in probability, even if they're independent. Otherwise finding the probability would give inaccurate results. 
    
Did you think that you can use anything other than T or F values for the values for the random variables? Explain why or why not.
    - You could, but you would have to make it consistent with all of the rain variables.  However it works much simpler to 
    use T and F for the values for readability and consistency. I tested it with strings for "Rain" and it worked, but I left it at T and F
    for readability's sake. 
    
Did the probabilities you chose indicate that the value of Rain is independent of the original values?
- Yes, it was independent of the original values. It took every existing value and divided it by half and doubled them to account
for F and T among the rains. When you get the probabilty of anything there, it is exactly the same as before despite the adition of 
rain.


P(toothache | rain) = P(toothache and Rain) / P(Rain), this was 

P(toothache and Rain) = (0.054 + 0.008 + 0.006 + 0.032) = .1

P(Rain) = .5 

P(toothache and Rain) / P(Rain) = .1 / .5 = .2

PC = enumerate_joint_ask('Toothache', {'Rain': T}, P)
- this showed as False: .8 and True: .2
'''