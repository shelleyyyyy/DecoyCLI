#!/bin/bash
while true
do
   mosquitto_pub -t "sim/tmp" -m $(( $RANDOM % 50 + 1 )) -h "192.168.1.177"
   sleep 3
done