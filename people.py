# Add to dependencies!
import math as m
import datetime as dt
# calculate humans by near n
def human(i:float, c:float, g:float, l:float, y:float):
    # where i is inital population
    # c is children per people, must be >= 0
    # g is time between having kids, in years >= 0
    # l is the average lifespan >= 0
    # y is years into the furture >= 0
    humans = i * (c/2)**(y/g)*(m.e)**(-y/l) # don't even ask me how this works
    return humans

def humansInYearList(upto:int, c:float, g:float, l:float, i:float):
    currentYear = dt.datetime.today().year 
    delta = upto - currentYear + 1 #assuming it is jan 1
    humanPopulations = []
    initial = i
    humanPopulations.append(initial)
    for x in range(delta+1):
        population = human(initial, c, g, l, 1)
        initial = population
        humanPopulations.append(m.floor(population))
    return humanPopulations


