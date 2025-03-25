# Add to dependencies!
import math as m
import requests
from bs4 import BeautifulSoup
import requests
from bs4 import BeautifulSoup

def get_world_population(): # live world population
    url = 'https://www.worldometers.info/world-population/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    population = soup.find('div', class_='col-md-8 country-pop-description').find('strong').text
    return population
# calculate humans by near n
def human(i, c, g, l, y):
    # where i is inital population
    # c is children per people
    # g is time between having kids, in years
    # l is the average lifespan
    # y is years into the furture
    i = get_world_population()
    humans = i * (c/2)**(y/g)*(m.e)**(-y/l) # don't even ask me how this works
    return humans
