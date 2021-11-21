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

global piso1,piso2,piso3,piso4
piso1 = 0
piso2 = 0
piso3 = 0
piso4 = 0
def callback_m1(data):
	global meta2, meta3, meta4, meta5, meta6, meta7, meta8, meta9, meta10, pub1,pub2,pub3,pub4,pub5,pub6,pub7,pub8,pub9,pub10	
	global piso1,piso2,piso3,piso4

	meta1=data.meta1

	print 'meta1 = ', meta1
	print 'meta2 = ', meta2
	print 'meta3 = ', meta3
	print 'meta4 = ', meta4
	print 'meta5 = ', meta5
	print 'meta6 = ', meta6
	print 'meta7 = ', meta7
	print 'meta8 = ', meta8
	print 'meta9 = ', meta9
	print 'meta10 = ', meta10

	if meta1 == 0 and meta2 == 0 :
		if meta3 == 0 and meta4 == 0 and meta5 == 0:
			if meta6 == 0 and meta7 == 0 and meta8 == 0:
				piso4=1
			else:
				piso3=1
		else:
			piso2=1
	else:
		piso1=1

	
	if piso1==1 :
		if meta1==1 and meta2==1:
	 		print("contribucion piso 1")
			pub1.publish(1)
			pub2.publish(1)
			pub3.publish(0)
			pub4.publish(0)
			pub5.publish(0)
			pub6.publish(0)
			pub7.publish(0)
			pub8.publish(0)
			pub9.publish(0)
			pub10.publish(0)
			piso1=0
		elif meta1==1 and meta2==0 :
			print("meta 1 activa")
			pub1.publish(1)
			pub2.publish(0)
			pub3.publish(0)
			pub4.publish(0)
			pub5.publish(0)
			pub6.publish(0)
			pub7.publish(0)
			pub8.publish(0)
			pub9.publish(0)
			pub10.publish(0)
			piso1=0
		elif meta1==0 and meta2==1 :
			print("meta 2 activa")
			pub1.publish(0)
			pub2.publish(1)
			pub3.publish(0)
			pub4.publish(0)
			pub5.publish(0)
			pub6.publish(0)
			pub7.publish(0)
			pub8.publish(0)
			pub9.publish(0)
			pub10.publish(0)
			piso1=0
		else :
			print("ninguna meta activa p1")
			pub1.publish(0)
			pub2.publish(0)
			pub3.publish(0)
			pub4.publish(0)
			pub5.publish(0)
			pub6.publish(0)
			pub7.publish(0)
			pub8.publish(0)
			pub9.publish(0)
			pub10.publish(0)
			piso1=0
	if piso2==1 :
		if meta3==1 and meta4==1 and meta5==1:
			print("contribucion piso 2")
			pub1.publish(0)
			pub2.publish(0)
			pub3.publish(1)
			pub4.publish(1)
			pub5.publish(1)
			pub6.publish(0)
			pub7.publish(0)
			pub8.publish(0)
			pub9.publish(0)
			pub10.publish(0)
			piso2=0
		elif  meta3==1 and meta4==1 and meta5==0:
			print("contribucion piso 2")
			pub1.publish(0)
			pub2.publish(0)
			pub3.publish(1)
			pub4.publish(1)
			pub5.publish(0)
			pub6.publish(0)
			pub7.publish(0)
			pub8.publish(0)
			pub9.publish(0)
			pub10.publish(0)
			piso2=0
		elif meta3==1 and meta4==0 and meta5==1:
			print("contribucion piso 2")
			pub1.publish(0)
			pub2.publish(0)
			pub3.publish(1)
			pub4.publish(0)
			pub5.publish(1)
			pub6.publish(0)
			pub7.publish(0)
			pub8.publish(0)
			pub9.publish(0)
			pub10.publish(0)
			piso2=0
		elif  meta3==0 and meta4==1 and meta5==1:
			print("contribucion piso 2")
			pub1.publish(0)
			pub2.publish(0)
			pub3.publish(0)
			pub4.publish(1)
			pub5.publish(1)
			pub6.publish(0)
			pub7.publish(0)
			pub8.publish(0)
			pub9.publish(0)
			pub10.publish(0)
			piso2=0
		elif meta3==1 and meta4==0 and meta5==0:
			print("meta 3 activa")
			pub1.publish(0)
			pub2.publish(0)
			pub3.publish(1)
			pub4.publish(0)
			pub5.publish(0)
			pub6.publish(0)
			pub7.publish(0)
			pub8.publish(0)
			pub9.publish(0)
			pub10.publish(0)
			piso2=0
		elif meta3==0 and meta4==1 and meta5==0:
			print("meta 4 activa")
			pub1.publish(0)
			pub2.publish(0)
			pub3.publish(0)
			pub4.publish(1)
			pub5.publish(0)
			pub6.publish(0)
			pub7.publish(0)
			pub8.publish(0)
			pub9.publish(0)
			pub10.publish(0)
			piso2=0

		elif meta3==0 and meta4==0 and meta5==1:
			print("meta 5 activa")
			pub1.publish(0)
			pub2.publish(0)
			pub3.publish(0)
			pub4.publish(0)
			pub5.publish(1)
			pub6.publish(0)
			pub7.publish(0)
			pub8.publish(0)
			pub9.publish(0)
			pub10.publish(0)
			piso2=0
		else :
			print("ninguna meta activa p2")
			pub1.publish(0)
			pub2.publish(0)
			pub3.publish(0)
			pub4.publish(0)
			pub5.publish(0)
			pub6.publish(0)
			pub7.publish(0)
			pub8.publish(0)
			pub9.publish(0)
			pub10.publish(0)
			piso2=0
	
	if piso3==1 :
		if meta6==1 and meta7==1 and meta8==1:
			print("contribucion piso 3")
			pub1.publish(0)
			pub2.publish(0)
			pub3.publish(0)
			pub4.publish(0)
			pub5.publish(0)
			pub6.publish(1)
			pub7.publish(1)
			pub8.publish(1)
			pub9.publish(0)
			pub10.publish(0)
			piso3=0
		elif  meta6==1 and meta7==1 and meta8==0:
			print("contribucion piso 3")
			pub1.publish(0)
			pub2.publish(0)
			pub3.publish(0)
			pub4.publish(0)
			pub5.publish(0)
			pub6.publish(1)
			pub7.publish(1)
			pub8.publish(0)
			pub9.publish(0)
			pub10.publish(0)
			piso3=0
		elif meta6==1 and meta7==0 and meta8==1:
			print("contribucion piso 3")
			pub1.publish(0)
			pub2.publish(0)
			pub3.publish(0)
			pub4.publish(0)
			pub5.publish(0)
			pub6.publish(1)
			pub7.publish(0)
			pub8.publish(1)
			pub9.publish(0)
			pub10.publish(0)
			piso3=0
		elif  meta6==0 and meta7==1 and meta8==1:
			print("contribucion piso 3")
			pub1.publish(0)
			pub2.publish(0)
			pub3.publish(0)
			pub4.publish(0)
			pub5.publish(0)
			pub6.publish(0)
			pub7.publish(1)
			pub8.publish(1)
			pub9.publish(0)
			pub10.publish(0)
			piso3=0
		elif meta6==1 and meta7==0 and meta8==0:
			print("meta 6 activa")
			pub1.publish(0)
			pub2.publish(0)
			pub3.publish(0)
			pub4.publish(0)
			pub5.publish(0)
			pub6.publish(1)
			pub7.publish(0)
			pub8.publish(0)
			pub9.publish(0)
			pub10.publish(0)
			piso3=0
		elif meta6==0 and meta7==1 and meta8==0:
			print("meta 7 activa")
			pub1.publish(0)
			pub2.publish(0)
			pub3.publish(0)
			pub4.publish(0)
			pub5.publish(0)
			pub6.publish(0)
			pub7.publish(1)
			pub8.publish(0)
			pub9.publish(0)
			pub10.publish(0)
			piso3=0
		elif meta6==0 and meta7==0 and meta8==1:
			print("meta 8 activa")
			pub1.publish(0)
			pub2.publish(0)
			pub3.publish(0)
			pub4.publish(0)
			pub5.publish(0)
			pub6.publish(0)
			pub7.publish(0)
			pub8.publish(1)
			pub9.publish(0)
			pub10.publish(0)
			piso3=0
		else :
			print("ninguna meta activa p3")
			pub1.publish(0)
			pub2.publish(0)
			pub3.publish(0)
			pub4.publish(0)
			pub5.publish(0)
			pub6.publish(0)
			pub7.publish(0)
			pub8.publish(0)
			pub9.publish(0)
			pub10.publish(0)
			piso3=0

	if piso4==1 :
		if meta9==1 and meta10==1:
			print("contribucion piso 4")
			pub1.publish(0)
			pub2.publish(0)
			pub3.publish(0)
			pub4.publish(0)
			pub5.publish(0)
			pub6.publish(0)
			pub7.publish(0)
			pub8.publish(0)
			pub9.publish(1)
			pub10.publish(1)
			piso4=0
		elif meta9==1 and meta10==0 :
			print("meta 9 activa")
			pub1.publish(0)
			pub2.publish(0)
			pub3.publish(0)
			pub4.publish(0)
			pub5.publish(0)
			pub6.publish(0)
			pub7.publish(0)
			pub8.publish(0)
			pub9.publish(1)
			pub10.publish(0)
			piso4=0
		elif meta9==0 and meta10==1:
			print("meta 10 activa")
			pub1.publish(0)
			pub2.publish(0)
			pub3.publish(0)
			pub4.publish(0)
			pub5.publish(0)
			pub6.publish(0)
			pub7.publish(0)
			pub8.publish(0)
			pub9.publish(0)
			pub10.publish(1)
			piso4=0
		else :
			print("ninguna meta activa p4")
			pub1.publish(0)
			pub2.publish(0)
			pub3.publish(0)
			pub4.publish(0)
			pub5.publish(0)
			pub6.publish(0)
			pub7.publish(0)
			pub8.publish(0)
			pub9.publish(0)
			pub10.publish(0)
			piso4=0

