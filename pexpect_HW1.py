# Homework 1

import pexpect

#creates primates2.nex file and stores it as object called newprimates
newprimates = open('primates2.nex', 'w')
#creates primates.nex file and store is as object called oldprimates
oldprimates = open('primates.nex').read()
#replaces 'mcmc' with 'mcmcp' in primates.nex file
corrected=oldprimates.replace('mcmc',  'mcmcp')
corrected.find('mcmcp')

#writes corrected primates file to primates2.nex file and closes it
newprimates.write(corrected)
newprimates.close()

child = pexpect.spawn('mb -i primates2.nex')
child.sendline(r'mcmc') 
child.sendline('no') 
child.expect('MrBayes >') 
print child.before
child.sendline('quit')