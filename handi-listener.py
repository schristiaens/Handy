import os, sys, inspect, thread, time
src_dir = os.path.dirname(inspect.getfile(inspect.currentframe()))
arch_dir = '../lib/x64' if sys.maxsize > 2**32 else '../lib/x86'
sys.path.insert(0, os.path.abspath(os.path.join(src_dir, arch_dir)))

import Leap
from Leap import CircleGesture, KeyTapGesture, ScreenTapGesture, SwipeGesture

class SampleListener(Leap.Listener):

	def on_connect(self, controller):
		print "Connected"


	def on_frame(self, controller):
		#print "Frame available"
	# Get info for the hand
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
	listener = SampleListener()
	controller = Leap.Controller()

	controller.add_listener(listener)

	# Keep this process running until Enter is pressed
	print "Press Enter to quit..."
	try:
		sys.stdin.readline()
	except KeyboardInterrupt:
		pass
	finally:
		controller.remove_listener(listener)

if __name__ == "__main__":
	main()