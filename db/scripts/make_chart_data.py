import json
import re
from urllib.parse import urlparse
from collections import Counter

import es_connector

def make_json_from_counters(counters, labels, filename, n=20):
    with open(f'./charts/{filename}', 'w') as outfile:
        output = {
            'data': {
                'labels': labels,
                'datasets': [{
                    'label': f'{filename} {counter_name}',
                    'data': list(
                        counters[counter_name].values()
                    )
                } for counter_name in counters.keys()],
            },
        }
        json.dump(output, outfile)

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

def get_top_rt(index_name, username=None):
    rt_counter = Counter()
    query = {
        'query': {
            'bool': {
                'must': [
                    {
                        'match': {
                            'retweet': True
                        }
                    },
                    {
                        'range': {
                            'date': {
                                'format': 'yyyy-MM-dd',
                                'gte': '2020-01-01',
                                'lte': '2020-12-31',
                            }
                        }
                    },
                    ({
                        'match': {
                            'username': username
                        }
                    } if username else None)
                ]
            }
        }
    }
    tweets = es_connector.query_tweets(query=query, index=index_name)
    for tweet in tweets:
        retweeted_username = '@' + tweet['_source']['tweet'].split('RT @')[-1].split(':')[0]
        rt_counter[retweeted_username.lower()] += 1
    
    return rt_counter

