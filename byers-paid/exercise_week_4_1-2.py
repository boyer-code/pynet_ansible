#!/usr/bin/env python
'''
1. Use Paramiko to retrieve the entire 'show version' output from pynet-rtr2. 

 
2. Use Paramiko to change the 'logging buffered <size>' configuration on pynet-rtr2. This will require that you enter into configuration mode.
'''

import paramiko
from getpass import getpass

ip_addr = '50.76.53.27'
username = 'pyclass'
port = 8022
password = getpass() #requests user input for password and hides it

remote_conn_pre = paramiko.SSHClient()
remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy()) #tells it to auto add keys...kinda dangerous, but will get a known_hosts error without it

remote_conn_pre.connect(ip_addr, username=username, password=password, look_for_keys=False, allow_agent=False, port=port) #here's where we actually connect
remote_conn = remote_conn_pre.invoke_shell() #needed

outp = remote_conn.recv(5000) #receive up to 5000 bytes

print outp #should return router prompt at this point

remote_conn.send("show ip int br\n") #sends our command and returns how many bytes it sent

outp = remote_conn.recv(5000) #receive up to 5000 bytes

print outp #should return results of show ip int br now
