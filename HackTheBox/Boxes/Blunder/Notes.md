# Info
```
* Name: Blunder
* IP: 10.10.10.191
* Box: Linux
* Level: Easy
* User.txt : 01b73ecef3cc5f64e1fefcfa24623ffa
* Root.txt : 
```

# Creds
```
## Users
  * fergus:snoopy1

```
# Enumeration
```
* Web fuzzing : 
  ** Bludit is installed ( /install.php )
  ** .gitignore file found (/.gitignore)
  ** Username found - fergus ( /todo.txt )
  ** Admin Login page (/admin/login)

* Port Scan : 
  ** 21 Ftp closed
  ** 80 http open


* Exploit : 
  ** Bruteforce exploit found.( Had to make some changes [open in encoding "latin"] )
  ** Authenticated exploit found.( Got creds from bruteforce exploit )
```

# Exploitation
```
* Found creds to hugo sha1 hashed in users.php
* sudo exploit used to get root 'sudo -u#-1 /bin/bash'
```
