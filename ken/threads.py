import threading
import time
import gpiozero
import datetime
import urllib.request
import json
import random
import pprint
from datetime import datetime
from urllib.request import urlopen
from datetime import timedelta
import time
#import RPi.GPIO as GPIO
import time
from time import sleep

import logging
logging.basicConfig(level=logging.DEBUG)
logging.basicConfig(filename="trains.log", format = '%(asctime)s %(levelname)-8s %(message)s', level=logging.DEBUG)



from random import *

x = randint(1, 3)

wiggle = 0

def fat_controller():
    threading.Timer( (90), fat_controller).start()  # called every 2 minutes

    global wiggle
    lowerbound = 250  # min seconds: 4 and a bit mins
    upperbound = 600  # max seconds: 10 mins

    gestalt = (datetime.utcnow())

    response = urlopen(
        'http://timetableapi.ptv.vic.gov.au/v3/departures/route_type/0/stop/1125/route/5?direction_id=1&max_results=2&include_cancelled=false&devid=3000271'
        + '&signature=056F18BC36CA7D08C5AD65524A1C3C7F4E3FC4B9').read().decode('utf8')

    wholething = dict(json.loads(response))
    departuretimes = (wholething["departures"])
    next_train = dict(departuretimes[0])

    nextnext_train = dict(departuretimes[1])

    if (next_train['estimated_departure_utc']) is None:
        next_train_utc = datetime.strptime(next_train['scheduled_departure_utc'], "%Y-%m-%dT%H:%M:%SZ")
    else:
        next_train_utc = datetime.strptime(next_train['estimated_departure_utc'], "%Y-%m-%dT%H:%M:%SZ")

    if (nextnext_train['estimated_departure_utc']) is None:
        nextnext_train_utc = datetime.strptime(nextnext_train['scheduled_departure_utc'], "%Y-%m-%dT%H:%M:%SZ")
    else:
        nextnext_train_utc = datetime.strptime(nextnext_train['estimated_departure_utc'], "%Y-%m-%dT%H:%M:%SZ")

    print("utc now is " + str(gestalt))
    print("next train at " + str(next_train_utc))
    print("next train after that is at " + str(nextnext_train_utc))
    seconds_gap = (next_train_utc - gestalt).total_seconds()
    nextseconds_gap = (nextnext_train_utc - gestalt).total_seconds()

    print("next train gap is " + str(seconds_gap) + " seconds")
    print("train after that gap is " + str(nextseconds_gap) + " seconds")
    print('2 minutes is 120 seconds, 5 minutes is 300 seconds, 10 minutes is 600 seconds, 20 minutes is 1200 seconds')


    if (int(seconds_gap) in range(lowerbound, upperbound) or int(nextseconds_gap) in range(lowerbound, upperbound)):
        print("this is the fat controller.")
        print("wiggle now")
        wiggle = 1
    else:
        wiggle = 0
        print("do not wiggle.")

    print(wiggle)



def wiggler ():
    global wiggle
    threading.Timer(90, wiggler).start()  # called every minute
    if wiggle is (1):
        print(wiggle)
        print ("This is the wiggler. I am wiggling now.")
    else:
        print(wiggle)
        print ("This is the wiggler. I am still.")



fat_controller()
sleep(15)
wiggler()






