FROM ubuntu:16.04

ENV HOME /root
ENV DEBIAN_FRONTEND noninteractive
# desktop env
RUN apt-get update \
	&& apt-get install -y supervisor \
		openssh-server vim tmux \
		xfce4 xfce4-goodies \
		x11vnc xvfb \
		python3-pip \
		libappindicator1 libdbusmenu-glib4 libdbusmenu-gtk4 libindicator7 libpango1.0 gdebi-core \
	&& wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb \
	&& gdebi -n google-chrome-stable_current_amd64.deb \
	&& rm google-chrome-stable_current_amd64.deb \
	&& apt-get autoclean \
	&& apt-get autoremove \
	&& rm -rf /var/lib/apt/lists/*
	
RUN pip3 install -U pip && pip install -U selenium shadowsocks ipython pyvirtualdisplay requests_toolbelt chardet

RUN wget https://chromedriver.storage.googleapis.com/2.29/chromedriver_linux64.zip \
	&& unzip chromedriver_linux64.zip \
	&& mv chromedriver /usr/bin

# flash
RUN sed "s|#\(.*multiverse\)|\1|g" /etc/apt/sources.list -i \
	&& apt-get update \
	&& apt-get install -y flashplugin-installer \
	&& apt-get autoclean \
	&& apt-get autoremove \
	&& rm -rf /var/lib/apt/lists/*
	
# another firefox 
#RUN wget https://ftp.mozilla.org/pub/firefox/releases/50.0/linux-x86_64/en-US/firefox-50.0.tar.bz2 -O firefox.tar.bz2 \
#	&& tar jxvf firefox.tar.bz2 -C /usr/lib \
#	&& ln -s /usr/lib/firefox/firefox /usr/bin/firefox \
#	&& rm firefox.tar.bz2

#RUN mkdir -p '/usr/share/mozilla/extensions/{ec8030f7-c20a-464f-9b0e-13a3a9e97384}' \
#	&& cd '/usr/share/mozilla/extensions/{ec8030f7-c20a-464f-9b0e-13a3a9e97384}' \
#	#&& cd /usr/lib/firefox/browser/features \
#	&& wget https://www.ebesucher.com/data/firefoxaddon/latest.xpi -O 'jid1-GxlI1BHOBUCNhw@jetpack.xpi' \
#	&& chmod 0755 'jid1-GxlI1BHOBUCNhw@jetpack.xpi' \
#	&& wget https://addons.cdn.mozilla.net/user-media/addons/774177/vagex-2.2.5-fx.xpi -O 'contact@vagex.com.xpi' \
#	&& chmod 0755 'contact@vagex.com.xpi' \
#	&& wget https://s3.amazonaws.com/com.alexa.toolbar/autoupdate/alxf/alxf-3.0.2.xpi -O 'alx-ffdeveloper@amazon.com.xpi' \
#	&& chmod 0755 'alx-ffdeveloper@amazon.com.xpi' \
#	&& cp * /usr/lib/firefox/browser/features

WORKDIR /root

ADD startup.sh ./
ADD supervisord.conf ./
ADD passwd ./
ADD ameblocal.py ./

RUN chmod 0600 passwd \
	&& chmod +x startup.sh

EXPOSE 5900
EXPOSE 22

ENTRYPOINT ["./startup.sh"]
