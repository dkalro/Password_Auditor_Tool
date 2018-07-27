import paramiko
import subprocess
#import platform
#from subprocess import PIPE,Popen
import ipaddress as ipa


def main():
    lines1 = open("ip.txt", "r").readlines()
    print(lines1)
    lines = open("input.txt", "r").readlines()
    print(lines)
    f = open('filtered_ip.txt', 'w+')
    for i in lines1:
        if '/' in i:
            network=ipa.ip_network(i.strip())
            print(network)
            for j in network.hosts():
                j=str(j)
                if pingtest(j)==True:
                        for l in lines:
                            splitted = l.strip().split("\t")
                            print(splitted[0], splitted[1])
                            if connect(j, splitted[0], splitted[1]) == True:
                                f.write(j + '\t' + splitted[0] + '\t' + splitted[1] + '\n')


        elif pingtest(i)==True:
            for l in lines:
                splitted = l.strip().split("\t")
                print(splitted[0], splitted[1])
                if connect(i, splitted[0], splitted[1]) == True:
                    f.write(i + '\t' + splitted[0] + '\t' + splitted[1] + '\n')
    f.close()

def pingtest(ip):
    try:
        output = subprocess.check_output(["ping", "-c", "1", ip])
        if 'exit status 1' not in output.decode('utf8').strip():
            return True
    except subprocess.CalledProcessError:
        return False


def connect(ip_address1, u_name, pwd):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        print(ip_address1)
        ssh.connect(ip_address1, username=u_name, password=pwd)
        return True
    except paramiko.AuthenticationException:
        return False

if __name__ == "__main__":
    main()
