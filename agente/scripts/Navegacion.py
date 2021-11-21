#!/usr/bin/env python
import rospy
import math
import sys
import time
import tf
from agente.msg import Nav
from std_msgs.msg import String
from agente.msg import Num
from agente.msg import Limpieza_mesa
from agente.msg import Ubicacion

from agente.msg import Pedido
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


from geometry_msgs.msg import Twist, Vector3
from nav_msgs.msg import Odometry
from tf.transformations import euler_from_quaternion, quaternion_from_euler
from math import degrees
from std_msgs.msg import Empty

global cuadro

cuadro=0.59

def rosconf():

	rospy.init_node('navega')

	global pub, pub_u,r

	r=rospy.Rate(1)

	pub = rospy.Publisher('mobile_base/commands/velocity',Twist,queue_size=10)
	pub_u = rospy.Publisher('ubicacion',Ubicacion,queue_size=10)


	rospy.Subscriber('/odom',Odometry, fsmx2y)
	r.sleep()

	rospy.Subscriber("Plan1", Meta1_activa, callback_P1) 
	rospy.Subscriber("Plan2", Meta2_activa, callback_P2)
#	rospy.Subscriber("Plan3", Meta3_activa, callback_P3)
	rospy.Subscriber("Plan4", Meta4_activa, callback_P4)
	rospy.Subscriber("Plan5", Meta5_activa, callback_P5)
	rospy.Subscriber("Plan6", Meta6_activa, callback_P6)
	rospy.Subscriber("Plan7", Meta7_activa, callback_P7)
	rospy.Subscriber("Plan8", Meta8_activa, callback_P8)
	rospy.Subscriber("Plan9", Meta9_activa, callback_P9)
	rospy.Subscriber("Plan10", Meta10_activa, callback_P10)

	r.sleep()

	rospy.Subscriber('Navegacion',Nav, callback)
	rospy.Subscriber('Navegacionm4',Nav, callbackm4)
	rospy.Subscriber('Navegacionm5',Nav, callbackm5)
	rospy.Subscriber('Navegacionm6',Nav, callbackm6)
	rospy.Subscriber('Navegacionm7',Nav, callbackm7)
	rospy.Subscriber('Navegacionm9',Nav, callbackm9)
	rospy.Subscriber('Navegacionm10',Nav, callbackm10)
	
	r.sleep()

	rospy.spin()
 
def callback(data):
	global nav
	nav = data.nav
#	print(nav)

def callbackm4(data):
	global nav4
	nav4 = data.nav
#	print(nav4)

def callbackm5(data):
	global nav5
	nav5 = data.nav
#	print(nav5)

def callbackm6(data):
	global nav6
	nav6 = data.nav
#	print(nav6)

def callbackm7(data):
	global nav7
	nav7 = data.nav
#	print(nav7)

def callbackm9(data):
	global nav9
	nav9 = data.nav
#	print(nav9)

def callbackm10(data):
	global nav10
	nav10 = data.nav
#	print(nav10)

def write(linear,angular):
	global pub
	pub.publish(Twist(Vector3(linear[0],linear[1],linear[2]),
                   Vector3(angular[0],angular[1],angular[2])))

def callback_P1(data):
	global nav
	meta1=data.meta1

	global Endfsm
	global goal_pointx, goal_pointy
	
	global cocina_x, cocina_y, limpieza_x, limpieza_y, mesa1_x, mesa1_y, mesa2_x, mesa2_y, carga_x, carga_y

	if meta1==1:
		print("meta1 on")
		if nav == "carga" :
			Endfsm = 0
			goal_pointx= carga_x
			goal_pointy= carga_y
			print("en el if1")
		else :
			meta1 = 0
			print("en el else1")
	else:
		print("metas off")

global unv 
unv = 0
def callback_P2(data):
	meta2=data.meta2

	global Endfsm , unv,r
	vel_msg = Twist()

	vel_msg.linear.y=0
	vel_msg.linear.z=0
	vel_msg.angular.x = 0
	vel_msg.angular.y = 0
	global pub
		
	vel_msg2 = Twist()

	vel_msg2.linear.y=0
	vel_msg2.linear.z=0
	vel_msg2.angular.x = 0
	vel_msg2.angular.y = 0

	if meta2==1:
		vel_msg.linear.x=-0.5
		vel_msg.angular.z=1.4
		print("meta2 on")
		Endfsm = 1
		pub.publish(vel_msg)
	else:
		print("metas off")	

