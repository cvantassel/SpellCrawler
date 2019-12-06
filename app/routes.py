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
    query = "SELECT DISTINCT Website.link, Suggestions.word, Suggestions.suggestion from Suggestions inner join Website on Website.id = Suggestions.relatedSite;"

    misspelledWords = client.run_query(query)

    print(misspelledWords)
            
    return render_template("index.html", misspelled=misspelledWords)
