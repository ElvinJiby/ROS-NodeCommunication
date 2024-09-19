#!/usr/bin/env python3

import rospy
from std_msgs.msg import Int64

# 30/04/2024
# COMP20170 Introduction to Robotics - Assignment 4 - Robotic Operating System
# Made by Elvin Jiby
#
# This is the ROS node that subscribes to the number_publisher and receives messages
# on the current number count

count = 0  # global variable to store count
pub = None  # variable to store the publisher


# function to handle incoming messages on /number topic
def callback_number(msg):
    rospy.loginfo("Received %d on /number topic", msg.data)  # print a message if data was received
    global count  # use the global variable defined
    count = msg.data  # increment the count by the received data

    new_msg = Int64()  # make a new message
    new_msg.data = count  # set its data to the updated count value

    pub.publish(new_msg)  # publish this new count value on the /number_count topic


if __name__ == '__main__':
    # initialise a ROS node called number_counter
    rospy.init_node('number_counter', anonymous=True)

    # subscribe to /number and use callback_number function to handle incoming messages
    rospy.Subscriber('/number', Int64, callback_number)

    # set the publisher to /number_count
    pub = rospy.Publisher('/number_count', Int64, queue_size=10)

    rospy.spin()  # loop until program is stopped
