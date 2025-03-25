import calculateEmissions as ce
import math


def co2_kg_to_temp(kg_co2, C_initial=420, lambda_value=3):
    mass_atmosphere = 5.15e12  # kg of air per ppm CO₂
    ppm_increase = kg_co2 / mass_atmosphere
    C_final = C_initial + ppm_increase
    delta_T = lambda_value * math.log(C_final / C_initial)
    return delta_T

