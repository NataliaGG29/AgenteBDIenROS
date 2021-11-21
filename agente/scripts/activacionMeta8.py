#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from agente.msg import Num
from agente.msg import Ayuda
from agente.msg import Meta8_activa

def callback_a(data_a):

	global pub

	if data_a.ayuda == 1:
		pub.publish(1)
		print("Meta activa")

	else:
		pub.publish(0)
		print("Meta no activa")
#	print(data_a)

 
def activacionMeta8():

	global pub

	rospy.init_node('activacionMeta8', anonymous=True)   

	rospy.Subscriber("CreenciasAyuda", Ayuda, callback_a)    

	pub = rospy.Publisher('Meta8_Activa',Meta8_activa, queue_size=10)    

	rospy.spin()

if __name__ == '__main__':
	activacionMeta8()
