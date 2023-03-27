FROM ubuntu:18.04

USER root
WORKDIR /root

COPY ENTRYPOINT.sh /

COPY battery /
COPY battery /

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
RUN apt install python3.8

# install pip3

RUN apt update -y
RUN apt install python3-pip

# install dependencies

RUN pip install -r battery/requirements.txt

EXPOSE 6633 6653 6640

ENTRYPOINT ["/ENTRYPOINT.sh"]
