# read parsed location info from json file instead of pexpect

import json

with open('civlocparsed.json', 'r') as infile:
   civlocparsed = json.load(infile)
for block in civlocparsed:
    print block['Identifier']
    print block.get('Ports')
print 'end of script - bye bye'
print
