#!/usr/bin/env python

#6. Write a Python program that creates a list. One of the elements of the list should be a dictionary with at least two keys. Write this list out to a file using both YAML and JSON formats. The YAML file should be in the expanded form.

import yaml
import json

my_list = range(10)
my_list.append('some string')
my_list.append('some other string')
my_list.append({})
my_list[-1]['ip_address'] = '1.2.3.4'
my_list[-1]['attribs'] = {}

with open("exercise_1_6.yaml" , "w") as f:
    f.write(yaml.dump(my_list , default_flow_style=False))

with open("exercise_1_6.json" , "w") as g:
    json.dump(my_list , g)


