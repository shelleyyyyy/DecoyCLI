#!/bin/bash
while true
do
   mosquitto_pub -t "test" -m "from h1" -h "192.168.174.135"
   sleep 3
done