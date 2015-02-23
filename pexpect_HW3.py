import pexpect, glob

def homework3(nexus, numgen=1500):
    run = pexpect.spawn('mb -i %s' %(nexus))
    run.sendline('set nowarn = yes')
    run.sendline(r'mcmcp ngen = %d' %(numgen))
    run.sendline(r'mcmc')
    run.sendline('no')
    run.sendline('quit')
	
def homework3b(nexusb):
    child = pexpect.spawn('mb -i %s' %(nexusb))
    child.sendline('execute %s' %(nexusb))
    child.sendline('sumt')
    child.sendline('sump')
    child.sendline('quit')
	
	
files1 = glob.glob('*.*')
t_files1 = glob.glob('*.t')

	
print("there are " + str(len(files1)) + " total files in the current directory and " + str(len(t_files1)) + " files that end in '.t'")

homework3('primates2.nex')
homework3b('primates2.nex')

files2 = glob.glob('*.*')
t_files2 = glob.glob('*.t')

print("there are " + str(len(files2)) + " total files in the current directory and " + str(len(t_files2)) + " files that end in '.t'")

print("these files end in '.t': " + str(t_files2))