#!/usr/bin/env python3

import rospy
from std_msgs.msg import Int64

# 30/04/2024
# COMP20170 Introduction to Robotics - Assignment 4 - Robotic Operating System
# Made by Elvin Jiby
#
# This is the number_publisher that allows ROS nodes to subscribe to it.
# Increments the count and sends a message to all subscribers containing this count

if __name__ == '__main__':
    rospy.init_node('number_publisher', anonymous=True)  # make an ROS node called number_publisher

    pub = rospy.Publisher('/number', Int64, queue_size=10)  # set the publisher to /number

    rate = rospy.Rate(1)  # set the rate of messages sent to 1 msg/sec

    count = 0  # initialise the counter to 0

    while not rospy.is_shutdown():  # loop until program is stopped
        rospy.loginfo("Publishing: %d" % count)  # display the current value of counter

        msg = Int64()  # make a new message
        msg.data = count  # initialise it with the current counter value
        pub.publish(msg)  # then publish that message to /number

        count += 1  # increment the counter

        rate.sleep()  # sleep to make sure only 1 message is sent per second

    rospy.loginfo("This node has stopped")  # if the node is stopped, display a message to indicate this
