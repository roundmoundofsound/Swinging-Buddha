import threading

import time
from time import sleep

import logging
#logging.basicConfig(filename= "ticktock.log", format='%(asctime)s %(levelname)-8s %(threadName)s %(funcName)s %(message)s', level=print, )
#logger = logging.getLogger(__name__)


from urllib.request import urlopen


import datetime
import urllib.request
import json

import RPi.GPIO as GPIO
from time import sleep



rainlight = 8
trainlight = 12

GPIO.setmode(GPIO.BOARD)
GPIO.setup(rainlight, GPIO.OUT)
GPIO.setup(trainlight, GPIO.OUT)
GPIO.setwarnings(False)




def fat_controller():
    threading.Timer( (60), fat_controller).start()  # called every 2 minutes
    lowerbound = 300  # min seconds: 5 mins
    upperbound = 600  # max seconds: 10 mins

    gestalt = (datetime.datetime.utcnow())

    response = urlopen(
        'http://timetableapi.ptv.vic.gov.au/v3/departures/route_type/0/stop/1125/route/5?direction_id=1&max_results=2&include_cancelled=false&devid=3000271'
        + '&signature=056F18BC36CA7D08C5AD65524A1C3C7F4E3FC4B9').read().decode('utf8')

    wholething = dict(json.loads(response))
    departuretimes = (wholething["departures"])
    next_train = dict(departuretimes[0])

    nextnext_train = dict(departuretimes[1])

    if (next_train['estimated_departure_utc']) is None:
        next_train_utc = datetime.datetime.strptime(next_train['scheduled_departure_utc'], "%Y-%m-%dT%H:%M:%SZ")
    else:
        next_train_utc = datetime.datetime.strptime(next_train['estimated_departure_utc'], "%Y-%m-%dT%H:%M:%SZ")

    if (nextnext_train['estimated_departure_utc']) is None:
        nextnext_train_utc = datetime.datetime.strptime(nextnext_train['scheduled_departure_utc'], "%Y-%m-%dT%H:%M:%SZ")
    else:
        nextnext_train_utc = datetime.datetime.strptime(nextnext_train['estimated_departure_utc'], "%Y-%m-%dT%H:%M:%SZ")

    print("it is  " + str(time.strftime("%a, %d %b %Y %H:%M:%S")))
    #print("utc now is " + str(gestalt))
    #print("next train at " + str(next_train_utc))
   # print("next train after that is at " + str(nextnext_train_utc))
    seconds_gap = (next_train_utc - gestalt).total_seconds()
    nextseconds_gap = (nextnext_train_utc - gestalt).total_seconds()
    minutes_gap = seconds_gap/60
    nextminutesgap = nextseconds_gap/60
    print("next train gap is " + str(seconds_gap) + " seconds")
    print("next train gap is " + str(minutes_gap) + " minutes")
    print("train after that gap is " + str(nextminutesgap) + " minutes")
    print('2 minutes is 120 seconds, 5 minutes is 300 seconds, 10 minutes is 600 seconds, 20 minutes is 1200 seconds')


    if (int(seconds_gap) in range(lowerbound, upperbound) or int(nextseconds_gap) in range(lowerbound, upperbound)):
        print("trainlight on.")
        GPIO.output(trainlight, GPIO.HIGH)  # on


    else:
        print("trainlight  off")
        GPIO.output(trainlight, GPIO.LOW)  # on


def rain():
    threading.Timer((600), rain).start()  # called every 10 mins
    print("rain function is running. ")
    response = urlopen('http://api.wunderground.com/api/135a2b023c32d48a/hourly/q/au/Melbourne.json').read().decode('utf8')
    wholething = json.loads(response)

    rainwords = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]

    forecasts = wholething["hourly_forecast"]

    # ridiculous
    hour1 = (forecasts[0])
    condit_hr1 = int(hour1["fctcode"])

    hour2 = (forecasts[1])
    condit_hr2 = int(hour2["fctcode"])
    
    hour3 = (forecasts[2])
    condit_hr3 = int(hour3["fctcode"])



# stupid
    print(condit_hr1)
    print(condit_hr2)
    print(condit_hr3)


# terrible
    if condit_hr1 in rainwords:
        print("pack an umbrella")
    else:
     print("dry")

    if condit_hr2 in rainwords:
        print("pack an umbrella")
    else:
        print("dry")

    if condit_hr3 in rainwords:
     print("pack an umbrella")
    else:
        print("dry")

    if (condit_hr1 in rainwords) or (condit_hr2 in rainwords) or (condit_hr3 in rainwords):
        print("gonna rain, light up the rain light")
        GPIO.output(rainlight, GPIO.HIGH)  # on



    else:
        print("Rain light off. Its dry.")
        GPIO.output(rainlight, GPIO.LOW)  # off



fat_controller()
sleep(15)
rain()

GPIO.cleanup()
