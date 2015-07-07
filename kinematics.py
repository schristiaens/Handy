import Leap, math, interface
#from Leap import CircleGesture, KeyTapGesture, ScreenTapGesture, SwipeGesture
#global reference_frame

def coerce(value,low,high):
	ans=value
	tol=.001
	if value>high-tol:
		ans=high
	if value<low+tol:
		ans=low
	return ans
		
def calcFourAngles(frame):
	hand=frame.hands[0]

	delta=90-hand.direction.pitch*180/3.14159
	alpha=90-hand.direction.yaw*180/3.14159
	gamma=90-hand.palm_normal.roll*180/3.14159
	height = hand.wrist_position[1]
	
	height=height/25.4-5
	height=coerce(height,0,7.4)
	beta=math.asin(height/7.5)*180/3.14159+90
	
	delta=delta+beta-90
	
	alpha=coerce(alpha,0,180)
	beta=coerce(beta,90,180)
	gamma=coerce(gamma,0,180)
	delta=coerce(delta,0,180)

	solution = (alpha, beta, gamma, delta)
	roundedSol = []
	for x in solution:
		roundedSol.append(round(x, 1))
	return roundedSol