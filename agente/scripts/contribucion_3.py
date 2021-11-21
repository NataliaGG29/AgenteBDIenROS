#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from agente.msg import Num
from agente.msg import Limpieza_mesa
from agente.msg import Meta6_activa
from agente.msg import Meta7_activa
from agente.msg import Meta8_activa


def callback_l_m(data_l_m):
	global numeroderecoleccion
	numerodemesa_l_m = data_l_m.numerodemesa_l
	numeroderecoleccion = data_l_m.numeroderecoleccion
	mesalimpia = data_l_m.mesalimpia

def callback_l_m_2(data_l_m):
	global numeroderecoleccion_2
	numerodemesa_l_m_2 = data_l_m.numerodemesa_l
	numeroderecoleccion_2 = data_l_m.numeroderecoleccion
	mesalimpia_2 = data_l_m.mesalimpia


def callback_m6(data):
	global meta6
	meta6=data.meta6

def callback_m7(data):
	global meta7
	meta7=data.meta7

def callback_m8(data):
	global meta7, meta6
	global pub8, pub7, pub6
	global numeroderecoleccion
	global numeroderecoleccion_2

	meta8=data.meta8

	limpieza1=-(numeroderecoleccion)
	limpieza2=-(numeroderecoleccion_2)

	if meta6==1 and meta7==1 and meta8==1:
		pub6.publish(0)
		pub7.publish(0)
		pub8.publish(1)
		print("Gano la meta 8")
	elif  meta6==1 and meta7==1 and meta8==0:

		if limpieza1 > limpieza2:		
			pub6.publish(1)
			pub7.publish(0)
			pub8.publish(0)
			print("Gano la meta 6")
		else:
			pub6.publish(0)
			pub7.publish(1)
			pub8.publish(0)
			print("Gano la meta 7")
	elif meta6==1 and meta7==0 and meta8==1:
		pub6.publish(0)
		pub7.publish(0)
		pub8.publish(1)
		print("Gano la meta 8")
	elif  meta6==0 and meta7==1 and meta8==1:
		pub6.publish(0)
		pub7.publish(0)
		pub8.publish(1)
		print("Gano la meta 8")
	elif meta6==1 and meta7==0 and meta8==0:
		
		pub6.publish(1)
		pub7.publish(0)
		pub8.publish(0)
		print("Gano la meta 6")
	elif meta6==0 and meta7==1 and meta8==0:
		pub6.publish(0)
		pub7.publish(1)
		pub8.publish(0)
		print("Gano la meta 7")
	elif meta6==0 and meta7==0 and meta8==1:
		pub6.publish(0)
		pub7.publish(0)
		pub8.publish(1)
		print("Gano la meta 8")
	else:
		pub6.publish(0)
		pub7.publish(0)
		pub8.publish(0)
		print("Metas no activas")


def listener():

	global pub8, pub7, pub6
    
	rospy.init_node('contribucion_3', anonymous=True)

	rospy.Subscriber("Meta6_Piramide", Meta6_activa, callback_m6)
	rospy.Subscriber("Meta7_Piramide", Meta7_activa, callback_m7)
	rospy.Subscriber("Meta8_Piramide", Meta8_activa, callback_m8)

	rospy.Subscriber("CreenciasLimpieza_mesa", Limpieza_mesa, callback_l_m)
	rospy.Subscriber("CreenciasLimpieza_mesa_2", Limpieza_mesa, callback_l_m_2)

	pub6 = rospy.Publisher('Intencion6',Meta6_activa, queue_size=10)
	pub7 = rospy.Publisher('Intencion7',Meta7_activa, queue_size=10)	
	pub8 = rospy.Publisher('Intencion8',Meta8_activa, queue_size=10)


	rospy.spin()

if __name__ == '__main__':
	listener()
