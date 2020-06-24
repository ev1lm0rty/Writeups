# Info
```
* Name: Resolute
* IP: 10.10.10.169
* Box: Windows
* Level: Medium
```

# Flags
```
User:0c3be45fcfe249796ccbee8d3a978540
Root:e1d94876a506850d0c20edb5405e619c
```

# Creds
```
* melanie:Welcome123! (smb)
* ryan: Serv3r4Admin4cc123!
```
# Enumeration
```
## Intresting
  * Enum4linux gathered bunch of passwords.
  * Got many usernames

## Findings
  * Got login on smb with melanie:Welcome123!
```

# Exploitation
```
##Login
  * evil winrm got shell as melanie
  * Got user.txt

## Privesc
  * using `dir -force` I found a hidden pstranscripts directrory.
  * Inside that i found ryan's password

## Root
  * use psexec psh module in metasploit I got root.

```
