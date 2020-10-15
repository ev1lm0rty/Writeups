# Lab: Server-side template injection using documentation

## Description
```
This lab is vulnerable to server-side template injection. To solve the lab, 
identify the template engine and use the documentation to work out how to execute arbitrary code, 
then delete the morale.txt file from Carlos's home directory.
You can access your own account with the following credentials:
    username = content-manager
    password = C0nt3ntM4n4g3r
Tip: You should try and solve this lab using only the documentation. However, if you get really stuck, you can try finding a well-known exploit by @albinowax that you can use to solve the lab. 
```


## Solution
* Login with the creds
* We find that we can edit template, hence we use it to identify the template engine that is running.
* On the template edit page we change the ${produce.name} to ${self} , then we hit the preview button and get a java error.
* Reading the error we find out that it's the Freemarker java template engine.
* Now reading it's documentation to find any vulnerable functions.
* I could'nt find a vulnerable function (idiot me) so I read [Blackhat SSTI Presentation](https://www.blackhat.com/docs/us-15/materials/us-15-Kettle-Server-Side-Template-Injection-RCE-For-The-Modern-Web-App-wp.pdf) and found an exploit
* Payload is as follows
```<#assign x="freemarker.template.utility.Execute"?new()> ${x("rm -rf /home/carlos/morale.txt")} ```
* Hitting the preview button solves the lab.
