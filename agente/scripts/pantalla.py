#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from agente.msg import Pantalla
from agente.msg import Meta3_activa


def callback_P3(data_pan):

	if data_pan.pantalla == 1:

		print("            ***************            ")
		print("         *********************         ")
		print("      ***************************      ")
		print("     *****************************     ")
		print("    *******************************    ")
		print("   ******    *************    ******   ")
		print("  ******  **  ***********  **  ******  ")
		print("  *******    *************    *******  ")
		print(" ************************************* ")
		print(" ************************************* ")
		print("***************************************")
		print("******************** ******************")
		print("*******************   *****************")
		print(" ************************************* ")
		print(" ******* ********************* ******* ")
		print("  *******  *****************  *******  ")
		print("  ********   *************   ********  ")
		print("   ********                 ********   ")
		print("    *********             *********    ")
		print("     *****************************     ")
		print("      ***************************      ")
		print("         *********************         ")
		print("            ***************            ")

	else:

		print("            ***************            ")
		print("         *********************         ")
		print("      ***************************      ")
		print("     *****************************     ")
		print("    *******************************    ")
		print("   ******    *************    ******   ")
		print("  ******  **  ***********  **  ******  ")
		print("  *******    *************    *******  ")
		print(" ************************************* ")
		print(" ************************************* ")
		print("***************************************")
		print("***************************************")
		print("***************************************")
		print(" ************************************* ")
		print(" ************************************* ")
		print("  ***********************************  ")
		print("  ********                   ********  ")
		print("   *******                   *******   ")
		print("    *******************************    ")
		print("     *****************************     ")
		print("      ***************************      ")
		print("         *********************         ")
		print("            ***************            ")
		print(" ")


 
def listener():
	
	rospy.init_node('Pantalla', anonymous=True)

	rospy.Subscriber("Plan3", Meta3_activa, callback_P3)

        rospy.sleep(1)
	rospy.spin()

if __name__ == '__main__':

	listener()
