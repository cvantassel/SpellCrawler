from app import app
from flask import render_template
# from app.SpellCrawler.spellcrawler import findMisspellingsForTopPages


from app.dbClient import dbClient
from app.config import config
import mysql.connector as conn

client = dbClient(config)


@app.route('/')
@app.route('/home')
def index():
    # misspelledWordsDict = findMisspellingsForTopPages()

    query = "SELECT Website.link, Suggestions.word, Suggestions.suggestion from Suggestions inner join Website on Website.id = Suggestions.relatedSite;"

    misspelledWords = client.run_query(query)

    misspelledWordsDict = {}
    tmplist = []
    # for words in misspelledWords:
    #     x = words[0]
    #     if x not in misspelledWordsDict:
    #         print("inserting " + str(words[1:]) + " into " + x)
    #         misspelledWordsDict[x] = tmplist
    #         misspelledWordsDict[x].append(list(words[1:]))
    #     else:
    #         print("fail: inserting " + str(words[1:]) + " into " + x)
    #         misspelledWordsDict[x].append(list(words[1:]))
    
    print(misspelledWords)
    print(misspelledWordsDict)
            
    return render_template("index.html", misspelled=misspelledWords)
