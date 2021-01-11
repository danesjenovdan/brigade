#!/bin/bash

# set execution so we fail the script when a command fials
# set -Eeuo pipefail

for user in "$@"
do
    echo "Scraping $user"
    twint -u $user --since "2019-10-01" --index-tweets=twint_sample_tweets --elasticsearch=51.15.239.174:9200
done
