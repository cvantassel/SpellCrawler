import scrapy
from spellchecker import SpellChecker
import html2text    
import sys
import re

class SpellCheckerSpider(scrapy.Spider):
    name = "spellChecker"
    start_urls = ['https://www.space.com/ad-astra-film-review.html']
    
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
            word = re.sub('[^A-Za-z0-9]+', ' ', word)
            noSymbolRes.append(word)
            #fo.write()
        spell = SpellChecker()
        matcher = re.compile('.*[http].*')
        for word in spell.unknown(noSymbolRes):
            if(not matcher.match(word)):
                fo.write(word + "\n")

        fo.close() 

        

        yield {
            'data' : h2t.handle(response.text)
        }

