# Basic

```
* Room : Blue
* Tasks: 
* Level: Easy
* IP: 10.10.199.156

```

# Tasks

```
1. Scan the machine 
  (Done)

2.How many ports are open with a port number under 1000?
  (3)

3. What is this machine vulnerable to?
  (ms17-010)

4. Start Metasploit
  (Done)

5.Find the exploitation code we will run against the machine. What is the full path of the code ?
  (exploit/windows/smb/ms17_010_eternalblue_win8)

6. Show options and set the one required value. What is the name of this value?
  (rhosts)

7. Run the exploit!
  (Done)

8. Escalate and find the name of the post module that we will use
  (Done| post/multi/manage/shell_to_meterpreter)

9. Which option is to be changed ?
  (SESSION)

10. Set the required option, you may need to list all of the sessions to find your target here.
  (Done)

11.Run! If this doesn't work, try completing the exploit from the previous task once more
  (Done)

12.Once the meterpreter shell conversion completes, select that session for use.
  (Done)

13. Run getsystem
  (Done)

14. Name of non default user
  (Jon)

15. Password
  (alqfna22)

##### search -f flag*.txt #####
16. Flag1
  (flag{access_the_machine})

17. Flag2
  (flag{sam_database_elevated_access})

18. Flag3
  (flag{admin_documents_can_be_valuable})
