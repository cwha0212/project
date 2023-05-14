#!/usr/bin/env python2

import rospy
import struct

from sensor_msgs import point_cloud2
from sensor_msgs.msg import PointCloud2, PointField
from std_msgs.msg import Header


rospy.init_node("create_cloud_xyzrgb_nvm")
pub = rospy.Publisher("point_cloud2", PointCloud2, queue_size=2)

points = []

i = 0
use_pose = 0
use_cloud = 0

with open("/home/chang/catkin_ws/src/project/7eng.txt", "r") as f:
  lines = f.readlines()
  for line in lines:
    i = i+1
    if i == 3:
      aa = line.split()
      use_pose = int(aa[0])
    if i == use_pose + 5:
      bb = line.split()
      use_cloud = int(bb[0])
    if i >= use_pose + 6 and i <= use_cloud + use_pose + 5:
      cc = line.split()
      x = float(cc[0])
      y = float(cc[1])
      z = float(cc[2])
      r = int(cc[3])
      g = int(cc[4])
      b = int(cc[5])
      a = 255
      rgb = struct.unpack('I', struct.pack('BBBB', b, g, r, a))[0]
      pt = [x, y, z, rgb]
      points.append(pt)

i = 0
use_pose = 0
use_cloud = 0

with open("/home/chang/catkin_ws/src/project/engfactory_result.txt", "r") as f:
  lines = f.readlines()
  for line in lines:
    i = i+1
    if i == 3:
      aa = line.split()
      use_pose = int(aa[0])
    if i == use_pose + 5:
      bb = line.split()
      use_cloud = int(bb[0])
    if i >= use_pose + 6 and i <= use_cloud + use_pose + 5:
      cc = line.split()
      x = float(cc[0])
      y = float(cc[1])
      z = float(cc[2])
      r = int(cc[3])
      g = int(cc[4])
      b = int(cc[5])
      a = 255
      rgb = struct.unpack('I', struct.pack('BBBB', b, g, r, a))[0]
      pt = [x, y, z, rgb]
      points.append(pt)

i = 0
use_pose = 0
use_cloud = 0

with open("/home/chang/catkin_ws/src/project/6eng_result.txt", "r") as f:
  lines = f.readlines()
  for line in lines:
    i = i+1
    if i == 3:
      aa = line.split()
      use_pose = int(aa[0])
    if i == use_pose + 5:
      bb = line.split()
      use_cloud = int(bb[0])
    if i >= use_pose + 6 and i <= use_cloud + use_pose + 5:
      cc = line.split()
      x = float(cc[0])
      y = float(cc[1])
      z = float(cc[2])
      r = int(cc[3])
      g = int(cc[4])
      b = int(cc[5])
      a = 255
      rgb = struct.unpack('I', struct.pack('BBBB', b, g, r, a))[0]
      pt = [x, y, z, rgb]
      points.append(pt)

i = 0
use_pose = 0
use_cloud = 0

with open("/home/chang/catkin_ws/src/project/3eng_result.txt", "r") as f:
  lines = f.readlines()
  for line in lines:
    i = i+1
    if i == 3:
      aa = line.split()
      use_pose = int(aa[0])
    if i == use_pose + 5:
      bb = line.split()
      use_cloud = int(bb[0])
    if i >= use_pose + 6 and i <= use_cloud + use_pose + 5:
      cc = line.split()
      x = float(cc[0])
      y = float(cc[1])
      z = float(cc[2])
      r = int(cc[3])
      g = int(cc[4])
      b = int(cc[5])
      a = 255
      rgb = struct.unpack('I', struct.pack('BBBB', b, g, r, a))[0]
      pt = [x, y, z, rgb]
      points.append(pt)

i = 0
use_pose = 0
use_cloud = 0

with open("/home/chang/catkin_ws/src/project/1eng_result.txt", "r") as f:
  lines = f.readlines()
  for line in lines:
    i = i+1
    if i == 3:
      aa = line.split()
      use_pose = int(aa[0])
    if i == use_pose + 5:
      bb = line.split()
      use_cloud = int(bb[0])
    if i >= use_pose + 6 and i <= use_cloud + use_pose + 5:
      cc = line.split()
      x = float(cc[0])
      y = float(cc[1])
      z = float(cc[2])
      r = int(cc[3])
      g = int(cc[4])
      b = int(cc[5])
      a = 255
      rgb = struct.unpack('I', struct.pack('BBBB', b, g, r, a))[0]
      pt = [x, y, z, rgb]
      points.append(pt)

fields = [PointField('x', 0, PointField.FLOAT32, 1),
          PointField('y', 8, PointField.FLOAT32, 1),
          PointField('z', 16, PointField.FLOAT32, 1),
          # PointField('rgb', 12, PointField.UINT32, 1),
          PointField('rgba', 24, PointField.UINT32, 1),
          ]


header = Header()
header.frame_id = "map"
pc2 = point_cloud2.create_cloud(header, fields, points)

while not rospy.is_shutdown():
    pc2.header.stamp = rospy.Time.now()
    pub.publish(pc2)
    rospy.sleep(1.0)
