import pexpect
child=pexpect.spawn('ssh psdsn@10.19.10.223')
child.expect('Password')
child.sendline('Password1234')
child.expect('>')

child.sendline('configure')
child.expect('#')
child.sendline('set system services netconf ssh')
child.expect('#')
child.sendline('commit')
child.expect('#')

print(child.before)
