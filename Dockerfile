FROM ubuntu:18.04

USER root
WORKDIR /root

COPY ENTRYPOINT.sh /

COPY battery /
COPY battery /
COPY h1_squid.sh /

RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    dnsutils \
    ifupdown \
    iproute2 \
    iptables \
    iputils-ping \
    mininet \
    net-tools \
    openvswitch-switch \
    openvswitch-testcontroller \
    tcpdump \
    vim \
    x11-xserver-utils \
    xterm \
 && rm -rf /var/lib/apt/lists/* \
 && touch /etc/network/interfaces \
 && chmod +x /ENTRYPOINT.sh

# install python3

RUN apt update -y
RUN apt install software-properties-common -y
RUN apt install python3.8 -y

# install pip3

RUN apt update -y
RUN apt install python3-pip -y

# install dependencies

RUN apt install mosquitto-clients -y


# RUN pip3 install -r /requirements.txt
RUN pip3 install neo4j
RUN pip3 install mininet

# create link to controller

RUN ln /usr/bin/ovs-testcontroller /usr/bin/controller 



EXPOSE 6633 6653 6640

ENTRYPOINT ["/ENTRYPOINT.sh"]

# CMD [ "python3", "/miniverse.py", "&"]

# RUN python3 /miniverse.py