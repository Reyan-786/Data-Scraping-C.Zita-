import requests
from bs4 import BeautifulSoup
import pandas as pd

#Imports the HTML into python
page = requests.get('https://www.carpages.ca/used-cars/search/?num_results=50&fueltype_id%5b0%5d=3&fueltype_id%5b1%5d=7&p=3')
soup = BeautifulSoup(page.text, 'lxml')
soup