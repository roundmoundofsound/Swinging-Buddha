import threading
import random
import time
from time import sleep

import logging
from urllib.request import urlopen


import datetime
import urllib.request
import json

Motor = 16
Light = 18



wiggle = 0


def fat_controller():
    threading.Timer( (10), fat_controller).start()  # called every 2 minutes

    global wiggle
    lowerbound = 300  # min seconds: 5 mins
    upperbound = 600  # max seconds: 10 mins

    gestalt = (datetime.datetime.utcnow())

    wiggle = random.randint(0, 1)
    print(wiggle)



def wiggler ():
    threading.Timer( (10), wiggler).start()  # called every 2 minutes


    while wiggle is 1:
        sleep(2)
        print ("wiggle is one")
        threadsopen = threading.active_count()
        print(threadsopen)





fat_controller()
sleep(5)
wiggler()
sleep (5)
#rain()

##GPIO.cleanup()
