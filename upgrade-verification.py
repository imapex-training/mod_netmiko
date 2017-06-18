import yaml

with open('upgrade-config.yaml') as fh:
    config = yaml.load(fh)

def run_commands(switch, username, password, commands):
    """
    This is a boilerplate function, please update with your code, as well as updating these docstrings.

    :param switch: string containing the ip address of the switches that commands should be run on
    :param username: string username to login to the switch
    :param password: string password to login to the switch
    :param commands: list containing strings, each representing a valid command

    :return: string
    """

    result = ""

    # Do your magic here

    return result

username = config['username']
password = config['password']
switches = config['switches']
commands = config['commands']


for s in switches:
    print s
    print "=" * 80
    for c in commands:
        print c
        print '-' * 80
