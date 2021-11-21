#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from agente.msg import Num
from agente.msg import Meta1_activa
from kobuki_msgs.msg import SensorState

def callback_sensor(data):

	global pub 

	if data.battery < 145 :
		pub.publish(1)
		print("Meta activa")
	else:
		pub.publish(0)
		print("Meta no activa")

def activacionMeta1():
	global pub 
	rospy.init_node('activacionMeta1', anonymous=True)

	rospy.Subscriber('CreenciasSensores', SensorState, callback_sensor)

	pub = rospy.Publisher('Meta1_Activa',Meta1_activa, queue_size=10)

	rospy.spin()

if __name__ == '__main__':
	activacionMeta1()
