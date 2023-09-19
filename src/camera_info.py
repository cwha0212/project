#!/usr/bin/env python

import rospy
from visualization_msgs.msg import Marker, MarkerArray
from sensor_msgs.msg import CameraInfo
import time

def publish_camera_info():
    rospy.init_node('camera_info', anonymous=True)
    pub = rospy.Publisher('/camera_info', CameraInfo, queue_size=10)

    camera_info = CameraInfo()
    camera_info.header.frame_id = "os_sensor"
    camera_info.height = 720
    camera_info.width = 1280
    camera_info.distortion_model = 'plumb_bob'
    camera_info.D = [-0.04320148, 0.02779473, 0.00054656, 0.00005142, 0.0]
    camera_info.K = [629.40286502, 0.0, 632.68559124, 0.0, 628.49713703, 371.45812419, 0.0, 0.0, 1.0]
    camera_info.R = [1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0]
    camera_info.P = [629.40286502, 0.0, 632.68559124, 0.0, 0.0, 628.49713703, 371.45812419, 0.0, 0.0, 0.0, 1.0, 0.0]
    camera_info.binning_x = 0
    camera_info.binning_y = 0
    camera_info.roi.x_offset = 0
    camera_info.roi.y_offset = 0
    camera_info.roi.height = 0
    camera_info.roi.width = 0
    camera_info.roi.do_rectify = False

    while not rospy.is_shutdown():
        rate = rospy.Rate(10)  # 10hz
        pub.publish(camera_info)
        rate.sleep()

if __name__ == '__main__':
    try:
        time.sleep(3)
        publish_camera_info()
    except rospy.ROSInterruptException:
        pass
