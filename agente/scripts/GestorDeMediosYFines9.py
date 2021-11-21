#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from agente.msg import Num
from agente.msg import Pedido
from agente.msg import Limpieza_mesa
from agente.msg import Ubicacion
from agente.msg import Interaccion
from agente.msg import Nav
from kobuki_msgs.msg import SensorState
from agente.msg import Meta9_activa

global paso
paso = 0

def callback_m9(data):
	global pub9, paso, pub_nav, ubicacion
	meta9=data.meta9
	limpiando =0
	if meta9 == 1 and ubicacion != "limpieza" and ubicacion != "limpiando":
		print("va a zona de limpieza")
		pub_nav.publish("limpieza") 
		pub9.publish(1)
	elif meta9 == 1 and ubicacion == "limpieza":
		print("limpiando")
		pub_nav.publish("n91")
		pub9.publish(1)
		meta9 = 0	
		pub9.publish(0)
	else:
		print("en el else")
		pub9.publish(0)
		pub_nav.publish("n99")
		meta9 = 0
	
def callback_u(data_u):
	global ubicacion
	ubicacion = data_u.donde_esta
#    print(data_u)

def listener():
    
	global pub9, pub_nav

	rospy.init_node('GestorDeMediosYFines9', anonymous=True)

	pub9 = rospy.Publisher('Plan9',Meta9_activa, queue_size=10)
	pub_nav = rospy.Publisher('Navegacionm9',Nav, queue_size=10)

	rospy.Subscriber("CreenciasUbicacion", Ubicacion, callback_u)
	rospy.Subscriber("Intencion9", Meta9_activa, callback_m9)

	rospy.spin()

if __name__ == '__main__':
	listener()