def callback_P3(data):
	meta3=data.meta3

	global cocina_x, cocina_y, limpieza_x, limpieza_y, mesa1_x, mesa1_y, mesa2_x, mesa2_y, carga_x, carga_y

	global Endfsm
	global goal_pointx, goal_pointy

def callback_P4(data):
	meta4=data.meta4

	global nav4

	global cocina_x, cocina_y, limpieza_x, limpieza_y, mesa1_x, mesa1_y, mesa2_x, mesa2_y, carga_x, carga_y

	global Endfsm
	global goal_pointx, goal_pointy

	if meta4==1:
		print("meta4 on")

		if nav4 == "cocina" :
			goal_pointx= cocina_x
			goal_pointy= cocina_y
			Endfsm = 0
			print("en el if4")
		elif nav4 == "mesa1":
			goal_pointx= mesa1_x
			goal_pointy= mesa1_y
			print("en el elif4")
			Endfsm = 0
		else :
			print("en el else4")
	else:
		print("metas off")


def callback_P5(data):
	meta5=data.meta5

	global nav5
	global cocina_x, cocina_y, limpieza_x, limpieza_y, mesa1_x, mesa1_y, mesa2_x, mesa2_y, carga_x, carga_y
	global Endfsm
	global goal_pointx, goal_pointy

	if meta5==1:
		print("meta5 on")

		if nav5 == "cocina" :
			goal_pointx= cocina_x
			goal_pointy= cocina_y
			Endfsm = 0
			print("en el if5")
		elif nav5 == "mesa2":
			goal_pointx= mesa2_x
			goal_pointy= mesa2_y
			Endfsm = 0
			print("en el elif5")
		else :
			print("en el else5")
	else:
		print("metas off")

def callback_P6(data):
	meta6=data.meta6
	global cocina_x, cocina_y, limpieza_x, limpieza_y, mesa1_x, mesa1_y, mesa2_x, mesa2_y, carga_x, carga_y

	global nav6

	global Endfsm
	global goal_pointx, goal_pointy

	if meta6==1:
		print("meta6 on")

		if nav6 == "mesa1":
			goal_pointx= mesa1_x
			goal_pointy= mesa1_y
			Endfsm = 0
			print("en el if6")
		elif nav6 == "cocina" :
			goal_pointx= cocina_x
			goal_pointy= cocina_y
			Endfsm = 0
			print("en el elif6")
		else :
			print("en el else6")
	else:
		print("metas off")

def callback_P7(data):
	meta7=data.meta7
	global cocina_x, cocina_y, limpieza_x, limpieza_y, mesa1_x, mesa1_y, mesa2_x, mesa2_y, carga_x, carga_y

	global nav7

	global Endfsm
	global goal_pointx, goal_pointy

	if meta7==1:
		print("meta7 on")

		if nav7 == "mesa2":
			goal_pointx= mesa2_x
			goal_pointy= mesa2_y
			Endfsm = 0
			print("en el if7")
		elif nav7 == "cocina" :
			goal_pointx= cocina_x
			goal_pointy= cocina_y
			Endfsm = 0
			print("en el elif7")
		else :
			print("en el else7")
	else:
		print("metas off")

def callback_P8(data):
	meta8=data.meta8
	global cocina_x, cocina_y, limpieza_x, limpieza_y, mesa1_x, mesa1_y, mesa2_x, mesa2_y, carga_x, carga_y

	global nav, nav4

	global Endfsm
	global goal_pointx, goal_pointy

def callback_P9(data):
	meta9=data.meta9
	global cocina_x, cocina_y, limpieza_x, limpieza_y, mesa1_x, mesa1_y, mesa2_x, mesa2_y, carga_x, carga_y

	global nav9

	global Endfsm
	global goal_pointx, goal_pointy, paso

	if meta9==1:
		paso=0
		print("meta9 on")

		if nav9 == "limpieza" :
			goal_pointx= limpieza_x
			goal_pointy= limpieza_y
			Endfsm = 0
			print("en el if9")

		elif nav9 == "n9":
			goal_pointx= 1.5
			goal_pointy= 0
			Endfsm = 0
			print("en el elif9")
			meta9 = 0

		else :
			meta9 = 0
			print("en el else9")

	else:
		print("metas off")



