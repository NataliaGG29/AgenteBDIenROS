#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from agente.msg import Num
from agente.msg import Meta2_activa
from kobuki_msgs.msg import SensorState

def callback_sensor(data):
	global pub	
	if data.bumper > 0 :
		print("hola1")
		if data.cliff > 0 :
			print("hola2")
			pub.publish(1)
			print("Meta activa")
		pub.publish(1)
		print("Meta activa")
	elif data.cliff > 0 :
		print("hola3")
		pub.publish(1)
		print("Meta activa")
	else:
		pub.publish(0)
		print("Meta no activa")
#		print(data.bumper)		
#		print(data.cliff)
 
def activacionMeta2():
	global pub
	rospy.init_node('activacionMeta2', anonymous=True)

	rospy.Subscriber('CreenciasSensores', SensorState, callback_sensor)

	pub = rospy.Publisher('Meta2_Activa',Meta2_activa, queue_size=10)

	rospy.spin()

if __name__ == '__main__':
	activacionMeta2()
