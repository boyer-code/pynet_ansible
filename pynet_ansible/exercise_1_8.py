#!/usr/bin/env python

#8. Write a Python program using ciscoconfparse that parses cisco_crypto.txt. Note, this config file is not fully valid (i.e. parts of the configuration are missing). The script should find all of the crypto map entries in the file (lines that begin with 'crypto map CRYPTO') and for each crypto map entry print out its children.

from ciscoconfparse import CiscoConfParse

cisco_cfg = CiscoConfParse("cisco_crypto.txt")
crypto_cfg = cisco_cfg.find_objects(r"^crypto map CRYPTO")

for line in crypto_cfg:
    print line.text
    for kids in line.children:
        print kids.text
    print


