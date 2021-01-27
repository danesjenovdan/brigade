with open('../people/user_info.txt') as infile:
    with open('../people/joined_timestamps.tsv', 'w') as outfile:
        for line in infile.readlines():
            joined_time = line.split('Joined: ')[-1].split(' UTC')[0]
            username = line.split(' | ')[2][1:]
            outfile.write(f'{username}\t{joined_time}\n')
