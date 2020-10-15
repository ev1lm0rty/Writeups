# Lab: Server-side template injection with information disclosure via user-supplied objects

## Description
```
This lab is vulnerable to server-side template injection due to the way an object is being passed into the template. 
This vulnerability can be exploited to access sensitive data.
To solve the lab, steal and submit the framework's secret key.
You can access your own account with the following credentials:
username = content-manager
password = C0nt3ntM4n4g3r
```
## Solution

* Login with the creds
* Open a blog and then click 'edit template'
* Looking for errors we found that it is django framework python
* ```{% debug %}``` gives us list of objects
* ```{{settings.SECRET_KEY}}``` gives us the secret key
