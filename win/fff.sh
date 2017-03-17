cd
tar jxvf firefox.tar.bz2 -C /usr/lib
rm /usr/bin/firefox
ln -s /usr/lib/firefox/firefox /usr/bin/firefox
exit;
