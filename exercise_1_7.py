#!/usr/bin/env python

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
