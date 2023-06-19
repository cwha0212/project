import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import cv2

class BagToImage:
    def __init__(self):
        self.bridge = CvBridge()
        self.sub = rospy.Subscriber('/device_0/sensor_1/Color_0/image/data', Image, self.callback)
        self.i = 0

    def callback(self, data):
        try:
            img = self.bridge.imgmsg_to_cv2(data, "bgr8")
            name = "frame" + str(self.i).zfill(5) + ".jpg"
            name = "/media/chang/jairlab_ssd/DATA/visual_sfm/3eng/" + name
            cv2.imwrite(name,img)
            self.i += 1
        except CvBridgeError as e:
            rospy.logerr(e)

if __name__ == '__main__':
    rospy.init_node('BagToImage')
    BagToImage = BagToImage()
    rospy.spin()
