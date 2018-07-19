from jnpr.junos import Device
from jnpr.junos.factory.factory_loader import FactoryLoader
import yaml

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

dev = Device(host='10.13.110.41',user='adi',passwd='adi123').open()
users = UserTable(dev)
users.get()

for account in users:
    print("Username is {}\nUser class is {}".format(account.username, account.userclass))

dev.close()  
