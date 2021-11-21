#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from agente.msg import Nav
from agente.msg import Pantalla
from agente.msg import Limpieza
from agente.msg import Meta
from agente.msg import Num
from agente.msg import Pedido
from agente.msg import Limpieza_mesa
from agente.msg import Ubicacion
from agente.msg import Interaccion
from kobuki_msgs.msg import SensorState

global pantalla_siono, pub_pan

def callback_meta(data_meta):
	meta = data_meta.meta
	#print(data_meta)

def callback(data):
	numerodemesa = data.numerodemesa
	numerodepedido = data.numerodepedido 
	tiempodepedido = data.tiempodepedido
	tipodepedido = data.tipodepedido 
	estadodelpedido = data.estadodelpedido
	#print(data)

def callback_l_m(data_l_m):
	numerodemesa_l = data_l_m.numerodemesa_l
	numeroderecoleccion = data_l_m.numeroderecoleccion
	mesalimpia = data_l_m.mesalimpia
	#print(data_l_m)

def callback_u(data_u):
	donde_esta = data_u.donde_esta
	#print(data_u)
	

def callback_i(data_i):
	hay_alguien = data_i.hay_alguien
	#print(data_i)

def callback_sensor(data):	
	global pantalla_siono, pub_pan
	lala = data
	pub_pan.publish(pantalla_siono.pantalla)
	
def planes():
	
	global pantalla_siono, pub_pan
	rospy.init_node('plan', anonymous=True)

	rospy.Subscriber("MetaActiva", Meta, callback_meta)

	rospy.Subscriber("CreenciasPedido", Pedido, callback)
	rospy.Subscriber("CreenciasLimpieza_mesa", Limpieza_mesa, callback_l_m)
	rospy.Subscriber("CreenciasUbicacion", Ubicacion, callback_u)
	rospy.Subscriber("CreenciasInteraccion", Interaccion, callback_i)
	rospy.Subscriber("CreenciasSensores", SensorState, callback_sensor)


	pub_nav = rospy.Publisher('Navegacion',Nav, queue_size=10)
	pub_pan = rospy.Publisher('Pantalla',Pantalla, queue_size=10)
	pub_lim = rospy.Publisher('Limpieza',Limpieza, queue_size=10)


	rospy.spin()

if __name__ == '__main__':
	global pantalla_siono
	pantalla_siono = Pantalla()
	pantalla_siono.pantalla = int(input("Carita feliz: ")) 
	planes()
