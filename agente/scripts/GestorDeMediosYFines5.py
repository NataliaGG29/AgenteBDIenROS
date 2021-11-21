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
from agente.msg import Meta5_activa

def callback_m5(data):
	global meta5
	meta5=data.meta5

def listener():

    	global pub5, pub_nav

	pub5 = rospy.Publisher('Plan5',Meta5_activa, queue_size=10)
	pub_nav = rospy.Publisher('Navegacionm5',Nav, queue_size=10)
    
	rospy.init_node('GestorDeMediosYFines5', anonymous=True)

	r = rospy.Rate(10)

	rospy.Subscriber('CreenciasSensores', SensorState, callback_sensor)
	r.sleep()
	rospy.Subscriber("CreenciasUbicacion",Ubicacion, callback_ubi)
	r.sleep()
	rospy.Subscriber("Intencion5", Meta5_activa, callback_m5)
	r.sleep()

	rospy.spin()

#def callback_pla(data):
#	global hay_plato
#	hay_plato = 1

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

def callback_m5(data):
	global pub5, paso, pub_nav, boton, ubicacion, cambio
	global haypedido, numerodemesa,numerodepedido,tiempodepedido,tipodepedido,estadodelpedido
	global mesalimpia, pub
	meta5=data.meta5

	if boton == 1 :
		cambio = 1
	if boton == 2 :
		cambio = 3


	if meta5 == 1 and ubicacion != "cocina"and cambio == 0:
		print("comence")
		pub5.publish(1) 
		pub_nav.publish("cocina")
		#paso=1

	elif ubicacion == "cocina" and cambio == 0 :
		pub5.publish(0)
		pub_nav.publish("n5")
		print("esperando el plato")

	
	elif   ubicacion != "mesa2" and meta5 == 1 and cambio == 1:
		print("voy a mesa2")
		pub5.publish(1) 
		pub_nav.publish("mesa2")
	
	
	elif ubicacion == "mesa2" and cambio == 1:
		pub5.publish(0) 
		pub_nav.publish("n5")
		print("esperando que quiten el plato")		

	else:
		print("chao")
		pub5.publish(0) 
		pub_nav.publish("n5")
		print("estoy en el else")


if __name__ == '__main__':
	listener()
