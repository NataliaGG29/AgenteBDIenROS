#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from agente.msg import Num
from agente.msg import Limpieza_mesa
from agente.msg import Meta6_activa

#LIMPIAR_MESA1

def callback_l_m(data_l_m):

	global pub

	numerodemesa_l = data_l_m.numerodemesa_l
	numeroderecoleccion = data_l_m.numeroderecoleccion
	mesalimpia = data_l_m.mesalimpia
    
	if numerodemesa_l == 1 and mesalimpia == 0:
		pub.publish(1)
		print("Meta activa")
	else:
		pub.publish(0)
		print("Meta no activa")
#	print(data_l_m)

 
def activacionMeta6():

	global pub
	rospy.init_node('activacionMeta6', anonymous=True)

	rospy.Subscriber("CreenciasLimpieza_mesa", Limpieza_mesa, callback_l_m)

	pub = rospy.Publisher('Meta6_Activa',Meta6_activa, queue_size=10)

	rospy.spin()

if __name__ == '__main__':
	activacionMeta6()
