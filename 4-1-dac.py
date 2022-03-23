import RPi.GPIO as GPIO
import time

dac = [26, 19, 13, 6, 5, 11, 9, 10]

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT) 

def decmal2binary(value):
    return[int(bit) for bit in bin(value)[2:].zfill(8)]

def isint(n):
    try:
        int(n)
        return True
    except ValueError:
        return False

try:
    print("Сколько яиц в корзине") 
    n = int(input())
except ValueError:
    print("Это не яйца.")
except TypeError:
    print("Это разбитые яйца.")
else:
    if n < 0:
        print("Яиц сликом мало.")
    if n > 255:
        print("Яиц слишком много.")

    number = decmal2binary(n)
    GPIO.output(dac, number)
    time.sleep(7)

    print("Напряжение DAC плюс минус равно", 3.3*n/256) 

finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()