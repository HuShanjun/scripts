#!/bin/bash

v1=$(cat /proc/cpuinfo |grep "physical id"|sort |uniq|wc -l)
v2=$(cat /proc/cpuinfo |grep "processor"|wc -l  )
v3=$(cat /proc/cpuinfo |grep "cores"|uniq|cut -d ":" -f2)
v4=$(free -g|grep Mem|awk '{print $2}';)

echo "$v1 physical cpu, $v3 cores, $v2 processor ; total mem:${v4}G"

