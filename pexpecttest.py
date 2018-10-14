# demonstration of pexpect and python

import pexpect

child = pexpect.spawn('ssh -l user1 10.10.10.110')
child.expect ('Password:')
child.sendline ('pass1')
child.expect ('Router1#')
child.sendline ('ter len 0')
child.expect ('Router1#')
child.sendline ('show int gi0/2')
child.expect ('Router1#')
show_int = child.before
child.sendline ('logout')
child.expect ('closed.')
print 'Below is the output of a show int'
# print show_int

for line in show_int.splitlines():
#    print line
    if 'input rate' in line:
#        print '+++++++++++++++++++++++++++'
        print
        print
        print
        print line.split()
        bps = int(line.split()[4])
        pps = int(line.split()[6])
        print 'input b/s is ', bps
        print 'input pps is ', pps
        av_packet_size = 0
        if bps > 0:
            av_packet_size = bps / 8 / pps
        print 'average packet size is', av_packet_size, 'bytes'

print '*** End of Script ***'

