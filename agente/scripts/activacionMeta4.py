#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from agente.msg import Num
from agente.msg import Pedido
from agente.msg import Limpieza_mesa
from agente.msg import Meta4_activa

#PEDIDO_MESA1

def callback(data):
	global haypedido, numerodemesa,numerodepedido,tiempodepedido,tipodepedido,estadodelpedido
	global mesalimpia, pub

	numerodemesa = data.numerodemesa
	numerodepedido = data.numerodepedido 
	tiempodepedido = data.tiempodepedido
	tipodepedido = data.tipodepedido 
	estadodelpedido = data.estadodelpedido
	haypedido = data.haypedido
    
	if haypedido == 1 and numerodemesa == 1 and estadodelpedido == 0 and mesalimpia == 1 :
		pub.publish(1)
		print("Meta activa")
	else:
		pub.publish(0)
		print("Meta no activa")
	

def callback_l_m(data_l_m):
	global numerodemesa_l , numeroderecoleccion , mesalimpia
	numerodemesa_l = data_l_m.numerodemesa_l
	numeroderecoleccion = data_l_m.numeroderecoleccion
	mesalimpia = data_l_m.mesalimpia
	

def activacionMeta4():
	global pub 
	rospy.init_node('activacionMeta4', anonymous=True)
	
	rospy.Subscriber("CreenciasPedido", Pedido, callback)
	rospy.Subscriber("CreenciasLimpieza_mesa", Limpieza_mesa, callback_l_m)

	pub = rospy.Publisher('Meta4_Activa',Meta4_activa, queue_size=10)

	rospy.spin()

if __name__ == '__main__':
	activacionMeta4()
