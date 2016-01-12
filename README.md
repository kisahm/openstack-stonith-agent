**openstack-stonith-agent**

**What it is**
It's a STONITH agent for openstack instances.<br>
If you are running a Pacemaker cluster on OpenStack instances you can use this STONITH agent to fence them.<br>
The STONITH agent is using the OpenStack APIs.<br>
<br>

**How to install**
```
$ git clone https://github.com/kisahm/openstack-stonith-agent.git
$ sudo cp openstack-stonith-agent/openstack /usr/lib/stonith/plugins/external/
```
