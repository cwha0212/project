#!/usr/bin/env python

import rospy
from sensor_msgs.msg import CompressedImage, Image
from cv_bridge import CvBridge, CvBridgeError
import cv2
import open3d

class CompressedToImage:
    def __init__(self):
        self.bridge = CvBridge()
        self.sub = rospy.Subscriber('/zed2i/zed_node/left_raw/image_raw_color/compressed', CompressedImage, self.callback)
        self.pub = rospy.Publisher('/image', Image, queue_size=1)

    def callback(self, data):
        try:
            img = self.bridge.compressed_imgmsg_to_cv2(data, "bgr8")
            cv2.imwrite("img.jpg",img)
            img_msg = self.bridge.cv2_to_imgmsg(img, "bgr8")
            self.pub.publish(img_msg)
        except CvBridgeError as e:
            rospy.logerr(e)

if __name__ == '__main__':
    rospy.init_node('compressed_to_image')
    compressed_to_image = CompressedToImage()
    rospy.spin()
