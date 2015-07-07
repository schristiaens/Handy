import servo, time

#print "Blink LED"
#time.sleep(1)
#servo.move(99,180)

# servo.move(1,90)
# servo.move(1,90)
# servo.move(1,90)
# servo.move(1,90)

time.sleep(1)
print "Moving Servo 1"
servo.move(1,150)

time.sleep(1)
print "Moving Servo 2"
servo.move(2,150)

time.sleep(1)
print "Moving Servo 3"
servo.move(3,10)

time.sleep(1)
print "Moving Servo 4"
servo.move(4,10)

print "Finished"
exit(1)