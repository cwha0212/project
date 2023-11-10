#!/usr/bin/env python

import rospy
from sensor_msgs.msg import Imu

def callback(data):
    new_data = Imu()
    new_data = data
    new_data.angular_velocity.y = 0
    pub.publish(new_data)

rospy.init_node('new_imu')
pub = rospy.Publisher('publish_imu', Imu, queue_size=100)
sub = rospy.Subscriber('/camera/imu', Imu, callback)
rospy.spin()