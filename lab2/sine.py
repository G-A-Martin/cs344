"""
This module implements local search on a simple abs function variant.
The function is a linear function  with a single, discontinuous max value
(see the abs function variant in graphs.py).

@author: kvlinden
@version 6feb2013
"""
from search import Problem, hill_climbing, simulated_annealing, \
    exp_schedule, genetic_search
from random import randrange
import math


class Sine(Problem):
    """
        State: x value for the abs function variant f(x)
        Move: a new x value delta steps from the current x (in both directions)
        """

    def __init__(self, initial, maximum=30.0, delta=0.001):
        self.initial = initial
        self.maximum = maximum
        self.delta = delta

    def actions(self, state):
        return [state + self.delta, state - self.delta]

    def result(self, stateIgnored, x):
        return x

    def value(self, x):
        return math.fabs(x * math.sin(x))


if __name__ == '__main__':
    # Formulate a problem with a 2D hill function and a single maximum value.
    maximum = 30
    bestHillClimbingResult = 0
    bestSimulatedAnnealingResult = 0

    listOfHillClimbingResults = []
    listOfSimulatedAnnealingResults = []

    for x in range(0, 100):
        initial = randrange(0, maximum)
        p = Sine(initial, maximum, delta=1)
        #print('Initial                      x: ' + str(p.initial)
        #    + '\t\tvalue: ' + str(p.value(initial))
        #    )

        # Solve the problem using hill-climbing.
        hill_solution = hill_climbing(p)

        # Solve the problem using simulated annealing.
        annealing_solution = simulated_annealing(
            p,
            exp_schedule(k=20, lam=0.005, limit=1000)
        )

        listOfHillClimbingResults.append(p.value(hill_solution))
        listOfSimulatedAnnealingResults.append(p.value(annealing_solution))

        if p.value(hill_solution) > bestHillClimbingResult:
            bestHillClimbingResult = p.value(hill_solution)

        if p.value(annealing_solution) > bestSimulatedAnnealingResult:
            bestSimulatedAnnealingResult = p.value(annealing_solution)

    sumOfHillClimbing = 0
    for i in range(0, len(listOfHillClimbingResults)):
        sumOfHillClimbing += listOfHillClimbingResults[i]

    sumOfSimulatedAnnealing = 0
    for i in range(0, len(listOfSimulatedAnnealingResults)):
        sumOfSimulatedAnnealing += listOfSimulatedAnnealingResults[i]

    print('\nAverage Hill-climbing solution       x: ' + str(hill_solution)
        + '\tvalue: ' + str(sumOfHillClimbing / len(listOfHillClimbingResults))
        )

    print('Best Hill-climbing solution       x: ' + str(hill_solution)
        + '\tvalue: ' + str(bestHillClimbingResult) + "\n"
        )

    print('Average Simulated annealing solution x: ' + str(annealing_solution)
          + '\tvalue: ' + str(sumOfSimulatedAnnealing / len(listOfSimulatedAnnealingResults))
          )

    print('Best Simulated annealing solution x: ' + str(annealing_solution)
          + '\tvalue: ' + str(bestSimulatedAnnealingResult)
          )