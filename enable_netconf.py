import pexpect


def configure_netconf(ip_address,username,password):

    child=pexpect.spawn('ssh ' +username+'@'+ip_address)
    child.expect('Password')
    child.sendline(password)
    child.expect('>')

    child.sendline('configure')
    child.expect('#')
    child.sendline('set system services netconf ssh')
    child.expect('#')
    child.sendline('commit and-quit')
    child.expect('>')
    print(child.before)
