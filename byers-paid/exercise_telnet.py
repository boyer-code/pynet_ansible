#!/usr/bin/env python

'''
2. telnetlib
    a. Write a script that connects using telnet to the pynet-rtr1 router. Execute the 'show ip int brief' command on the router and return the output.

Try to do this on your own (i.e. do not copy what I did previously). You should be able to do this by using the following items:

telnetlib.Telnet(ip_addr, TELNET_PORT, TELNET_TIMEOUT)
remote_conn.read_until(<string_pattern>, TELNET_TIMEOUT)
remote_conn.read_very_eager()
remote_conn.write(<command> + '\n')
remote_conn.close()


username = 'pyclass'
password = '88newclass'
IP address = 50.76.53.27
pynet-rtr1 (Cisco 881) snmp_port=7961, ssh_port=22
'''

import telnetlib

ip_addr = '50.76.53.27'
username = 'pyclass'
password = '88newclass'
TELNET_PORT = 23
TELNET_TIMEOUT = 10

conn = telnetlib.Telnet(ip_addr, TELNET_PORT, TELNET_TIMEOUT)

login = conn.read_until('ser:', TELNET_TIMEOUT)
login = conn.write(username + '\n')
login = conn.read_until('ssword:', TELNET_TIMEOUT)
login += conn.write(password + '\n')
print login

login = conn.write('term len 0' + '\n')
login = conn.write('show ip int brief' + '\n')
login = conn.read_very_eager()
print login
