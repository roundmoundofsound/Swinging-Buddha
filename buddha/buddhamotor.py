import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)

Motor = 16
Light = 18


GPIO.setup(Motor, GPIO.OUT)
GPIO.setup(Light, GPIO.OUT)



print ("Turning motor on")


#resonant frequency is around 2.8 hz (.35 of a second)

#go for 1.05 sec freq

counter = 0

while counter <= 40:  # 42 of these cycles make up a minute
    GPIO.output(Motor, GPIO.HIGH)  # on
    GPIO.output(Light, GPIO.HIGH)  # on

    print("feel the force, buddha. magnet on.")
    # threadsopen = threading.active_count()
    # print(threadsopen)

    sleep(.72)

    GPIO.output(Motor, GPIO.LOW)  # off
    GPIO.output(Light, GPIO.LOW)  # off

    print("magnet off.")

    sleep(1.8)

    counter += 1

print("Stop moving. Turning magnet off")

