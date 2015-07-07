import servo, time

print "Blink LED"
time.sleep(1)
servo.move(99,180)

time.sleep(1)
print "Moving Servo 1"
servo.move(1,40)
time.sleep(1)
servo.move(1,140)
time.sleep(1)
print "Moving Servo 2"
servo.move(2,90)
time.sleep(1)
servo.move(2,140)
time.sleep(1)
print "Moving Servo 3"
servo.move(3,0)
time.sleep(1)
servo.move(3,180)
time.sleep(1)
print "Moving Servo 4"
servo.move(4,0)
time.sleep(1)
servo.move(4,180)
time.sleep(1)

print "Exiting"
exit(1)