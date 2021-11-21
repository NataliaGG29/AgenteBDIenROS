#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from agente.msg import Num
from agente.msg import Limpieza_mesa
from agente.msg import Meta7_activa

#LIMPIAR_MESA2

def callback_l_m_2(data_l_m):

	global pub

	numerodemesa_l2 = data_l_m.numerodemesa_l
	numeroderecoleccion2 = data_l_m.numeroderecoleccion
	mesalimpia2 = data_l_m.mesalimpia
    
	if numerodemesa_l2 == 2 and mesalimpia2 == 0:
		pub.publish(1)
		print("Meta activa")
	else:
		pub.publish(0)
		print("Meta no activa")

#	print(data_l_m)

def activacionMeta7():

	global pub
	rospy.init_node('activacionMeta7', anonymous=True)

	rospy.Subscriber("CreenciasLimpieza_mesa_2", Limpieza_mesa, callback_l_m_2)

	pub = rospy.Publisher('Meta7_Activa',Meta7_activa, queue_size=10)

	rospy.spin()

if __name__ == '__main__':
	activacionMeta7()
