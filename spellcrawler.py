import scrapy
from spellchecker import SpellChecker
import html2text    
import sys
import requests
import re

# apiKey = 'AIzaSyDW3q3O9vy3c8tFohu7FsoQtLUiv4ZQSM8'
# cx = '014357231247660817202:8nrqpcejysl'

# apiRequestURL = 'https://www.googleapis.com/customsearch/v1?key=' + apiKey
#             + '&cx=' + cx
#             + '&q=' + word



  

class SpellCheckerSpider(scrapy.Spider):
    name = "spellChecker"
    # start_urls = ['https://www.space.com/ad-astra-film-review.html']
    start_urls = ['https://en.wikipedia.org/wiki/Commonly_misspelled_English_words']
    
    def parse(self, response):

        res = response.text
        fo = open("response.txt", "w+")
        fo.write(res)
        fo.close()

        h2t = html2text.HTML2Text()
        h2t.ignore_links = True
        h2t.escape_all = True

        fo = open("responseh2t.txt", "w+")
        resWords = h2t.handle(response.text)
        #fo.write(resWords)

        noSymbolRes = []
        for word in resWords.split():
            word = re.sub('[^A-Za-z0-9]+', '', word)
            noSymbolRes.append(word)
            

        requestURL = 'http://suggestqueries.google.com/complete/search?client=firefox&q=' + word

        for word in noSymbolRes:

            # sending get request and saving the response as response object 
            r = requests.get(url = requestURL) 
            
            # extracting data in json format 
            data = r.json() 
            suggestion = ""
            if (len(data[1]) > 0):
                suggestion = data[1][0]

            if (word != suggestion):
                fo.write(word + " should be: " + suggestion)

        fo.close() 

        

        yield {
            'data' : h2t.handle(response.text)
        }

