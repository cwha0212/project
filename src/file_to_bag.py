#!/usr/bin/env python

import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
from std_msgs.msg import Header
import cv2
import time

class ImageToBag:
  def __init__(self):
    self.bridge = CvBridge()
    self.pub1 = rospy.Publisher('/RGB', Image, queue_size=10)
    self.pub2 = rospy.Publisher('/DEPTH', Image, queue_size=10)
    self.i = 5
    self.RGB_path = '/home/chang/data/00/2011_10_03_drive_0027_sync/image_02/data/'
    self.DEPTH_path = '/home/chang/data/00/groundtruth/image_02/'
    self.timestamp_file = '/home/chang/data/00/2011_10_03_drive_0027_sync/image_02/data/timestamp.txt'
    self.publish()

  def publish(self):
      num = str(self.i).zfill(10) + ".png"
      RGB_name = self.RGB_path + num
      DEPTH_name = self.DEPTH_path + num
      RGB = cv2.imread(RGB_name, cv2.IMREAD_COLOR)
      DEPTH = cv2.imread(DEPTH_name, cv2.IMREAD_COLOR)
      RGB_msg = self.bridge.cv2_to_imgmsg(RGB, "bgr8")
      DEPTH_msg = self.bridge.cv2_to_imgmsg(DEPTH, "bgr8")
      RGB_msg.header.stamp = rospy.get_rostime()
      DEPTH_msg.header.stamp = rospy.get_rostime()
      self.pub1.publish(RGB_msg)
      self.pub2.publish(DEPTH_msg)
      self.i += 1
      time.sleep(0.1)


if __name__ == '__main__':
  rospy.init_node('image_to_bag')
  rate = rospy.Rate(1)  # 20hz
  ImageToBag = ImageToBag()
  for i in range(5000):
    ImageToBag.publish()
  rospy.spin()