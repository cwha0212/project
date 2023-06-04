#!/usr/bin/env python2

import rospy
import struct
import numpy as np
import time

from sensor_msgs import point_cloud2
from sensor_msgs.msg import PointCloud2, PointField
from std_msgs.msg import Header


rospy.init_node("create_cloud_xyzrgb")
pub = rospy.Publisher("/ouster/points", PointCloud2, queue_size=2)
pub1 = rospy.Publisher("/help", PointCloud2, queue_size=2)

points = []

fields = [PointField('x', 0, PointField.FLOAT32, 1),
          PointField('y', 8, PointField.FLOAT32, 1),
          PointField('z', 16, PointField.FLOAT32, 1),
          # PointField('rgb', 12, PointField.UINT32, 1),
          PointField('rgba', 24, PointField.UINT32, 1),
          ]

# points = []
# points1 = []
# filepath1 = ('/media/chang/jairlab_ssd/new/01/velodyne/0_')
# filepath2 = ('/media/chang/jairlab_ssd/new/01/labels/0_')
# clouds = np.load(filepath1 + '00510' + '.npy')
# labels = np.load(filepath2 + '00510' + '.npy')
# time.sleep(0.1)
# for i,j in enumerate(clouds):
#   if labels[i] == 1:
#     y = j[0] - 0.82
#     x = 0-j[1] + 11.13125969450233216
#     z = j[2] + 0.24521209812845968
#     r = 150
#     g = 255
#     b = 0
#     a = 255
#     rgb = struct.unpack('I', struct.pack('BBBB', b, g, r, a))[0]
#     pt = [x, y, z, rgb]
#     points.append(pt)
#   if labels[i] == 0:
#     y = j[0] - 0.82
#     x = 0-j[1] + 11.13125969450233216
#     z = j[2] + 0.24521209812845968
#     r = 0
#     g = 0
#     b = 255
#     a = 255
#     rgb = struct.unpack('I', struct.pack('BBBB', b, g, r, a))[0]
#     pt = [x, y, z, rgb]
#     points1.append(pt)
# header = Header()
# header.frame_id = "map"
# pc2 = point_cloud2.create_cloud(header, fields, points)
# pc1 = point_cloud2.create_cloud(header, fields, points1)
# while not rospy.is_shutdown():
#     pc2.header.stamp = rospy.Time.now()
#     pc1.header.stamp = rospy.Time.now()
#     pub.publish(pc2)
#     pub1.publish(pc1)
#     rospy.sleep(1.0)

# for i in range(1,1000):
#   points = []
#   i = str(i)
#   num = i.zfill(5)
#   filepath1 = ('/media/chang/jairlab_ssd/new/01/velodyne/0_')
#   filepath2 = ('/media/chang/jairlab_ssd/new/01/labels/0_')
#   clouds = np.load(filepath1 + num + '.npy')
#   labels = np.load(filepath2 + num + '.npy')
#   time.sleep(0.1)
#   for i,j in enumerate(clouds):
#     if labels[i] == 1:
#       x = j[0]
#       y = j[1]
#       z = j[2]
#       r = 0
#       g = 0
#       b = 255
#       a = 255
#       rgb = struct.unpack('I', struct.pack('BBBB', b, g, r, a))[0]
#       pt = [x, y, z, rgb]
#       points.append(pt)
#   header = Header()
#   header.frame_id = "map"
#   pc2 = point_cloud2.create_cloud(header, fields, points)
#   pc2.header.stamp = rospy.Time.now()
#   pub.publish(pc2)

for i in range(1,6000):
  points = []
  i = str(i)
  num = i.zfill(5)
  filepath1 = ('/media/chang/jairlab_ssd/RandLA-Net/data/sequence_0.06/01/velodyne/0_')
  filepath2 = ('/media/chang/jairlab_ssd/RandLA-Net/data/sequence_0.06/01/labels/0_')
  clouds = np.load(filepath1 + num + '.npy')
  labels = np.load(filepath2 + num + '.npy',allow_pickle=True)
  time.sleep(0.06)
  for i,j in enumerate(clouds):
    x = j[0]
    y = j[1]
    z = j[2]
    if labels[i] == 1:
      r = 0
      g = 0
      b = 255
      a = 255
    else:
      r = 255
      g = 0
      b = 0
      a = 255
    rgb = struct.unpack('I', struct.pack('BBBB', b, g, r, a))[0]
    pt = [x, y, z, rgb]
    points.append(pt)
  header = Header()
  header.frame_id = "os_sensor"
  pc2 = point_cloud2.create_cloud(header, fields, points)
  pc2.header.stamp = rospy.Time.now()
  pub.publish(pc2)
