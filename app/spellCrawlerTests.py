import unittest 
from dbClient import *
import mysql.connector as conn
from config import config

import sys
sys.path.append('/home/caskla/bin/python/spellcrawler/app/SpellCrawler')
from spellcrawler import getTopPages
from misspellFinder import MisspellFinder


class TestSpellCrawler(unittest.TestCase):

    def testGetTopPages(self):
        topPages = getTopPages('file:///home/caskla/bin/python/spellcrawler/GoogleTrends.html')
        
        checkResults = ['https://www.cbsnews.com/news/ups-truck-police-chase-miramar-hostage-frank-ordonez-was-on-his-first-day-as-driver-coworker-says/', 'https://www.npr.org/2019/12/06/785476331/shooting-puts-pensacola-navy-base-on-lockdown-sheriff-says-shooter-is-dead', 'https://www.cnn.com/2019/12/06/entertainment/kylie-rae-harris-drunk-speeding-crash-death-trnd/index.html', 'https://www.washingtonpost.com/sports/2019/12/06/nfc-east-is-embarrassing-itself/', 'https://people.com/style/keanu-reeves-girlfriend-alexandra-grant-explains-gray-hair/', 'https://www.techradar.com/news/india-vs-west-indies-live-stream-how-to-watch-2019-t20-series-cricket-from-anywhere', 'https://djbooth.net/features/2019-12-06-roddy-ricch-please-excuse-me-for-being-antisocial-album-review-new-music', 'https://www.boston.com/sports/boston-bruins/2019/12/06/bruins-blackhawks-score-highlights-recap', 'https://www.cnn.com/2019/12/06/politics/nancy-pelosi-donald-trump-impeachment/index.html', 'https://www.vulture.com/2019/12/listen-camila-cabello-new-album-romance.html', 'https://www.cnn.com/2019/12/06/asia/mulan-trailer-disney-hong-kong-intl-hnk/index.html', 'https://www.npr.org/2019/12/05/785356513/r-kelly-bribed-official-to-marry-15-year-old-aaliyah-government-alleges', 'https://decider.com/2019/12/06/v-wars-season-2-on-netflix/', 'https://www.businessinsider.com/youtubes-rewind-2019-video-features-pewdiepie-after-2018-snub-2019-12', 'https://www.cnn.com/2019/12/06/politics/joe-biden-iowa-voter-confrontation-analysis/index.html', 'https://www.usatoday.com/story/life/parenting/2019/12/05/eddie-murphy-10-children-seems-ok-men-women-react-differently-to-his-large-family/2618907001/', 'https://www.cbssports.com/nba/news/rockets-vs-raptors-odds-line-spread-2019-nba-picks-dec-5-predictions-from-model-on-15-3-roll/', 'https://variety.com/2019/film/news/tom-holland-spider-man-bob-iger-drunk-call-1203426897/', 'https://www.cbsnews.com/news/north-korea-warns-donald-trump-dotard-war-of-words-rocket-man-nuclear-talks-deadline-today-2019-12-06/', 'https://www.usatoday.com/story/news/politics/2019/12/06/karen-mcdougal-sues-fox-news-over-tucker-carlson-segment-trump/4351801002/', 'https://www.thedailybeast.com/jagged-little-pill-alanis-morissette-conquers-broadway-with-brilliant-powerful-jukebox-musical', 'https://www.foxnews.com/sports/mets-jake-marisnick-astros-trade', 'https://www.countryliving.com/life/entertainment/a30138541/a-charlie-brown-christmas-songs-characters-how-to-watch/', 'https://www.espn.com/soccer/report?gameId=541700', 'https://nypost.com/2019/12/06/this-steve-belichick-video-gem-couldnt-stay-hidden-for-long/', 'https://ourcommunitynow.com/style/what-happens-when-you-wear-an-ugly-christmas-sweater', 'https://www.cbssports.com/nba/news/sixers-vs-wizards-odds-spread-2019-nba-picks-dec-5-predictions-from-advanced-computer/', 'https://people.com/music/demi-lovato-teases-new-music-next-time-you-hear-from-me-ill-be-singing/']

        self.assertEqual(topPages, checkResults)
    

class TestMisspellFinder(unittest.TestCase):

    def testGetMisspelledWords(self):
        link = 'https://en.wikipedia.org/wiki/Commonly_misspelled_English_words'
        misspellFinder = MisspellFinder()   
        misspells = misspellFinder.getMisspelledWords(link)
        checkResults = {'refered': 'referred', 'orignal': 'original', 'welfair': 'welfare', 'concious': 'conscious', 'dumbell': 'dumbbell', 'awfull': 'awful', 'collaegue': 'colleague', 'religius': 'religious', 'dacquiri': 'daiquiri', 'wierd': 'weird', "book's": 'books', 'successfull': 'successful', 'skilfull': 'skilful', 'advizable': 'advisable', 'dilema': 'dilemma', 'religous': 'religious', 'readible': 'readable', 'neice': 'niece', 'annualy': 'annually', 'consciencious': 'conscientious', 'occassionally': 'occasionally', 'freind': 'friend', 'colum': 'column', 'vaccuum': 'vacuum', 'carribean': 'caribbean', 'consious': 'conscious', 'similer': 'similar', 'comming': 'coming', 'camoflage': 'camouflage', 'alegiance': 'allegiance', 'foriegn': 'foreign', 'acerage': 'acreage', 'usible': 'usable', 'referance': 'reference', 'drunkeness': 'drunkenness', 'relize': 'realize', 'adress': 'address', 'libary': 'library', 'liesure': 'leisure', 'ignorence': 'ignorance', 'acrage': 'acreage', 'vacume': 'vacuum', 'abcense': 'absence', 'diffrence': 'difference', 'daquiri': 'daiquiri', 'necessery': 'necessary', 'acknowlege': 'acknowledge', 'vaccum': 'vacuum', 'lisence': 'license', 'mideval': 'medieval', 'occassion': 'occasion', 'ommision': 'omission', 'guage': 'gauge', 'recomend': 'recommend', 'medevil': 'medieval', 'adviseable': 'advisable', 'agression': 'aggression', 'ordeurves': 'horderves', 'becomeing': 'becoming', 'milennium': 'millennium', 'reccommend': 'recommend', 'anually': 'annually', 'solider': 'soldier', 'wilfull': 'wilful', 'begining': 'beginning', 'collegue': 'colleague', 'buisness': 'business', 'omision': 'omission', 'firey': 'fiery', 'allegaince': 'allegiance', 'aquire': 'acquire', 'visious': 'vicious', 'sieze': 'seize', 'becuase': 'because', 'occurrance': 'occurrence', 'aweful': 'awful', 'decieve': 'deceive', 'jewelery': 'jewelry', 'neccessary': 'necessary', 'absance': 'absence', 'liason': 'liaison', 'guidence': 'guidance', 'beleive': 'believe', 'wellfare': 'welfare', 'occasionaly': 'occasionally', 'refrence': 'reference', 'embarass': 'embarrass', 'medeval': 'medieval', 'camoflague': 'camouflage', 'allegience': 'allegiance', 'sucessful': 'successful', 'recieve': 'receive', 'aknowledge': 'acknowledge', 'fullfil': 'fulfil'}

        self.assertEqual(misspells, checkResults)
    
    
if __name__ == '__main__':
    unittest.main()