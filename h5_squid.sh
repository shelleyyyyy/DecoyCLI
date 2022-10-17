#!/bin/bash
while true
do
   mosquitto_pub -t "test" -m "from h5" -h "192.168.174.135"
   sleep 3
done