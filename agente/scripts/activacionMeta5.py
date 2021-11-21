#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from agente.msg import Num
from agente.msg import Pedido
from agente.msg import Limpieza_mesa
from agente.msg import Meta5_activa


#PEDIDO_MESA2
def callback_p_2(data):
	global haypedido2, numerodemesa2,numerodepedido2,tiempodepedido2,tipodepedido2,estadodelpedido2
	global mesalimpia2, pub
	numerodemesa2 = data.numerodemesa
	numerodepedido2 = data.numerodepedido 
	tiempodepedido2 = data.tiempodepedido
	tipodepedido2 = data.tipodepedido
	estadodelpedido2 = data.estadodelpedido
	haypedido2 = data.haypedido
	print("ayudaaaaaaaa")

	if haypedido2 == 1 and numerodemesa2 == 1 and estadodelpedido2 == 0 and mesalimpia2 == 1:
		pub.publish(1)
		print("Meta activa")
	else:
		pub.publish(0)
		print("Meta no activa")


def callback_l_m_2(data_l_m):
	global numerodemesa_l2 , numeroderecoleccion2 , mesalimpia2
	numerodemesa_l2 = data_l_m.numerodemesa_l
	numeroderecoleccion2 = data_l_m.numeroderecoleccion
	mesalimpia2 = data_l_m.mesalimpia
	#print(data_l_m)
 
def activacionMeta5():
	global pub 
	rospy.init_node('activacionMeta5', anonymous=True)

	rospy.Subscriber("CreenciasPedido_2", Pedido, callback_p_2)
	rospy.Subscriber("CreenciasLimpieza_mesa_2", Limpieza_mesa, callback_l_m_2)

	pub = rospy.Publisher('Meta5_Activa',Meta5_activa, queue_size=10)

	rospy.spin()

if __name__ == '__main__':
	activacionMeta5()
