#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from agente.msg import Num
from agente.msg import Pedido
from agente.msg import Meta3_activa
from agente.msg import Meta4_activa
from agente.msg import Meta5_activa
import math


def callback_p(data):
	global numerodepedido, tipodepedido
	numerodemesa = data.numerodemesa
	numerodepedido = data.numerodepedido 
	tiempodepedido = data.tiempodepedido
	tipodepedido = data.tipodepedido 
	estadodelpedido = data.estadodelpedido

def callback_p_2(data):
	global numerodepedido_2, tipodepedido_2
	numerodemesa_2 = data.numerodemesa
	numerodepedido_2 = data.numerodepedido 
	tiempodepedido_2 = data.tiempodepedido
	tipodepedido_2 = data.tipodepedido 
	estadodelpedido_2 = data.estadodelpedido


def callback_m3(data):
	global meta3
	meta3=data.meta3

def callback_m4(data):
	global meta4
	meta4=data.meta4

def callback_m5(data):
	global numerodepedido, tipodepedido
	global numerodepedido_2, tipodepedido_2
	global meta4, meta3
	global pub3,pub4,pub5

	meta5=data.meta5

	pedido1= ((-(numerodepedido))*(0.25))+((tipodepedido)*(0.25))*100
	pedido2= ((-(numerodepedido_2))*(0.25))+((tipodepedido_2)*(0.25))*100	

	if meta3==1 and meta4==1 and meta5==1:
		pub3.publish(1)
		pub4.publish(0)
		pub5.publish(0)
		print("Gano la meta 3")
	elif  meta3==1 and meta4==1 and meta5==0:
		pub3.publish(1)
		pub4.publish(0)
		pub5.publish(0)
		print("Gano la meta 3")
	elif meta3==1 and meta4==0 and meta5==1:
		pub3.publish(1)
		pub4.publish(0)
		pub5.publish(0)
		print("Gano la meta 3")
	elif  meta3==0 and meta4==1 and meta5==1:
		if pedido1 > pedido2:	
			pub3.publish(0)
			pub4.publish(1)
			pub5.publish(0)
			print("Gano la meta 4")
		else:
			pub3.publish(0)
			pub4.publish(0)
			pub5.publish(1)
			print("Gano la meta 5")
	elif meta3==1 and meta4==0 and meta5==0:
		print("meta 3 activa")
		pub3.publish(1)
		pub4.publish(0)
		pub5.publish(0)
	elif meta3==0 and meta4==1 and meta5==0:
		print("meta 4 activa")
		pub3.publish(0)
		pub4.publish(1)
		pub5.publish(0)
	elif meta3==0 and meta4==0 and meta5==1:
		print("meta 5 activa")
		pub3.publish(0)
		pub4.publish(0)
		pub5.publish(1)
	elif meta3==0 and meta4==0 and meta5==0:
		print("metas no activas")
		pub3.publish(0)
		pub4.publish(0)
		pub5.publish(0)
	else:
		print("metas no activas")
		pub3.publish(0)
		pub4.publish(0)
		pub5.publish(0)

def listener():

	global pub3,pub4,pub5
    
	rospy.init_node('contribucion_2', anonymous=True)

	rospy.Subscriber("CreenciasPedido", Pedido, callback_p)
	rospy.Subscriber("CreenciasPedido_2", Pedido, callback_p_2)

	rospy.Subscriber("Meta3_Piramide", Meta3_activa, callback_m3)
	rospy.Subscriber("Meta4_Piramide", Meta4_activa, callback_m4)
	rospy.Subscriber("Meta5_Piramide", Meta5_activa, callback_m5)

	pub3 = rospy.Publisher('Intencion3',Meta3_activa, queue_size=10)	
	pub4 = rospy.Publisher('Intencion4',Meta4_activa, queue_size=10)
	pub5 = rospy.Publisher('Intencion5',Meta5_activa, queue_size=10)	


	rospy.spin()

if __name__ == '__main__':
	listener()
