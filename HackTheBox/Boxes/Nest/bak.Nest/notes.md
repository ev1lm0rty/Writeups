# Basic
* Name : Nest
* IP: 10.10.10.178
* Level : Easy
* Box : Windows

# Creds
* welcomeemail- TempUser:welcome2019
* c.smith:xRxRxPANCAK3SxRxRx
* HQK:WBQ201953D8w 

# Flags
* user: cf71b25404be5d84fd827e05f426e987

# Enumeration
* Use -Pn flag in nmap scan
* logged in smb share
* found creds at "\Shared\Templates\HR\Welcome Email.txt"
* Logged in using TempUser to Secure$ share
* Found config file with a hash
* Found IT\Carl directory
* Found a vb file and modified it to get password
* dotnetfiddle

# Exploitation
* Got user C.Smith
* Found a file debug mode password in the share
* `allinfo Debug mode password.txt`
* `get "Debug mode password.txt:Password`
* found debug mode password
