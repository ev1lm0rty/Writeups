# Basic
```
* Name: Nest
* Level : Easy
* IP: 10.10.10.178
* Box: Windows
* Release: 25 Jan 2020

```
# Flags

```
User: cf71b25404be5d84fd827e05f426e987

```

# Creds

```
** SMB
  Username: TempUser
  Password: welcome2019
**

** Debug mode password
  WBQ201953D8w
**

** SMB
  c.smith:xRxRxPANCAK3SxRxRx
**

```
# Enumeration

```
* Accessing SMB share '//10.10.10.178/User' we get some creds
* Found a hidden directory from notepadplusplus config file and downloaded the contents.
* Reversed the Code to get password 
* Logged in with c.smith to Users share.
* A File with alternate data stream found in Debugmodepassword file in the share `allinfo "Debugmodepassword.txt" && get "Debugmodepassword.txt:Password"`
* A service is running on the port :4386 
* 
```

# Ldap conf

```
Domain=nest.local
Port=389
BaseOu=OU=WBQ Users,OU=Production,DC=nest,DC=local
User=Administrator
Password=yyEq0Uvvhq2uQOcWG8peLoeRQehqip/fKdeG/kjEVb4=


```
