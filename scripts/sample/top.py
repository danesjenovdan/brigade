import json
from collections import Counter

from operator import itemgetter
import heapq
def least_common_values(counter, to_find=None):
    if to_find is None:
        return sorted(counter.items(), key=itemgetter(1), reverse=False)
    return heapq.nsmallest(to_find, counter.items(), key=itemgetter(1))


with open('../hashtags_sample.txt') as infile:
    hashtags = Counter(json.load(infile))
    print(hashtags.most_common(50))
    print('\n\n')
    print(least_common_values(hashtags)[:50])
