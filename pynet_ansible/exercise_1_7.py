#!/usr/bin/env python

#7. Write a Python program that reads both the YAML file and the JSON file created in exercise6 and pretty prints the data structure that is returned.

import yaml
import json
from pprint import pprint as pp

with open("exercise_6.yaml") as f:
    yaml_list = yaml.load(f)

with open("exercise_6.json") as g:
    json_list = json.load(g)

pp(yaml_list)

print
print

pp (json_list)
