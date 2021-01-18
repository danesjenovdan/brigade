#!/bin/bash

# set execution so we fail the script when a command fials
# set -Eeuo pipefail

host="localhost"

for user in "$@"
do
    echo "Scraping $user"
    # ONLY RETWEETS
    twint -u $user --since "2019-10-01" --native-retweets --index-tweets=twint_sample_tweets --elasticsearch="$host:9200"
    # ALL
    twint -u $user --since "2019-10-01" --timeline --index-tweets=twint_sample_tweets --elasticsearch="$host:9200"
    # REGULAR
    twint -u $user --since "2019-10-01" --index-tweets=twint_sample_tweets --elasticsearch="$host:9200"
done
