# Nagios-Plugin

Plugins are compiled executables or scripts (Perl scripts, shell scripts, etc.) that can be run from a command line to check the status or a host or service. Nagios uses the results from plugins to determine the current status of hosts and services on your network.

In this repo we are creating a plugin which will monitor the NFS mount storage space on a linux server or Xen hypervisor and as per the requirement you can set the warning/critical alerts for this plugin. 

Steps to create a customised Nagios plugin for your infrastructure. Things to note:

1) We are using SNMP client which is a agentless client for the monitoring but you can use NRPE agent as well.
2) We are using Python as the language for creating the script, you can use bash/shell as well. 

We need to copy the check_snmp_extend.py script to your Nagios XI server i.e which will access the info from Linux hosts.

Copy the check_snmp_extend.py script to the plugin location of the nagios (/usr/local/nagios/libexec).

change the mode and ownership : 

chmod +x /usr/local/nagios/libexec/check_snmp_extend.py

chown apache:nagios /usr/local/nagios/libexec/check_snmp_extend.py 

You need to add A SNMP EXEC (EXTEND) to the Linux/Xen host and give the community name to the config:

edit /etc/snmp/snmpd.conf and add a line like this :

extend <script name> /usr/bin/<location of the script>

We need to run the script as : 

./check_snmp_extend.py --host localhost --snmp-version 2c --community <community name> --extend-name <name>
  
For writing the script, you need to keep in mind the exit codes:

Return code	Service status: 

0	OK
1	WARNING
2	CRITICAL
3	UNKNOWN

Create a check command: First you should define a command in the commands.cfg file. This file location depends on the configuration you've done, in my case it is in /usr/local/nagios/etc/objects/commands.cfg. name : check_nfsstorage 

Create a service: You need to create a service and select the above check command and in the $ARG1$ mention the warning level and in the $ARG2$ mention the critical level. 


In order to verify your configuration, run Nagios with the -v command line option like so:

/usr/local/nagios/bin/nagios -v /usr/local/nagios/etc/nagios.cfg

The last step is to restart the nagios service using this command

service nagios restart
