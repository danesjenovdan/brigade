import logging
import re

import es_connector

logger = logging.getLogger('log')
console = logging.StreamHandler()
logfile = logging.FileHandler('fix_and_upload.log')
logger.addHandler(console)
logger.addHandler(logfile)
logger.setLevel('INFO')

pipe_regex = re.compile(r'(\|+.*?\|+;|.*?;)')

def is_full_row(row):
    chunks = pipe_regex.findall(row)
    if len(chunks) == 17:
        return True
    return False
    
def process_row(full_row_candidate, row, save_function):
    logger.debug('[BEGIN TEST]')
    success = False
    logger.debug('## TESTING CANDIDATE WITH ROW ##')
    new_candidate = 'NEWLINE'.join(full_row_candidate + [row.strip()])
    if is_full_row(new_candidate):
        success = True
        full_row_candidate = []
        save_function(new_candidate)
    else:
        full_row_candidate.append(row.strip())
    logger.debug(f'[SUCCESS: {success}]')
    return (success, full_row_candidate)

def get_tweet_dict_from_row(row):
    chunks = pipe_regex.findall(row)
    tweet_dict = [chunk.replace('|', '')[:-1] for chunk in chunks] + [row.split(';')[-1]]
    
    es_dict = {
        'cashtags': '',
        'conversation_id': 0,
        'created_at': '',
        'essid': '',
        'hashtags': tweet_dict[6],
        'id': tweet_dict[0],
        'mentions': list(map(
            lambda mention: ({
                'screen_name': mention,
                'name': '',
                'id': 0,
            }), tweet_dict[5].split(',')
        )),
        'name': tweet_dict[11],
        'nlikes': tweet_dict[8],
        'nreplies': tweet_dict[9],
        'nretweets': tweet_dict[10],
        'reply_to': {
                'screen_name': tweet_dict[2],
                'name': '',
                'id': 0,
                'user_id': 0
        },
        'retweet': 'true' if 'RT @' in tweet_dict[1] else 'false',
        # 'retweet_date': tweet_dict['source_pub_date'].replace('T', ' ').split('+')[0] if 'RT @' in tweet_dict['text'] else None,
        # 'retweet_id': tweet_dict['source_id_str'] if 'RT @' in tweet_dict['text'] else None,
        'tweet': tweet_dict[1].replace('NEWLINE', '\n').replace('DOUBLEPIPE', '||'),
        'urls': tweet_dict[7],
        'username': tweet_dict[12]
    }

    try:
        es_dict['day'] = int(tweet_dict[13].split('-')[-1].split('T')[0])
        es_dict['hour'] = int(tweet_dict[13].split('T')[-1].split(':')[0])
        es_dict['date'] = tweet_dict[13].replace('T', ' ').split('+')[0]
    except:
        logger.info('BROKEN ROW, POSSIBLY NO DATE')
        logger.info(row)
        # es_dict['day'] = 0
        # es_dict['hour'] = 0
        # es_dict['date'] = '2022-01-01 00:00:00'
    
    return es_dict

with open('../full_index_dump.csv', 'r') as infile:
    # with open('../fixed_full_index_dump.csv', 'w') as outfile:
    rows = []
    full_row_candidate = []
    for i, row in enumerate(infile):
        if i < ((4190 * 1000) + 1):
            continue
        # if i == 0:
        #     continue
        logger.debug('\n')
        logger.debug('[BEGIN ROW]')
        logger.debug(row)
        success, full_row_candidate = process_row(
            full_row_candidate,
            row.replace('||', 'DOUBLEPIPE'),
            # row,
            lambda tweet_string: rows.append(tweet_string)
        )

        if len(full_row_candidate) > 50:
            logger.error(full_row_candidate)
            exit(1)

        if i % 10000 == 0 and success and len(rows) > 0:
            logger.info(f'Sending {len(rows)} tweets to ES.')
            es_connector.bulk_import(
                map(
                    lambda tweet_row: get_tweet_dict_from_row(tweet_row),
                    rows
                ),
                index='all_tweets'
            )
            logger.info(f'{i} lines processed.')
            rows = []

    logger.info(f'Sending {len(rows)} tweets to ES.')
    es_connector.bulk_import(
        map(
            lambda tweet_row: get_tweet_dict_from_row(tweet_row),
            rows
        ),
        index='all_tweets'
    )
    logger.info(f'{i} lines processed.')
    rows = []
# 200000 lines processed