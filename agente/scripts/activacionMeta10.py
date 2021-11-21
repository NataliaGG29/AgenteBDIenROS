#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from agente.msg import Num
from agente.msg import Pedido
from agente.msg import Limpieza_mesa
from agente.msg import Meta10_activa
from kobuki_msgs.msg import SensorState

def callback_p(data):
	global haypedido, numerodemesa,numerodepedido,tiempodepedido,tipodepedido,estadodelpedido
	global mesalimpia, pub, numerodemesa_l ,numeroderecoleccion, bumper , battery, platoencima
	global haypedido2, numerodemesa2,numerodepedido2,tiempodepedido2,tipodepedido2,estadodelpedido2
	numerodemesa = data.numerodemesa
	numerodepedido = data.numerodepedido 
	tiempodepedido = data.tiempodepedido
	tipodepedido = data.tipodepedido 
	estadodelpedido = data.estadodelpedido
	haypedido = data.haypedido
    
	if haypedido == 0 and platoencima == 0 and battery <= 140 and mesalimpia == 1 and haypedido2 == 0 and mesalimpia2 == 1:
		pub.publish(1)
		print("Meta activa")
	else:
		pub.publish(0)
		print("Meta no activa")
#	print(data)

def callback_p_2(data):
	global haypedido2, numerodemesa2,numerodepedido2,tiempodepedido2,tipodepedido2,estadodelpedido2
	numerodemesa2 = data.numerodemesa
	numerodepedido2 = data.numerodepedido
	tiempodepedido2 = data.tiempodepedido
	tipodepedido2 = data.tipodepedido
	estadodelpedido2 = data.estadodelpedido
	haypedido2 = data.haypedido
#	print(data)


def callback_l_m(data_l_m):
	global numerodemesa_l , numeroderecoleccion , mesalimpia
	numerodemesa_l = data_l_m.numerodemesa_l
	numeroderecoleccion = data_l_m.numeroderecoleccion
	mesalimpia = data_l_m.mesalimpia
#	print(data_l_m)

def callback_l_m_2(data_l_m):
	global numerodemesa_l2 , numeroderecoleccion2 , mesalimpia2
	numerodemesa_l2 = data_l_m.numerodemesa_l
	numeroderecoleccion2 = data_l_m.numeroderecoleccion
	mesalimpia2 = data_l_m.mesalimpia
#	print(data_l_m)


def callback_sensor(data):
	global bumper , battery , platoencima
	battery = data.battery
	bumper = data.bumper
	platoencima = 0	
#	print(data)
 
def activacionMeta10():
	global pub
	rospy.init_node('activacionMeta10', anonymous=True)

	rospy.Subscriber("CreenciasPedido", Pedido, callback_p)
	rospy.Subscriber("CreenciasPedido_2", Pedido, callback_p_2)
	rospy.Subscriber("CreenciasLimpieza_mesa", Limpieza_mesa, callback_l_m)
	rospy.Subscriber("CreenciasLimpieza_mesa_2", Limpieza_mesa, callback_l_m_2)
	rospy.Subscriber("CreenciasSensores", SensorState, callback_sensor)

	pub = rospy.Publisher('Meta10_Activa',Meta10_activa, queue_size=10)

	rospy.spin()

if __name__ == '__main__':
	activacionMeta10()
