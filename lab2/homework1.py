from search import Problem, hill_climbing, UndirectedGraph, simulated_annealing, exp_schedule

import random
import time
import math


class TSP(Problem):

    def __init__(self, locations, initial):
        self.initial = initial
        self.locations = locations
        self.unVisitedLocations = list(locations.keys())
        self.currentState = initial
        self.cost = 0

    def actions(self, state):
        actions = []
        for location in self.locations:
            if location in self.unVisitedLocations and location != state:
                actions.append(location)
        return actions

    def calculate_distance(self, location1, location2):
        x1 = location1[0]
        x2 = location2[0]
        y1 = location1[1]
        y2 = location2[1]
        dist = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        return dist

    def result(self, state, action):
        new_state = action
        self.currentState = new_state
        oldLocation = self.locations.get(state)
        newLocation = self.locations.get(new_state)
        tripCost = self.calculate_distance(oldLocation, newLocation)
        self.cost = self.cost - tripCost
        self.unVisitedLocations.remove(new_state)
        print("Travel to " + action + " with a travel cost of " + str(tripCost))
        return new_state

    def goal_test(self, state):
        if len(self.unVisitedLocations) == 0:
            return True
        else:
            return False

    def value(self, state):
        oldLocation = self.locations.get(self.currentState)
        newLocation = self.locations.get(state)
        value = self.cost - self.calculate_distance(oldLocation, newLocation)
        return value



if __name__ == '__main__':
    romania = UndirectedGraph(dict(
        arad=dict(zerind=75, sibiu=140, timisoara=118),
        bucharest=dict(urziceni=85, pitesti=101, giurgiu=90, fagaras=211),
        craiova=dict(dobreta=120, rimnicuvilcea=146, pitesti=138),
        dobreta=dict(mehadia=75),
        eforie=dict(hirsova=86),
        fagaras=dict(sibiu=99),
        hirsova=dict(urziceni=98),
        iasi=dict(vaslui=92, neamt=87),
        lugoj=dict(timisoara=111, mehadia=70),
        oradea=dict(zerind=71, sibiu=151),
        pitesti=dict(rimnicuvilcea=97),
        rimnicuvilcea=dict(sibiu=80),
        urziceni=dict(vaslui=142)))

    locations = dict(
        arad=(91, 492),
        bucharest=(400, 327),
        craiova=(253, 288),
        dobreta=(165, 299),
        eforie=(562, 293),
        fagaras=(305, 449),
        giurgiu=(375, 270),
        hirsova=(534, 350),
        iasi=(473, 506),
        lugoj=(165, 379),
        mehadia=(168, 339),
        neamt=(406, 537),
        oradea=(131, 571),
        pitesti=(320, 368),
        rimnicuvilcea=(233, 410),
        sibiu=(207, 457),
        timisoara=(94, 410),
        urziceni=(456, 350),
        vaslui=(509, 444),
        zerind=(108, 531))

initial1 = random.choice(list(locations.keys()))
problem1 = TSP(locations, initial1)
initial2 = random.choice(list(locations.keys()))
problem2 = TSP(locations, initial2)


hill_solution = hill_climbing(problem1)
print('\nHill-climbing solution       x: ' + '\tvalue: ' + str(math.fabs(problem1.value(hill_solution))) + "\n\n")


annealing_solution = simulated_annealing(problem2, exp_schedule(k=20, lam=0.005, limit=15000))
print('\nAnnealing solution       x: ' + '\tvalue: ' + str(math.fabs(problem2.value(annealing_solution))) + "\n\n")

