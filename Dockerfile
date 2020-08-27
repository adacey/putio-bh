FROM python:3.8-slim

MAINTAINER Andrew Dacey <adacey@gmail.com>

ENV	CONFIG_DIR	/config
ENV	HOME		$CONFIG_DIR
ENV	BASE_DIR	/data/torrent
ENV	BLACKHOLE_DIR	$BASE_DIR/watch
ENV	COMPLETE_DIR	$BASE_DIR
ENV	INCOMPLETE_DIR	$BASE_DIR/incomplete
ENV 	UID	99
ENV	GID	100

RUN	mkdir -p $CONFIG_DIR && \
	mkdir -p $BASE_DIR && \
	mkdir -p $BLACKHOLE_DIR && \
	mkdir -p $COMPLETE_DIR && \
	mkdir -p $INCOMPLETE_DIR

RUN	pip install --no-cache-dir putio.py
RUN	useradd -d "$HOME" \
	-g $GID \
	-u $UID \
	putio
WORKDIR	$CONFIG_DIR
COPY	putio-bh.py /usr/src/myapp/ 
COPY	config.json $CONFIG_DIR
RUN	chmod 755 /usr/src/myapp/putio-bh.py && \
	chown -R putio $CONFIG_DIR && \
	chown -R putio $BASE_DIR

USER	putio
ENV	PATH	/usr/src/myapp:$PATH
VOLUME	["/config","$BASE_DIR"]

ENTRYPOINT ["putio-bh.py"]
