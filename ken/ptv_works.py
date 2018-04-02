import gpiozero
import datetime
import urllib.request
import json
import random
import pprint
from datetime import datetime
from urllib.request import urlopen
from datetime import timedelta

import RPi.GPIO as GPIO
import time


response = urlopen('http://timetableapi.ptv.vic.gov.au/v3/departures/route_type/0/stop/1125/route/5?direction_id=1&max_results=1&devid=3000271&'
                   +'signature=1B35067000E6A61BAE72DC913193BF9F148113BA').read().decode('utf8')
wholething = dict(json.loads(response))

#pp = pprint.PrettyPrinter(indent=4)

#pp.pprint(wholething)

departuretimes = (wholething["departures"])

next_train = dict(departuretimes[0])

next_train_utc = datetime.strptime(next_train ['estimated_departure_utc'], "%Y-%m-%dT%H:%M:%SZ" )

print ("next train utc is " + str(next_train_utc))

gestalt = (datetime.utcnow())

print ("utc now is " +str(gestalt) )


#nexttrain = (wholething["departures"] ['estimated_departure_utc'])

seconds_gap = (next_train_utc - gestalt).total_seconds()


print ("gap is " + str(seconds_gap) + "seconds")

lowerbound = 250 #min seconds
upperbound = 500 #max seconds


if seconds_gap in range(lowerbound, upperbound):
    print ("wiggle")




