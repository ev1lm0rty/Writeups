# Info
```
* Name: Cat
* Category: Android
* Points: 20
* Released: 17 Mar 2020
````
# Flag
* HTB{ThisBackupIsUnprotected}

# Writeup
```
* Run the following command
  ( printf "\x1f\x8b\x08\x00\x00\x00\x00\x00" ; tail -c +25 cat.ab ) |  tar xfvz -
* Traverse to shared/0/Pictures
* Zoom in to the picture and find the flag in bottom.
```
