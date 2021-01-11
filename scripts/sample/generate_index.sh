curl -XDELETE "51.15.239.174:9200/$1?pretty" -H 'Content-Type: application/json'

curl -XPUT "51.15.239.174:9200/$1?pretty" -H 'Content-Type: application/json' -d '
{
    "settings": {
        "analysis": {
            "normalizer": {
                "hashtag_normalizer": {
                    "filter": [
                        "lowercase",
                        "asciifolding"
                    ],
                    "type": "custom",
                    "char_filter": []
                }
            }
        }
    }
}'

curl -XPUT "51.15.239.174:9200/$1/_mapping?pretty" -H 'Content-Type: application/json' -d'
{
    "dynamic": false,
    "properties": {
        "cashtags": {
            "type": "keyword",
            "normalizer": "hashtag_normalizer"
        },
        "conversation_id": {
            "type": "long"
        },
        "created_at": {
            "type": "text"
        },
        "date": {
            "type": "date",
            "format": "yyyy-MM-dd HH:mm:ss"
        },
        "day": {
            "type": "integer"
        },
        "essid": {
            "type": "keyword"
        },
        "geo_near": {
            "type": "geo_point"
        },
        "geo_tweet": {
            "type": "geo_point"
        },
        "hashtags": {
            "type": "keyword",
            "normalizer": "hashtag_normalizer"
        },
        "hour": {
            "type": "integer"
        },
        "id": {
            "type": "long"
        },
        "lang": {
            "type": "keyword"
        },
        "language": {
            "type": "text",
            "fields": {
                "keyword": {
                    "type": "keyword",
                    "ignore_above": 256
                }
            }
        },
        "link": {
            "type": "text"
        },
        "location": {
            "type": "keyword"
        },
        "mentions": {
            "type": "nested",
            "properties": {
                "id": {
                    "type": "long"
                },
                "name": {
                    "type": "text"
                },
                "screen_name": {
                    "type": "text"
                }
            }
        },
        "name": {
            "type": "text"
        },
        "near": {
            "type": "text"
        },
        "nlikes": {
            "type": "integer"
        },
        "nreplies": {
            "type": "integer"
        },
        "nretweets": {
            "type": "integer"
        },
        "photos": {
            "type": "text"
        },
        "profile_image_url": {
            "type": "text"
        },
        "quote_url": {
            "type": "text"
        },
        "reply_to": {
            "type": "nested",
            "properties": {
                "id": {
                    "type": "text",
                    "fields": {
                        "keyword": {
                            "type": "keyword",
                            "ignore_above": 256
                        }
                    }
                },
                "name": {
                    "type": "text",
                    "fields": {
                        "keyword": {
                            "type": "keyword",
                            "ignore_above": 256
                        }
                    }
                },
                "screen_name": {
                    "type": "text",
                    "fields": {
                        "keyword": {
                            "type": "keyword",
                            "ignore_above": 256
                        }
                    }
                },
                "user_id": {
                    "type": "keyword"
                },
                "username": {
                    "type": "keyword"
                }
            }
        },
        "retweet": {
            "type": "text"
        },
        "retweet_date": {
            "type": "date",
            "format": "yyyy-MM-dd HH:mm:ss",
            "ignore_malformed": true
        },
        "retweet_id": {
            "type": "keyword"
        },
        "search": {
            "type": "text"
        },
        "source": {
            "type": "keyword"
        },
        "thumbnail": {
            "type": "text"
        },
        "timezone": {
            "type": "keyword"
        },
        "trans_dest": {
            "type": "keyword"
        },
        "trans_src": {
            "type": "keyword"
        },
        "translate": {
            "type": "text"
        },
        "tweet": {
            "type": "text"
        },
        "urls": {
            "type": "keyword"
        },
        "user_id_str": {
            "type": "keyword"
        },
        "user_rt": {
            "type": "keyword"
        },
        "user_rt_id": {
            "type": "keyword"
        },
        "username": {
            "type": "keyword",
            "normalizer": "hashtag_normalizer"
        },
        "video": {
            "type": "integer"
        }
    }
}'