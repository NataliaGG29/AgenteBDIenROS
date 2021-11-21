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
from agente.msg import Meta6_activa

def listener():

    	global pub6, pub_nav
    
	rospy.init_node('GestorDeMediosYFines6', anonymous=True)

	r = rospy.Rate(10)

	pub6 = rospy.Publisher('Plan6',Meta6_activa, queue_size=10)
	pub_nav = rospy.Publisher('Navegacionm6',Nav, queue_size=10)

	rospy.Subscriber('CreenciasSensores', SensorState, callback_sensor)
	r.sleep()
	rospy.Subscriber("CreenciasUbicacion",Ubicacion, callback_ubi)
	r.sleep()

	rospy.Subscriber("Intencion6", Meta6_activa, callback_m6)

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

def callback_m6(data):
	global pub6, paso, pub_nav, boton, ubicacion, cambio
	global haypedido, numerodemesa,numerodepedido,tiempodepedido,tipodepedido,estadodelpedido
	global mesalimpia, pub
	meta6=data.meta6

	if boton == 1 :
		cambio = 1

	if   ubicacion != "mesa1" and meta6 == 1 and cambio == 0:
		print("voy a mesa1")
		pub6.publish(1) 
		pub_nav.publish("mesa1")

	elif ubicacion == "mesa1" and cambio == 0:
		pub6.publish(0) 
		pub_nav.publish("n6")
		print("esperando que pongan el plato")		

	elif   ubicacion != "cocina" and meta6 == 1 and cambio == 1:
		print("voy a cocina")
		pub6.publish(1) 
		pub_nav.publish("cocina")

	else:
		print("holaaaaaaaaa")
		pub6.publish(0) 
		pub_nav.publish("n6") 
		print("estoy en el else")




if __name__ == '__main__':
	listener()
