import pexpect

def delete_netconf(ip_address,username,password):
    child = pexpect.spawn('ssh -o StrictHostKeyChecking=no ' + username + '@' + ip_address)
    i = child.expect([pexpect.TIMEOUT, '[Pp]assword:'])
    if i == 0:
        print('Timeout error')
        print(child.before)
        print(child.after)
    elif i == 1:
        child.sendline(password)
        child.expect('>')
        child.sendline('configure')
        child.expect('#')
        child.sendline('delete system services netconf ssh')
        child.expect('#')
        child.sendline('commit and-quit')
        child.expect('>')
        print(child.before)
