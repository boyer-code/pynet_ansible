#!/usr/bin/env python

'''
1. Using SNMPv3 create a script that detects router configuration changes.

If the running configuration has changed, then send an email notification to yourself identifying the router that changed and the time that it changed.

Note, the running configuration of pynet-rtr2 is changing every 15 minutes (roughly at 0, 15, 30, and 45 minutes after the hour).  
This will allow you to test your script in the lab environment. 

In this exercise, you will possibly need to save data to an external file. One way you can accomplish this is by using a pickle file, see:  
    http://youtu.be/ZJOJjyhhEvM  

A pickle file lets you save native Python data structures (dictionaries, lists, objects) directly to a file.

Here is some additional reference material that you will probably need to solve this problem:

Cisco routers have the following three OIDs:
# Uptime when running config last changed
ccmHistoryRunningLastChanged = '1.3.6.1.4.1.9.9.43.1.1.1.0'   

# Uptime when running config last saved (note any 'write' constitutes a save)    
ccmHistoryRunningLastSaved = '1.3.6.1.4.1.9.9.43.1.1.2.0'   

# Uptime when startup config last saved   
ccmHistoryStartupLastChanged = '1.3.6.1.4.1.9.9.43.1.1.3.0'

From the above descriptions, the router will save the sysUptime timestamp (OID sysUptime = 1.3.6.1.2.1.1.3.0) when a running configuration change occurs. 
The router will also record the sysUptime timestamp when the running configuration is saved to the startup config.

Here is some data on the behavior of these OIDs. Note, sysUptime times are in hundredths of seconds so 317579 equals 3175.79 seconds (i.e. a bit less than one hour)

# After reboot
pynet-rtr2.twb-tech.com
317579        (sysUptime)
2440            (ccmHistoryRunningLastChanged--running-config is changed during boot)
0                  (ccmHistoryRunningLastSaved -- i.e. reset to 0 on reload)
0                  (ccmHistoryStartupLastChanged -- i.e. reset to 0 on reload)

# After config change on router (but no save to startup config)
pynet-rtr2.twb-tech.com
322522        (sysUptime)
322219        (ccmHistoryRunningLastChanged)
0                  (ccmHistoryRunningLastSaved)
0                  (ccmHistoryStartupLastChanged)

# After 'write mem' on router
pynet-rtr2.twb-tech.com
324543        (sysUptime)
322219        (ccmHistoryRunningLastChanged)
323912        (ccmHistoryRunningLastSaved)
323912        (ccmHistoryStartupLastChanged)

# After another configuration change (but no save to startup config)
pynet-rtr2.twb-tech.com
327177        (sysUptime)
326813        (ccmHistoryRunningLastChanged)
323912        (ccmHistoryRunningLastSaved)
323912        (ccmHistoryStartupLastChanged)

# After 'show run' command (note, this causes 'ccmHistoryRunningLastSaved' to 
# increase i.e. 'write terminal' causes this OID to be updated)
pynet-rtr2.twb-tech.com
343223        (sysUptime)
326813        (ccmHistoryRunningLastChanged)
342898        (ccmHistoryRunningLastSaved)
323912        (ccmHistoryStartupLastChanged)


Bonus challenge: instead of saving your data in a pickle file, save the data using either a YAML or a JSON file. 

My alternate solution supports pickle, YAML, or JSON depending on the name of the file (.pkl, .yml, or .json).
'''

import email_helper
import snmp_helper
import time
import pickle

IP = '50.76.53.27'
a_user = 'pysnmp'
auth_key = 'galileo1'
encrypt_key = 'galileo1'
snmp_user = (a_user, auth_key, encrypt_key)
pynet_rtr1 = (IP, 7961)
pynet_rtr2 = (IP, 8061)

#grab our SNMP info in an ugly format
uptime = snmp_helper.snmp_get_oid_v3(pynet_rtr2, snmp_user, oid='1.3.6.1.2.1.1.3.0')
runninglastchanged = snmp_helper.snmp_get_oid_v3(pynet_rtr2, snmp_user, oid='1.3.6.1.4.1.9.9.43.1.1.1.0')
runninglastsaved = snmp_helper.snmp_get_oid_v3(pynet_rtr2, snmp_user, oid='1.3.6.1.4.1.9.9.43.1.1.2.0')
startlastchanged = snmp_helper.snmp_get_oid_v3(pynet_rtr2, snmp_user, oid='1.3.6.1.4.1.9.9.43.1.1.3.0')
#the below extracts it into something a little more legibile
uptime = snmp_helper.snmp_extract(uptime)
runninglastchanged = snmp_helper.snmp_extract(runninglastchanged)
runninglastsaved = snmp_helper.snmp_extract(runninglastsaved)
startlastchanged = snmp_helper.snmp_extract(startlastchanged)

file_read = open("storage.pkl", "rb")
check_runningchanged = pickle.load(file_read)
check_runningsaved = pickle.load(file_read)
check_startchanged = pickle.load(file_read)
file_read.close()

file_opened = open("storage.pkl", "wb")
pickle.dump(runninglastchanged, file_opened)
pickle.dump(runninglastsaved, file_opened)
pickle.dump(startlastchanged, file_opened)
file_opened.close()


def convert_to_time(change_me):
	'''this will attempt to take our time change and convert it to a float, then convert the microsecond value to a time in minutes'''
	try:
		change_me = float(change_me)
		change_me = (change_me*.01)/60
		return change_me
	except:
		print 'something went horribly wrong'

if check_runningchanged >= runninglastchanged:
	runninglastchanged = check_runningchanged
	timestamp = convert_to_time(uptime) - convert_to_time(runninglastchanged)
	recipient = 'joey@networkbit.com'
	subject = 'Pynet status change' #could use some logic to enter device name here if we rewrote some of the above
	message = '''
	
	Something changed on the configuration of rtr2 %s minutes ago!
	
	''' % timestamp
	
	sender = 'joey@theboyers.org'
	email_helper.send_mail(recipient, subject, message, sender)
	
if check_runningsaved >= runninglastsaved:
	runninglastsaved = check_runningsaved
	timestamp = convert_to_time(uptime) - convert_to_time(runninglastsaved)
	recipient = 'joey@networkbit.com'
	subject = 'Pynet status change' #could use some logic to enter device name here if we rewrote some of the above
	message = '''
	
	Something changed on the configuration of rtr2 %s minutes ago!
	
	''' % timestamp
	
	sender = 'joey@theboyers.org'
	email_helper.send_mail(recipient, subject, message, sender)
	
if check_startchanged >= startlastchanged:
	startlastchanged = check_startchanged
	timestamp = convert_to_time(uptime) - convert_to_time(startlastchanged)
	recipient = 'joey@networkbit.com'
	subject = 'Pynet status change' #could use some logic to enter device name here if we rewrote some of the above
	message = '''
	
	Something changed on the configuration of rtr2 %s minutes ago!
	
	''' % timestamp
	
	sender = 'joey@theboyers.org'
	email_helper.send_mail(recipient, subject, message, sender)

