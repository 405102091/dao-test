cd
wget https://ftp.mozilla.org/pub/firefox/releases/50.0/linux-x86_64/en-US/firefox-50.0.tar.bz2 -O firefox.tar.bz2
tar jxvf firefox.tar.bz2 -C /usr/lib 
rm /usr/bin/firefox
ln -s /usr/lib/firefox/firefox /usr/bin/firefox 
bash check.sh
