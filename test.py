import scrapy
from spellchecker import SpellChecker
import html2text    
import sys
import requests
import re
from bs4 import BeautifulSoup, element

# start_urls = ['https://en.wikipedia.org/wiki/Commonly_misspelled_English_words']
start_urls = ['https://www.espn.com/nfl/story/_/id/28224055/source-panthers-cam-newton-plans-foot-surgery']


def getSuggestion(word):
    gSearchPage = 'https://www.google.com/search?q=' + word
    r = requests.get(url = gSearchPage) 
    content = r.text
    soup = BeautifulSoup(content, features="lxml")
    results = soup.find_all("b")
    if (len(results) > 0):
        return soup.find_all("b")[0].text
    else:
        return ""


def findErrors():

    h2t = html2text.HTML2Text()
    h2t.ignore_links = True
    h2t.escape_all = True

    fo = open("responseh2t.txt", "w+")

    r = requests.get(url = start_urls[0]) 


    resWords = h2t.handle(r.text)

    noSymbolRes = []
    for word in resWords.split():
        symbolLessWord = re.sub("[^A-Za-z'\-@]+", '', word)
        urlLessWord = re.sub('.*[http].*', '', symbolLessWord)
        if (urlLessWord != '' and urlLessWord[0] != '@' and urlLessWord[-4:] != '.com'):
            noSymbolRes.append(urlLessWord)


    potentiallyWrongWords = getPotentiallyWrongWords(noSymbolRes)
    print(potentiallyWrongWords)

    for word in potentiallyWrongWords:
        suggestion = getSuggestion(word)
        suggestionConcat = suggestion.replace(" ", "")
        if (suggestion != "" and word != suggestionConcat):
            fo.write(word + " should be: " + suggestion + "\n")
        # if (word != suggestion and suggestion != "" and not " " in data[1][suggestionNumber]):
        #     fo.write(word + " should be: " + suggestion + "\n")

    fo.close() 

def getPotentiallyWrongWords(words):

    spell = SpellChecker()
    misspelled = spell.unknown(words)
    x = []
    for word in misspelled:
        x.append(word)
    return x
    
def main():
    findErrors()

if __name__== "__main__":
    main()