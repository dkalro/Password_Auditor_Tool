import paramiko

def main():
    lines1 = open("ip.txt", "r").readlines()
    print(lines1)
    f = open('filtered_ip.txt', 'w+')
    for i in lines1:
        ip = i[:-1]
        lines = open("input.txt", "r").readlines()
        print(lines)
        for l in lines:
            splitted = l.strip().split("\t")
            print(splitted[0], splitted[1])
            if connect(ip, splitted[0], splitted[1]) == True:
                f.write(ip + '\t'+ splitted[0]+'\t'+splitted[1]+'\n')
                #changepassword(ip, splitted[0], splitted[1])
    f.close()



def connect(ip_address, u_name, pwd):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        print(ip_address)
        ssh.connect(ip_address, username=u_name, password=pwd)
        return True
    except  paramiko.AuthenticationException:
        return False



if __name__ == "__main__":
    main()
