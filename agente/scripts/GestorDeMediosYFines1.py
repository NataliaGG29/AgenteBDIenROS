#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from agente.msg import Num

from agente.msg import Nav
from agente.msg import Pedido
from agente.msg import Limpieza_mesa
from agente.msg import Ubicacion
from agente.msg import Interaccion
from kobuki_msgs.msg import SensorState
from agente.msg import Meta1_activa
from agente.msg import Meta2_activa
from agente.msg import Meta3_activa
from agente.msg import Meta4_activa
from agente.msg import Meta5_activa
from agente.msg import Meta6_activa
from agente.msg import Meta7_activa
from agente.msg import Meta8_activa
from agente.msg import Meta9_activa
from agente.msg import Meta10_activa

global paso
paso = 0

def callback_m1(data):
	global meta1,paso,pub_nav, pub1
	meta1=data.meta1
	if meta1 == 1 and paso == 0:	
		#goto carga
		print("va a carga")
		pub_nav.publish("carga") 
		pub1.publish(1)
		paso = 1
	elif meta1 == 1 and paso == 1:
		#finaliza
		pub_nav.publish("n1")
		pub1.publish(0)
		paso = 0
	else:
		pub_nav.publish("n1")
		pub1.publish(0)


def callback_u(data_u):
    donde_esta = data_u.donde_esta
    print(data_u)


def listener():
	global pub_nav , pub1   	
	
	rospy.init_node('GestorDeMediosYFines1', anonymous=True)
	
	rospy.Subscriber("Intencion1", Meta1_activa, callback_m1)
	rospy.Subscriber("CreenciasUbicacion", Ubicacion, callback_u)

	pub1 = rospy.Publisher('Plan1',Meta1_activa, queue_size=10)

	pub_nav = rospy.Publisher('Navegacion',Nav, queue_size=10)


	rospy.spin()

if __name__ == '__main__':
	listener()

