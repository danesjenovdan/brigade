from time import sleep
import twint

def get_group(group_name):
    with open(f'../people/{group_name}.txt', 'r') as infile:
        for line in infile.readlines():
            username = line.strip()
            get_person(username)
            sleep(5)

def get_person(username):
    c = twint.Config()
    c.Username = username

    try:
        success = twint.run.Lookup(c)
    except:
        success = f'ERROR {username}'
    if success:
        print(success)

# get_group('politiki')
# get_group('sample')
# get_group('brigade')
# get_group('v2_errored')
get_group('trolls')