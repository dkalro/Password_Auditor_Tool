from jnpr.junos import Device

def main():
    lines = open("info.txt", "r").readlines()
    print(lines)
    for l in lines:
        splitted = l.strip().split("\t")
        print(splitted[0], splitted[1], splitted[2])
        connect(splitted[0], splitted[1], splitted[2])


def connect(ip_address, u_name, pwd):
    try:
        dev = Device(host=ip_address, user=u_name, passwd=pwd)
        dev.open()
    except ConnectError as err:
        print("Cannot connect to device: {0}".format(err))
        return
    cmd=open('commands.txt','r').readlines()
    with open('{}.txt'.format(ip_address), 'w+') as f:
        f.write('IP address: ' + ip_address +'\n')
        version=dev.cli("show version")
        version=version.split('\n')
        for v in version:
            if "Model" in v:
                f.write(v+ '\n'+'\n')
                break
        for c in cmd:
            command=c.strip()
            a= dev.cli(command)
            f.write('Command: '+command)
            f.write(a+'\n'+'\n'+'\n')
    dev.close()


if __name__ == '__main__':
    main()