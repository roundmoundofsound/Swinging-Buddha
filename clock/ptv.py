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
# GPIO.setmode(GPIO.BOARD)
#
# GPIO.setup(3, GPIO.OUT)
# pwm=GPIO.PWM(3, 50)
# pwm.start(0)




pp = pprint.PrettyPrinter(indent=4)

#
#
# #setup servo
# def SetAngle(angle):
#     duty = angle / 18 + 2
#     GPIO.output(3, True)
#     pwm.ChangeDutyCycle(duty)
#     sleep(1)
#     GPIO.output(3, False)
#     pwm.ChangeDutyCycle(0)


lowerbound = 250 #min seconds: 4 and a bit mins
upperbound = 600 #max seconds: 10 mins

gestalt = (datetime.utcnow())

response = urlopen('http://timetableapi.ptv.vic.gov.au/v3/departures/route_type/0/stop/1125/route/5?direction_id=1&max_results=2&include_cancelled=false&devid=3000271'
+'&signature=056F18BC36CA7D08C5AD65524A1C3C7F4E3FC4B9').read().decode('utf8')


wholething = dict(json.loads(response))
departuretimes = (wholething["departures"])




next_train = dict(departuretimes[0])

nextnext_train = dict(departuretimes[1])


if (next_train ['estimated_departure_utc']) is None:
    next_train_utc = datetime.strptime(next_train ['scheduled_departure_utc'], "%Y-%m-%dT%H:%M:%SZ" )
else: next_train_utc = datetime.strptime(next_train ['estimated_departure_utc'], "%Y-%m-%dT%H:%M:%SZ" )


if (nextnext_train ['estimated_departure_utc']) is None:
    nextnext_train_utc = datetime.strptime(nextnext_train ['scheduled_departure_utc'], "%Y-%m-%dT%H:%M:%SZ" )
else: nextnext_train_utc = datetime.strptime(nextnext_train ['estimated_departure_utc'], "%Y-%m-%dT%H:%M:%SZ" )



print ("utc now is " +str(gestalt) )
print ("next train at " + str(next_train_utc))
print ("next train after that is at " + str(nextnext_train_utc))



seconds_gap = (next_train_utc - gestalt).total_seconds()
nextseconds_gap = (nextnext_train_utc - gestalt).total_seconds()

print ("next train gap is " + str(seconds_gap) + " seconds")
print ("train after that gap is " + str(nextseconds_gap) + " seconds")
print ('2 minutes is 120 seconds, 5 minutes is 300 seconds, 10 minutes is 600 seconds, 20 minutes is 1200 seconds')

if (int(seconds_gap) in range(lowerbound, upperbound) or int(nextseconds_gap) in range(lowerbound, upperbound)):
     print ("wiggle")
     wiggle = "yes"
else:
     wiggle = "no"
     print("do not wiggle")

print(wiggle)
print (type(wiggle))

#if wiggle = "yes":
 #   t_end = time.time() + 60
 #   while time.time() < t_end:
 #       SetAngle(90)
        # sleep(.1)
        # SetAngle(87)
        # sleep (.1)
 #       SetAngle(91)
        # sleep (.1)
        # SetAngle(88)
        # sleep (.1)

  #  pwm.stop()

# GPIO.cleanup()



# if wiggle = "yes":
#         for pulse in range(50, 250, .5):
#                 wiringpi.pwmWrite(18, pulse)
#                 time.sleep(delay_period)
#         for pulse in range(250, 120, -.5):
#                 wiringpi.pwmWrite(18, pulse)
#                 time.sleep(delay_period)
