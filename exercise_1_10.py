#!/usr/bin/env python

#9 Find all of the crypto map entries that are using PFS group2

from ciscoconfparse import CiscoConfParse

cisco_cfg = CiscoConfParse("cisco_crypto.txt")
#crypto_cfg = cisco_cfg.find_objects(r"^crypto map CRYPTO")
#cisco_cfg.find_objects_w_child(parentspec=r"^interface", childspec=r"no ip address")
group_2_crypto = cisco_cfg.find_objects_w_child(parentspec=r"^crypto map CRYPTO", childspec=r"group2")

print "\nThese Crypto Maps use PFS group 2"
for line in group_2_crypto:
    print line.text

