from elasticsearch import Elasticsearch, helpers

host = 'localhost:9200'
# host = 'https://es.brigade.k8s.djnd.si'
es = Elasticsearch(host)

def just_query(query={}, index='safety_index'):
    return es.search(index=index, body=query)

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
    except Exception as e:
        print('Something went wrong.')
        print(e)
        print(objects_iterator)
