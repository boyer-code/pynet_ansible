#!/usr/bin/env python

'''
Create a script that connects to both routers (pynet-rtr1 and pynet-rtr2) and prints out both the MIB2 sysName and sysDescr.
'''

from snmp_helper import snmp_get_oid,snmp_extract

community_string = 'galileo'
ip = '50.76.53.27'
pynet_rtr1_snmp_port = 7961
pynet_rtr2_snmp_port = 8061

pynet_rtr1 = (ip, community_string, pynet_rtr1_snmp_port)
pynet_rtr2 = (ip, community_string, pynet_rtr2_snmp_port)

sysName = '1.3.6.1.2.1.1.5.0'
sysDescr = '1.3.6.1.2.1.1.1.0'

rtr1_sysName = snmp_get_oid(pynet_rtr1, oid=sysName)
rtr2_sysName = snmp_get_oid(pynet_rtr2, oid=sysName)

rtr1_sysDescr = snmp_get_oid(pynet_rtr1, oid=sysDescr)
rtr2_sysDescr = snmp_get_oid(pynet_rtr2, oid=sysDescr)

rtr1_sysName = snmp_extract(rtr1_sysName)
rtr2_sysName = snmp_extract(rtr2_sysName)

rtr1_sysDescr = snmp_extract(rtr1_sysDescr)
rtr2_sysDescr = snmp_extract(rtr2_sysDescr)

print "rtr1\'s Sysname is: %s \n\nthe sysDescr for it is: %s\n\n" % (rtr1_sysName,rtr1_sysDescr)
print "rtr2\'s Sysname is: %s \n\nthe sysDescr for it is: %s\n\n" % (rtr2_sysName,rtr2_sysDescr)
