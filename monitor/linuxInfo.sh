#!/bin/bash

v1=$(cat /proc/cpuinfo |grep "physical id"|sort |uniq|wc -l)
v2=$(cat /proc/cpuinfo |grep "processor"|wc -l  )
v3=$(cat /proc/cpuinfo |grep "cores"|uniq)
v4=$(free -g|grep Mem|awk '{print $2}';)

echo "$v1physical cpu, $v2 cores, $v3 processor ; total mem:$v4G"
