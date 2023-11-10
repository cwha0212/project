#!/usr/bin/env python3
import rospy
import struct
from sensor_msgs import point_cloud2
from sensor_msgs.msg import PointCloud2, PointField
from geometry_msgs.msg import PoseStamped
from std_msgs.msg import Header
import numpy as np
import cv2

def callback_point2(data):
   File = open("/home/chang/jinsudang_6.txt", "w")
   if (len(data.data)>=1000):
      for point in point_cloud2.read_points(data):
         pt_x = point[0]
         pt_y = point[1]
         pt_z = point[2]
         rgb = struct.unpack('I', struct.pack('BBBB', 255,255,255, 255))[0]
         pt_c = rgb
         File.write(str(pt_x)+' '+str(pt_y)+' '+str(pt_z)+' '+str(pt_c)+"\n")
         print("save")
   File.close()

def Point_sub():

   rospy.Subscriber('/orb_slam3/all_points',PointCloud2,callback_point2)

   rospy.spin()

if __name__ == '__main__':      
   rospy.init_node('point_sub',anonymous=True)
        
   try:
      Point_sub() 
      
   except rospy.ROSInterruptException:
      pass
