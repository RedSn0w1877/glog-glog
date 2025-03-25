# formula for co2: ΔT=λ⋅ln(C/​C0​)
# the triangleT thing is like how mmuch is change
# the half life logo means climate sensitivity, it's like 2.5-4.5 degrees celcious (we in 'MERICA why we using mmetric)
# the C is co2 concentraion in parts per million
# the c with a 0 is pre-industrial co2 in ppm like 280ppm
# bruh more math
# ok so time for kg -> ppm 
# Δppm= M*10^-12/(mGt)(f)
# where triangle ppm is the answer
# m is the mass of the co2 added in kilograms
# mGt is the mass of the atmosphere 5.15*10^6 gigatones, aka 515000000000000000 kilograms
# and f is the fraction of co2
# screw lines 8-12 just know that 7810000000000 kg of co2 gets u 1ppm
# a ppm is like a part per million
import people
import calculateEmissions as ce
import calculateTempChange as ctc
import time
def main(uptoYear,childrenPerGeneration, childMakingAge, lifespan, populationNow, carbonPerPerson):
    emissions = ce.emissions(upto=uptoYear, c=childrenPerGeneration, g=childMakingAge, l=lifespan, i=populationNow, carbonPerPerson=carbonPerPerson)
    o = ctc.co2_kg_to_temp(emissions, 420, 3)
    return o

upto = int(input("Up to which year? "))
children = int(input("How many children does each couple have? "))
age = int(input("How old will poeple get before having children? "))
initial = int(input("What is the current population? "))
ls = int(input("What is the average lifespan? "))
carbon = int(input("How much CO2 does each person create per year (Set to 15 if you do not know.)? "))
print(f'The temperature will increase by {main(uptoYear=upto, childrenPerGeneration=children, childMakingAge=age,populationNow=initial,carbonPerPerson=carbon, lifespan=ls)} degrees celcius.')
time.sleep(10)
