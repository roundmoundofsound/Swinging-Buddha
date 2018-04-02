import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)

Motor = 12


GPIO.setup(Motor, GPIO.OUT)



print ("Turning motor on")


#resonant frequency is around 2.8 hz (.35 of a second)

#go for 1.05 sec freq

counter = 0
while counter <= 30:
    GPIO.output(Motor, GPIO.HIGH) #on

    sleep(.04)


    GPIO.output(Motor, GPIO.LOW) #off


    sleep (1.01)

    print("go jesus")

    counter += 1


print ("Turning motor off")

GPIO.output(Motor, GPIO.LOW)

GPIO.cleanup()