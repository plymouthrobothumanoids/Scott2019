#!/usr/bin/env python
# license removed for brevity
from __future__  import division
from Servo import Servos
import rospy
from std_msgs.msg import Float64
import math
import time

def talker():
    RA1 = Servos('RA1_controller', "MX-64")
    RA2 = Servos('RA2_controller', "MX-64")
    RA3 = Servos('RA3_controller', "MX-64")
    LA1 = Servos('LA1_controller', "MX-64")
    LA2 = Servos('LA2_controller', "MX-64")
    LA3 = Servos('LA3_controller', "MX-64")
    RL1 = Servos('RL1_controller', "MX-106")
    RL2 = Servos('RL2_controller', "MX-106")
    RL3 = Servos('RL3_controller', "MX-106")
    RL4 = Servos('RL4_controller', "MX-106")
    RL5 = Servos('RL5_controller', "MX-106")
    RL6 = Servos('RL6_controller', "MX-106")
    LL1 = Servos('LL1_controller', "MX-106")
    LL2 = Servos('LL2_controller', "MX-106")
    LL3 = Servos('LL3_controller', "MX-106")
    LL4 = Servos('LL4_controller', "MX-106")
    LL5 = Servos('LL5_controller', "MX-106")
    LL6 = Servos('LL6_controller', "MX-106")
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    position1 = 2048
    position7 = 2031
    position9 = 1975
    position11 = 1884
    position13 = 2051
    position15 = 1959
    position17 = 2018
    position8 = 2068
    position10 = 2060
    position12 = 2205
    position14 = 2059
    position16 = 2126
    position18 = 2042
    #RA1.setPosition(position1)
    RL1.setPosition(position7)
    RL2.setPosition(position9)
    RL3.setPosition(position11)
    RL4.setPosition(position13)
    RL5.setPosition(position15)
    RL6.setPosition(position17)
    LL1.setPosition(position8)
    LL2.setPosition(position10)
    LL3.setPosition(position12)
    LL4.setPosition(position14)
    LL5.setPosition(position16)
    LL6.setPosition(position18)
    time.sleep(1)

    constTime = 3

    while not rospy.is_shutdown():
        #hello_str = "hello world %s" % rospy.get_time()

	#position11 = 1314
	#position13 = 997
	#position15 = 2622
	#position12 = 2791
	#position14 = 930
	#position16 = 1516
	RL1.setPosition(position7)
        RL2.setPosition(position9)
        RL3.setPosition(position11)
        RL4.setPosition(position13)
        RL5.setPosition(position15)
        RL6.setPosition(position17)
        LL1.setPosition(position8)
        LL2.setPosition(position10)
        LL3.setPosition(position12)
        LL4.setPosition(position14)
        LL5.setPosition(position16)
        LL6.setPosition(position18)

	
	position1 = 2580 #2080       
        position2 = 1570
	position3 = 2400
	print("Arm down")

        rospy.loginfo(position1)
	rospy.loginfo(position2)
	rospy.loginfo(position3)
	RA1.setPosition(position1)
        RA2.setPosition(position2)
	RA3.setPosition(position3)	
        rate.sleep()
	time.sleep(1.5)
	position1 = 3100
	position2 = 1700
	position3 = 3450
	print("Arm up")

        rospy.loginfo(position1)
	rospy.loginfo(position2)
	rospy.loginfo(position3)	
    	RA1.setPosition(position1)
        RA2.setPosition(position2)
	RA3.setPosition(position3)



        #RL1.setPosition(position7)
        #RL2.setPosition(position9)
        #RL3.setPosition(position11)
        #RL4.setPosition(position13)
        #RL5.setPosition(position15)
        #RL6.setPosition(position17)
        #LL1.setPosition(position8)
        #LL2.setPosition(position10)
        #LL3.setPosition(position12)
        #LL4.setPosition(position14)
        #LL5.setPosition(position16)
        #LL6.setPosition(position18)
        rate.sleep()
	time.sleep(1.5)
 
if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
