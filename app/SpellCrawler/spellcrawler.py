from misspellFinder import MisspellFinder
from selenium import webdriver

import sys
sys.path.append('/home/caskla/bin/python/spellcrawler/app')

from dbClient import dbClient
from config import config
import mysql.connector as conn

client = dbClient(config)

def findMisspellingsForTopPages():

    misspellFinder = MisspellFinder()

    topPages = __getTopPages()

    misspellings = {}

    for page in topPages:
        misspellings[page] = (misspellFinder.getMisspelledWords(page))
        if (topPages.index(page) == 2):
            break

    return misspellings



def __getTopPages():
    browser = webdriver.Firefox()
    browser.get('https://trends.google.com/trends/trendingsearches/daily?geo=US')
    summaries = browser.find_elements_by_class_name("summary-text")

    topPages = []

    for summary in summaries:
        topPages.append(summary.find_element_by_tag_name("a").get_attribute("href"))
    print(topPages)
    
    browser.close()
    return topPages

#temp
if __name__ == '__main__':
    misspellings = findMisspellingsForTopPages()

    query = ""
    client.run_insert_query(query)

    
    print(misspellings)

    {"link" : {'word':'suggestion', "word", suggestion}, repeeat}