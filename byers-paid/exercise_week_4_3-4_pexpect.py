#!/usr/bin/env python
'''
3. Use Pexpect to retrieve the output of 'show ip int brief' from pynet-rtr2.

 
4. Use PExpect to change the logging buffer size (logging buffered <size>) on pynet-rtr2. Verify this change by examining the output of 'show run'.
'''

import pexpect
import sys
import time
from getpass import getpass

ip_addr = '50.76.53.27'
username = 'pyclass'
port = 8022
password = getpass()

#ssh -l pyclass 50.76.53.27 -p 8022
ssh_conn = pexpect.spawn('ssh -l {} {} -p {}'.format(username, ip_addr, port)) #spawns child process for ssh
ssh_conn.logfile = sys.stdout #prints output to stdout
ssh_conn.timeout = 3
ssh_conn.expect('ssword:') #looking for something that says ssword:

ssh_conn.sendline(password) #then send the password
ssh_conn.expect('#') #look for a #

router_name = ssh_conn.before #print what we saw before the # (so between the two expects)
router_name = router_name.strip()
print router_name

ssh_conn.sendline("show ip int br") #auto sends \n so no need to add
print ssh_conn.before #will show you everything from show ip int brief up to the #

print '\n\n\n\n\n\n\n\n\n\nnow for the next example'
ssh_conn.expect('#') #look for a #
ssh_conn.sendline("conf t")
ssh_conn.sendline("logging buffered 6000")
time.sleep(1)
ssh_conn.expect("#")
ssh_conn.sendline("end")
time.sleep(1)
ssh_conn.sendline("term len 0")
ssh_conn.expect('#') #look for a #
time.sleep(1)
ssh_conn.sendline("show run | in buffered")
print '\n\n'
print ssh_conn.before
