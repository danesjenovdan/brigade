import json
import re
from urllib.parse import urlparse
from collections import Counter

import es_connector

def make_json_from_counter(counter, filename, n=20):
    with open(f'./charts/{filename}', 'w') as outfile:
        output = {
            'data': {
                'labels': list(map(
                    lambda item: item[0],
                    counter.most_common(n)
                )),
                'datasets': [{
                    'label': filename,
                    'data': list(map(
                        lambda item: item[1],
                        counter.most_common(n)
                    ))
                }],
            },
        }
        json.dump(output, outfile)

def get_top_rt(index_name):
    rt_counter = Counter()
    query = {
        'query': {
            'bool': {
                'must': [
                    {
                        'match': {
                            'retweet': True
                        }
                    }
                ]
            }
        }
    }
    tweets = es_connector.query_tweets(query=query, index=index_name)
    for tweet in tweets:
        retweeted_username = '@' + tweet['_source']['tweet'].split('RT @')[-1].split(':')[0]
        rt_counter[retweeted_username.lower()] += 1
    
    return rt_counter

def get_top_mentions(index_name):
    mentions_counter = Counter()
    query = {
        'query': {
            'bool': {
                'must': [
                    {
                        'match': {
                            'retweet': False
                        }
                    }
                ]
            }
        }
    }
    tweets = es_connector.query_tweets(query=query, index=index_name)
    for tweet in tweets:
        mentioned_username_pattern = re.compile(r'(?<=^|(?<=[^a-zA-Z0-9-_\.]))@([A-Za-z]+[A-Za-z0-9-_]+)')
        mentioned_username = mentioned_username_pattern.search(tweet['_source']['tweet'])
        if mentioned_username:
            mentions_counter[mentioned_username[0].lower()] += 1
    
    return mentions_counter

def get_top_hashtags(index_name):
    hashtags_counter = Counter()
    query = {
        'query': {
            'regexp': {
                'tweet': '.+'
            }
        }
    }
    tweets = es_connector.query_tweets(query=query, index=index_name)
    for tweet in tweets:
        hashtag_pattern = re.compile(r'(?<=^|(?<=[^a-zA-Z0-9-_\.]))#([A-Za-z]+[A-Za-z0-9-_]+)')
        hashtag = hashtag_pattern.search(tweet['_source']['tweet'])
        if hashtag:
            hashtags_counter[hashtag[0].lower()] += 1
    
    return hashtags_counter

def get_top_domains(index_name):
    domains_counter = Counter()
    query = {
        'query': {
            'regexp': {
                'urls': '.+'
            }
        }
    }
    tweets = es_connector.query_tweets(query=query, index=index_name)
    for tweet in tweets:
        urls = tweet['_source']['urls']
        if len(urls) > 0:
            for url in urls:
                domain = urlparse(url).netloc
                domains_counter[domain.lower()] += 1
    
    return domains_counter

# # GET TOP RTs
make_json_from_counter(get_top_rt('twint_politiki_tweets'), 'politiki_RT.json')
make_json_from_counter(get_top_rt('twint_sample_tweets'), 'sample_RT.json')
make_json_from_counter(get_top_rt('twint_trolls_tweets'), 'trolls_RT.json')
make_json_from_counter(get_top_rt('twint_500_tweets'), '500_RT.json')

# GET TOP mentions
make_json_from_counter(get_top_mentions('twint_politiki_tweets'), 'politiki_mentions.json')
make_json_from_counter(get_top_mentions('twint_sample_tweets'), 'sample_mentions.json')
make_json_from_counter(get_top_mentions('twint_trolls_tweets'), 'trolls_mentions.json')
make_json_from_counter(get_top_mentions('twint_500_tweets'), '500_mentions.json')

# GET TOP hashtags
make_json_from_counter(get_top_hashtags('twint_politiki_tweets'), 'politiki_hashtags.json')
make_json_from_counter(get_top_hashtags('twint_sample_tweets'), 'sample_hashtags.json')
make_json_from_counter(get_top_hashtags('twint_trolls_tweets'), 'trolls_hashtags.json')
make_json_from_counter(get_top_hashtags('twint_500_tweets'), '500_hashtags.json')

# GET TOP domains
make_json_from_counter(get_top_domains('twint_politiki_tweets'), 'politiki_domains.json')
make_json_from_counter(get_top_domains('twint_sample_tweets'), 'sample_domains.json')
make_json_from_counter(get_top_domains('twint_trolls_tweets'), 'trolls_domains.json')
make_json_from_counter(get_top_domains('twint_500_tweets'), '500_domains.json')
