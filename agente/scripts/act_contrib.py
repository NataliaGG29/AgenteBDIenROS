#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from agente.msg import Num
from agente.msg import Pedido
from agente.msg import Limpieza_mesa
from agente.msg import Ubicacion
from agente.msg import Interaccion
from agente.msg import Meta
from kobuki_msgs.msg import SensorState



def callback(data):
    numerodemesa = data.numerodemesa
    numerodepedido = data.numerodepedido 
    tiempodepedido = data.tiempodepedido
    tipodepedido = data.tipodepedido 
    estadodelpedido = data.estadodelpedido
    print(data)

def callback_l_m(data_l_m):
    numerodemesa_l = data_l_m.numerodemesa_l
    numeroderecoleccion = data_l_m.numeroderecoleccion
    mesalimpia = data_l_m.mesalimpia
    print(data_l_m)

def callback_u(data_u):
    donde_esta = data_u.donde_esta
    print(data_u)

def callback_i(data_i):
    hay_alguien = data_i.hay_alguien
    print(data_i)

def callback_sensor(data):
    print(data)
 
def act_contrib():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('act_contrib', anonymous=True)

    rospy.Subscriber("CreenciasPedido", Pedido, callback)
    rospy.Subscriber("CreenciasLimpieza_mesa", Limpieza_mesa, callback_l_m)
    rospy.Subscriber("CreenciasUbicacion", Ubicacion, callback_u)
    rospy.Subscriber("CreenciasInteraccion", Interaccion, callback_i)
    rospy.Subscriber("CreenciasSensores", SensorState, callback_sensor)

    pub = rospy.Publisher('MetaActiva',Meta, queue_size=10)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    act_contrib()
