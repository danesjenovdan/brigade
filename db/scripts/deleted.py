import re

def count_deleted(filename):
    current_username = ''
    deleted = 0
    with open(filename, 'r') as infile:
        with open('politiki_deleted.tsv', 'w') as outfile:
            for line in infile.readlines():
                if re.match(r'^Scraping.*', line):
                    new_username = line.split('Scraping ')[-1].strip()
                if current_username != new_username:
                    print(f'{deleted} deleted tweets for {current_username}')
                    outfile.write(f'{current_username}\t{deleted}\n')

                    current_username = new_username
                    deleted = 0
                    print(f'Counting {current_username}')
                elif re.match(r'found \d+ deleted tweets in this search\.', line):
                    deleted = max(deleted, int(line.split('found ')[-1].split(' ')[0]))
                    # deleted += int(line.split('found ')[-1].split(' ')[0])
            print(f'{deleted} deleted tweets for {current_username}')


count_deleted('log/politiki.log')
