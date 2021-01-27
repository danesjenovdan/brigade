import sys
import json

import es_connector

def dump_index(index_name=''):
    query = {
        'query': {
            'regexp': {
                'tweet': '.+'
            }
        }
    }
    tweets = list(
        map(
            lambda record: record['_source'],
            es_connector.query_tweets(query=query, index=index_name)
        )
    )

    with open(f'./dumps/{index_name}.json', 'w') as outfile:
        json.dump(tweets, outfile)

# dump_index(index_name='twint_sample_tweets')
# dump_index(index_name='twint_politiki_tweets')
# dump_index(index_name='twint_trolls_tweets')

if __name__ == '__main__':
    dump_index(index_name=sys.argv[1])
