import requests

url = "https://docker.registry.htb/v2"
header = {'Authorization': 'Basic YWRtaW46YWRtaW4='}

filepath = '/home/jkr/HackSpace/misc/wordlist.txt'
with open(filepath) as fp:
   line = fp.readline()
   cnt = 1
   while line:
      # print("Line {}: {}".format(cnt, line.strip()))
       print("Trying: ", line.strip())
       pp = url+'/'+line.strip()
       r = requests.get(pp,headers=header)
       print(r.status_code)
       line = fp.readline()
       cnt += 1
