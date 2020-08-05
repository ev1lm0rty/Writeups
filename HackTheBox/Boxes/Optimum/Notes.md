# Optimum
```
* IP: 10.10.10.8
* Level: Easy
* Box: Windows
```

# Flags
```
* User: d0c39409d7b994a9a1389ebf38ef5f73
* Root: 51ed1b36553c8461f4552c2e92b3eeed

```

# Enumeration
```
* Port 80 looks something non-standard.
* HFS 2.3 looks exploitatble.
* Metasploit exploit (windows/http/rejetto_hfs_exec) worked.
```

# Exploitatation
```
* Metasploit gave us the user shell.
* Running exploit suggestor on the our meterpreter session gave us
  and exploit (windows/local/ms16_032_secondary_logon_handle_privesc)
* Running this gave us the system shell

```
