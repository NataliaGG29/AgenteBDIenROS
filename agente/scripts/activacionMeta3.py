#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from agente.msg import Num
from agente.msg import Interaccion
from agente.msg import Meta3_activa


def callback_i(data_i):
	global pub
	hay_alguien = data_i.hay_alguien
	print(data_i)
	if hay_alguien == 1 :
		pub.publish(1)
		print("Meta activa")
	else:
		pub.publish(0)
		print("Meta no activa")

def activacionMeta3():
	global pub
	rospy.init_node('activacionMeta3', anonymous=True)

	rospy.Subscriber("CreenciasInteraccion", Interaccion, callback_i)

	pub = rospy.Publisher('Meta3_Activa',Meta3_activa, queue_size=10)

	rospy.spin()

if __name__ == '__main__':
    activacionMeta3()
