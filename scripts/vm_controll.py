#!/usr/bin/python

### Required packages
# python-novaclient

from novaclient import client
import sys
import getopt

def main(argv):                      
	global _debug, _instance, _username, _password, _tenant, _authurl, _action
	_debug = 0
	_action = "reboot-force" # reboot, reboot-force, stop   
	
	try:
		opts, args = getopt.getopt(argv,"hdi:u:p:t:a:A:",["help", "debug", "instance=", "username=", "password=", "tenant=", "auth-url=", "action="])
   	except getopt.GetoptError:
		help()
      		sys.exit(2)
	for opt, arg in opts:
		if opt in ("-h", "--help"):
			help()                     
			sys.exit()                  
		elif opt == '-d':           
			_debug = 1                  
		elif opt in ("-i", "--instance"):
			_instance = arg
		elif opt in ("-u", "--username"):
			_username = arg
		elif opt in ("-p", "--password"):
			_password = arg
		elif opt in ("-t", "--tenant"):
			_tenant = arg
		elif opt in ("-a", "--auth-url"):
			_authurl = arg
		elif opt in ("-A", "--action"):
			_action = arg
	if _instance == "":
		print "ERROR - you must set a instance name"
                sys.exit(3)
	elif _username == "":
		print "ERROR - you must set your openstack username"
                sys.exit(3)
	elif _password == "":
                print "ERROR - you must set your openstack password"
                sys.exit(3)
	elif _tenant == "":
		print "ERROR - you must set your openstack tenant (project) name"
                sys.exit(3)
	elif _authurl == "":
		sys.exit(3)
		print "ERROR - you must set the authentication url (keystone url) from the openstack cloud"
		sys.exit(3)
	elif _action != "reboot" and _action != "reboot-force" and _action != "shutdown":
		print "ERROR - you must set a shutdown action (reboot, reboot-force or stop)"
		sys.exit(3)
	#nova = client.Client(VERSION, USERNAME, PASSWORD, PROJECT_ID, AUTH_URL)
	nova = client.Client(2, _username, _password, _tenant, _authurl)
	found = 0
	instances = nova.servers.list()
	for instance in instances:
		if instance.name == _instance:
			found = 1
			currentstatus = instance.status
			id = instance.id
			if _debug:
				print "Found instance '" + _instance +"' in tenant '"+_tenant+"'"
			break
	if found == 1:
		if _debug:
			print "Current state of instance '"+_instance+"': "+currentstatus
	else:
		print "ERROR - Cannot find any instance with name '"+_instance+"'"
		sys.exit(3)

	try:
		if _action == "reboot":
			nova.servers.reboot(id,reboot_type='SOFT')
		elif _action == "reboot-force":
			nova.servers.reboot(id,reboot_type='HARD')
		else:
			nova.servers.stop(id)
	except:
		print "ERROR - Cannot shutdown instance '"+_instance+"'"
		exit(4)	
	

def help():
	print "-h = help"

      


if __name__ == "__main__":
	main(sys.argv[1:])
