# Basic
```
* Name: USB Ripper
* Points: 20
* Category: Forensic
* Flag: HTB{mychemicalromance}
```

# Writeup
````
* Download the tool usbrip
* pip3 install --upgrade usbripper
* usbripper events violations auth.json -f syslog
* MD5 crack the Serial number hash and get the flag
```
