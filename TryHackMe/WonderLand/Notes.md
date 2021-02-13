# About
* Name: Wonderland
* IP: 10.10.133.3
* Level: Medium
* Box: Linux

# Enumeration and Exploitation
* Download the rabbit photo present on webpage
* Extracted hint.txt using steghide
* found /r/a/b/b/i/t page with ssh creds in source
* We are as user alice
* sudo -l reveals we can run python program as user rabbit
* it says 'import random' so we create our own random.py file
* ` import os; os.system("/bin/bash");`
* We are now the user rabbit
* we get a suid file
* it uses date without absolute path
* `echo "/bin/bash" > /tmp/date && export PATH=/tmp:$PATH && ./teaParty`
* This gives us shell as hatter
* we find hatter's password in his home dir
* ssh into hatter
* finding capabilited we get perl
* looking up online we get `perl -e 'use POSIX qw(setuid); POSIX::setuid(0); exec "/bin/sh";'`
* `cat /root/root.txt ; cat /root/user.txt`


