# About
```
* Name: Tabby
* IP: 10.10.10.194
* Level: Easy
* Box: Linux
```

# Flags
```
* User: fd1a551b2ed485afe2c14a0889660ee3
* Root: cd5d59a4588942b65235a652b8c8a3b8
```
# Creds
```
* tomcat:$3cureP4s5w0rd123!
* ash:admin@it
```
# Enumeration
```
* Ports
  * 22
  * 80
  * 8080 - Tomcat Default install

* Port 80
  * /files looks intersting
  * Got a domain name ( megahosting.htb )
  * Got an email address ( sales@megahosting.htb )

* Port 8080
  * /shell
  * /manager

* Found LFI at (http://megahosting.htb/news.php?file=../.../../../../../etc/passwd)

* tomcat was insatlled in some other dir so i got tomcat-users.xml from that
  and got the creds

* Created java reverse shell from msfvenom
* Uploading it with tomcat manager
* Found a zip file at /var/www/html/files
* Cracking it by frackzip gave us a cred
* Creating a authorized_key file gave us an ssh shell.
* found lxd 
* privesc using lxd (https://www.hackingarticles.in/lxd-privilege-escalation/)
```
