# Write your code here :-)
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO_TRIGGER = 18
GPIO_ECHO = 20
GPIO_LED = 4

GPIO.setup(GPIO_ECHO, GPIO.IN)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_LED, GPIO.OUT)

def distance():
    GPIO.output(GPIO_TRIGGER, True)

    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)

    StartTime = time.time()
    StopTime = time.time()

    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()

    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()

    TimeElapsed = StopTime - StartTime
    distance = (TimeElapsed * 34300) / 2

    return distance

if __name__ == '__main__':
    pwm = GPIO.PWM(4, 100)
    dc = 0
    pwm.start(dc)
    try:
        while True:
            dist = distance()
            print("distance=%.1f cm" % dist)
            if dist > 100:
                dist = 100
            pwm.ChangeDutyCycle(dist)
            time.sleep(1)
    except KeyboardInterrupt:
        print("stopped")

