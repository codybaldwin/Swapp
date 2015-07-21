from __future__ import print_function
import os
from twython import Twython
#from twython import TwythonStreamer


KEYPATH = 'OTHPATH'
GEOCODE = '30.4671,-84.2568,100mi'
TAGS = ['#SwappWant', '#SwappHave']


def get_api_keys():
    '''get the twitter api keys and put them in a dict'''
    keyfile = os.environ.get(KEYPATH) + 'keyfile.txt'
    Odict = dict()
    lines = [line.strip() for line in open(keyfile)]
    for line in lines:
        key, value = tuple(line.split('='))
        Odict[key] = value
    return Odict


def main():
    acctDict = get_api_keys()
    twitter = Twython(acctDict['ConsumerKey'], acctDict['ConsumerSecret'],
        acctDict['AccessToken'], acctDict['AccessTokenSecret'])

    wantSearch = twitter.search(q='#SwappWant', count=10, geocode=GEOCODE)
    haveSearch = twitter.search(q='#SwappHave', count=10, geocode=GEOCODE)
    search = twitter.search(q='', count=100)

    tweets = search['statuses']

    for tweet in tweets:
        print(tweet['text'].encode('utf-8'), '\n')
"""
    for tag in TAGS:
        search = twitter.search(q=tag, count=100, geocode=GEOCODE)
        tweets = search['statuses']
        for tweet in tweets:
            reponses.append(tweet['id_str'], '\n', tweet['text'], '\n\n')

    return responses
"""

if __name__ == '__main__':
    main()
