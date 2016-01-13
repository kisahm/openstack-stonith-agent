**openstack-stonith-agent - BETA!!!**

**What it is**<br>
It's a STONITH agent for openstack instances.<br>
If you are running a Pacemaker cluster on OpenStack instances you can use this STONITH agent to fence them.<br>
The STONITH agent is using the OpenStack APIs.<br>
<br>

**Requirements**<br>
git<br>
python-novaclient
<br>
<br>
Install on CentOS:
```
yum install -y https://rdoproject.org/repos/rdo-release.rpm
yum update
yum install git python-novaclient
```

Install on Ubuntu: 
```
$ apt-get install git python-novaclient
```
<br>

**How to install**
```
$ git clone https://github.com/kisahm/openstack-stonith-agent.git
$ sudo cp openstack-stonith-agent/openstack /usr/lib/stonith/plugins/external/
```
<br>

**What you need**
- The OpenStack tenant name (project name)
- An OpenStack user name passwort in this tenant
- The OpenStack instance names in this tenant
- The authentication url (the Keystone url)  
  Example: https://mycloud.example.com/v2.0/
- A decision how to fence the instance:
  - reboot - soft reboot of the instance
  - reboot-force - hard reboot of the instance
  - stop - power off the instance
<br>

**How to integrate in pacemaker**
```
root@clusternode-1:~# crm
crm(live)# configure

crm(live)configure# primitive stonith-clusternode-1 stonith:external/openstack params openstack_instance=clusternode-1 openstack_username=mystonithuser openstack_password=mypassword openstack_tenant=myclustertenant openstack_authurl=https://mycloud.example.com/v2.0/ openstack_poweraction=reboot

crm(live)configure# primitive stonith-clusternode-2 stonith:external/openstack params openstack_instance=clusternode-2 openstack_username=mystonithuser openstack_password=mypassword openstack_tenant=myclustertenant openstack_authurl=https://mycloud.example.com/v2.0/ openstack_poweraction=reboot

crm(live)configure# location loc-stonith-clusternode-1 stonith-clusternode-1 -inf: clusternode-1
crm(live)configure# location loc-stonith-clusternode-2 stonith-clusternode-2 -inf: clusternode-2

crm(live)configure# property stonith-enabled=true

#Only at two node cluster
crm(live)configure# no-quorum-policy="ignore"

crm(live)configure# verify
crm(live)configure# commit
```