def callback_P10(data):
	meta10=data.meta10

	global nav10
	global cocina_x, cocina_y, limpieza_x, limpieza_y, mesa1_x, mesa1_y, mesa2_x, mesa2_y, carga_x, carga_y

	global Endfsm
	global goal_pointx, goal_pointy

	if meta10==1:

		print("meta10 on")
		if nav10 == "carga" :
			Endfsm = 0
			goal_pointx= carga_x
			goal_pointy= carga_y
			print("en el if10")
		else :
			meta10 = 0
			print("en el else10")
	else:
		print("metas off")

global Endfsm,st,x1,y1,obs, goal_pointx , goal_pointy
goal_pointx = 0
goal_pointy = 0
Endfsm = 1
st = 0
x1 = 0
y1 = 0
obs = 0

global meta1, meta2, meta3, meta4, meta5, meta6, meta7, meta8, meta9, meta10
meta1=0
meta2=0 
meta3=0 
meta4=0 
meta5=0 
meta6=0 
meta7=0 
meta8=0
meta9=0 
meta10=0

global cocina_x, cocina_y, limpieza_x, limpieza_y, mesa1_x, mesa1_y, mesa2_x, mesa2_y, carga_x, carga_y

cocina_x=4
cocina_y=0

limpieza_x=2
limpieza_y=0

mesa1_x=4
mesa1_y=3

mesa2_x=2
mesa2_y=2

carga_x=0
carga_y=0

