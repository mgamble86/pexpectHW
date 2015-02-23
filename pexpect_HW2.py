# Homework 2

import pexpect

#spawn an interactive mrbayes process
child = pexpect.spawn('mb -i primates2.nex')
#send the command 'execute primates2.nex' to mrbayes
child.sendline('execute primates2.nex')
#send the sumt command to mrbayes, creates tree data
child.sendline('sumt')
child.expect('MrBayes >') 
print child.before
child.sendline('sump')
child.sendline('quit')