#!/usr/bin/env python2.7

import rospy
from std_msgs.msg import String

#Subscriber node function which will subscribe the messages from the Topic
def messageSubscriber():
	#initialize the subscriber node called 'messageSubNode'
	rospy.init_node('messageSubNode', anonymous=False)    

	#This is to subscribe to the messages from the topic named 'messageTopic'
	rospy.Subscriber('/minihawk_SIM/MH_usb_camera_link_optical/tag_detections', String, callback_str)    

	#rospy.spin() stops the node from exitind until the node has been shut down
	rospy.spin()

#Callback function to print the subscribed data on the terminal
def callback_str(subscribedData):
	rospy.loginfo('Subscribed: ' + subscribedData.data)	
	

if __name__ == '__main__':
	try:
		messageSubscriber()

	except rospy.ROSInterruptException:
		pass