def get_top_mentions(index_name, username=None):
    mentions_counter = Counter()
    query = {
        'query': {
            'bool': {
                'must': [
                    {
                        'match': {
                            'retweet': False
                        }
                    },
                    {
                        'range': {
                            'date': {
                                'format': 'yyyy-MM-dd',
                                'gte': '2020-01-01',
                                'lte': '2020-12-31',
                            }
                        }
                    },
                    ({
                        'match': {
                            'username': username
                        }
                    } if username else None)
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

def get_top_hashtags(index_name, username=None):
    hashtags_counter = Counter()
    query = {
        'query': {
            'bool': {
                'must': [
                    {
                        'regexp': {
                            'tweet': '.+'
                        }
                    },
                    {
                        'range': {
                            'date': {
                                'format': 'yyyy-MM-dd',
                                'gte': '2020-01-01',
                                'lte': '2020-12-31',
                            }
                        }
                    },
                    ({
                        'match': {
                            'username': username
                        }
                    } if username else None)
                ],
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

def get_top_domains(index_name, username=None):
    domains_counter = Counter()
    query = {
        'query': {
            'bool': {
                'must': [
                    {
                        'regexp': {
                            'urls': '.+'
                        }
                    },
                    {
                        'range': {
                            'date': {
                                'format': 'yyyy-MM-dd',
                                'gte': '2020-01-01',
                                'lte': '2020-12-31',
                            }
                        }
                    },
                    ({
                        'match': {
                            'username': username
                        }
                    } if username else None)
                ],
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

def get_monthly_activity(index_name, number_of_users=1):
    months = {}
    query = {
        'query': {
            'regexp': {
                'tweet': '.+'
            }
        },
        'size': 0,
        'aggs': {
            'tweets_over_time': {
                'date_histogram': {
                    'field': 'date',
                    'calendar_interval': 'month'
                }
            }
        }
    }
    response = es_connector.just_query(query=query, index=index_name)
    buckets = response['aggregations']['tweets_over_time']['buckets']
    for bucket in buckets:
        # print(bucket)
        if '2020' in bucket['key_as_string']:
            months[bucket['key_as_string'].split(' ')[0]] = bucket['doc_count']/number_of_users
    return months

def get_troll_info(troll):
    with open('testing.txt', 'r') as infile:
        for line in infile.readlines():
            if troll.lower() in line.lower():
                return [thing.strip() for thing in line.split('|')]

def get_counter_with_padding(counter, n=20):
    return counter.most_common(n) + [((' ' * i), 0) for i in range(n - len(counter.most_common(n)))]

def make_troll_json(troll):
    RTs = get_top_rt('twint_trolls_tweets', username=troll)
    mentions = get_top_mentions('twint_trolls_tweets', username=troll)
    hashtags = get_top_hashtags('twint_trolls_tweets', username=troll)
    domains = get_top_domains('twint_trolls_tweets', username=troll)
    try:
        info = get_troll_info(troll)
        info_dict = dict(
            name=info[1],
            likes=info[12].split('Likes: ')[-1],
            followers=info[11].split('Followers: ')[-1],
            following=info[10].split('Following: ')[-1],
            location=info[6].split('Location: ')[-1],
            created=info[8].split('Joined: ')[-1],
            tweets=info[9].split('Tweets: ')[-1],
            imageUrl=info[14].split('Avatar: ')[-1],
            userName=info[2],
        )
    except:
        # print(f'WARNING!\tFailed with {troll}.')
        print(troll)
        info_dict = dict()

    final = dict(
        mentions={thing[0]: thing[1] for thing in get_counter_with_padding(mentions, 20)},
        retweets={thing[0]: thing[1] for thing in get_counter_with_padding(RTs, 20)},
        hashtags={thing[0]: thing[1] for thing in get_counter_with_padding(hashtags, 20)},
        domains={thing[0]: thing[1] for thing in get_counter_with_padding(domains, 20)},
        accountInfo=info_dict
    )

    with open(f'checks/trolls/{troll.split("@")[-1]}info.json', 'w') as outfile:
        json.dump(final, outfile)

# # GET TOP RTs
# make_json_from_counter(get_top_rt('twint_politiki_tweets'), 'politiki_RT.json')
# make_json_from_counter(get_top_rt('twint_sample_tweets'), 'sample_RT.json')
# make_json_from_counter(get_top_rt('twint_trolls_tweets'), 'trolls_RT.json')
# make_json_from_counter(get_top_rt('twint_500_tweets'), '500_RT.json')

# # GET TOP mentions
# make_json_from_counter(get_top_mentions('twint_politiki_tweets'), 'politiki_mentions.json')
# make_json_from_counter(get_top_mentions('twint_sample_tweets'), 'sample_mentions.json')
# make_json_from_counter(get_top_mentions('twint_trolls_tweets'), 'trolls_mentions.json')
# make_json_from_counter(get_top_mentions('twint_500_tweets'), '500_mentions.json')

# # GET TOP hashtags
# make_json_from_counter(get_top_hashtags('twint_politiki_tweets'), 'politiki_hashtags.json')
# make_json_from_counter(get_top_hashtags('twint_sample_tweets'), 'sample_hashtags.json')
# make_json_from_counter(get_top_hashtags('twint_trolls_tweets'), 'trolls_hashtags.json')
# make_json_from_counter(get_top_hashtags('twint_500_tweets'), '500_hashtags.json')

# # GET TOP domains
# make_json_from_counter(get_top_domains('twint_politiki_tweets'), 'politiki_domains.json')
# make_json_from_counter(get_top_domains('twint_sample_tweets'), 'sample_domains.json')
# make_json_from_counter(get_top_domains('twint_trolls_tweets'), 'trolls_domains.json')
# make_json_from_counter(get_top_domains('twint_500_tweets'), '500_domains.json')

# GET monthly activity
# make_json_from_counters(
#     {
#         'politiki': get_monthly_activity('twint_politiki_tweets', 87),
#         'sample': get_monthly_activity('twint_sample_tweets', 120),
#         'trolls': get_monthly_activity('twint_trolls_tweets', 26),
#         '500': get_monthly_activity('twint_500_tweets', 500)
#     },
#     [f'2020-{"0" if len(str(i + 1)) == 1 else ""}{i + 1}' for i in range(12)],
#     'monthly.json'
# )

# GENERATE troll data
with open('../people/trolls.txt', 'r') as infile:
    for line in infile.readlines():
        # print(f'Handling {line.strip()}')
        make_troll_json(line.strip())
