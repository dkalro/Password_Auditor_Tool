import paramiko
from getpass import getpass
from jnpr.junos import Device
from jnpr.junos.utils.config import Config
from jnpr.junos.factory.factory_loader import FactoryLoader
import yaml
#from myTables.ConfigTables import UserConfigTable
from lxml import etree


myyaml2="""
UserConfigTable:
  set: system/login/user
  key-field: username
  view: UserConfigView 
UserConfigView:
  fields:
    username: name
  fields_auth:
    password: plain-text-password
"""
globals().update(FactoryLoader().load(yaml.load(myyaml2)))

lines1=open("ip.txt","r").readlines()
print(lines1)

def main():
	for i in lines1:
		ip=i[:-1]
		lines=open("input.txt","r").readlines()
		for l in lines:
			splitted=l.strip().split("\t")
			print(splitted[0],splitted[1])
			if connect(ip,splitted[0],splitted[1])==True:
				changepassword(ip,splitted[0],splitted[1])


def connect(ip_address,u_name,pwd):
	
	ssh = paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	try:
		print(ip_address)			
		ssh.connect(ip_address,username=u_name,password=pwd)          	
		return True	
	except  paramiko.AuthenticationException:
		return False

def changepassword(ip_address,u_name,pwd):
	print('The currently configured password is one of the commonly used ones. We suggest you to change the password, otherwise your device may be 	compromised')
	b=raw_input('Do you want to change the password? Y(yes), N (no): ')
	print b
	if b=='y' or b=='Y':
		
		while True:
	#		pd=getpass("New password:")
	#		pd1=getpass("Retype new password:")
	#		if pd==pd1:
	#			break;
		# dev = Device(host=ip_address, user=u_name, passwd=pwd)
		# dev.open()
		# uc = UserConfigTable(dev)
		# uc.username=u_name	
		# uc.password=pd
		# uc.append()
		# uc.set()
		
		dev = Device(host='192.168.56.4', user='root', password='pass4root')
		dev.open()
		cu=Config(dev)
		#############################
		new_User='set system login user saran class read-only authentication plain-text-password-value juniper12345'
		# pass_New='juniper123'
		# pass_Repeat='juniper123'
		##############################

		cu.load(new_User, format='set')
		# cu.load(pass_New,format='set')
		# cu.load(pass_Repeat,format='set')

		# configXML = uc.get_table_xml()
		# if (configXML is not None):
    	# 		print (etree.tostring(configXML, encoding='unicode', pretty_print=True))
	
	dev.close()
			
main()
