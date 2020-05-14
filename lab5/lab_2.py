from probability import BayesNet, enumeration_ask, elimination_ask, gibbs_ask

# Utility variables
T, F = True, False

# From AIMA code (probability.py) - Fig. 14.2 - burglary example
cancer = BayesNet([
    ('Cancer', '', .01),
    ('Test1', 'Cancer', {T: .9, F: .2}),
    ('Test2', 'Cancer', {T: .9, F: .2})
    ])

print("\nP(Cancer | Test1 and Test2)")
print(enumeration_ask('Cancer', dict(Test1=T, Test2=T), cancer).show_approx())

print("\nP(Cancer | Test1 and negative Test2)")
print(enumeration_ask('Cancer', dict(Test1=T, Test2=F), cancer).show_approx())


#
# P(Cause | T1 And T2) = alpha * <P(C) * P(T1 | C) * P(T2 | C), P( not C) * P(T1 | not C) * P(T2 | not C)>
# = alpha * <.01 * .9 * .9, .99 * .2 * .2>
# = alpha * <.0081, .0396>
# = <.17, .83> (after normalization)

#   P(C | T1 and T2) = alpha * <P(C) * P(T1 | C) * P(not T2 | C), P(not C) * P(T1 | not C) * P(not T2 | Not C)>
#   = alpha * <.01 * .9 * .1, .99 * .2 * .8>
#   = alpha * <.0009, .1584>
#   = <.00565, .994> (after normalization)
#

# This makes sense because the chance of getting cancer is very low while the chance of getting a false positive is high.
# These two things combined cause the probabilty of having cancer given two positive test results and even a postive and a negative
# as being really low. 