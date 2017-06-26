#!/usr/bin/env python
'''
2. Using Arista's pyeapi, create a script that allows you to add a VLAN (both the VLAN ID and the VLAN name).  

Your script should first check that the VLAN ID is available and only add the VLAN if it doesn't already exist.  Use VLAN IDs between 100 and 999.  You should be able to call the script from the command line as follows:

   python eapi_vlan.py --name blue 100     # add VLAN100, name blue

If you call the script with the --remove option, the VLAN will be removed.

   python eapi_vlan.py --remove 100          # remove VLAN100

Once again only remove the VLAN if it exists on the switch.  You will probably want to use Python's argparse to accomplish the argument processing.

'''
import pyeapi
from pprint import pprint 
import argparse

# Argument parsing
parser = argparse.ArgumentParser(description="addition/removal of VLAN to Arista switch")
parser.add_argument("vlan_id", help="VLAN number to create or remove", action="store", type=int)
parser.add_argument("--name",help="Specify VLAN name",action="store",dest="vlan_name",type=str)
parser.add_argument("--remove", help="Remove the given VLAN ID", action="store_true")

cli_args = parser.parse_args()
vlan_id = cli_args.vlan_id
vlan_id = int(vlan_id)
remove = cli_args.remove
vlan_name = cli_args.vlan_name

pynet_sw2 = pyeapi.connect_to("pynet-sw2") #this name is from the config file

output = pynet_sw2.enable("show vlan") #the .enable indicates it's going to run it as enable mode...only looking for commands

def pyeapi_result(output):
    '''
    Return the 'result' value from the pyeapi output
    '''
    return output[0]['result']

s_v = pyeapi_result(output)

#this strips the returned data to JUST the vlans
s_v = s_v['vlans']
vlan_exists = False
cmds = []

#this iterates through the list of VLANs for our VLAN we specified to remove, and sets remove_the_vlan from False to True if it's there
for k,v in s_v.items():
    k = int(k)
    if k == vlan_id:
    	vlan_exists = True

vlan_id = str(vlan_id)
#update our command list (command) with removing the VLAN if it needs to go
if remove:
	if vlan_exists == True:
		temp_str = 'no vlan '+ vlan_id
		cmds = [temp_str]
	else:
		print "the VLAN doesn't exist, can't delete it"
else: #otherwise check to see if it exists and don't add it or add it if it's not there
	if vlan_exists == True:
		print "the VLAN already exists, we can't create it"
	else:
		id_str = 'vlan '+ vlan_id
		name_str = 'name '+ vlan_name
		cmds = [id_str,name_str]


#issue our commands
pynet_sw2.config(cmds)
#write mem after done
pynet_sw2.enable("write memory")
