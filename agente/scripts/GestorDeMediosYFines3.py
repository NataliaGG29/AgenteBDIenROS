#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from agente.msg import Num
from agente.msg import Pedido
from agente.msg import Limpieza_mesa
from agente.msg import Ubicacion
from agente.msg import Interaccion
from kobuki_msgs.msg import SensorState
from agente.msg import Meta3_activa

def listener():

	global pub3
    
	rospy.init_node('GestorDeMediosYFines3', anonymous=True)

	rospy.Subscriber("Intencion3", Meta3_activa, callback_m3)
	pub3 = rospy.Publisher('Plan3',Meta3_activa, queue_size=10)

	rospy.spin()

def callback_m3(data):
	global pub3
	meta3=data.meta3

if __name__ == '__main__':
	listener()
