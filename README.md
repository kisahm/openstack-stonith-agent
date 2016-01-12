**openstack-stonith-agent - UNDER CONSTRUCTION!!!**

**What it is**<br>
It's a STONITH agent for openstack instances.<br>
If you are running a Pacemaker cluster on OpenStack instances you can use this STONITH agent to fence them.<br>
The STONITH agent is using the OpenStack APIs.<br>
<br>

**Requirements**<br>
python-novaclient
<br>
<br>
Install on Ubuntu: 
```
apt-get install python-novaclient
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
