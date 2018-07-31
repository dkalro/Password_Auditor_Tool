from getpass import getpass
from jnpr.junos import Device
from jnpr.junos.utils.config import Config
from jnpr.junos.factory.factory_loader import FactoryLoader
from jnpr.junos.exception import ConnectError
from jnpr.junos.exception import LockError
from jnpr.junos.exception import UnlockError
from jnpr.junos.exception import ConfigLoadError
from jnpr.junos.exception import CommitError
import yaml
import enable_netconf as netconf
import disable_netconf as del_netconf

myYAML = """
---
UserTable:
  get: system/login/user
  view: UserView 
UserView:
  fields:
    username: name
    userclass: class
"""

globals().update(FactoryLoader().load(yaml.load(myYAML)))


def main():
    lines=open("ip_at_risk.txt", "r").readlines()
    print(lines)
    for l in lines:
        splitted = l.strip().split("\t")
        print(splitted[0],splitted[1],splitted[2])
        changepassword(splitted[0],splitted[1],splitted[2])


def changepassword(ip_address, u_name, pwd):
    print(
        'The currently configured password is one of the commonly used ones. We suggest you to change the password, it maybe compromised in the future')

    while True:
        b = input('Do you want to change the password? Y(yes), N (no): ')
        if b == 'y' or b == 'Y' or b=='n' or b=='N':
            break
        else:
            print('Invalid input. Please try again')
    if b=='y' or b=='Y':
        print('Enabling netconf')
        netconf.configure_netconf(ip_address,u_name,pwd)
        try:
            dev = Device(host=ip_address, user=u_name, passwd=pwd)
            dev.open()
        except ConnectError as err:
            print("Cannot connect to device: {0}".format(err))
            return
        while True:
            pd = getpass("New password:")
            pd1 = getpass("Retype new password:")
            if pd != pd1:
                print('Passwords do not match. Please try again')
            elif pd == pd1 and pd == pwd:
                print('New Password cannot be same as the old password. Please try again.')
            elif pd == pd1 and pd != pwd:
                break;
        users = UserTable(dev)
        users.get()
        cls = users[u_name].userclass
        command = "set system login user " + u_name + " class " + cls + " authentication plain-text-password-value " + pd

        dev.bind(cu=Config)

        # Lock the configuration, load configuration changes, and commit
        print("Locking the configuration")
        try:
            dev.cu.lock()
        except LockError as err:
            print("Unable to lock configuration: {0}".format(err))
            dev.close()
            return

        print("Loading configuration changes")
        try:
            dev.cu.load(command, format='set')
        except (ConfigLoadError, Exception) as err:
            print("Unable to load configuration changes: {0}".format(err))
            print("Unlocking the configuration")
            try:
                dev.cu.unlock()
            except UnlockError:
                print("Unable to unlock configuration: {0}".format(err))
                dev.close()
                return

        print("Committing the configuration")
        try:
            dev.cu.commit(comment='Loaded by example.')
        except CommitError as err:
            print("Unable to commit configuration: {0}".format(err))
            print("Unlocking the configuration")
            try:
                dev.cu.unlock()
            except UnlockError as err:
                print("Unable to unlock configuration: {0}".format(err))
                dev.close()
                return

        print("Unlocking the configuration")
        try:
            dev.cu.unlock()
        except UnlockError as err:
            print("Unable to unlock configuration: {0}".format(err))

        # End the NETCONF session and close the connection
        dev.close()
        print('Deleting netconf')
        del_netconf.delete_netconf(ip_address,u_name,pd)


if __name__ == "__main__":
    main()