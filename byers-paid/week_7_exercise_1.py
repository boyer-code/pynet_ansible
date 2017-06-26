#!/usr/bin/env python

#1. Use Arista's eAPI to obtain 'show interfaces' from the switch. Parse the 'show interfaces' output to obtain the 'inOctets' and 'outOctets' fields for each of the interfaces on the switch.  Accomplish this using Arista's pyeapi.

import pyeapi
from pprint import pprint 

pynet_sw2 = pyeapi.connect_to("pynet-sw2") #this name is from the config file

output = pynet_sw2.enable("show interfaces") #the .enable indicates it's going to run it as enable mode...only looking for commands

def pyeapi_result(output):
    '''
    Return the 'result' value from the pyeapi output
    '''
    return output[0]['result']

s_i = pyeapi_result(output)

s_i = s_i['interfaces']

for k,v in s_i.items():
	try:
		inOct = v['interfaceCounters']['inOctets']
		outOct = v['interfaceCounters']['outOctets']
		print k,'\ninOctets:  ' ,inOct,'\noutOctets: ' ,outOct,'\n'
	except:
		print 'no counters on: ' + k
