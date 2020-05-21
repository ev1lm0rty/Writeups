# Basic
```
Name: Cache
IP: 10.10.10.188
Box: Linux
Level: Medium
Released: 09 May 2020
```
# Flags
```
user.txt : 1fdeca0ae5754ca34f108cd023490f22
root.txt : 6a48ba46c5694e96d53c6a84fd38252e
```

# Username
```
* doit
```
# Creds
```
* ash:H@v3_fun ( works on the box)
* luffy: 0n3_p1ec3
```
# Enum
```
* domain name: cache.htb
* found password in javascript file ( Looks like a rabbit hole )
* found domain name cache.htb
* found another domain hms.htb
* found an rce exploit (searchsploit -x exploits/php/webapps/43232.txt) [ not working yet ] 
* Directory traversal ( http://hms.htb/sites/)
* siteid: default ; dbname:openemr ; sitename :OpenEmr ; Version: 5.0.1(3) 
```
# User Exploitation
```
* SQL injection in the portal field
* Get password hash from that
* Crack the hash using john
* Get reverse shell using rce exploit(modified)
* Idk why but the user.txt file is not working
* memcached server running on port 11211
* extracted password of luffy user from that

```
# Root
```
* user luffy was in docker group.
* a docker image was present
* ` docker run -v /root:/mnt -it ubuntu `
* this mounted the root folder to the /mnt folder and hence we got root
```
