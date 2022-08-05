#!/usr/bin/env python3
import json

_ = {'item': 'Samsung s10e', 'prices': [4_500, 5_500], 'os': 'Android', 'version': 12}
json.dumps(_, indent=3, sort_keys=True) # sort list of key value
