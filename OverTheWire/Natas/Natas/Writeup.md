# Natas

## Level 0
```
* Viewing source code of the page gives us password ( Ctrl + u )
* natas1:gtVrDuiDfck831PqWsLEZy5gyDz1clto

```

## Level 0 - 1
```
* Source code gives us password ( Ctrl + u )
* natas2:ZluruAthQk7Q2MqmDeTiUij2ZvWy2mBi

```

## Level 1 - 2
```
* Viewing the source code we see "files/pixel.png"
* Visiting the url "http://natas2.natas.labs.overthewire.org/files" lists directory contents.
* Clicking on users.txt gives us password for the next level.
* natas3:sJIJNW6ucpu6HPZ1ZAchaDtwd7oGrD14

```

## Level 2 - 3
```
* Viewing the source code we find a comment saying "Not even google will find it"
* Google does not index paths listed in /robots.txt file, hence we visit it and find
  /s3cr3t/ directory. 
* Visiting it we get users.txt and the password for the next level.(http://natas3.natas.labs.overthewire.org/s3cr3t/users.txt)
* natas4:Z9tkRkWmpt9Qr7XrR5jWRkgOU901swEZ

```

## Level 3 - 4
```
* Understanding the error on the page, I guessed that the "Referer" header should be set to http://natas5.natas.labs.overthewire.org/
* Intercepting request from burp proxy and adding Referer: http://natas5.natas.labs.overthewire.org/ to the request gives us the 
  password.
* natas5:iX6IOfmpN7AYOQGPwtn3fXpbaJVJcHfq

```
## Level 4 - 5
```
* The page gives error that we are not logged in.
* We check the cookies and change the value of the logged in cookie from 0 to 1.
* Refreshing the page gives us password to next level.
* natas6:aGoY4q2Dc6MgDq4oL4YtoKtyAg9PeHa1
```

## Level 5 - 6
```
* Viewing source code we see a file being included "includes/secret.inc"
* We visit that url but find a blank page.
* Viewing source code reveals the secret.
* Input this value of secret to the box and get the password to next level.
* natas7:7z3hEENjQtflzgnT29q7wAvMNfZdh0i9
```

## Level 6 - 7
```
* We visit the index page and see two links
* Clicking on these links we can see a /?page= parameter being passed in the url.
* Trying LFI ( Local file inclusion ) , I got the password to natas7 from the following url
  (http://natas7.natas.labs.overthewire.org/index.php?page=../../../../../etc/natas_webpass/natas8)
* natas8:DBfUBfqQG69KvJvJ1iAbMoIpwSNQ9bWe

```

## Level 7 - 8
```
* Viewing source code we deduce that the secret is being
  base64 > stringreverse > hex
* Reversing this we will get the secret
  hexdecode > string reverse > base64 decode
* The secret after decoding : oubWYf2kBq
* natas9:W0mMhUcRRnG8dcghE4qvk3JA9lGt8nDl

```

## Level 8 - 9
```
* Viewing the source code we see a passthru() used. 
* Its taking unsanitized input and hence we can try to get RCE ( Remote code execution )
* test; cat /etc/natas_webpass/natas10 # 
* using the above payload we get the natas10 password.
* natas10:nOpp1igQAkUzaI1GUUjzn1bFVj7xCNzu
```

## Level 9 - 10
```
* Viewing souce code we see that special keywords are banned
* grep can be used to print multiple files
* test  /etc/natas_webpass/natas11 will print the password
* natas11:U82q5TCMMQ9xuFoI3dYX61s7OZD9JKoK
```

## Level 10 - 11
```
* It says that cookies are encrypted by XOR Encryption.
* Decoding using code.php provided ( Saw writeup ).
* natas12:EDXp0pS26wLKHZy1rDBPUZk0RKfLGIR3
```

# Level 11-12
```
* Creating a simple php file to read natas13 password
* echo exec("cat /etc/natas_webpass/natas13")
* Upload it and change the extension from jpg to php using burp.
* natas13:jmLTY0qiPZBbaKc9341cqPQZBJv7MQbY
```

## Level 12 - 13
```
* To bypass this I put a GIF8 header before my file and changed the php to jpg
using burp as in previous level.
* natas14:Lg96M10TdfaPyVBkJdjymbllQ5L6qdl1
```

## Level 13-14
```
* This required simple sql injection
* In the admin field i tried to inject sql statement
  natas15 " or 1=1 #
* natas15:AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J
```

## Level 14-15
```
* We are dealing with blind sql injection here
* I created a script for getting the password
* Attached below
* natas16:WaIHEacj63wnNIBROHeqi3p9t0m5nhmh
```
