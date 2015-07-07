import os, sys, inspect, thread, time
src_dir = os.path.dirname(inspect.getfile(inspect.currentframe()))
arch_dir = '../lib/x64' if sys.maxsize > 2**32 else '../lib/x86'
sys.path.insert(0, os.path.abspath(os.path.join(src_dir, arch_dir)))

import time
import servo
import Leap
from Leap import CircleGesture, KeyTapGesture, ScreenTapGesture, SwipeGesture
		
def getAverage(controller):
	#Average a hand position for the last 10 frames
	count = 0
	average = Leap.Vector()
	hand_to_average = controller.frame().hands[0]
	for i in range(0,9):
	    hand_from_frame = controller.frame(i).hand(hand_to_average.id)
	    if(hand_from_frame.is_valid):
	        average = average + hand_from_frame.palm_normal
	        count += 1
	average = average/count
	return average

def getAngle(controller):
	print "Press Enter to define start angle..."
	sys.stdin.readline()
	starting_angle = controller.frame()
	print "Press Enter to define stop angle..."
	sys.stdin.readline()
	angle = controller.frame().hands[0].rotation_angle(starting_angle) # Get angle change between now and previous frame.
	return angle


def otherstuff():
	frame = controller.frame()
	hands = frame.hands
	hand = hands[0]
# Get normal vector for the hand
	position = hand.palm_position
	velocity = hand.palm_velocity
	normal = hand.palm_normal
	direction = hand.direction
	#print normal
	print position
	#Lookup moving average

def main():
	controller = Leap.Controller()

	while not(controller.is_connected):
		print "Waiting for controller..."
		time.sleep(1)
	print "Connected!"

	while controller.is_connected:
		#average = getAverage(controller)
		#print average
		angle = getAngle(controller)
		print "Angle of rotation in radians = %s" % angle
		time.sleep(.5)
	

	servo.move(99,0)
	time.sleep(2)
	servo.move(99,180)
	time.sleep(2)
	

		#processFrame(controller.frame(20))

if __name__ == "__main__":
	main()