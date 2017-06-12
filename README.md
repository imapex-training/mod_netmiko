
You can view this content in slideshow format at:

https://rawgit.com/imapex-training/mod_netmiko/master/slides/index.html#/

[item]: # (slide)

![](http://imapex.io/images/imapex_standing_text_sm.png)

### Module: Netmiko Introdution

[item]: # (/slide)



While having proper API access to a device is important, the reality is that a lot of legacy networking gear
will not have this capability.  That shouldn't stop us from thinking about operating infrastructure in a
programmatic way.  We can use the [netmiko library](https://github.com/ktbyers/netmiko) to automate tasks that
are normally accomplished via ssh.

The purpose of this repository is to provide an introduction to using this library, based largely upon
[this tutorial](https://pynet.twb-tech.com/blog/automation/netmiko.html)

All credit/props to Kirk Byers (@ktbyers) for his great work on this library


[item]: # (slide)

## Table Of Contents

* [About Netmiko](#about-netmiko)
* [Installing Netmiko](#installing-netmiko)
* [Define Device Variables](#define-device-variables)
* [Construct a Device Definition Dictionary](#construct-a-device-definition-dictionary)
* [define command we would like to run](#define-command-we-would-like-to-run)
* [initiate ssh connection to device](#initiate-ssh-connection-to-device)
* [execute command](#execute-command)
* [challenge](#challenge)

[item]: # (/slide)

[item]: # (slide)

#### About Netmiko

* open-source Python library that simplifies SSH management to network devices
* based on the Paramiko SSH library

#### Provides the following capabilities
* establish an SSH connection to the device
* Simplify the execution of show commands and the retrieval of output data
* Simplify execution of configuration commands including possibly commit actions
* Do the above across a broad set of networking vendors and platforms


[item]: # (/slide)

[item]: # (slide)

## Netmiko Device types

Netmiko handles low level ssh management by customing things like login, password, and shell prompts through
the use of device

[item]: # (/slide)

[item]: # (slide)

###### Regularly tested device types

* Arista vEOS
* Cisco ASA
* Cisco IOS
* Cisco IOS-XE
* Cisco IOS-XR
* Cisco NX-OS
* Cisco SG300
* HP Comware7
* HP ProCurve
* Juniper Junos
* Linux

[table of contents](#table-of-contents)
[item]: # (/slide)

[item]: # (slide)

###### Limited testing device types

* Alcatel AOS6/AOS8
* Avaya ERS
* Avaya VSP
* Brocade VDX
* Brocade ICX/FastIron
* Brocade MLX/NetIron
* Cisco WLC
* Dell-Force10 DNOS9
* Dell PowerConnect
* Huawei
* Mellanox
* Palo Alto PAN-OS
* Pluribus
* Vyatta VyOS
[table of contents](#table-of-contents)

[item]: # (/slide)

[item]: # (slide)

###### Experimental Device Types

* A10
* Alcatel-Lucent SR-OS
* Ciena SAOS
* Cisco Telepresence
* CheckPoint Gaia
* Enterasys
* Extreme EXOS
* Extreme Wing
* F5 LTM
* Fortinet

[table of contents](#table-of-contents)

[item]: # (/slide)

[item]: # (slide)

## Installing Netmiko


Installation of netmiko is accomplished via pip, preferably in a virtualenv.

```
virtualenv venv
source venv/bin/activate
pip install netmiko
```

[table of contents](#table-of-contents)

[item]: # (/slide)

[item]: # (slide)


# Getting Started

The remainder of this tutorial will demonstrate netmiko functionality using the Open NX-OS with Nexus 9K
sandbox from devnet, which are available on-demand at https://devnetsandbox.cisco.com/RM/Topology

[table of contents](#table-of-contents)

[item]: # (/slide)

[item]: # (slide)

#### define device variables

```
host = '10.10.20.58'
user = 'admin'
password = 'cisco123'
device_type = 'cisco_nxos'

```
[table of contents](#table-of-contents)

[item]: # (/slide)



[item]: # (slide)

#### construct a device definition dictionary
```
device = {"device_type": 'cisco_nxos',
          "ip": host,
          "username": user,
          "password": password,
          }

```
[table of contents](#table-of-contents)

[item]: # (/slide)

[item]: # (slide)

#### define command we would like to run
```
command = 'show version'

```
[table of contents](#table-of-contents)

[item]: # (/slide)


[item]: # (slide)

#### initiate ssh connection to device

```
session = ConnectHandler(**device)

```

[table of contents](#table-of-contents)

[item]: # (/slide)


[item]: # (slide)

#### execute command

```
output = session.send_command(command)
print(output)

```
[table of contents](#table-of-contents)

[item]: # (/slide)


[item]: # (slide)

#### challenge

Create a function that meets the following requirements

* Takes as input a list of devices
* Takes as input a list of commands
* Displays the result of each command on each device

[table of contents](#table-of-contents)

[item]: # (/slide)
