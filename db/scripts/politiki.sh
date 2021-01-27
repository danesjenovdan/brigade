#!/bin/bash

# set execution so we fail the script when a command fials
# set -Eeuo pipefail

host="localhost"

for user in "$@"
do
    echo "Scraping $user"
    # ONLY NATIVE RETWEETS
    twint -u $user --since "2019-12-31" --native-retweets --index-tweets=twint_politiki_tweets --elasticsearch="$host:9200"
    # ONLY RETWEETS
    twint -u $user --since "2019-12-31" --retweets --index-tweets=twint_politiki_tweets --elasticsearch="$host:9200"
    # ALL
    twint -u $user --since "2019-12-31" --timeline --index-tweets=twint_politiki_tweets --elasticsearch="$host:9200"
    # REGULAR
    twint -u $user --since "2019-12-31" --index-tweets=twint_politiki_tweets --elasticsearch="$host:9200"
done
