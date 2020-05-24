# Level 0 to Level 1
```
Looking at the source code of the page we get the commented password
natas1:gtVrDuiDfck831PqWsLEZy5gyDz1clto
```

# Level 1 to Level 2
```
Cntrl+u to view source, we find the commented password.
natas2:ZluruAthQk7Q2MqmDeTiUij2ZvWy2mBi
```

# Level 2 to Level 3
```
Looking at the source code we find a folder called files
Inside it we find users.txt with the flag
natas3:sJIJNW6ucpu6HPZ1ZAchaDtwd7oGrD14
```

# Level 3 to Level 4 
```
The source code comment gives us the hint that even google can't find it.
Which means the folder would be in robots.txt file
We open it and go to the s3cr3t folder and then user.txt to find the flag
natas4:Z9tkRkWmpt9Qr7XrR5jWRkgOU901swEZ
```

# Level 4 to Level 5
```
Adding a Referer: http://natas5.natas.labs.overthewire.org/ 
to the http request
We get the flag
natas5:iX6IOfmpN7AYOQGPwtn3fXpbaJVJcHfq
```

# Level 5 to Level 6
```
Changing the cookie value in the header from 0 to 1 gives us the flag
natas6:aGoY4q2Dc6MgDq4oL4YtoKtyAg9PeHa1
```

# Level 6 to Level 7
```
We view the source code and see a file at includes/secret.inc
We open it and view its source code and find the flag
natas7:7z3hEENjQtflzgnT29q7wAvMNfZdh0i9
```

# Level 7 to Level 8
```
We modify the url natas..../index.php?page=/etc/natas_webpass/natas8 and get the flag
natas8:DBfUBfqQG69KvJvJ1iAbMoIpwSNQ9bWe
```

# Level 8 to 9
```
We look at the function and find that it first base64 encodes then reverse and then hexencode the secret
We reverse this process from any online decoder and get the secret.
We input the secret and get the flag
natas9:W0mMhUcRRnG8dcghE4qvk3JA9lGt8nDl
```

# Level 9 to Level 10
```
Looking at the source we find no user input sanitation 
so we enter the following string in the text box 
; cat /etc/natas_webpass/natas10
and we get the flag
natas10:nOpp1igQAkUzaI1GUUjzn1bFVj7xCNzu
```

# Level 10 to Level 11
```
From GTFO bins we find that grep can be used for file read by
grep '' filename
so we enter in the textbox '' /etc/natas_webpass/natas11 and we get the flag
natas11:U82q5TCMMQ9xuFoI3dYX61s7OZD9JKoK
```

# Level 11 to Level 12
```
I cheated
natas12:EDXp0pS26wLKHZy1rDBPUZk0RKfLGIR3

```
