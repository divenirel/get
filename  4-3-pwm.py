import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(22, GPIO.OUT, initial = 0)

p = GPIO.PWM(22, 1000)
def ChangeDutyCycle(dutycycle):
        p.start(dutycycle)


try:
    while True:
        inputSt = input("Вdtlbnt 0 -100; 'q' xnj,s dsqnb:")

        if inputSt.isdigit():
            dutycycle = int(inputSt)
            if dutycycle > 100:
                print("Ошиб0чка")
                continue
            ChangeDutyCycle(dutycycle)
            print(str(3.3 * dutycycle /100) + " V ")
        elif inputSt == 'q':
            break
        else:
            print("Ошиб0чка")    
finally:
    p.stop()
    GPIO.cleanup()

            