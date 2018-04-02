import RPi.GPIO as GPIO
import time
from time import sleep


GPIO.setmode(GPIO.BOARD)
GPIO.setup(3, GPIO.OUT)
pwm=GPIO.PWM(3, 50)
pwm.start(0)

GPIO.setwarnings(False)


def SetAngle(angle):
        duty = angle / 18 + 2
        GPIO.output(3, True)
        pwm.ChangeDutyCycle(duty)
        sleep(1)
        GPIO.output(3, False)
        pwm.ChangeDutyCycle(0)







t_end = time.time() + 60
while time.time() < t_end:
        SetAngle(0)
        sleep(.1)
        SetAngle(180)
        sleep (.1)
        SetAngle (0)

pwm.stop()

GPIO.cleanup()