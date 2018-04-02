import gpiozero
import datetime
import urllib.request
import json
import random


from urllib.request import urlopen

import RPi.GPIO as GPIO
import time


# GPIO.output(17,GPIO.LOW)
response = urlopen('http://api.wunderground.com/api/135a2b023c32d48a/hourly/q/au/melbourne.json').read().decode('utf8')
wholething = json.loads(response)
#
# rainwords = [10,11,12,13,14,15,16,17,18,19,20, 21, 22, 23, 24]
#
# #rainwords= list(map(int, rainwords))
#
#
# forecasts = wholething ["hourly_forecast"]
#
#
# #ridiculous
# hour1 = (forecasts [0])
# condit_hr1 = int(hour1 ["fctcode"])
#
# hour2 = (forecasts [1])
# condit_hr2 = int(hour2 ["fctcode"])
#
# hour3 = (forecasts [2])
# condit_hr3 = int(hour3 ["fctcode"])
#
#
# GPIO.output(17,GPIO.HIGH)
# time.sleep(3)
# GPIO.output(17,GPIO.LOW)
#
#
# #stupid
# print (condit_hr1)
# print (condit_hr2)
# print (condit_hr3)

#test only
#condit_hr1 = random.randint(1,15)
#condit_hr2 = random.randint(1,15)
#condit_hr3 = random.randint(1,15)


# #terrible
# if condit_hr1 in rainwords:
#     print ("pack an umbrella")
# else:
#     print ("dry")
#
# if condit_hr2 in rainwords:
#     print ("pack an umbrella")
# else:
#     print ("dry")
#
# if condit_hr3 in rainwords:
#     print ("pack an umbrella")
# else:
#     print ("dry")
#
#
#
#
# if (condit_hr1 in rainwords) or (condit_hr2 in rainwords) or (condit_hr3 in rainwords):
#    print ("cat beckons")
#    GPIO.output(23, GPIO.HIGH)
#    GPIO.output(17,GPIO.HIGH)
##   time.sleep(5)
##   GPIO.output(23,GPIO.LOW)
##   time.sleep(5)
##   GPIO.output(23, GPIO.HIGH)
##   time.sleep(5)
##   GPIO.output(23,GPIO.LOW)
# ##   time.sleep(5)
# ##   GPIO.output(23, GPIO.HIGH)
#
#
# else:
#     print ("cat is still")
#
#
#
#
#
#








