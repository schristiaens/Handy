/*
 * ------------------------------
 *   MultipleSerialServoControl
 * ------------------------------
 *
 * Uses the Arduino Serial library
 *  (http://arduino.cc/en/Reference/Serial)
 * and the Arduino Servo library
 *  (http://arduino.cc/en/Reference/Servo)
 * to control multiple servos from a PC using a USB cable.
 *
 * Dependencies:
 *   Arduino 0017 or higher
 *     (http://www.arduino.cc/en/Main/Software)
 *   Python servo.py module
 *     (http://principialabs.com/arduino-python-4-axis-servo-control/)
 *
 * Created:  23 December 2009
 * Author:   Brian D. Wendt
 *   (http://principialabs.com/)
 * Version:  1.1
 * License:  GPLv3
 *   (http://www.fsf.org/licensing/)
 *
 */

// Import the Arduino Servo library
#include <Servo.h> 

// Create a Servo object for each servo
Servo servo1;
Servo servo2;
Servo servo3;
Servo servo4;
// TO ADD SERVOS:
//   Servo servo5;
//   etc...

// Common servo setup values
int minPulse = 600;   // minimum servo position, us (microseconds)
int maxPulse = 2400;  // maximum servo position, us

// User input for servo and position
int userInput[3];    // raw input from serial buffer, 3 bytes
int startbyte;       // start byte, begin reading input
int servo;           // which servo to pulse?
int pos;             // servo angle 0-180
int pos_arr[4]= {90,90,90,90};
int curr_pos_arr[4] = {90,90,90,90};
int ms_deg[4];// ms per deg delay (speed)
int time[4];

int i;               // iterator
int S1 = 90;         // Current servo state
int S2 = 90;
int S3 = 90;
int S4 = 90;


// LED on Pin 13 for digital on/off demo
int ledPin = 13;
int pinState = LOW;

void setup() 
{ 
  // Attach each Servo object to a digital pin
  servo1.attach(0, 1250, 2200);
  servo2.attach(1, 1250, 2200);
  servo3.attach(2, 600, 1600);
  servo4.attach(3, 600, 1600);
  // TO ADD SERVOS:
  //   servo5.attach(YOUR_PIN, minPulse, maxPulse);
  //   etc...

  // LED on Pin 13 for digital on/off demo
  pinMode(ledPin, OUTPUT);

  // Open the serial connection, 9600 baud
  Serial.begin(9600);
} 

void loop() 
{ 
  // Wait for serial input (min 3 bytes in buffer)
  if (Serial.available() > 2) 
  {
    // Read the first byte
    startbyte = Serial.read();
    // If it's really the startbyte (255) ...
    if (startbyte == 255) 
	{
      // ... then get the next two bytes
      for (i=0;i<2;i++) {
        userInput[i] = Serial.read();
      }
      // First byte = servo to move?
      servo = userInput[0];
      // Second byte = which position?
      pos = userInput[1];
      // Packet error checking and recovery
      if (pos == 255) { servo = 255; }
	  // Assign new position to appropriate servo
		switch (servo) 
		{
		case 1:
		  pos_arr[0] = pos;
		  break;
		case 2:
		  pos_arr[1] = pos;
		  break;
		case 3:
		  pos_arr[2] = pos;
		  break;
		case 4:
		  pos_arr[3] = pos;
		  break;

			// TO ADD SERVOS:
			//     case 5:
			//       servo5.write(pos);
			//       break;
			// etc...
			
			// LED on Pin 13 for digital on/off demo
			case 99:
			  if (pos == 180) {
				if (pinState == LOW) { pinState = HIGH; }
				else { pinState = LOW; }
			  }
			  if (pos == 0) {
				pinState = LOW;
			  }
			  digitalWrite(ledPin, pinState);
			  break;
		}
    }		
  }
  for(int i=0;i<4;i++)
  {
	  set_pos(i);
  }
  servo1.write(curr_pos_arr[0]);
  servo2.write(curr_pos_arr[1]);
  servo3.write(curr_pos_arr[2]);
  servo4.write(curr_pos_arr[3]);
}

void set_pos(int servo_num)
{

	ms_deg[servo_num] = abs(pos_arr[servo_num]-curr_pos_arr[servo_num])/5; // = 
//	time[servo_num] = millis(); //set time = ms timer
	
//	if(millis() - time[servo_num] >= ms_deg[servo_num])
//	{
		if(curr_pos_arr[servo_num]<pos_arr[servo_num])
		{
			curr_pos_arr[servo_num] = curr_pos_arr[servo_num] + ms_deg[servo_num];
			time[servo_num] = millis();
		}
		if(curr_pos_arr[servo_num]>pos_arr[servo_num])
		{
			curr_pos_arr[servo_num] = curr_pos_arr[servo_num] - 1;
			time[servo_num] = millis();
		}
//	}
	
}

