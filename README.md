
You can view this content in slideshow format at:

https://rawgit.com/imapex-training/mod_netmiko/master/slides/index.html#/

# netmiko-intro


While having proper API access to a device is important, the reality is that a lot of legacy networking gear
will not have this capability.  That shouldn't stop us from thinking about operating infrastructure in a
programmatic way.  We can use the [netmiko library](https://github.com/ktbyers/netmiko) to automate tasks that
are normally accomplished via ssh.

The purpose of this repository is to provide an introduction to using this library, based largely upon
[this tutorial](https://pynet.twb-tech.com/blog/automation/netmiko.html)

All credit/props to Kirk Byers (@ktbyers) for his great work on this library


# Install Netmiko


Installation of netmiko is accomplished via pip, preferably in a virtualenv.

```
virtualenv venv
source venv/bin/activate
pip install netmiko
```


# Getting Started



