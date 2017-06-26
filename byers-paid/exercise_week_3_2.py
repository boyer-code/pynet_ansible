#!/usr/bin/env python

'''
2. Using SNMPv3 create two SVG image files.  

The first image file should graph the input and output octets on interface FA4 on pynet-rtr1 every five minutes for an hour.  Use the pygal library to create the SVG graph file. 
Note, you should be doing a subtraction here (i.e. the input/output octets transmitted during this five minute interval).  

The second SVG graph file should be the same as the first except graph the unicast packets received and transmitted.

The relevant OIDs are as follows:

('ifDescr_fa4', '1.3.6.1.2.1.2.2.1.2.5')
('ifInOctets_fa4', '1.3.6.1.2.1.2.2.1.10.5')
('ifInUcastPkts_fa4', '1.3.6.1.2.1.2.2.1.11.5')
('ifOutOctets_fa4', '1.3.6.1.2.1.2.2.1.16.5'),
('ifOutUcastPkts_fa4', '1.3.6.1.2.1.2.2.1.17.5')


Note, you should be able to scp (secure copy) your image file off the lab server. You can then open up the file using a browser.  For example, on MacOs I did the following (from the MacOs terminal):

scp kbyers@<hostname>:SNMP/class2/test.svg .

This copied the file from ~kbyers/SNMP/class2/test.svg to the current directory on my MAC.  

The format of the command is:

scp <remote-username>@<remote-hostname>:<remote_path>/<remote_file> .

The period at the end indicates the file should be copied to the current directory on the local machine.
'''
import pygal
import snmp_helper
import time

IP = '50.76.53.27'
a_user = 'pysnmp'
auth_key = 'galileo1'
encrypt_key = 'galileo1'
snmp_user = (a_user, auth_key, encrypt_key)
pynet_rtr1 = (IP, 7961)
pynet_rtr2 = (IP, 8061)
fa4_in_octets_list = []
fa4_out_octets_list = []
fa4_in_packets_list = []
fa4_out_packets_list = []

x = 40

while x < 65:
	fa4_in_octets = snmp_helper.snmp_get_oid_v3(pynet_rtr1, snmp_user, oid='1.3.6.1.2.1.2.2.1.10.5')
	fa4_out_octets = snmp_helper.snmp_get_oid_v3(pynet_rtr1, snmp_user, oid='1.3.6.1.2.1.2.2.1.16.5')
	#
	fa4_in_octets = snmp_helper.snmp_extract(fa4_in_octets)
	fa4_out_octets = snmp_helper.snmp_extract(fa4_out_octets)
	#
	fa4_in_octets_list.append(int(fa4_in_octets))
	fa4_out_octets_list.append(int(fa4_out_octets))
	#
	fa4_in_packets = snmp_helper.snmp_get_oid_v3(pynet_rtr1, snmp_user, oid='1.3.6.1.2.1.2.2.1.11.5')
	fa4_out_packets = snmp_helper.snmp_get_oid_v3(pynet_rtr1, snmp_user, oid='1.3.6.1.2.1.2.2.1.17.5')
	#
	fa4_in_packets = snmp_helper.snmp_extract(fa4_in_packets)
	fa4_out_packets = snmp_helper.snmp_extract(fa4_out_packets)
	#
	fa4_in_packets_list.append(int(fa4_in_packets))
	fa4_out_packets_list.append(int(fa4_out_packets))
	#
	x +=5
	print x
	time.sleep(10)
'''
#fa4_in_octets_list[::-1]
#fa4_out_octets_list[::-1]

chart_octets_in = []
chart_octets_out = []
chart_packets_in = []
chart_packets_out = []

for i in fa4_in_octets_list:
	temp = fa4_in_octets_list[0]
	chart_octets_in.append(i - temp)

for i in fa4_out_octets_list:
	temp = fa4_out_octets_list[0]
	chart_octets_out.append(i - temp)

for i in fa4_in_packets_list:
	temp = fa4_in_packets_list[0]
	chart_packets_in.append(i - temp)

for i in fa4_out_packets_list:
	temp = fa4_out_packets_list[0]
	chart_packets_out.append(i - temp)
'''

# Create a Chart of type Line
line_chart = pygal.Line()

# Title
line_chart.title = 'Input/Output Packets and Bytes'

# X-axis labels (samples were every five minutes)
line_chart.x_labels = ['5', '10', '15', '20', '25', '30', '35', '40', '45', '50', '55', '60']

# Add each one of the above lists into the graph as a line with corresponding label
line_chart.add('InPackets', fa4_in_packets_list)
line_chart.add('OutPackets',  fa4_out_packets_list)
line_chart.add('InBytes', fa4_out_octets_list)
line_chart.add('OutBytes', fa4_in_octets_list)

# Create an output image file from this
line_chart.render_to_file('test.svg')
