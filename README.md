# OCI SSH configuration

Use Oracle Cloud search to automate SSH connections

`oci_ssh.py` depends on the [oci-python-sdk](https://github.com/oracle/oci-python-sdk), python 3.5+ and `netcat`

## Installation

#### Install Netcat

#####   Ubuntu
    sudo apt update   
    sudo apt install netcat
#####   OL/CentOS/RHEL
    sudo yum update
    sudo yum install nc
#####   Mac OS X
    brew install netcat
    
#### Download and configure oci_ssh

* Clone the repository within your `~/.ssh/` folder
* Intall required packages `pip -r ~/.ssh/oci-ssh/requirements.txt`
* Add `Include oci-ssh/config` in the ~/.ssh/config` file  
* Make sure that your OCI credentials are [configured](https://docs.oracle.com/en-us/iaas/Content/API/Concepts/sdkconfig.htm) properly

## Syntax

`oci+instance display name+region+profile(optional)`

e.g.

`ssh oci+myserver+us-ashburn-1` or `ssh oci+myserver+us-ashburn-1+mytenancyprofile`
