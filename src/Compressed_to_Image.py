#!/usr/bin/env python

import rospy
from sensor_msgs.msg import CompressedImage, Image
from cv_bridge import CvBridge, CvBridgeError
import cv2

# class CompressedToImage:
#     def __init__(self):
#         self.bridge = CvBridge()
#         self.sub = rospy.Subscriber('/zed2i/zed_node/left/image_rect_color/compressed', CompressedImage, self.callback)
#         self.pub = rospy.Publisher('/image', Image, queue_size=1)
#         self.i=0

#     def callback(self, data):
#         try:
#             img = self.bridge.compressed_imgmsg_to_cv2(data, "bgr8")
#             name = "frame" + str(self.i).zfill(5) + ".jpg"
#             name = "/media/chang/jairlab_ssd/1.DATA/proj_jbnu/map8_img/" + name
#             cv2.imwrite(name,img)
#             self.i += 1
#             # img = self.bridge.imgmsg_to_cv2(data, "bgr8")
#             # img_msg = self.bridge.cv2_to_imgmsg(img, "bgr8")
#             # self.pub.publish(img_msg)
#         except CvBridgeError as e:
#             rospy.logerr(e)

class CompressedToImage:
    def __init__(self):
        self.bridge = CvBridge()
        self.sub = rospy.Subscriber('/zed2i/zed_node/left/image_rect_color/compressed', CompressedImage, self.callback)
        self.pub = rospy.Publisher('/left_raw', Image, queue_size=1)
        self.i=0

    def callback(self, data):
        try:
            img = self.bridge.compressed_imgmsg_to_cv2(data, "bgr8")
            # name = "frame.jpg"
            # name = "/home/chang/" + name
            # cv2.imwrite(name,img)
            # self.i += 1
            # img = self.bridge.imgmsg_to_cv2(data, "bgr8")
            img_msg = self.bridge.cv2_to_imgmsg(img, "bgr8")
            img_msg.header = data.header
            self.pub.publish(img_msg)
        except CvBridgeError as e:
            rospy.logerr(e)

if __name__ == '__main__':
    rospy.init_node('compressed_to_image')
    compressed_to_image = CompressedToImage()
    rospy.spin()
