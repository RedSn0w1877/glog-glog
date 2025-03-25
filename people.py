# Add to dependencies!
import math as m
# calculate humans by near n
def human(i, c, g, l, y):
    # where i is inital population
    # c is children per people, must be >= 0
    # g is time between having kids, in years >= 0
    # l is the average lifespan >= 0
    # y is years into the furture >= 0
    humans = i * (c/2)**(y/g)*(m.e)**(-y/l) # don't even ask me how this works
    return humans

print(human(i=8000000000,c=2,g=28,l=80,y=50)) #ok we need to have 4 children or we go extinct
