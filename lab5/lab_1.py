'''
This module implements the Bayesian network shown in the text, Figure 14.2.
It's taken from the AIMA Python code.

@author: kvlinden
@version Jan 2, 2013
'''

from probability import BayesNet, enumeration_ask, elimination_ask, gibbs_ask

# Utility variables
T, F = True, False

# From AIMA code (probability.py) - Fig. 14.2 - burglary example
burglary = BayesNet([
    ('Burglary', '', 0.001),
    ('Earthquake', '', 0.002),
    ('Alarm', 'Burglary Earthquake', {(T, T): 0.95, (T, F): 0.94, (F, T): 0.29, (F, F): 0.001}),
    ('JohnCalls', 'Alarm', {T: 0.90, F: 0.05}),
    ('MaryCalls', 'Alarm', {T: 0.70, F: 0.01})
    ])

# Compute P(Burglary | John and Mary both call).
print(enumeration_ask('Burglary', dict(JohnCalls=T, MaryCalls=T), burglary).show_approx())
# elimination_ask() is a dynamic programming version of enumeration_ask().
print(elimination_ask('Burglary', dict(JohnCalls=T, MaryCalls=T), burglary).show_approx())
# gibbs_ask() is an approximation algorithm helps Bayesian Networks scale up.
print(gibbs_ask('Burglary', dict(JohnCalls=T, MaryCalls=T), burglary).show_approx())
# See the explanation of the algorithms in AIMA Section 14.4.

print("\nP(Alarm | burglary and not earthquake)")
print(enumeration_ask('Alarm', dict(Burglary=T, Earthquake=F), burglary).show_approx())

print("\nP(John | burglary and not earthquake) ")
print(enumeration_ask('JohnCalls', dict(Burglary=T, Earthquake=F), burglary).show_approx())

print("\nP(Burglary | Alarm) ")
print(enumeration_ask('Burglary', dict(Alarm=T), burglary).show_approx())

print("\nP(Burglary | JohnCalls and MaryCalls) ")
print(enumeration_ask('Burglary', dict(JohnCalls=T, MaryCalls=T), burglary).show_approx())

# Rather than use the exact inference alogirthm, they use random sampling which is a faster more scaleable option than applying the exact algorithm to the entire problem. It is a workaround that allows it to scale to massive problems while still getting great results. 



