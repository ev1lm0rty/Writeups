# Basic
1. Name: TraceBack
2. IP: 10.10.10.181
3. Level: Easy
4. Box: Linux
5. Release Date: 14 Mar 2020

# Enumeration
* Looks like there is a backdoor present somewhere
* Looked for the Xh4H github page and found a list
* smevk.php found
* Found a login page http://10.10.10.181/smevk.php
* admin:admin worked

# Exploitation
* Uploaded reverse php shell
* got shell as user `webadmin`
* `sudo -u sysadmin /home/sysadmin/luvit -e 'os.execute("/bin/bash")'
* got shell as sysadmin`
* enumeration by pspy I found that root user copies the /etc/update-motd/ files every 30 seconds
* Generated a ssh key and added it to the authorized keys 
* added `cat root/root.txt` to /etc/update-motd/00header file
* logged in using ssh (sysadmin user) and got root hash in the header file



# Flags
* user: 2d0602a37bd07ce3431829f5f789ef44
* root: f0531f3af8685294ef4c746fc46adb2d 
