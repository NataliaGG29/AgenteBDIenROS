#!/usr/bin/env python
import rospy
import math
import sys
import time
import tf

from std_msgs.msg import String
from agente.msg import Num
from agente.msg import Ubicacion
from kobuki_msgs.msg import SensorState
from agente.msg import Meta2_activa

from geometry_msgs.msg import Twist, Vector3
from nav_msgs.msg import Odometry
from tf.transformations import euler_from_quaternion, quaternion_from_euler
from math import degrees
from std_msgs.msg import Empty

def listener():

	global pub2
    
	rospy.init_node('GestorDeMediosYFines2', anonymous=True)

	rospy.Subscriber("Intencion2", Meta2_activa, callback_m2)

	pub2 = rospy.Publisher('Plan2',Meta2_activa, queue_size=10)

	rospy.spin()


def callback_m2(data):
	global pub2
	meta2=data.meta2

	if meta2 == 1 :
		pub2.publish(1)
		print("publicando")
		meta2=0
		
	else: 
		pub2.publish(0)
		meta2=0
		print("en el else")


if __name__ == '__main__':
	listener()
