#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import String
from agente.msg import Num
from agente.msg import Pedido
from agente.msg import Limpieza_mesa
from agente.msg import Ubicacion
from agente.msg import Interaccion
from agente.msg import Ayuda
from kobuki_msgs.msg import SensorState


def talker():

#	rospy.Subscriber("Pedido_feedback", Pedido, callback_p)
#	rospy.Subscriber("Pedidoe_feedback", Pedido, callback_pe)

#	rospy.Subscriber("Limpieza_mesa_feedback", Limpieza_mesa, callback_l_m)
#	rospy.Subscriber("Limpieza_mesae_feedback", Limpieza_mesa, callback_l_me)


	pub_p = rospy.Publisher('Pedido',Pedido, queue_size=10)
	pub_pe = rospy.Publisher('Pedido2',Pedido, queue_size=10)
	pub_l_m = rospy.Publisher('Limpieza_mesa',Limpieza_mesa, queue_size=10)
	pub_l_me = rospy.Publisher('Limpieza_mesa_2',Limpieza_mesa, queue_size=10)
	pub_i = rospy.Publisher('Interaccion',Interaccion, queue_size=10)
	pub_a = rospy.Publisher('Ayuda',Ayuda, queue_size=10)
	pub_pla = rospy.Publisher('Platoencima',Interaccion, queue_size=10)
    
	rospy.init_node('AGENTEDECONTROL', anonymous=True)
	rate = rospy.Rate(10) # 10hz
	ped = Pedido()
	ped2 = Pedido()
	lim_m = Limpieza_mesa()
	lim_me = Limpieza_mesa()
	inter = Interaccion()
	ayud = Ayuda()
	hayplato = Interaccion()
	camara = Interaccion()
	while not rospy.is_shutdown():
		ped.haypedido = 0        
		ped.numerodemesa = 1
        	ped.numerodepedido = 0
        	ped.tiempodepedido = rospy.get_rostime()
        	ped.tipodepedido = 0
        	ped.estadodelpedido = 0
		ped2.haypedido = 0        
		ped2.numerodemesa = 1
        	ped2.numerodepedido = 0
        	ped2.tiempodepedido = rospy.get_rostime()
        	ped2.tipodepedido = 0
        	ped2.estadodelpedido = 0
        	lim_m.numerodemesa_l = 1
        	lim_m.numeroderecoleccion = 0
        	lim_m.mesalimpia = 1
        	lim_me.numerodemesa_l = 0
        	lim_me.numeroderecoleccion = 0
        	lim_me.mesalimpia = 1
		inter.hay_alguien = 0
		ayud.ayuda = 0
		hayplato.hay_alguien = 0
		camara.hay_alguien = 0	

 #       	pub_p.publish(ped)
#		print'Pedido1= ', ped
 #       	pub_pe.publish(ped2)
#		print'Pedido2= ', ped2
 #       	pub_l_m.publish(lim_m)
#		print'Limpieza_mesa1= ', lim_m
 #       	pub_l_me.publish(lim_me)
#		print'Limpieza_mesa2= ', lim_me


        	pub_p.publish(ped)
		print(ped)
        	pub_pe.publish(ped2)
		print(ped2)
        	pub_l_m.publish(lim_m)
		print(lim_m)
        	pub_l_me.publish(lim_me)
		print(lim_me)
        	pub_i.publish(inter)
		print(inter)
        	pub_a.publish(ayud)
		print(ayud)
        	pub_pla.publish(hayplato)
		print 'hayplato:', 0   
        	rate.sleep()

if __name__ == '__main__':
	try:
		talker()
	except rospy.ROSInterruptException:
		pass
