#!/usr/bin/env python
import rospy
from std_msgs.msg import String
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

#import imutils
#import wringpi



def callback_m1(data):
    print(data)

def callback_m2(data):
    print(data)

def callback_m3(data):
    print(data)

def callback_m4(data):
    print(data)

def callback_m5(data):
    print(data)

def callback_m6(data):
    print(data)

def callback_m7(data):
    print(data)

def callback_m8(data):
    print(data)

def callback_m9(data):
    print(data)

def callback_m10(data):
    print(data)

def listener():
    
    rospy.init_node('gestordemetas', anonymous=True)

    rospy.Subscriber("Meta1_Activa", Meta1_activa, callback_m1)
    rospy.Subscriber("Meta2_Activa", Meta2_activa, callback_m2)
    rospy.Subscriber("Meta3_Activa", Meta3_activa, callback_m1)
    rospy.Subscriber("Meta4_Activa", Meta4_activa, callback_m2)
    rospy.Subscriber("Meta5_Activa", Meta5_activa, callback_m1)
    rospy.Subscriber("Meta6_Activa", Meta6_activa, callback_m2)
    rospy.Subscriber("Meta7_Activa", Meta7_activa, callback_m1)
    rospy.Subscriber("Meta8_Activa", Meta8_activa, callback_m2)
    rospy.Subscriber("Meta9_Activa", Meta9_activa, callback_m1)
    rospy.Subscriber("Meta10_Activa", Meta10_activa, callback_m2)    

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()


if __name__ == '__main__':
   listener()
