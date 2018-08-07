import pexpect


def configure_netconf(ip_address,username,password):
    child=pexpect.spawn('ssh -o StrictHostKeyChecking=no ' +username+'@'+ip_address)
    i=child.expect([pexpect.TIMEOUT,'[Pp]assword','Password:'])
    if i == 0:
        print("Timeout error")
        print(child.before)
        print(child.before)
    elif i==1 or i==2:
        #child.expect('[Pp]assword')
        child.sendline(password)
        child.expect('>')
        try:
            child.sendline('configure')
            child.expect('#')
            child.sendline('set system services netconf ssh')
            child.expect('#')
            child.sendline('commit and-quit')
            child.expect('>')
            #print(child.before)
            return True
        except pexpect.TIMEOUT:
            return False