def fsmx2y(data):

	global Endfsm,st,x1,y1,obs,cuadro, pub_u
	global goal_pointx, goal_pointy	
	global cocina_x, cocina_y, limpieza_x, limpieza_y, mesa1_x, mesa1_y, mesa2_x, mesa2_y, carga_x, carga_y

	x = data.pose.pose.position.x
	y = data.pose.pose.position.y
	#q1 = data.pose.pose.orientation.x
	#q2 = data.pose.pose.orientation.y
	q3 = data.pose.pose.orientation.z
	q4 = data.pose.pose.orientation.w
	#q = (q1, q2, q3, q4)	
	q = (0, 0, q3, q4)
	e = euler_from_quaternion(q)
	th = degrees(e[2])
	th = to_positive_angle(th)	
	print("llegue aqui")
	print(th)


	if Endfsm == 1:
		if goal_pointx == cocina_x and goal_pointy == cocina_y :
			pub_u.publish("cocina")
		elif goal_pointx == limpieza_x and goal_pointy == limpieza_y:
			pub_u.publish("limpieza")
		elif goal_pointx == mesa1_x and goal_pointy == mesa1_y:
			pub_u.publish("mesa1")
		elif goal_pointx == mesa2_x and goal_pointy == mesa2_y:
			pub_u.publish("mesa2")
		elif goal_pointx == carga_x and goal_pointy == carga_y:
			pub_u.publish("carga")
		elif goal_pointx == 1.5 and goal_pointy == 0:
			pub_u.publish("limpiando")
		elif goal_pointx == 1.5 and goal_pointy == -0.5:
			pub_u.publish("limpiando1")
		elif goal_pointx == 2 and goal_pointy == -0.5:
			pub_u.publish("limpiando2")
		elif goal_pointx == 2 and goal_pointy == 0.1:
			pub_u.publish("limpiando3")
		else: 
			pub_u.publish("n")

	goalx = (goal_pointx * cuadro)	
	goaly = (goal_pointy * cuadro)

	if Endfsm == 0:		
		if st == 0:
			if obs == 0:
				if x < (goalx+0.02):
					if not(359.5<th) :	 			
						write([0,0,0],[0,0,-0.3])
						print (th)				
						st = 0
						print("fsm0 buscando 360")
					else:
						y1 = y
						print("pase a 1")
						write([0,0,0],[0,0,0.0])
						st = 1		
				if x > (goalx-0.02):
					if not(179.5<th<180.5) :	 			
						write([0,0,0],[0,0,0.3])
						print (th)				
						st = 0	
						print("fsm0 buscando 180")			
					else:
						y1 = y
						print("pase a 11")
						write([0,0,0],[0,0,0.0])
						st = 11	

				if (goalx-0.02)<x<=(goalx+0.02):
					st = 1
					print("fsm0 x check")

		if st == 1:
			if obs == 0:
				if x!=goalx:
					print(x)
					if y1+0.01 > y > y1-0.01 :						
						write([0.1,0,0],[0,0,0.0])
						st = 1
						print("fsm1 derecho y")
					if not y1+0.01 > y :							
						write([0.1,0,0],[0,0,-0.3])
						st = 1
						print("fsm1 izquierda y")
					if not  y > y1-0.01 :							
						write([0.1,0,0],[0,0,0.3])
						st = 1
						print("fsm1 derecha y")			
				if (goalx-0.02)<x<=(goalx+0.02):
					print(th)
					print(x)
					print(y)
					print(y1)
					st = 2
					print("fsm1 x check")
		if st == 11:
			if obs == 0:
				if x!=goalx:
					print(x)
					if y1+0.01 > y > y1-0.01 :						
						write([0.1,0,0],[0,0,0.0])
						st = 11
						print("fsm11 derecho y")
					if not y1+0.01 > y :							
						write([0.1,0,0],[0,0,0.3])
						st = 11
						print("fsm11 izquierda y")
					if not  y > y1-0.01 :							
						write([0.1,0,0],[0,0,-0.3])
						st = 11		
						print("fsm11 derecha y")	
				if (goalx-0.02)<x<=(goalx+0.02):
					print(th)
					print(x)
					print(y)
					print(y1)
					st = 2
					print("fsm11 x check")
		if st == 2:
			if obs == 0:
				if y < goaly:
					if not(89.5<th<90.5) :	 			
						write([0,0,0],[0,0,-0.3])
						print (th)				
						st = 2	
						print("fsm2 buscando 90")
					else:
						x1 = x
						write([0,0,0],[0,0,0.0])
						st = 3	
						print("pase a 3")	
				if y > goaly:
					if not(269.5<th<270.5) :	 			
						write([0,0,0],[0,0,-0.3])
						print (th)				
						st = 2
						print("fsm2 buscando 270")				
					else:
						x1 = x
						write([0,0,0],[0,0,0.0])
						st = 33
						print("pase a 33")

				if (goaly-0.02)<y<=(goaly+0.02):
					st = 3
					print("fsm2 y check")

		if st == 3:
			if obs == 0:
				if y!=goaly:
					print(y)
					if x1+0.01 > x > x1-0.01 :						
						write([0.1,0,0],[0,0,0.0])
						st = 3
						print("fsm3 derecho x")
					if not x1+0.01 > x :							
						write([0.1,0,0],[0,0,0.3])
						st = 3
						print("fsm3 izquierda x")
					if not  x > x1-0.01 :							
						write([0.1,0,0],[0,0,-0.3])
						st = 3			
						print("fsm3 derecha x")
				if (goaly-0.02)<y<=(goaly+0.02):
					print(th)
					print(x)
					print(y)
					print(y1)
					print(x1)
					st = 0
					Endfsm = 1
					print("fsm3 y check")

		if st == 33:
			if obs == 0:
				if y!=goaly:
					print(y)
					if x1+0.01 > x > x1-0.01 :						
						write([0.1,0,0],[0,0,0.0])
						st = 33
						print("fsm33 derecho x")
					if not x1+0.01 > x :							
						write([0.1,0,0],[0,0,-0.3])
						st = 33
						print("fsm33 izquierda x")

					if not  x > x1-0.01 :							
						write([0.1,0,0],[0,0,0.3])
						st = 33	
						print("fsm33 derecha x")
		
				if (goaly-0.02)<y<=(goaly+0.02):
					print(th)
					print(x)
					print(y)
					print(y1)
					print(x1)
					st = 0
					Endfsm = 1
					print("fsm33 y check")

def to_positive_angle(th):
	while True:
		if th < 0:
			th += 360
		if th > 0:
			ans = th % 360
			return ans
			break

if __name__ == '__main__':

	print("llegue rosconf")
	rosconf()
	print("sali")
	
