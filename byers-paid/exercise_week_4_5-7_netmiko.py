#!/usr/bin/env python
'''
5. Use Netmiko to enter into configuration mode on pynet-rtr2. Also use Netmiko to verify your state (i.e. that you are currently in configuration mode).

 
6. Use Netmiko to execute 'show arp' on pynet-rtr1, pynet-rtr2, and juniper-srx.

 
7. Use Netmiko to change the logging buffer size (logging buffered <size>) on pynet-rtr2.
'''

from netmiko import ConnectHandler
from getpass import getpass
password = getpass()

pynet1 = {
	'device_type': 'cisco_ios',
	'ip': '50.76.53.27',
	'username': 'pyclass',
	'password': password,
}

pynet2 = {
	'device_type': 'cisco_ios',
	'ip': '50.76.53.27',
	'username': 'pyclass',
	'password': password,
	'port': 8022,
}

juniper_srx = {
	'device_type': 'juniper',
	'ip': '50.76.53.27',
	'username': 'pyclass',
	'password': password,
	'secret': '',
	'port': 9822,
}

pynet_rtr1 = ConnectHandler(**pynet1) #passes this dictionary and key values as arguments into the connect handler

print pynet_rtr1.find_prompt()

pynet_rtr1.config_mode()
print pynet_rtr1.check_config_mode()
print pynet_rtr1.find_prompt()
pynet_rtr1.exit_config_mode()
print pynet_rtr1.find_prompt()
print 'so concludes exercise 5'

print '\n\n\n here begins exercise 6'
pynet_rtr1 = ConnectHandler(**pynet1) #passes this dictionary and key values as arguments into the connect handler
pynet_rtr2 = ConnectHandler(**pynet2) #passes this dictionary and key values as arguments into the connect handler
srx = ConnectHandler(**juniper_srx) #passes this dictionary and key values as arguments into the connect handler

rtr1_arp = pynet_rtr1.send_command("show arp")
rtr2_arp = pynet_rtr2.send_command("show arp")
srx_arp = srx.send_command("show arp")

print "here's the router 1 arp:\n",rtr1_arp
print "\n\n here's the router 2 arp:\n",rtr2_arp
print "\n\n here's the SRX' arp:\n",srx_arp
print "\nso concludes exercise 6"

print "\n\nhere begins exercise 7"
pynet_rtr2.config_mode()
print pynet_rtr2.find_prompt()
pynet_rtr2.send_command("logging buffered 9000")
pynet_rtr2.exit_config_mode()
print pynet_rtr2.send_command("show run | in buffered")

print "\n here ends exercise 7...go to the other file for exercises 8/9"
