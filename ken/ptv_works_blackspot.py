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


lowerbound = 250 #min seconds: 4 and a bit mins
upperbound = 600 #max seconds: 10 mins

gestalt = (datetime.utcnow())


response = urlopen('http://timetableapi.ptv.vic.gov.au/v3/departures/route_type/0/stop/1125/route/5?direction_id=1&max_results=1&devid=3000271&'
                   +'signature=1B35067000E6A61BAE72DC913193BF9F148113BA').read().decode('utf8')
wholething = dict(json.loads(response))


departuretimes = (wholething["departures"])

next_train = dict(departuretimes[0])

if (next_train ['estimated_departure_utc']) is None:
    next_train_utc = datetime.strptime(next_train ['scheduled_departure_utc'], "%Y-%m-%dT%H:%M:%SZ" )
else: next_train_utc = datetime.strptime(next_train ['estimated_departure_utc'], "%Y-%m-%dT%H:%M:%SZ" )


print ("utc now is " +str(gestalt) )

print ("next train at " + str(next_train_utc))

seconds_gap = (next_train_utc - gestalt).total_seconds()

print ("gap is " + str(seconds_gap) + " seconds")

print ('2 minutes is 120 seconds, 5 minutes is 300 seconds, 10 minutes is 600 seconds, 20 minutes is 1200 seconds')

if int(seconds_gap) in range(lowerbound, upperbound):
    print ("wiggle")
    wiggle = "yes"
else:
    wiggle = "no"
    print("do not wiggle")

print(wiggle)



# wigglestart = next_train_utc - upperbound
#
# wigglestop = next_train_utc - lowerbound

# wiggletime = int(seconds_gap) - lowerbound
#
# wiggle_countdown  = int(seconds_gap) - upperbound

# print ("countdown to wiggle time is" + str(wiggle_countdown) + " seconds")
#
#
# print ("duration of wiggle time would be " + str(wiggletime) + " seconds")




# if wiggle = "yes":
#         for pulse in range(50, 250, .5):
#                 wiringpi.pwmWrite(18, pulse)
#                 time.sleep(delay_period)
#         for pulse in range(250, 120, -.5):
#                 wiringpi.pwmWrite(18, pulse)
#                 time.sleep(delay_period)
