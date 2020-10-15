# Lab: Server-side template injection in a sandboxed environment

## Description
```
This lab uses the Freemarker template engine. It is vulnerable to server-side template injection due to its poorly implemented sandbox. 
To solve the lab, break out of the sandbox to read the file my_password.txt from Carlos's home directory. Then submit the contents of the file.
You can access your own account with the following credentials:
username = content-manager
password = C0nt3ntM4n4g3r

```
## Solution
* Login with creds
* Blog->View Details->Edit Template
* Passing ${self} gives us an error, and we find that the template engine is Freemarker
* Reading the documentation we find
