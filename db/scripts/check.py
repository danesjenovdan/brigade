from elasticsearch import Elasticsearch, helpers
from datetime import datetime, timedelta

class Checks(object):
  def __init__(self):
    self.es = Elasticsearch()

  def get_oldest_tweets(self, index='twint_sample_tweets', username=None):
    query = {
      "query": {
        "bool": {
          "must": [
            {
              "match": {
                "username": username,
              }
            },
            {
              "match": {
                "retweet": False,
              }
            }
          ]
        }
      },
      "sort": [{
        "date": {
          "order": "desc"
        }
      }, ],
    }

    res = helpers.scan(self.es, index = index, query = query)
    tweets = list()
    for t in res:
      tweets.append(t)
    return sorted(tweets, key=lambda tweet: tweet['_source']['date'])
  
  def get_youngest_retweets(self, index='twint_sample_tweets', username=None):
    query = {
      "query": {
        "bool": {
          "must": [
            {
              "match": {
                "username": username,
              }
            },
            {
              "match": {
                "retweet": True,
              }
            }
          ]
        }
      },
      "sort": [{
        "date": {
          "order": "desc"
        }
      }, ],
    }
    res = helpers.scan(self.es, index = index, query = query)
    tweets = list()
    for t in res:
      tweets.append(t)
    return sorted(tweets, key=lambda tweet: tweet['_source']['date'])

checks = Checks()

def find_joined_date(username):
  with open('../people/joined_timestamps.tsv', 'r') as infile:
    for line in infile.readlines():
      if username.lower() in line.lower():
        return datetime.strptime(line.split('\t')[-1].strip(), '%Y-%m-%d %H:%M:%S')

def check_group(group_name, index):
  with open(f'../people/{group_name}.txt', 'r') as infile:
    with open(f'checks/{group_name}_oldest.tsv', 'w') as outfile:
      with open(f'checks/{group_name}_tweet_holes.txt', 'w') as tweetholefile:
        with open(f'checks/{group_name}_retweet_holes.txt', 'w') as retweetholefile:
          for line in infile.readlines():
            username = line.strip()
            tweets = checks.get_oldest_tweets(username=username, index=index)
            retweets = checks.get_youngest_retweets(username=username, index=index)

            tweet = { '_source': {'date': '' } }
            retweet = { '_source': {'retweet_date': '' } }

            if len(tweets) == 0:
              print(f'No tweet data for {username} with {len(tweets)} tweets.')
            else:
              tweet = tweets[0]

            if len(retweets) == 0:
              print(f'No retweet data for {username} with {len(retweets)} retweets.')
            else:
              retweet = retweets[0]

            outfile.write(f'{username}\t{tweet["_source"]["date"]}\t{retweet["_source"]["retweet_date"].split(" CE")[0]}\n')
            
            if len(tweets) != 0:
              tweet_date = datetime.strptime(tweets[0]['_source']['date'], '%Y-%m-%d %H:%M:%S')
              joined_date = find_joined_date(username)
              try:
                if (tweet_date - timedelta(days=14)) > find_joined_date(username) and (tweet_date > datetime(year=2020, month=1, day=1)):
                  print('PROBLEMATIC', username)
                  tweetholefile.write(f'{username}\t{tweet_date}\t{joined_date}\n')
              except:
                print(f'FAILED TWEET HOLE with {username}, {tweet_date}, {joined_date}')
            
            if len(retweets) != 0:
              tweet_date = datetime.strptime(retweets[0]['_source']['retweet_date'].split(' C')[0], '%Y-%m-%d %H:%M:%S')
              joined_date = find_joined_date(username)
              try:
                if (tweet_date - timedelta(days=14)) > find_joined_date(username) and (tweet_date > datetime(year=2020, month=1, day=1)):
                  print('PROBLEMATIC', username)
                  retweetholefile.write(f'{username}\t{tweet_date}\t{joined_date}\n')
              except:
                print(f'FAILED RETWEET HOLE with {username}, {tweet_date}, {joined_date}')
            # print(tweet['_source']['date'], retweet['_source']['retweet_date'])

check_group('politiki', 'twint_politiki_tweets')
check_group('sample', 'twint_sample_tweets')
check_group('trolls', 'twint_trolls_tweets')
# check_group('brigade', 'twint_500_tweets')
