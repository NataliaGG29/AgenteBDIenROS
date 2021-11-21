#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from agente.msg import Limpieza
import math
import sys
import time
import tf

from geometry_msgs.msg import Twist, Vector3
from nav_msgs.msg import Odometry
from tf.transformations import euler_from_quaternion, quaternion_from_euler
from math import degrees
from std_msgs.msg import Empty

global cuadro

cuadro=0.59


def callback_lim(data_lim):
	limpieza = data_lim.limpieza
	print(data_lim)
 
def limpieza_zona():

	rospy.init_node('limpieza_zona', anonymous=True)

	pub = rospy.Publisher('mobile_base/commands/velocity',Twist,queue_size=10)
	(rospy.sleep (1))

	rospy.Subscriber("Limpieza", Limpieza, callback_lim)

	rospy.spin()

def write(linear,angular):
	global pub
	pub.publish(Twist(Vector3(linear[0],linear[1],linear[2]),
                   Vector3(angular[0],angular[1],angular[2])))


if __name__ == '__main__':
    limpieza_zona()
