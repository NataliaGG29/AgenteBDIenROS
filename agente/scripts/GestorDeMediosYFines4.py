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
from agente.msg import Meta4_activa

global paso
paso=0

def listener():
    	global pub4, pub_nav
	rospy.init_node('GestorDeMediosYFines4', anonymous=True)
	
	r = rospy.Rate(10)
	pub4 = rospy.Publisher('Plan4',Meta4_activa, queue_size=10)
	pub_nav = rospy.Publisher('Navegacionm4',Nav, queue_size=10)

	rospy.Subscriber('CreenciasSensores', SensorState, callback_sensor)
	r.sleep()
	rospy.Subscriber("CreenciasUbicacion",Ubicacion, callback_ubi)
	r.sleep()
	rospy.Subscriber("Intencion4", Meta4_activa, callback_m4)
	r.sleep()
	
	rospy.spin()
	
def callback_ubi(data):
	global ubicacion
	ubicacion = data.donde_esta
	print(ubicacion)

def callback_sensor(data):
	global boton	
	boton = data.buttons
	print (boton)

global hay_plato
hay_plato= 0

global cambio
cambio=0

def callback_m4(data):
	global pub4, paso, pub_nav, boton, ubicacion, cambio
	global haypedido, numerodemesa,numerodepedido,tiempodepedido,tipodepedido,estadodelpedido
	global mesalimpia, pub
	meta4=data.meta4

	if boton == 1 :
		cambio = 1
	if boton == 2 :
		cambio = 3

	if meta4 == 1 and ubicacion != "cocina" and cambio == 0:
		print("comence")
		pub4.publish(1) 
		pub_nav.publish("cocina")
		#paso=1

	elif ubicacion == "cocina" and cambio == 0:
		pub4.publish(0)
		pub_nav.publish("n4")
		print("esperando el plato")


	
	elif   ubicacion != "mesa1" and meta4 == 1 and cambio == 1:
		print("voy a mesa1")
		pub4.publish(1) 
		pub_nav.publish("mesa1")
#		paso = 3
	
	
	elif ubicacion == "mesa1" and cambio == 1:
		pub4.publish(0) 
		pub_nav.publish("n4")
		print("esperando que quiten el plato")		

	elif cambio == 3:
		print("holaaaaaaaaa")
		pub4.publish(0) 
		pub_nav.publish("n4")
	else: 
		print("estoy en el else")

if __name__ == '__main__':
	listener()
