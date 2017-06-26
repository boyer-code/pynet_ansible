#!/usr/bin/env python
'''
1. Use Paramiko to retrieve the entire 'show version' sh_verut from pynet-rtr2. 

 
2. Use Paramiko to change the 'logging buffered <size>' configuration on pynet-rtr2. This will require that you enter into configuration mode.
'''

import paramiko
from getpass import getpass
import time

ip_addr = '50.76.53.27'
username = 'pyclass'
port = 8022
password = getpass() #requests user input for password and hides it

remote_conn_pre = paramiko.SSHClient()
remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy()) #tells it to auto add keys...kinda dangerous, but will get a known_hosts error without it

remote_conn_pre.connect(ip_addr, username=username, password=password, look_for_keys=False, allow_agent=False, port=port) #here's where we actually connect
remote_conn = remote_conn_pre.invoke_shell() #needed

sh_ver = remote_conn.recv(5000) #receive up to 5000 bytes

remote_conn.send("term len 0\n")
time.sleep(2) #wait 2 seconds
sh_ver = remote_conn.recv(100) #clear the term len 0 portion of the buffer
remote_conn.send("show ver\n") #sends our command and returns how many bytes it sent
time.sleep(2)
sh_ver = remote_conn.recv(5000) #receive up to 5000 bytes

print sh_ver #should return results of show ip int br now
print '\n\nthat was question 1...below is question 2\n\n'
####

remote_conn.send("show run | in logging\n")
time.sleep(2) #wait 2 seconds
logging_buff = remote_conn.recv(5000) #clear the term len 0 portion of the buffer
print logging_buff, "is what we have right now"
remote_conn.send("conf t\n") #sends our command and returns how many bytes it sent
remote_conn.send("logging buffered 5879\n")
remote_conn.send("end\n")
time.sleep(2)
remote_conn.send("show run | in logging\n")
time.sleep(1)
logging_buff = remote_conn.recv(5000) #clear the term len 0 portion of the buffer
print logging_buff
