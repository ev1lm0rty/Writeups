# Lab: Basic SSRF against the local server

## Description
```
This lab has a stock check feature which fetches data from an internal system.
To solve the lab, change the stock check URL to access the admin interface at http://localhost/admin and delete the user carlos. 
```

## Solution
* Visit 'View Details' section of any one item.
* Intercept the "Stock" request
* Change the stock api to "http://localhost/admin" (URL encode)
* We are returned an admin page from which we can delete the 'carlos' user
* Then we change the stock api to "http://localhost/admin?deleteuser=carlos" (url encode)
* Lab solved
