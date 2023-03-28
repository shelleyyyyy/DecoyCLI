#!/bin/bash
while true
do
   mosquitto_pub -t "sim/tmp" -m $(( $RANDOM % 10 + 60 )) -h "broker.emqx.io"
   sleep 3
done