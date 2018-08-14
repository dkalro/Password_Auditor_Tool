#!/bin/sh

apt-get update
apt-get install python3-pip -y
apt-get install python3-dev -y
apt-get install libxml2-dev -y
apt-get install libxslt-dev -y
apt-get install libssl-dev -y
apt-get install libffi-dev -y


pip3 install junos-eznc