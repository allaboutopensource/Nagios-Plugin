#!/usr/bin/python
import os, sys
import subprocess
#input = sys.argv[1]
limit = 85
usage = []
volumes = ['nfs_vol04', 'nfs_vol03', 'nfs_vol01', 'nfs_vol2']
cmd = 'df -h | grep 192.25.xx.xx:'
server = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
output =server.communicate()
result= str(output)
s = result.split()
t = s[4::5]
count = 0
for i in t:
    usage.append(i[:-1])
loi = list(map(int,usage))
for i in loi:
    if any(i > limit for i in loi):
        print ("One of the storage mount point usage is Critical")
        sys.exit(2)
    elif any(i == limit for i in loi):
        print ("One of the storage mount point usage reached warning")
        sys.exit(1)
    else:
        print ("All storage mount points usage are OK")
        sys.exit(0)
