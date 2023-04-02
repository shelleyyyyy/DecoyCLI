FROM iwaseyusuke/mininet

USER root
WORKDIR /app

# COPY ENTRYPOINT.sh /

COPY battery /app
COPY h1_squid.sh /app

# RUN apt-get update && apt-get install -y --no-install-recommends \
#     curl \
#     dnsutils \
#     ifupdown \
#     iproute2 \
#     iptables \
#     iputils-ping \
#     mininet \
#     net-tools \
#     openvswitch-switch \
#     openvswitch-testcontroller \
#     tcpdump \
#     vim \
#     x11-xserver-utils \
#     xterm \
#     nano \
#  && rm -rf /var/lib/apt/lists/* \
#  && touch /etc/network/interfaces \
#  && chmod +x /ENTRYPOINT.sh

RUN apt update -y

RUN apt install nano

# install python3

# RUN apt update -y
RUN apt install software-properties-common -y
RUN apt install python3.8 -y

# install pip3

# RUN apt update -y
RUN apt install python3-pip -y

# install dependencies

RUN apt install mosquitto-clients -y
RUN apt install bc


# RUN pip3 install -r /requirements.txt
RUN pip3 install neo4j
RUN pip3 install mininet
RUN pip3 install paho-mqtt

# create link to controller

RUN ln /usr/bin/ovs-testcontroller /usr/bin/controller 

CMD ["python3", "/app/miniverse.py"]

# EXPOSE 6633 6653 6640

# ENTRYPOINT ["/ENTRYPOINT.sh"]

# CMD [ "python3", "/miniverse.py", "&"]

# RUN python3 /miniverse.py