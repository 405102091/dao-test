# tonido
FROM ubuntu:16.04
MAINTAINER xiaofd <admin@chit.cf>

RUN sed -i "s#archive.ubuntu.com#us.archive.ubuntu.com#g" /etc/apt/sources.list

RUN apt update && \
	apt clean  && \
	apt install -y wget tmux libjpeg8 libfontconfig1 --no-install-recommends && \
	apt clean && \
	rm -rf /var/lib/apt/lists/*

RUN mkdir /usr/local/tonido && \
	cd /usr/local/tonido && \
	wget http://www.tonido.com/download.php?tonido64.tar.gz -O tonido.tar.gz && \
	tar -zxvf tonido.tar.gz && \
	rm tonido.tar.gz
	
RUN cd /usr/local/tonido && \
	echo "#!/bin/bash" > locrun.sh && \
 	echo "/usr/local/tonido/tonido.sh start" >> locrun.sh && \
	echo "top" >> locrun.sh && \
	chmod +x locrun.sh
	
EXPOSE 10001

ENTRYPOINT ["/usr/local/tonido/locrun.sh"]
