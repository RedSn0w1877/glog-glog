import people
import matplotlib.pyplot as plt
import numpy as np
import datetime as dt
def emissions(upto:int, c:float, g:float, l:float, i:float,carbonPerPerson:float):
    populationList = people.humansInYearList(upto, c, g, l, i)
    #print(populationList)
    #print(len(populationList))
    #for x in range(len(populationList)):f plot(upto)
     #   print(populationList[x])
    emissionsList = []
    for x in range(len(populationList)):
        emission = populationList[x] * carbonPerPerson * 1000 + 4500000000000 + 6000000000000 # in kg
        emissionsList.append(emission)
        return sum(emissionsList)  


    #return sum(emissionsList)
    

def convertToPPM(kilograms):
    return kilograms/5.15e12
