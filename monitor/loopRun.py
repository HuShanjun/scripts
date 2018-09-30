# coding: utf8
import os
import subprocess
import sys
import time

cmd = sys.argv[1]
timelength = float(sys.argv[2])
exargs = sys.argv[3]
count = 0
print('start run [%s]!' % cmd)
print('sustain [%f] hour!' % timelength)
print('startTime:%s' % (time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))))
last_time = time.time()
while True:
    count = count + 1
    if time.time() - last_time >= 60 * 60 * timelength:
        print ('already running：%d' % (time.time() - last_time))
        print('endTime:%s' % time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
        break
    try:
        r = subprocess.check_output("%s %s" % (cmd, exargs), shell=True)
        print("finish %d times" % count)
        print(r)
    except Exception as e:
        print("----------No %d run failed ----------" % count)
        print(e)
