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
	global  pub_p
	pub_p.publish(data)
#	print(data)
    
def callback_l_m(data_l_m):
	global  pub_l_m
	pub_l_m.publish(data_l_m)
#	print(data_l_m)
    
def callback_2(data):
	global  pub_p_2
	pub_p_2.publish(data)
#	print(data)
    
def callback_l_m_2(data_l_m):
	global  pub_l_m_2
	pub_l_m_2.publish(data_l_m)
#	print(data_l_m)
    
def callback_u(data_u):
	global  pub_u
	pub_u.publish(data_u)
	print(data_u)

def callback_i(data_i):
	global  pub_i    
	pub_i.publish(data_i)
#	print(data_i)
    
def callback_sensor(data_s):
	global pub_s
	pub_s.publish(data_s)
#	print(data_s)
    
def callback_a(data):
	global pub_a
	pub_a.publish(data)
#	print(data)
    
def callback_pla(data):
	global pub_pla
	hayplato = data.hay_alguien
	pub_pla.publish(data)
#	print(data)

def callback_cam(data):
	camara = data.hay_alguien
#	print(data)
	
    
def listener():

	global  pub_p,pub_l_m,pub_u,pub_i,pub_s, pub_a,pub_p_2, pub_l_m_2, pub_pla

	rospy.init_node('agentecreencias', anonymous=True)

	pub_p = rospy.Publisher('CreenciasPedido',Pedido, queue_size=10)
	pub_l_m = rospy.Publisher('CreenciasLimpieza_mesa',Limpieza_mesa, queue_size=10)
	pub_p_2 = rospy.Publisher('CreenciasPedido_2',Pedido, queue_size=10)
	pub_l_m_2 = rospy.Publisher('CreenciasLimpieza_mesa_2',Limpieza_mesa, queue_size=10)
	pub_u = rospy.Publisher('CreenciasUbicacion',Ubicacion, queue_size=10)
	pub_i = rospy.Publisher('CreenciasInteraccion',Interaccion, queue_size=10)
	pub_s = rospy.Publisher('CreenciasSensores',SensorState, queue_size=10)
	pub_a = rospy.Publisher('CreenciasAyuda',Ayuda, queue_size=10)
	pub_pla = rospy.Publisher('Creenciashayplato',Interaccion, queue_size=10)

	rospy.Subscriber("Pedido", Pedido, callback)
	rospy.Subscriber("Limpieza_mesa", Limpieza_mesa, callback_l_m)
 	rospy.Subscriber("Pedido2", Pedido, callback_2)
	rospy.Subscriber("Limpieza_mesa_2", Limpieza_mesa, callback_l_m_2)
	rospy.Subscriber("ubicacion", Ubicacion, callback_u)
	rospy.Subscriber("Interaccion", Interaccion, callback_i)
	rospy.Subscriber("Ayuda", Ayuda, callback_a)
	rospy.Subscriber("/mobile_base/sensors/core", SensorState, callback_sensor)
	rospy.Subscriber("Platoencima",Interaccion, callback_pla)
	rospy.Subscriber("Camara",Interaccion, callback_cam)

	rospy.spin()

if __name__ == '__main__':
	listener()

