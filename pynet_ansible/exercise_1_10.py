#!/usr/bin/env python

#10. Using ciscoconfparse find the crypto maps that are not using AES (based-on the transform set name). Print these entries and their corresponding transform set name.

from ciscoconfparse import CiscoConfParse

cisco_cfg = CiscoConfParse("cisco_crypto.txt")
#crypto_cfg = cisco_cfg.find_objects(r"^crypto map CRYPTO")
#cisco_cfg.find_objects_w_child(parentspec=r"^interface", childspec=r"no ip address")
#cisco_cfg.find_objects_wo_child(parentspec=r"^interface", childspec=r"no ip address")
#group_2_crypto = cisco_cfg.find_objects_w_child(parentspec=r"^crypto map CRYPTO", childspec=r"group2")
no_aes = cisco_cfg.find_objects_wo_child(parentspec=r"^crypto map CRYPTO", childspec=r"AES")


print "\nThese crypto maps aren't using AES in their transform-set:"
for line in no_aes:
    print line.text
    for kids in line.children:
            if "transform" in kids.text:
                    print kids.text

