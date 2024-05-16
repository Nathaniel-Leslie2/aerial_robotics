#!/usr/bin/env python

#Nathaniel Leslie-Rivas
#CS 491
#Purpose: Publish info from rostopic /minihawk_SIM/mavros/rc/override

#import the rospy package and the String message type
import rospy
from std_msgs.msg import String

#function to publish messages at the rate of 2 messages per second
def messagePublisher():
	#define a topic to which the messages will be published
	message_publisher = rospy.Publisher("/minihawk_SIM/mavros/rc/override", String, queue_size=10)

	#initialize the Publisher node. 
	#Setting anonymous=True will append random integers at the end of our publisher node
	rospy.init_node('messagePubNode', anonymous=True)    

	#publishes at a rate of 2 messages per second
	rate = rospy.Rate(1)    

	#Keep publishing the messages until the user interrupts 
	while not rospy.is_shutdown():
		message = "rostopic pub -r 10 /minihawk_SIM/mavros/rc/override mavros_msgs/OverrideRCIn 'channels: [1500, 1500, 1500, 1500, 1800, 1000, 1000, 1800, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]' "    

	#display the message on the terminal	
	rospy.loginfo('Published: ' + message)    

	#publish the message to the topic
	message_publisher.publish(message)    

	#rate.sleep() will wait enough until the node publishes the message to the topic
	rate.sleep()

if __name__ == '__main__':
    try:
	messagePublisher()
    #capture the Interrupt signals
    except rospy.ROSInterruptException:
	pass
