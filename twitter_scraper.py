import os
from twython import Twython, TwythonError


KEYPATH = 'OTHPATH'
GEOCODE = '30.4671,-84.2568,15mi'
TAGS = ['#forsale', '#seling', '#Swapp', '#trade']


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

	twitter = Twython(acctDict['ConsumerKey'], acctDict['ConsumerSecret'], acctDict['AccessToken'], acctDict['AccessTokenSecret'])

	geo = '30.4671,-84.2568,5mi' #tallahassee geocode

	for tag in TAGS:
		search = twitter.search(q=tag, count=100, geocode=GEOCODE)
		tweets = search['statuses']
		for tweet in tweets:
			reponses.append(tweet['id_str'], '\n', tweet['text'], '\n\n')

	return responses


if __name__ == '__main__':
    main()