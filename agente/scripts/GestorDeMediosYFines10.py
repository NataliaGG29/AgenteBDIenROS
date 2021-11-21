#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from agente.msg import Num
from agente.msg import Pedido
from agente.msg import Limpieza_mesa
from agente.msg import Ubicacion
from agente.msg import Nav
from agente.msg import Interaccion
from kobuki_msgs.msg import SensorState
from agente.msg import Meta10_activa

global paso
paso = 0

def callback_ubi(data):
	global ubicacion
	ubicacion = data.donde_esta
	print(ubicacion)

def callback_m10(data):
	global pub10, pub_nav, ubicacion
	meta10=data.meta10

	if   ubicacion != "carga" and meta10 == 1:
		print("voy a carga")
		pub10.publish(1) 
		pub_nav.publish("carga")

	else: 
		print("estoy en el else")
		pub10.publish(0)
		pub_nav.publish("n10")

def callback_u(data_u):
    donde_esta = data_u.donde_esta
#    print(data_u)


def listener():
    
	global pub_nav , pub10  

	rospy.init_node('GestorDeMediosYFines10', anonymous=True)


	rospy.Subscriber("CreenciasUbicacion", Ubicacion, callback_u)

	pub10 = rospy.Publisher('Plan10',Meta10_activa, queue_size=10)

	pub_nav = rospy.Publisher('Navegacionm10',Nav, queue_size=10)

	rospy.Subscriber("CreenciasUbicacion",Ubicacion, callback_ubi)

	rospy.Subscriber("Intencion10", Meta10_activa, callback_m10)

	rospy.spin()

if __name__ == '__main__':
	listener()
