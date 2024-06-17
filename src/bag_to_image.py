import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import cv2
import os
# class BagToImage:
#     def __init__(self):
#         self.bridge = CvBridge()
#         self.sub = rospy.Subscriber('/camera/color/image_raw', Image, self.callback)
#         self.i = 0

#     def callback(self, data):
#         try:
#             if self.i % 5 == 0:
#                 img = self.bridge.imgmsg_to_cv2(data, "bgr8")
#                 name = "frame" + str(self.i).zfill(5) + ".jpg"
#                 name = "/media/chang/jairlab_ssd/proj_library/realsense_0717_library/img/" + name
#                 cv2.imwrite(name,img)
#             self.i += 1
#         except CvBridgeError as e:
#             rospy.logerr(e)

class BagToImage:
    def __init__(self):
        self.bridge = CvBridge()
        self.sub = rospy.Subscriber('/stereo/right/image_raw', Image, self.callback)
        self.i = 0
        self.img_list = os.listdir('/home/chang/Downloads/urban38-pankyo/image/stereo_right/')
        self.img_list.sort()

        print("list call complete!~")

    def callback(self, data):
        try:
            img = self.bridge.imgmsg_to_cv2(data, "32FC1")
            normalized_img = cv2.normalize(img, None, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_32F)
            uint8_img = cv2.convertScaleAbs(normalized_img, alpha=(255.0))
            img = cv2.cvtColor(uint8_img, cv2.COLOR_BayerBG2RGB)
            name = "/home/chang/Downloads/urban38-pankyo/image/color/" + self.img_list[self.i]
            cv2.imwrite(name,img)
            print("save")
            self.i +=1
        except CvBridgeError as e:
            rospy.logerr(e)

if __name__ == '__main__':
    rospy.init_node('BagToImage')
    BagToImage = BagToImage()
    rospy.spin()
