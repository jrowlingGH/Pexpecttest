# pexect trial with IOS

import pexpect, json
def parseblock(text):
# parseblock returns a list of blocks
# each block is a dictionary that contains
# the text between separators turned into
# key: value pairs
    blocklist = []
    block = []
    lines = text.splitlines()
    dict1 = {}
    for line in lines:
        if not line == "--------------------------":
            if not line.find(':') == -1:
#                print line
                split1 = line.split(":")
                dict1[split1[0].rstrip()] = split1[1].strip()
        else:
            if not dict1 == {}:
                blocklist.append(dict1)
            dict1 = {}
    return blocklist

child = pexpect.spawn('telnet 10.1.1.202 23')
child.expect ('Password:')
child.sendline ('cisco')
child.expect ('Switch>')
child.sendline ('ter len 0')
child.expect ('Switch>')
child.sendline ('show location civic static')
child.expect ('Switch>')
civlocraw = child.before
child.sendline ('logout')
child.expect ('foreign')
civlocparsed = parseblock(civlocraw)
with open('civlocparsed.json', 'w') as outfile:
  json.dump(civlocparsed, outfile)
for block in civlocparsed:
    print block['Identifier']
    print block.get('Ports')
print 'end of script - bye bye'
print
