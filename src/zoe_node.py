import numpy as np
from torchvision.transforms import ToTensor
from PIL import Image as Img
from zoedepth.utils.misc import get_image_from_url, colorize
import torch
import time
from zoedepth.models.builder import build_model
from zoedepth.utils.config import get_config
from pprint import pprint

import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import cv2


class ZoeNode:
    def __init__(self):
        self.bridge = CvBridge()
        self.sub = rospy.Subscriber('/camera/color/image_raw', Image, self.callback)
        self.pubImage = rospy.Publisher('/image', Image, queue_size=1)
        self.pubDepth = rospy.Publisher('/depth', Image, queue_size=1)
        torch.hub.help("intel-isl/MiDaS", "DPT_BEiT_L_384", force_reload=True) 

        self.DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
        if self.DEVICE == "cpu":
            print("WARNING: Running on CPU. This will be slow. Check your CUDA installation.")

        print("*" * 20 + " Testing zoedepth " + "*" * 20)
        conf = get_config("zoedepth", "infer")

        print("Config:")
        pprint(conf)

        self.model = build_model(conf).to(self.DEVICE)
        self.model.eval()

        self.x = torch.rand(1, 3, 384, 512).to(self.DEVICE)

        print("-"*20 + "Testing on a random input" + "-"*20)

        with torch.no_grad():
            out = self.model(self.x)

        if isinstance(out, dict):
            # print shapes of all outputs
            for k, v in out.items():
                if v is not None:
                    print(k, v.shape)
        else:
            print([o.shape for o in out if o is not None])

        print("\n\n")
        print("-"*20 + " Testing on an indoor scene from url " + "-"*20)

    def callback(self, data):
        try :
            # Test img
            t1 = time.time()
            img = self.bridge.imgmsg_to_cv2(data, "8UC3")
            color_coverted = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            pil_image=Img.fromarray(color_coverted)
            orig_size = pil_image.size
            X = ToTensor()(pil_image)
            X = X.unsqueeze(0).to(self.DEVICE)
            out = self.model.infer(X).cpu()
            pred = Img.fromarray(colorize(out))
            pred = pred.resize(orig_size, Img.ANTIALIAS)
            numpy_img = np.array(pred)
            cv_img = cv2.cvtColor(numpy_img, cv2.COLOR_RGB2BGR)
            depth_meg = self.bridge.cv2_to_imgmsg(cv_img, "bgr8")
            depth_meg.header = data.header
            self.pubImage.publish(data)
            self.pubDepth.publish(depth_meg)
        except CvBridgeError as e:
            rospy.logerr(e)

if __name__ == '__main__':
    rospy.init_node('ZoeNode')
    BagToImage = ZoeNode()
    rospy.spin()
