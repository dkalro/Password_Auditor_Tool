import pexpect


def configure_netconf(ip_address,username,password):
    child=pexpect.spawn('ssh -o StrictHostKeyChecking=no ' +username+'@'+ip_address)
    i=child.expect([pexpect.TIMEOUT,'[Pp]assword'])
    if i == 0:
        print("Timeout error")
        print(child.before)
        print(child.before)
    elif i==1:
        #child.expect('[Pp]assword')
        child.sendline(password)
        child.expect('>')
        child.sendline('configure')
        child.expect('#')
        child.sendline('set system services netconf ssh')
        child.expect('#')
        child.sendline('commit and-quit')
        child.expect('>')
        print(child.before)

