# About
```
* Name: OpenKeys
* IP: 10.10.10.199
* Level: Medium
* OS: OpenBSD
```

# Flags
```
* User: 36ab21239a15c537bde90626891d2b10
* Root: f3a553b1697050ae885e7c02dbfc6efa
```

# Enumeration
```
* Ports
  * 80
  * 22

* /includes/auth.php.swp
* vi -r auth.php.swp gave us the source code
* if we bypass escapeshellcmd then we can get a shell
* got second file from the script
* need to bypass that for code execution
* found a way to bypass auth (https://www.secpod.com/blog/openbsd-authentication-bypass-and-local-privilege-escalation-vulnerabilities/)
* username:-schallenge&password:passwd
* added a cookie username:jennifer( got from swp file)
* got keys of jennifer
```

# Privesc
```
* uname -a 
* found kernel exploit
* running it got us root
```
