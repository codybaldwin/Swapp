import os
from twython import TwythonStreamer


KEYPATH = 'OTHPATH'


def get_api_keys():
    '''get the twitter api keys and put them in a dict'''
    keyfile = os.environ.get(KEYPATH) + 'keyfile.txt'
    Odict = dict()
    lines = [line.strip() for line in open(keyfile)]
    for line in lines:
        key, value = tuple(line.split('='))
        Odict[key] = value
    return Odict


class TweetStreamer(TwythonStreamer):
    def on_success(self, data):
        if 'text' in data:
            print data['text'].encode('utf-8')

    def on_error(self, status_code, data):
        print status_code
        self.disconnect()


def main():
    acct = get_api_keys()
    streamer = TweetStreamer(acct['ConsumerKey'], acct['ConsumerSecret'],
                            acct['AccessToken'], acct['AccessTokenSecret'])
                            #timeout=10, retry_count=3, retry_in=30)

    streamer.statuses.filter(track='#SwappWant')


if __name__ == '__main__':
    main()
