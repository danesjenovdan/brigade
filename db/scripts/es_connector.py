from elasticsearch import Elasticsearch, helpers

es = Elasticsearch()

def query_tweets(query={}, index='twint_sample_tweets'):
    res = helpers.scan(es, index=index, query=query)
    tweets = list()
    for t in res:
      tweets.append(t)
    
    # return tweets sorted by date, ascending
    return sorted(tweets, key=lambda tweet: tweet['_source']['date'])
