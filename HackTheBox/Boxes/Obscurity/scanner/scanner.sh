#!/bin/bash

cat test.txt | while read line ; 
do
  echo Attempt $line
  wget http://10.10.10.168:8080/$line/SuperSecureServer.py > /dev/null
done
