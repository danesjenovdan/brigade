from elasticsearch import Elasticsearch, helpers
from datetime import datetime, timedelta

import json
from collections import Counter

host = 'localhost:9200'
# host = 'https://es.brigade.k8s.djnd.si'

class Checks(object):
  def __init__(self):
    self.es = Elasticsearch(host)

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

  def get_most_tweets(self, index='twint_sample_tweets', username=None, retweet=False, metric='nlikes'):
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
                "retweet": retweet,
              }
            }
          ]
        }
      },
      "sort": [{
        metric: {
          "order": "asc"
        }
      }, ],
    }
    res = helpers.scan(self.es, index=index, query=query)
    tweets = list()
    for t in res:
      tweets.append(t)
    sorted_tweets = sorted(tweets, key=lambda tweet: int(tweet['_source'][metric]))
    sorted_tweets.reverse()
    return sorted_tweets

  def get_political_mentions(self, index='twint_politiki_tweets', politician=None, username=None):
    query = {
      'query': {
        "bool": {
          "must": {
            'bool': {
              'must': [{
                "match": {
                  "username": politician,
                }
              },
              {
                'regexp': {
                  'tweet': f'.*{username}.*'
                }
              }]
            },
          }
        },
      }
    }
    res = helpers.scan(self.es, index=index, query=query)
    tweets = list()
    for t in res:
      tweets.append(t)
    # sorted_tweets = sorted(tweets, key=lambda tweet: int(tweet['_source'][metric]))
    # return sorted_tweets
    return tweets


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

def get_most_liked_original_tweets(group_name, index):
  with open(f'../people/{group_name}.txt', 'r') as infile:
    with open(f'checks/localhost_{group_name}_likest.tsv', 'w') as outfile:
      for i, line in enumerate(infile.readlines()):
        username = line.strip()
        most_liked = checks.get_most_tweets(username=username, index=index, metric='nlikes')
        if len(most_liked) > 0:
        # outfile.write(f'{username}\t{most_liked[0]["_source"]["nlikes"]}\thttps://twitter.com/{username}/{most_liked[0]["_source"]["id"]}\n')
          output = f'{username}\t{most_liked[0]["_source"]["nlikes"]}\thttps://twitter.com/{username}/status/{most_liked[0]["_source"]["id"]}\n'
        else:
          output = f'{username}\tN/A\tN/A\n'

        outfile.write(output)

def get_most_rted_original_tweets(group_name, index):
  with open(f'../people/{group_name}.txt', 'r') as infile:
    with open(f'checks/localhost_{group_name}_RTest.tsv', 'w') as outfile:
      for i, line in enumerate(infile.readlines()):
        username = line.strip()
        most_liked = checks.get_most_tweets(username=username, index=index, metric='nretweets')
        if len(most_liked) > 0:
        # outfile.write(f'{username}\t{most_liked[0]["_source"]["nlikes"]}\thttps://twitter.com/{username}/{most_liked[0]["_source"]["id"]}\n')
          output = f'{username}\t{most_liked[0]["_source"]["nlikes"]}\thttps://twitter.com/{username}/status/{most_liked[0]["_source"]["id"]}\n'
        else:
          output = f'{username}\tN/A\tN/A\n'

        outfile.write(output)

def get_most_rted_retweets(group_name, index):
  with open(f'../people/{group_name}.txt', 'r') as infile:
    with open(f'checks/localhost_{group_name}_likest_RT.tsv', 'w') as outfile:
      for i, line in enumerate(infile.readlines()):
        username = line.strip()
        most_liked = checks.get_most_tweets(username=username, index=index, retweet=True, metric='nretweets')
        if len(most_liked) > 0:
        # outfile.write(f'{username}\t{most_liked[0]["_source"]["nlikes"]}\thttps://twitter.com/{username}/{most_liked[0]["_source"]["id"]}\n')
          output = f'{username}\t{most_liked[0]["_source"]["nretweets"]}\thttps://twitter.com/{username}/status/{most_liked[0]["_source"]["id"]}\n'
        else:
          output = f'{username}\tN/A\tN/A\n'

        outfile.write(output)

def get_user_info(troll):
    with open('../people/user_info.txt', 'r') as infile:
        for line in infile.readlines():
            if troll.lower() in line.lower():
                return [thing.strip() for thing in line.split('|')]

def get_political_mentions(group_name):
  with open(f'checks/localhost_{group_name}_politicians.tsv', 'w') as outfile:
    with open('../people/politiki.txt', 'r') as polfile:
      for i, poline in enumerate(polfile.readlines()):
        mentions = {}
        politician = poline.strip()
        with open(f'../people/{group_name}.txt', 'r') as infile:
          for userline in infile.readlines():
            username = userline.strip()
            mentions[username] = len(checks.get_political_mentions(username=username, politician=politician))
          if i == 0:
            outfile.write(f'politician\t{"	".join(sorted(mentions.keys()))}\n')
          else:
            values = [politician] + [str(mentions[key]) for key in sorted(mentions.keys())]
            outfile.write(f'{"	".join(values)}\n')

def get_political_mentions_json(group_name):
  output = {}
  with open(f'checks/localhost_{group_name}_politicians.json', 'w') as outfile:
    with open(f'../people/{group_name}.txt', 'r') as infile:
      for userline in infile.readlines():
        username = userline.strip()
        output[username] = {}
        with open('../people/politiki.txt', 'r') as polfile:
          for i, poline in enumerate(polfile.readlines()):
            politician = poline.strip()
            output[username][politician] = len(checks.get_political_mentions(username=username, politician=politician))
          # if i == 0:
          #   outfile.write(f'politician\t{"	".join(sorted(mentions.keys()))}\n')
          # else:
          #   values = [politician] + [str(mentions[key]) for key in sorted(mentions.keys())]
          #   outfile.write(f'{"	".join(values)}\n')
      json.dump(
        {
          username: {
            politician[0]: {
              'mentions': politician[1],
              'imageUrl': get_user_info(politician[0])[14].split('Avatar: ')[-1]
            } for politician in Counter(output[username]).most_common(5)
          } for username in output.keys()
        },
        outfile
      )

# check_group('politiki', 'twint_politiki_tweets')
# check_group('sample', 'twint_sample_tweets')
# check_group('trolls', 'twint_trolls_tweets')
# check_group('brigade', 'twint_500_tweets')
# check_group('all', 'all_tweets')

# get_most_liked_original_tweets('trolls', 'twint_trolls_tweets')
# get_most_rted_original_tweets('trolls', 'twint_trolls_tweets')
# get_political_mentions('trolls')
get_political_mentions_json('trolls')