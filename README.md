#How to use the tool?

##Installing PyEZ and all the dependent packages:

1. Execute the `install_dependencies_ubuntu.sh` file as the root (sudo ./install_dependencies_ubuntu.sh)


Password Validation:

1. Add various username/password combinations to `input.txt` file. Each combination should be inserted on a separate line in the file. There should be a space of `tab `between the username and the password (_username password_)
2. Add the management IP of the device or the subnet the device is a part of to `ip.txt` file. Each IP address or the subnet should be inserted on a separate line in the file.
3. Run `check_password.py` file.
4. The IP addresses for which the ssh login is successful will be stored in `ip_at_risk.txt` file along with the username/password combination with which the login was successful.
5. Run 'change_password.py' file. It will ask you whether you want to change the password for the the 1st IP address in `'ip_at_risk.txt'` file. If you say yes then it will prompt you to enter the password. If you say no then the script moves onto the 2nd IP address in the `'ip_at_risk.txt'` file.



Logging device info:

1. Add IP address and valid username/password credentials to log onto the device to the `info.txt` file. There should be a space of `tab` between each of IP address username and password. (ex. __192.168.0.5_ username password*_ )
2. Add the `show` commands you want to query the device for to the `commands.txt` file. Each show command should be added on a new line in the file.
3. The output of the show commands is stored in `'IP'.txt` file.


