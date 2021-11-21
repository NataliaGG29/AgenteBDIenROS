#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from agente.msg import Num
from agente.msg import Limpieza
from kobuki_msgs.msg import SensorState
from agente.msg import Meta9_activa
from agente.msg import Meta10_activa


def callback_m9(data):
	global meta9
	meta9=data.meta9

def callback_m10(data):
	global meta9, pub9 , pub10
	meta10=data.meta10

	if meta9 == 1 and meta10 ==1:
		pub9.publish(1)
		pub10.publish(0)
		print("meta9 on")
	elif meta9 == 1 and meta10 ==0:
		pub9.publish(1)
		pub10.publish(0)
		print("meta9 on")
	elif meta9 == 0 and meta10 ==1:
		pub9.publish(0)
		pub10.publish(1)
		print("meta9 on")
	else:
		pub9.publish(0)
		pub10.publish(0)
		print("metas off")

def listener():
    
        global pub9 , pub10

	rospy.init_node('contribucion_4', anonymous=True)

	rospy.Subscriber("Meta9_Piramide", Meta9_activa, callback_m9)
	rospy.Subscriber("Meta10_Piramide", Meta10_activa, callback_m10) 

	pub9 = rospy.Publisher('Intencion9',Meta9_activa, queue_size=10)	
	pub10 = rospy.Publisher('Intencion10',Meta10_activa, queue_size=10)

	rospy.spin()

if __name__ == '__main__':
	listener()
