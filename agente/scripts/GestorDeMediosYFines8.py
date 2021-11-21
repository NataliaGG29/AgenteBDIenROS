#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from agente.msg import Num
from agente.msg import Pedido
from agente.msg import Limpieza_mesa
from agente.msg import Ubicacion
from agente.msg import Interaccion
from kobuki_msgs.msg import SensorState
from agente.msg import Meta1_activa
from agente.msg import Meta2_activa
from agente.msg import Meta3_activa
from agente.msg import Meta4_activa
from agente.msg import Meta5_activa
from agente.msg import Meta6_activa
from agente.msg import Meta7_activa
from agente.msg import Meta8_activa
from agente.msg import Meta9_activa
from agente.msg import Meta10_activa

def callback_m8(data):
	global meta8
	meta8=data.meta8

def listener():
    
	rospy.init_node('GestorDeMediosYFines8', anonymous=True)

	rospy.Subscriber("Intencion8", Meta8_activa, callback_m8)

	pub8 = rospy.Publisher('Plan8',Meta8_activa, queue_size=10)

	rospy.spin()

if __name__ == '__main__':
	listener()
