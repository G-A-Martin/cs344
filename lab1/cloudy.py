from probability import BayesNet, enumeration_ask, elimination_ask, gibbs_ask

# Utility variables
T, F = True, False

# From AIMA code (probability.py) - Fig. 14.2 - burglary example
cloudy = BayesNet([
    ('Cloudy', '', 0.5),
    ('Sprinkler', 'Cloudy', {T: .1, F: .5}),
    ('Rain', 'Cloudy', {T: .8, F: .2}),
    ('WetGrass', 'Sprinkler Rain', {(T, T): 0.99, (T, F): 0.9, (F, T): 0.9, (F, F): 0.0}),
    ])


print("\nP(Cloudy)")
print(enumeration_ask('Cloudy', dict(), cloudy).show_approx())

print("\nP(Sprinkler | Cloudy)")
print(enumeration_ask('Sprinkler', dict(Cloudy=True), cloudy).show_approx())

print("\nP(Cloudy | Sprinkler and no Rain)")
print(enumeration_ask('Cloudy', dict(Sprinkler=True, Rain=False), cloudy).show_approx())

print("\nP(Wet Grass | sprinkler and cloudy and raining)")
print(enumeration_ask("WetGrass", dict(Sprinkler=True, Rain=True), cloudy).show_approx())

print("\nP(Cloudy | no wet grass)")
print(enumeration_ask("Cloudy", dict(WetGrass=False), cloudy).show_approx())

