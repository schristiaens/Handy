import os, sys, inspect, thread, time, kinematics
src_dir = os.path.dirname(inspect.getfile(inspect.currentframe()))
arch_dir = '../lib/x64' if sys.maxsize > 2**32 else '../lib/x86'
sys.path.insert(0, os.path.abspath(os.path.join(src_dir, arch_dir)))

import servo
import Leap
from Leap import CircleGesture, KeyTapGesture, ScreenTapGesture, SwipeGesture
global reference_frame
global initCount
global Enable_flag
global hand_state
initCount=0

def getAngle(controller):
	global measurements
	global angleAverage
	global initCount
	
	global measurementOne
	global measurementTwo
	global measurementThree
	global measurementFour
	global measurementFive
		
		
	
	if initCount==0:
		measurementOne=[0,0,0,0]
		measurementTwo=[0,0,0,0]
		measurementThree=[0,0,0,0]
		measurementFour=[0,0,0,0]
		measurementFive=[0,0,0,0]
		angleAverage=[0,0,0,0]
	while (initCount<6):
		initCount+=1

		measurementOld=measurementFive
		measurementFive=measurementFour
		measurementFour=measurementThree
		measurementThree=measurementTwo
		measurementTwo=measurementOne
		measurementOne=kinematics.calcFourAngles(controller)

		j=0
		while j<4:
			angleAverage[j]=angleAverage[j]+0.2*measurementOne[j]-0.2*measurementOld[j]
			j+=1


	param1 = 0
	while param1 == 0:
#		sys.stdin.readline()

		measurementOld=measurementFive
		measurementFive=measurementFour
		measurementFour=measurementThree
		measurementThree=measurementTwo
		measurementTwo=measurementOne
		measurementOne=kinematics.calcFourAngles(controller)		
		
		if measurementOne[2]>0:
			param1=1
		
		j=0
		while j<4:
			angleAverage[j]=angleAverage[j]-0.2*measurementOld[j]+0.2*measurementOne[j]
			j+=1
		#print angleAverage

	return angleAverage

def check_gesture(frame):
	if len(frame.hands) is 2:
		#if frame.gestures()[0].type is Leap.Gesture.TYPE_CIRCLE:
		if frame.gestures()[0].type is Leap.Gesture.TYPE_SWIPE:
			#if frame.gestures()[0].state is Leap.Gesture.STATE_STOP:
			for gesture in frame.gestures():
				if frame.gestures()[0].state is Leap.Gesture.STATE_STOP:
				#print "circle"
					print "swipe"
					return True
	return False
	
def check_hands(frame):
	global hand_state 
	global Enable_flag
	
	#print "hand_state = ", hand_state
	#print "Enable_flag = ", Enable_flag
	
	if hand_state is 1:
		if len(frame.hands) is 2:
			hand_state = 2
	if hand_state is 2:
		if len(frame.hands) is 1:
			hand_state = 3		
	if hand_state is 3:
		Enable_flag = True
		if len(frame.hands) is 2:
			hand_state = 4
	if hand_state is 4:
		Enable_flag = False
		if len(frame.hands) is 1:
			hand_state = 1
	return
	
		
		
	
def set_servos(four_angles):
	servo.move(1, int(four_angles[0]))
	servo.move(2, int(four_angles[1]))
	servo.move(3, int(four_angles[2]))
	servo.move(4, int(four_angles[3]))

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
	


def setup(controller):
	global reference_frame
	print "Press Enter to define start angle..."
	sys.stdin.readline()
	reference_frame = controller.frame()
	
	
def main():
	controller = Leap.Controller()
	controller.enable_gesture(Leap.Gesture.TYPE_CIRCLE)
	controller.enable_gesture(Leap.Gesture.TYPE_SWIPE)
	controller.config.set("Gesture.Circle.MinRadius", 10.0)
	controller.config.set("Gesture.Circle.MinArc", .5)
	controller.config.save()
	
	while not(controller.is_connected):
		print "Waiting for controller..."
		time.sleep(1)
	print "Connected!"
	
	global Enable_flag
	Enable_flag = False
	global hand_state
	hand_state = 1
	
	
	try: 
		while controller.is_connected:
			frame = controller.frame()
			check_hands(frame)
					
			if Enable_flag:
				servo_angles = getAngle(frame)
				set_servos(servo_angles)
		
	except KeyboardInterrupt:
		pass
	finally:
		#set_servos([90,90,90,90])
		print "Goodbye."
				
if __name__ == "__main__":
	main()