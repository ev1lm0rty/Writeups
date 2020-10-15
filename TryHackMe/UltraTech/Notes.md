# About
```
* Name: UltraTech
* IP: 10.10.148.203
* Level: Medium
* Box: Linux
```

# Creds
```
* mr00t:n100906
* admin:mrsheafy
```

# Let's Hack
```
* Ports: 21 , 22 , 8081, 31331
* Found a js file in :31331/patners.js (api.js)
* Revealed a path :8081/ping?id=
* RCE !!! :8081/ping?id=`whoami`
* Found a db file lying around
* Cracked hases and found password to ssh
* User part of docker group ( Simple privesc )
```
