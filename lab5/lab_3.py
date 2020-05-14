from probability import BayesNet, enumeration_ask, elimination_ask, gibbs_ask

# Utility variables
T, F = True, False

# From AIMA code (probability.py) - Fig. 14.2 - burglary example
happy = BayesNet([
    ('Sunny', '', .7),
    ('Raise', '', .01),
    ('Happy', 'Sunny Raise', {(T, T): 1.0, (T, F): 0.7, (F, T): 0.9, (F, F): .1}),
    ])

print("\nP(Raise | Sunny)")
print(enumeration_ask('Raise', dict(Sunny=T), happy).show_approx())

#   P(Raise | sunny) = alpha * <P(Raise) * P(Sunny | Raise), P(Not raise) * P(Sunny | not raise)>
#   = alpha * <.01 * .7, .99 * .7>
#   = alpha * <.007, .693>
#   = <.01, .99> -independent events so they don't affect eachother.
#
#


print("\nP(Raise | Happy and Sunny)")
print(enumeration_ask('Raise', dict(Happy=T, Sunny=T), happy).show_approx())

#   P(Raise | Happy and Sunny) = alpha * <P(Happy | Sunny and Raise) * P(Sunny) * P(Raise), P(Happy | Sunny and Not raise) * P(Sunny) * P( No raise)
#   = alpha * <.01 * .7 * .01, .7 * .7 * .99>
#   = <.0142, .986>
#

# These makes sense to me too. The first one, has P(Raise | Sunny) as independent so they didn't affect eachother at all.
# This is a sunny day has nothing to do with getting a raise
# The second one makes sense because it shows the probability of getting a raise given that you're happy and sunny
# While the sunny doesn't directly affect the raise, it affects happiness which is also affected by raise, so this one shows,
# that the probability that someone got a raise is slightly higher if they're happy.

print("\nP(Raise | Happy)")
print(enumeration_ask('Raise', dict(Happy=T), happy).show_approx())

print("\nP(Raise | Happy and Not sunny)")
print(enumeration_ask('Raise', dict(Happy=T, Sunny=F), happy).show_approx())

# These results do make sense to me as well. They show that the probability of having gotten a raise
# substaintally goes up if you're happy. It could be sunny, or it could not be, but if its not and you're still happy, that's
# an even better indicator that you got a raise, because you're happy despite the lack of sun.

