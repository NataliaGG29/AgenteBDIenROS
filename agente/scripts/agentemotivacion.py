#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from agente.msg import Num
from agente.msg import Pedido
from agente.msg import Limpieza_mesa
from agente.msg import Ubicacion
from agente.msg import Interaccion
from kobuki_msgs.msg import SensorState



def callback(data):
	numerodemesa = data.numerodemesa
	numerodepedido = data.numerodepedido 
	tiempodepedido = data.tiempodepedido
	tipodepedido = data.tipodepedido 
	estadodelpedido = data.estadodelpedido
	print(data)

def callback_l(data_l_m):
	numerodemesa_l = data_l_m.numerodemesa_l
	numeroderecoleccion = data_l_m.numeroderecoleccion
	mesalimpia = data_l_m.mesalimpia
	print(data_l_m)

def callback_u(data_u):
	donde_esta = data_u.donde_esta
	print(data_u)

def callback_i(data_i):
	hay_alguien = data_i.hay_alguien
	print(data_i)

def callback_sensor(data):
	print(data)
 
def agente():

	rospy.init_node('listener', anonymous=True)

	rospy.Subscriber("CreenciasPedido", Pedido, callback)
	rospy.Subscriber("CreenciasLimpieza_mesa", Limpieza_mesa, callback_l_m)
	rospy.Subscriber("CreenciasUbicacion", Ubicacion, callback_u)
	rospy.Subscriber("CreenciasInteraccion", Interaccion, callback_i)
	rospy.Subscriber("CreenciasSensores", SensorState, callback_sensor)

	rospy.spin()

if __name__ == '__main__':

	listener()
