#!/bin/bash
while true
do
   mosquitto_pub -t "sim/tmp" -m $(( $RANDOM % 50 + 1 )) -h "broker.emqx.io"
   sleep 3
done