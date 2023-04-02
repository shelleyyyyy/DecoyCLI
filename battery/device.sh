#!/bin/bash

device=$1
topic=$2
broker="broker.emqx.io"

if [[ $device == "temp" ]]; then
  while true; do
    value=$(echo "scale=2; 50 + $RANDOM % 11" | bc)
    mosquitto_pub -h $broker -t $topic -m "$value"
    sleep 1
  done
elif [[ $device == "ph" ]]; then
  while true; do
    value=$(echo "scale=2; $RANDOM / 32767" | bc)
    mosquitto_pub -h $broker -t $topic -m "$value"
    sleep 1
  done
else
  echo "Invalid device: $device"
  exit 1
fi
