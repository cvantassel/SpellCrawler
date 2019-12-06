from spellchecker import SpellChecker
import html2text    
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException        

import sys
import requests
import re
from bs4 import BeautifulSoup, element

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
        
    # def __getSuggestion(self, word):
    #     gSearchPage = 'https://www.google.com/search?q=' + word
    #     r = requests.get(url = gSearchPage) 
    #     content = r.text
    #     soup = BeautifulSoup(content, features="lxml")
    #     results = soup.find_all("b")
    #     if (len(results) > 0 and results[0] != "About this page"):
    #         return results[0].text
    #     else:
    #         return ""

    def __getSuggestion(self, word, browser):
        gSearchPage = 'https://www.google.com/search?q=' + word

        browser.set_window_position(0, 0)
        browser.set_window_size(1024, 768)
        browser.get(gSearchPage)
    
        try:
            suggestion = browser.find_elements_by_tag_name("b")
            if (len(suggestion) > 0):
                word = suggestion[0].find_element_by_tag_name("i").text
            else:
                raise NoSuchElementException
            return word
        except NoSuchElementException:
            return ""

    def getMisspelledWords(self, url):

        misspelled = {}

        responseWords = self.__parsePage(url)

        preparedWords = self.__formatPagesWords(responseWords)

        potentiallyWrongWords = self.__getPotentiallyWrongWords(preparedWords)

        print(potentiallyWrongWords)
        browser = webdriver.Firefox()

        for word in potentiallyWrongWords:
            suggestion = self.__getSuggestion(word,browser)
            suggestionConcat = suggestion.replace(" ", "")
            suggestionWithS = suggestion[:-2] + "'s"
            if (suggestion != "" and word != suggestionConcat and word != suggestionWithS):
                misspelled[word] = suggestion       

        browser.close()
        return misspelled

