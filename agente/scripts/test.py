#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from agente.msg import Num
from agente.msg import Pedido
from agente.msg import Limpieza_mesa
from agente.msg import Ubicacion
from agente.msg import Interaccion
from agente.msg import Ayuda
from kobuki_msgs.msg import SensorState


def callback(data):
	print(data)
def callback1(data):
	print(data)
def callback2(data):
	print(data)
def callback3(data):
	print(data)
def callback4(data):
	print(data)
def callback5(data):
	print(data)
def callback6(data):
	print(data)
def callback7(data):
	print(data)
def callback8(data):
	print(data)
def callback9(data):
	print(data)

def listener():

	rospy.init_node('test', anonymous=True)
	rospy.Subscriber("CreenciasPedido", Pedido, callback)
	rospy.Subscriber("CreenciasLimpieza_mesa", Limpieza_mesa, callback1)
 	rospy.Subscriber("CreenciasPedido_2", Pedido, callback2)
	rospy.Subscriber("CreenciasLimpieza_mesa_2", Limpieza_mesa, callback3)
	rospy.Subscriber("CreenciasUbicacion", Ubicacion, callback4)
	rospy.Subscriber("CreenciasInteraccion", Interaccion, callback5)
	rospy.Subscriber("CreenciasAyuda", Ayuda, callback6)
	rospy.Subscriber("CreenciasSensores", SensorState, callback7)
	rospy.Subscriber("Platoencima",Interaccion, callback8)
	rospy.Subscriber("Creenciashayplato",Interaccion, callback9)
	
	rospy.spin()

if __name__ == '__main__':
	listener()
