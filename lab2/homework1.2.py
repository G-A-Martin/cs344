from csp import backtracking_search
import random
import csp

import itertools




def CourseScheduler():
    courses = "cs108 cs112 cs212 cs214 cs232 cs262 cs344".split()
    variables = courses
    professors = 'VanderLinden Norman, Adams, Bailey'.split()
    times = 'mwf900 mwf1030 tth1130 tth1230'.split()
    classrooms = 'nh253 sb382'.split()
    possibleValues = list(itertools.product(classrooms, professors, times))
    random.shuffle(possibleValues)
    domains = {}
    for course in variables:
        domains[course] = possibleValues
    #print(domains)
    neighbors = {}
    for course in variables:
        courseCopyList = variables[:]
        courseCopyList.remove(course)
        neighborList = courseCopyList
        neighbors[course] = neighborList
    #print(neighbors)

    def constraints(A, a, B, b):
        #print("A " + str(A))
        #print("a " + str(a))
        #print("B " + str(B))
        #print("b " + str(b))
        # Room has space for one class at a time
        one_class_per_room_per_time = True
        # Faculty teaches 1 ting per time slot
        one_faculty_per_time = True
        # Course is taught by only one professor
        one_faculty_per_class = True

        # If the course is the same
        if A == B:
            # Then the same prof should be teaching it
            one_faculty_per_class = a[1] == b[1]
        # if the time is the same, but the course is not the same
        if a[2] == b[2] and A != B:
            # The same prof can't be teaching both classes
            one_faculty_per_time = (a[1] != b[1])
        # if the room is the same, and the time is the same
        if a[0] == b[0] and a[2] == b[2]:
            # then the class should be the same (no two courses in the same room at the same time)
            one_class_per_room_per_time = (A == B)
        return one_faculty_per_class and one_faculty_per_time and one_class_per_room_per_time

    return csp.CSP(variables, domains, neighbors, constraints)

solution = backtracking_search(CourseScheduler())

print(solution)