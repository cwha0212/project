import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import cv2

class BagToImage:
    def __init__(self):
        self.bridge = CvBridge()
        self.sub = rospy.Subscriber('/camera/color/image_raw', Image, self.callback)
        self.i = 0

    def callback(self, data):
        try:
            img = self.bridge.imgmsg_to_cv2(data, "bgr8")
            name = "frame" + str(self.i).zfill(5) + ".jpg"
            name = "/media/chang/jairlab_ssd/proj_library/realsense_0717_library/orig_img/" + name
            cv2.imwrite(name,img)
            self.i += 1
        except CvBridgeError as e:
            rospy.logerr(e)

if __name__ == '__main__':
    rospy.init_node('BagToImage')
    BagToImage = BagToImage()
    rospy.spin()
