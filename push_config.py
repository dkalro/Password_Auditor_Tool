from jnpr.junos import Device
import os
from jnpr.junos.utils.config import Config
from jnpr.junos.exception import ConnectError
from jnpr.junos.exception import LockError
from jnpr.junos.exception import UnlockError
from jnpr.junos.exception import ConfigLoadError
from jnpr.junos.exception import CommitError
from jnpr.junos.utils.start_shell import StartShell

def main():
    # open a connection with the device and start a NETCONF session

    hostname = "192.168.56.4"
    username = "root" 
    password = "pass4root"
    try:
        dev = Device(host=hostname, user=username, passwd=password)
        dev.open()
    except ConnectError as err:
        print ("Cannot connect to device: {0}".format(err))
        return
    dev.bind(cu=Config)

    # Lock the configuration, load configuration changes, and commit
    print ("Locking the configuration")
    try:
        dev.cu.lock()
    except LockError as err:
        print ("Unable to lock configuration: {0}".format(err))
        dev.close()
        return
    new_User='set system login user saran class read-only authentication plain-text-password-value juniper1234'

    print ("Loading configuration changes")
    try:
        dev.cu.load(new_User, format='set')
    except (ConfigLoadError, Exception) as err:
        print ("Unable to load configuration changes: {0}".format(err))
        print ("Unlocking the configuration")
        try:
                dev.cu.unlock()
        except UnlockError:
            print ("Unable to unlock configuration: {0}".format(err))
        dev.close()
        return

    print ("Committing the configuration")
    try:
        dev.cu.commit(comment='Loaded by example.')
    except CommitError as err:
        print ("Unable to commit configuration: {0}".format(err))
        print ("Unlocking the configuration")
        try:
        	dev.cu.unlock()
        except UnlockError as err:
        	print ("Unable to unlock configuration: {0}".format(err))
        	dev.close()
        	return

    print ("Unlocking the configuration")
    try:
        dev.cu.unlock()
    except UnlockError as err:
        print ("Unable to unlock configuration: {0}".format(err))

    # End the NETCONF session and close the connection
    dev.close()

if __name__ == "__main__":
    main()
