from elasticsearch import Elasticsearch, helpers

es = Elasticsearch()

def query_tweets(query={}, index='safety_index'):
    res = helpers.scan(es, index=index, query=query)
    tweets = list()
    for t in res:
      tweets.append(t)
    
    # return tweets sorted by date, ascending
    return sorted(tweets, key=lambda tweet: tweet['_source']['date'])

def bulk_import(objects_iterator=[], index='safety_index'):
    try:
        response = helpers.bulk(es, objects_iterator, index=index)
    except:
        print('Something went wrong.')
