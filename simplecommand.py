from netmiko import ConnectHandler


# A simple intro to netmiko
# https://github.com/ktbyers/netmiko

# https://pynet.twb-tech.com/blog/automation/netmiko.html

# set credentials for device
host = '10.10.20.58'
user = 'admin'
password = 'cisco123'
device_type = 'cisco_nxos'

# construct a device definition
device = {"device_type": 'cisco_nxos',
          "ip": host,
          "username": user,
          "password": password,
          }

# command we would like to run
command = 'show version'
session = ConnectHandler(**device)
output = session.send_command(command)
print(output)