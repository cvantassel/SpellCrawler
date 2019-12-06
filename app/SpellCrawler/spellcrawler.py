from misspellFinder import MisspellFinder
from selenium import webdriver
import time

import sys
sys.path.append('/home/caskla/bin/python/spellcrawler/app')

from dbClient import dbClient
from config import config
import mysql.connector as conn

client = dbClient(config)

def findMisspellingsForTopPages():

    misspellFinder = MisspellFinder()

    topPages = getTopPages()

    misspellings = {}

    for page in topPages:
        misspellings[page] = (misspellFinder.getMisspelledWords(page))
        #TESTING
        if (topPages.index(page) == 2):
            break

    return misspellings

def getTopPages(link='https://trends.google.com/trends/trendingsearches/daily?geo=US'):
    browser = webdriver.Firefox()
    browser.set_window_position(0, 0)
    browser.set_window_size(1024, 768)
    browser.get(link)
    summaries = browser.find_elements_by_class_name("summary-text")
    time.sleep(2)
    topPages = []

    for summary in summaries:
        topPages.append(summary.find_element_by_tag_name("a").get_attribute("href"))
    print(topPages)
    
    browser.close()
    return topPages

def insertWebsite(link):
    query = "insert into Website (link) values ('%s')" % (link)
    client.run_insert_query(query)

def getWebsiteId(link):
    query = "select id from Website where link = '%s';" % (link)
    return client.run_query(query)[0][0]

def updateValues(misspellingsDict):
    valuesString = ""
    for link, words in misspellingsDict.items():
        if (words != {}):
            insertWebsite(link)
            websiteId = getWebsiteId(link)
            for word, suggestion in words.items():
                valuesString += "(" 
                valuesString += "'" + word.replace("'", r"\'") + "', '" + suggestion.replace("'", r"\'") + "', "
                valuesString += "'" + str(websiteId) + "'), "
    valuesString = valuesString[:-2] + ";"

    query = "insert into Suggestions (word, suggestion, relatedSite) values " + valuesString
    
    print(query)
    client.run_insert_query(query)
        

#temp
if __name__ == '__main__':
    misspellings = findMisspellingsForTopPages()
    print(misspellings)


    updateValues(misspellings)
    