def callback_m2(data):
	global meta2
	meta2=data.meta2

def callback_m3(data):
	global meta3
	meta3=data.meta3

def callback_m4(data):
	global meta4
	meta4=data.meta4

def callback_m5(data):
	global meta5
	meta5=data.meta5

def callback_m6(data):
	global meta6
	meta6=data.meta6

def callback_m7(data):
	global meta7
	meta7=data.meta7

def callback_m8(data):
	global meta8
	meta8=data.meta8

def callback_m9(data):
	global meta9
	meta9=data.meta9

def callback_m10(data):
	global meta10
	meta10=data.meta10


def listener():
    
	rospy.init_node('piramide', anonymous=True)

	global pub1,pub2,pub3,pub4,pub5,pub6,pub7,pub8,pub9,pub10

	
	rospy.Subscriber("Meta2_Activa", Meta2_activa, callback_m2)
	rospy.Subscriber("Meta3_Activa", Meta3_activa, callback_m3)
	rospy.Subscriber("Meta4_Activa", Meta4_activa, callback_m4)
	rospy.Subscriber("Meta5_Activa", Meta5_activa, callback_m5)
	rospy.Subscriber("Meta6_Activa", Meta6_activa, callback_m6)
	rospy.Subscriber("Meta7_Activa", Meta7_activa, callback_m7)
	rospy.Subscriber("Meta8_Activa", Meta8_activa, callback_m8)
	rospy.Subscriber("Meta9_Activa", Meta9_activa, callback_m9)
	rospy.Subscriber("Meta10_Activa", Meta10_activa, callback_m10)
	rospy.Subscriber("Meta1_Activa", Meta1_activa, callback_m1) 

	pub1 = rospy.Publisher('Meta1_Piramide',Meta1_activa, queue_size=10)	
	pub2 = rospy.Publisher('Meta2_Piramide',Meta2_activa, queue_size=10)
	pub3 = rospy.Publisher('Meta3_Piramide',Meta3_activa, queue_size=10)	
	pub4 = rospy.Publisher('Meta4_Piramide',Meta4_activa, queue_size=10)
	pub5 = rospy.Publisher('Meta5_Piramide',Meta5_activa, queue_size=10)	
	pub6 = rospy.Publisher('Meta6_Piramide',Meta6_activa, queue_size=10)
	pub7 = rospy.Publisher('Meta7_Piramide',Meta7_activa, queue_size=10)	
	pub8 = rospy.Publisher('Meta8_Piramide',Meta8_activa, queue_size=10)
	pub9 = rospy.Publisher('Meta9_Piramide',Meta9_activa, queue_size=10)	
	pub10 = rospy.Publisher('Meta10_Piramide',Meta10_activa, queue_size=10)

	rospy.spin()

if __name__ == '__main__':
	listener()
