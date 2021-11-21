#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from agente.msg import Num
from agente.msg import Pedido
from agente.msg import Limpieza_mesa
from agente.msg import Ubicacion
from agente.msg import Interaccion
from kobuki_msgs.msg import SensorState
from agente.msg import Nav
from agente.msg import Meta7_activa

def listener():

    	global pub7, pub_nav
    
	rospy.init_node('GestorDeMediosYFines7', anonymous=True)

	r = rospy.Rate(10)

	pub7 = rospy.Publisher('Plan7',Meta7_activa, queue_size=10)
	pub_nav = rospy.Publisher('Navegacionm7',Nav, queue_size=10)

	rospy.Subscriber('CreenciasSensores', SensorState, callback_sensor)
	r.sleep()
	rospy.Subscriber("CreenciasUbicacion",Ubicacion, callback_ubi)
	r.sleep()
	rospy.Subscriber("Intencion7", Meta7_activa, callback_m7)

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

def callback_m7(data):
	global pub7, paso, pub_nav, boton, ubicacion, cambio
	global haypedido, numerodemesa,numerodepedido,tiempodepedido,tipodepedido,estadodelpedido
	global mesalimpia, pub
	meta7=data.meta7

	if boton == 1 :
		cambio = 1

	if   ubicacion != "mesa2" and meta7 == 1 and cambio == 0:
		print("voy a mesa2")
		pub7.publish(1) 
		pub_nav.publish("mesa2")	
	
	elif ubicacion == "mesa2" and cambio == 0:
		pub7.publish(0) 
		pub_nav.publish("n7")
		print("esperando que pongan el plato")		

	elif   ubicacion != "cocina" and meta7 == 1 and cambio == 1:
		print("voy a cocina")
		pub7.publish(1) 
		pub_nav.publish("cocina")

	else:
		print("holaaaaaaaaa")
		pub7.publish(0) 
		pub_nav.publish("n7") 
		print("estoy en el else")



if __name__ == '__main__':
	listener()
