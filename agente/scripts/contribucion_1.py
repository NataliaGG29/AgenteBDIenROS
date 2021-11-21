#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from agente.msg import Num
from agente.msg import Pedido
from agente.msg import Limpieza_mesa
from agente.msg import Ubicacion
from agente.msg import Interaccion
from kobuki_msgs.msg import SensorState
from agente.msg import Meta1_activa
from agente.msg import Meta2_activa


def callback_m1(data):
	global meta1
	meta1=data.meta1

def callback_m2(data):
	global meta2, meta1, pub1 , pub2

	meta2=data.meta2

	if meta1 == 1 and meta2 ==1:
		pub1.publish(0)
		pub2.publish(1)
		print("meta2 on")
	elif meta1 == 1 and meta2 ==0:
		pub1.publish(1)
		pub2.publish(0)
		print("meta1 on")
	elif meta1 == 0 and meta2 ==1:
		pub1.publish(0)
		pub2.publish(1)
		print("meta2 on")
	else:
		pub1.publish(0)
		pub2.publish(0)
		print("metas off")


def listener():
        global pub1 , pub2
	rospy.init_node('contribucion_1', anonymous=True)

	rospy.Subscriber("Meta1_Piramide", Meta1_activa, callback_m1)
	rospy.Subscriber("Meta2_Piramide", Meta2_activa, callback_m2)

	pub1 = rospy.Publisher('Intencion1',Meta1_activa, queue_size=10)	
	pub2 = rospy.Publisher('Intencion2',Meta2_activa, queue_size=10)


	

	rospy.spin()

if __name__ == '__main__':
	listener()
