import csv
import itertools

import es_connector

def grouper(n, iterable):
    it = iter(iterable)
    while True:
        chunk = tuple(itertools.islice(it, n))
        if not chunk:
            return
        yield chunk

def transform_tweet_dict(tweet_dict):
    print(tweet_dict)
    return {
        'cashtags': '',
        'conversation_id': 0,
        'created_at': '',
        'date': tweet_dict['pub_date'].replace('T', ' ').split('+')[0],
        'day': int(tweet_dict['pub_date'].split('-')[-1].split('T')[0]),
        'essid': '',
        'hashtags': tweet_dict['hashtags'],
        'hour': int(tweet_dict['pub_date'].split('T')[-1].split(':')[0]),
        'id': tweet_dict['tweet_id'],
        'mentions': list(map(
            lambda mention: ({
                'screen_name': mention,
                'name': '',
                'id': 0,
            }), tweet_dict['mentions'].split(',')
        )),
        'name': tweet_dict['user_name'],
        'nlikes': tweet_dict['favorite_count'],
        'nreplies': tweet_dict['reply_count'],
        'nretweets': tweet_dict['retweet_count'],
        'reply_to': {
                'screen_name': tweet_dict['in_reply_to_screen_name'],
                'name': '',
                'id': 0,
                'user_id': 0
        },
        'retweet': 'true' if 'RT @' in tweet_dict['text'] else 'false',
        # 'retweet_date': tweet_dict['source_pub_date'].replace('T', ' ').split('+')[0] if 'RT @' in tweet_dict['text'] else None,
        # 'retweet_id': tweet_dict['source_id_str'] if 'RT @' in tweet_dict['text'] else None,
        'tweet': tweet_dict['text'],
        'urls': tweet_dict['urls'],
        'username': tweet_dict['screen_name']
    }

def import_all(file_name='../fixed_full_index_dump.csv', index_name='all_tweets'):
    with open(file_name, 'r') as infile:
        reader = csv.DictReader(infile, delimiter=';', quotechar='|')
        for i, batch in enumerate(grouper(10000, reader)):
            print(f'Batch {i}')
            es_connector.bulk_import(
                map(
                    transform_tweet_dict,
                    batch
                ),
                index_name
            )

def preview_import(file_name='../fixed_full_index_dump.csv', index_name='all_tweets'):
    with open(file_name, 'r') as infile:
        reader = csv.DictReader(infile, delimiter=';', quotechar='|')
        for i, row in enumerate(reader):
            tweet = transform_tweet_dict(row)
            print(i)
            print('RT @' in tweet['tweet'])
            print()
            if i > 15:
                return

# import_all()
preview_import()
