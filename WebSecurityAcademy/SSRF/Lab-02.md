# Lab: Basic SSRF against another back-end system

## Description
```
This lab has a stock check feature which fetches data from an internal system.
To solve the lab, use the stock check functionality to scan the internal 192.168.0.X 
range for an admin interface on port 8080, then use it to delete the user carlos
```
## Solution
* Steps similar to Lab-01
* Sending the request to intruder and fuzzing ( Numbers from 1 to 255 )
* The 200 request is the one and then we can delete user carlos
