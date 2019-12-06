from spellchecker import SpellChecker
import html2text    
import sys
import requests
import re
from bs4 import BeautifulSoup, element

# start_urls = ['https://en.wikipedia.org/wiki/Commonly_misspelled_English_words']
# start_urls = ['https://www.cbssports.com/mlb/news/mlb-hot-stove-astros-trade-jake-marisnick-to-the-mets-in-exchange-for-two-prospects/']

class MisspellFinder():

    def __parsePage(self, url):
        h2t = html2text.HTML2Text()
        h2t.ignore_links = True
        h2t.escape_all = True

        r = requests.get(url) 

        return h2t.handle(r.text)

    def __formatPagesWords(self, responseWords):
        preparedWords = []
        for word in responseWords.split():
            symbolLessWord = re.sub("[^A-Za-z'\-@]+", '', word)
            urlLessWord = re.sub('.*[http].*', '', symbolLessWord)
            if (urlLessWord != '' and urlLessWord[0] != '@' and urlLessWord[-3:] != 'com'):
                preparedWords.append(urlLessWord)
        return preparedWords

    def __getPotentiallyWrongWords(self, words):
        spell = SpellChecker()
        misspelled = spell.unknown(words)
        x = []
        for word in misspelled:
            x.append(word)
        return x
        
    def __getSuggestion(self, word):
        gSearchPage = 'https://www.google.com/search?q=' + word
        r = requests.get(url = gSearchPage) 
        content = r.text
        soup = BeautifulSoup(content, features="lxml")
        results = soup.find_all("b")
        if (len(results) > 0):
            return soup.find_all("b")[0].text
        else:
            return ""

    def getMisspelledWords(self, url):

        misspelled = {}

        responseWords = self.__parsePage(url)

        preparedWords = self.__formatPagesWords(responseWords)

        potentiallyWrongWords = self.__getPotentiallyWrongWords(preparedWords)

        print(potentiallyWrongWords)

        for word in potentiallyWrongWords:
            suggestion = self.__getSuggestion(word)
            suggestionConcat = suggestion.replace(" ", "")
            suggestionWithS = suggestion + "'s"
            if (suggestion != "" and word != suggestionConcat and word != suggestionWithS):
                misspelled[word] = suggestion       
                # fo.write(word + " should be: " + suggestion + "\n")
        return misspelled

