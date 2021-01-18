import csv
from datetime import datetime, timedelta
import pytz

CET = pytz.timezone('CET')
UTC = pytz.timezone('UTC')

time_format = '%Y-%m-%dT%H:%M:%S'

def datetime_range(start, end, delta):
    current = start
    while current < end:
        yield current
        current += delta

def get_intervals_from_csv(filename):
    with open(filename, 'r') as infile:
        reader = csv.reader(infile, quotechar='"', delimiter=',')
        timestamp_index = 9 if filename == 'ros.csv' else 10
        times = sorted([datetime.strptime(row[timestamp_index].split('+00')[0], time_format).replace(tzinfo=UTC) for row in reader])

        start = times[0].replace(minute=0, second=0)
        end = (times[-1] + timedelta(hours=1)).replace(minute=0, second=0)

        # generate interval beginnings and set index to 0
        interval_starts = list(datetime_range(start, end, timedelta(hours=1)))
        interval_index = 0

        # create first interval
        intervals = {
            interval_starts[interval_index].strftime(time_format): 0
        }

        # iterate over all tweet times
        for t in times:
            # tweet is within interval
            if (interval_starts[interval_index] + timedelta(hours=1)) > t:
                # increment interval
                intervals[interval_starts[interval_index].strftime(time_format)] += 1

            # tweet is out of interval
            else:
                # increment interval index to next appropriate interval
                # generate interval in the dictionary to keep zeros
                while (interval_starts[interval_index] + timedelta(hours=1)) < t:
                    interval_index += 1
                    intervals[interval_starts[interval_index].strftime(time_format)] = 0

                # increment interval
                intervals[interval_starts[interval_index].strftime(time_format)] += 1
        
        return intervals

# intervals = get_intervals_from_csv('knafelj.csv')

# for key in intervals.keys():
#     print(f'{datetime.strptime(key, time_format).replace(tzinfo=UTC).astimezone(CET).strftime("%d. %m. %Y - %H:%M:%S")}   {intervals[key]}')

# print('\n##############################\n')
# print(f'TOTAL:                    {sum(intervals.values())}')

people = [
    'damijan',
    'gale',
    'jenull',
    'knafelj',
    'magnifico',
    'ros',
    'znidarsic'
]

for person in people:
    print(f'Handling {person}')
    intervals = get_intervals_from_csv(f'{person}.csv')
    with open(f'{person}_hourly.tsv', 'w') as outfile:
        for key in intervals.keys():
            slovenian_time = datetime.strptime(key, time_format).replace(tzinfo=UTC).astimezone(CET)
            outfile.write(f'{slovenian_time.strftime(time_format)}\t{intervals[key]}\n')
