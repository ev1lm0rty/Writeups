# About
```
* Name: TomGhost
* IP: 10.10.218.68
* Level: Easy
```

# Creds
```
skyfuck:8730281lkjlkjdqlksalks
tryhackme.asc:alexandru
merin: asuyusdoiuqoilkda312j31k2j123j1g23g12k3g12kj3gk12jg3k12j3kj123j
```

# Flags
```
User: THM{GhostCat_1s_so_cr4sy}
Root: THM{Z1P_1S_FAKE}

```

# Enumeration
```
## Ports
  * 22 Openssh 7.2
  * 8009 Apache Jserv v1.3
  * 8080 Apache Tomcat 9.0.30

## Os
  * Ubuntu 2.8

## Potential Exploits
  * Ghostcat vulnerability
  * (https://github.com/00theway/Ghostcat-CNVD-2020-10487)

```

# Exploitation
```
## Login
  * Got ssh creds from above vulnerability.

## Post Exploitation
  * Got user flag
  * Got a gpg and a asc file.
  * Brute forced asc file to get a password
  * Decrypted the gpg file to get merlin password.
    ``
      gpg --import tryhackme.asc && gpg --decrypt credential.gpg
    ``

## Interesting
  * Writable Path
  * Crontab for root:
  `*  *    * * *   root    cd /root/ufw && bash ufw.sh`
  *User melanie can run zip as root

## Privesc
  * Got zip exploit from gtfobins
  * Run the following commands
    TF=$(mktmp -u)
    sudo zip $TF /etc/hosts -T -TT 'sh #'

  
```
