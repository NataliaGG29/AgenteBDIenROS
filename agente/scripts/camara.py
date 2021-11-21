#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import String
from agente.msg import Interaccion


def talker():

	pub_i = rospy.Publisher('Camara',Interaccion, queue_size=10)
	
	rospy.init_node('Camara', anonymous=True)
	rate = rospy.Rate(10) # 10hz
	
	camara = Interaccion()
	while not rospy.is_shutdown():

		camara.hay_alguien = 0	

		pub_i.publish(camara)
		print(camara)

        	rate.sleep()

if __name__ == '__main__':
	try:
		talker()
	except rospy.ROSInterruptException:
		pass
