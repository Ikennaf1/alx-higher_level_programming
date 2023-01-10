#!/usr/bin/python3

from os import path
from sys import argv

load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

if path.exists('add_item.json'):
    my_obj = load_from_json_file('add_item.json')
else:
    my_obj = []

for i in range(1, len(argv)):
    my_obj.append(argv[i])

save_to_json_file(my_obj, 'add_item.json')
