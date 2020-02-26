'''
Creator: Glynn Moody
Module: ROCO318
Dependencies: rospy, math
Purpose: Allows for user control of pan tilt robot using either the keyboard or mouse
'''

from __future__  import division
import rospy
from std_msgs.msg import Float64
import math

#Converts joint position to joint angle
def convertPosition(position, maxAngle, midPoint):
	angle = ((position - midPoint)/midPoint)*maxAngle
        #print(angle)
        return angle

#Class to allow for easy position setting of servo joint angles
class Servos:

	def __init__(self, controllerName, controllerType):
		self.controller = controllerName
		self.type = controllerType
		
		#Sets the maximum angle for servo type
		if self.type == "RX-28":
		    self.maxAngle = ((150/180)*math.pi)
		    self.midPoint = 512
		elif "MX" in self.type:
		    self.maxAngle = math.pi
		    self.midPoint = 2048

		#Initialise servo
		controllerMode = "/" + self.controller + "/command"

		self.Servo = rospy.Publisher(controllerMode, Float64, queue_size=10)	

	#Publishes joint angle
	def setPosition(self, position):
		intPosition = convertPosition(position, self.maxAngle, self.midPoint)
		self.Servo.publish(intPosition)
		rospy.loginfo(intPosition)
