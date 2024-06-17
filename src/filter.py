import numpy as np
from numpy.linalg import inv
import rospy
import sensor_msgs.point_cloud2 as pc2
from sensor_msgs.msg import PointCloud2
from project.msg import Nex1, Nex1_pred
from visualization_msgs.msg import Marker, MarkerArray
from geometry_msgs.msg import Point, Vector3
from std_msgs.msg import ColorRGBA
import numpy as np


class K_filter:
  def __init__(self):
    self.pub = rospy.Publisher('/Nex1_pred',Nex1_pred, queue_size=100)
    self.sub = sub = rospy.Subscriber('/Nex1_pub', Nex1, self.callback)
    self.x_0 = 100
    self.P_0 = 6
    self.i = 0
    self.z_meas = 0
    self.x_esti = None
    self.P = None
    self.J = 0

  def kalman_filter(self, z_meas, x_esti, P):
      A = 1
      H = 1
      Q = 0
      R = 4
      # (1) Prediction.
      x_pred = A * x_esti
      P_pred = A * P * A + Q

      # (2) Kalman Gain.
      K = P_pred * H / (H * P_pred * H + R)

      # (3) Estimation.
      x_esti = x_pred + K * (z_meas - H * x_pred)

      # (4) Error Covariance.
      P = P_pred - K * H * P_pred

      return x_esti, P

  def callback(self, msg):
      pred_msg = Nex1_pred()
      pred_msg.header = msg.header
      ACS1 = msg.ACS1
      self.z_meas = ACS1
      if self.i == 0:
        self.i = self.i+1
        self.x_esti = self.x_0
        self.P = self.P_0
      else:
        self.x_esti, self.P = self.kalman_filter(self.z_meas, self.x_esti, self.P)
      pred_msg.ACS1_pred = self.x_esti
      self.pub.publish(pred_msg)
      if self.z_meas - self.x_esti >= 400:
         if int(msg.header.frame_id) >= 5045 and int(msg.header.frame_id) <= 5499:
            self.J += 1
            print(self.J)


if __name__ == '__main__':
    rospy.init_node('ACS_filter')
    compressed_to_image = K_filter()
    rospy.spin()
