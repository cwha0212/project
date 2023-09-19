#!/usr/bin/env python2

import rospy
import struct

from sensor_msgs import point_cloud2
from sensor_msgs.msg import PointCloud2, PointField
from std_msgs.msg import Header

rospy.init_node("create_cloud_xyzrgb")
pub = rospy.Publisher("point_cloud2", PointCloud2, queue_size=2)

points = []

i = 0
use_pose = 0
use_cloud = 0
# with open("/home/chang/map_merge/hand/map1_new.txt", "r") as f:
#     lines = f.readlines()
#     for i, line in enumerate(lines):
#         cc = line.split()
#         x = float(cc[0])
#         y = float(cc[1])
#         z = float(cc[2])
#         r = int(cc[3])
#         g = int(cc[4])
#         b = int(cc[5])
#         a = 255
#         rgb = struct.unpack('I', struct.pack('BBBB', b, g, r, a))[0]
#         pt = [x, y, z, rgb]
#         points.append(pt)
# with open("/home/chang/map_merge/hand/map2_new.txt", "r") as f:
#     lines = f.readlines()
#     for i, line in enumerate(lines):
#         cc = line.split()
#         x = float(cc[0])
#         y = float(cc[1])
#         z = float(cc[2])
#         r = int(cc[3])
#         g = int(cc[4])
#         b = int(cc[5])
#         a = 255
#         rgb = struct.unpack('I', struct.pack('BBBB', b, g, r, a))[0]
#         pt = [x, y, z, rgb]
#         points.append(pt)
# with open("/home/chang/map_merge/hand/map3_new.txt", "r") as f:
#     lines = f.readlines()
#     for i, line in enumerate(lines):
#         cc = line.split()
#         x = float(cc[0])
#         y = float(cc[1])
#         z = float(cc[2])
#         r = int(cc[3])
#         g = int(cc[4])
#         b = int(cc[5])
#         a = 255
#         rgb = struct.unpack('I', struct.pack('BBBB', b, g, r, a))[0]
#         pt = [x, y, z, rgb]
#         points.append(pt)
# with open("/home/chang/map_merge/hand/map4_new.txt", "r") as f:
#     lines = f.readlines()
#     for i, line in enumerate(lines):
#         cc = line.split()
#         x = float(cc[0])
#         y = float(cc[1])
#         z = float(cc[2])
#         r = int(cc[3])
#         g = int(cc[4])
#         b = int(cc[5])
#         a = 255
#         rgb = struct.unpack('I', struct.pack('BBBB', b, g, r, a))[0]
#         pt = [x, y, z, rgb]
#         points.append(pt)
# with open("/home/chang/map_merge/hand/map5_new.txt", "r") as f:
#     lines = f.readlines()
#     for i, line in enumerate(lines):
#         cc = line.split()
#         x = float(cc[0])
#         y = float(cc[1])
#         z = float(cc[2])
#         r = int(cc[3])
#         g = int(cc[4])
#         b = int(cc[5])
#         a = 255
#         rgb = struct.unpack('I', struct.pack('BBBB', b, g, r, a))[0]
#         pt = [x, y, z, rgb]
#         points.append(pt)
# with open("/home/chang/map_merge/hand/map6_new.txt", "r") as f:
#     lines = f.readlines()
#     for i, line in enumerate(lines):
#         cc = line.split()
#         x = float(cc[0])
#         y = float(cc[1])
#         z = float(cc[2])
#         r = int(cc[3])
#         g = int(cc[4])
#         b = int(cc[5])
#         a = 255
#         rgb = struct.unpack('I', struct.pack('BBBB', b, g, r, a))[0]
#         pt = [x, y, z, rgb]
#         points.append(pt)
# with open("/home/chang/map_merge/hand/map7_new.txt", "r") as f:
#     lines = f.readlines()
#     for i, line in enumerate(lines):
#         cc = line.split()
#         x = float(cc[0])
#         y = float(cc[1])
#         z = float(cc[2])
#         r = int(cc[3])
#         g = int(cc[4])
#         b = int(cc[5])
#         a = 255
#         rgb = struct.unpack('I', struct.pack('BBBB', b, g, r, a))[0]
#         pt = [x, y, z, rgb]
#         points.append(pt)
# with open("/home/chang/map_merge/hand/map8_new.txt", "r") as f:
#     lines = f.readlines()
#     for i, line in enumerate(lines):
#         cc = line.split()
#         x = float(cc[0])
#         y = float(cc[1])
#         z = float(cc[2])
#         r = int(cc[3])
#         g = int(cc[4])
#         b = int(cc[5])
#         a = 255
#         rgb = struct.unpack('I', struct.pack('BBBB', b, g, r, a))[0]
#         pt = [x, y, z, rgb]
#         points.append(pt)
with open("/home/chang/map_merge/newnew/t/merge.txt", "r") as f:
    lines = f.readlines()
    for i, line in enumerate(lines):
        cc = line.split()
        x = float(cc[0])
        y = float(cc[1])
        z = float(cc[2])
        r = int(cc[3])
        g = int(cc[4])
        b = int(cc[5])
        a = 255
        if r==74 and g==204 and b==254:
            rgb = struct.unpack('I', struct.pack('BBBB', b, g, r, a))[0]
            pt = [x, y, z, rgb]
            points.append(pt)
        else :
            pass


# with open("/home/chang/map_merge/newnew/t/map8_t.txt", "r") as f:
#     lines = f.readlines()
#     for i, line in enumerate(lines):
#         cc = line.split()
#         x = float(cc[0])
#         y = float(cc[1])
#         z = float(cc[2])
#         r = int(cc[3])
#         g = int(cc[4])
#         b = int(cc[5])
#         a = 255
#         rgb = struct.unpack('I', struct.pack('BBBB', b, g, r, a))[0]
#         pt = [x, y, z, rgb]
#         points.append(pt)


# with open("/home/chang/map_merge/newnew/t/map5_t2.txt", "r") as f:
#     lines = f.readlines()
#     for i, line in enumerate(lines):
#         cc = line.split()
#         x = float(cc[0])
#         y = float(cc[1])
#         z = float(cc[2])
#         r = int(cc[3])
#         g = int(cc[4])
#         b = int(cc[5])
#         a = 255
#         rgb = struct.unpack('I', struct.pack('BBBB', b, g, r, a))[0]
#         pt = [x, y, z, rgb]
#         points.append(pt)

# with open("/home/chang/map_merge/orig/map8_t.txt", "r") as f:
#     lines = f.readlines()
#     for i, line in enumerate(lines):
#         cc = line.split()
#         x = float(cc[0])
#         y = float(cc[1])
#         z = float(cc[2])
#         r = int(cc[3])
#         g = int(cc[4])
#         b = int(cc[5])
#         a = 255
#         if r==74 and g==204 and b==254:
#             rgb = struct.unpack('I', struct.pack('BBBB', b, g, r, a))[0]
#             pt = [x, y, z, rgb]
#             points.append(pt)
#         else :
#             pass

# with open("/home/chang/map_merge/orig/map7_t.txt", "r") as f:
#     lines = f.readlines()
#     for i, line in enumerate(lines):
#         cc = line.split()
#         x = float(cc[0])
#         y = float(cc[1])
#         z = float(cc[2])
#         r = int(cc[3])
#         g = int(cc[4])
#         b = int(cc[5])
#         a = 255
#         if r==74 and g==204 and b==254:
#             rgb = struct.unpack('I', struct.pack('BBBB', b, g, r, a))[0]
#             pt = [x, y, z, rgb]
#             points.append(pt)
#         else :
#             pass

# with open("/home/chang/map_merge/orig/map6_t.txt", "r") as f:
#     lines = f.readlines()
#     for i, line in enumerate(lines):
#         cc = line.split()
#         x = float(cc[0])
#         y = float(cc[1])
#         z = float(cc[2])
#         r = int(cc[3])
#         g = int(cc[4])
#         b = int(cc[5])
#         a = 255
#         if r==74 and g==204 and b==254:
#             rgb = struct.unpack('I', struct.pack('BBBB', b, g, r, a))[0]
#             pt = [x, y, z, rgb]
#             points.append(pt)
#         else :
#             pass
# with open("/home/chang/map_merge/orig/map5_t.txt", "r") as f:
#     lines = f.readlines()
#     for i, line in enumerate(lines):
#         cc = line.split()
#         x = float(cc[0])
#         y = float(cc[1])
#         z = float(cc[2])
#         r = int(cc[3])
#         g = int(cc[4])
#         b = int(cc[5])
#         a = 255
#         if r==74 and g==204 and b==254:
#             rgb = struct.unpack('I', struct.pack('BBBB', b, g, r, a))[0]
#             pt = [x, y, z, rgb]
#             points.append(pt)
#         else :
#             pass

# with open("/home/chang/map_merge/orig/map4_t.txt", "r") as f:
#     lines = f.readlines()
#     for i, line in enumerate(lines):
#         cc = line.split()
#         x = float(cc[0])
#         y = float(cc[1])
#         z = float(cc[2])
#         r = int(cc[3])
#         g = int(cc[4])
#         b = int(cc[5])
#         a = 255
#         if r==74 and g==204 and b==254:
#             rgb = struct.unpack('I', struct.pack('BBBB', b, g, r, a))[0]
#             pt = [x, y, z, rgb]
#             points.append(pt)
#         else :
#             pass

# with open("/home/chang/map_merge/orig/map3_t.txt", "r") as f:
#     lines = f.readlines()
#     for i, line in enumerate(lines):
#         cc = line.split()
#         x = float(cc[0])
#         y = float(cc[1])
#         z = float(cc[2])
#         r = int(cc[3])
#         g = int(cc[4])
#         b = int(cc[5])
#         a = 255
#         if r==74 and g==204 and b==254:
#             rgb = struct.unpack('I', struct.pack('BBBB', b, g, r, a))[0]
#             pt = [x, y, z, rgb]
#             points.append(pt)
#         else :
#             pass

# with open("/home/chang/map_merge/orig/map2_t.txt", "r") as f:
#     lines = f.readlines()
#     for i, line in enumerate(lines):
#         cc = line.split()
#         x = float(cc[0])
#         y = float(cc[1])
#         z = float(cc[2])
#         r = int(cc[3])
#         g = int(cc[4])
#         b = int(cc[5])
#         a = 255
#         if r==74 and g==204 and b==254:
#             rgb = struct.unpack('I', struct.pack('BBBB', b, g, r, a))[0]
#             pt = [x, y, z, rgb]
#             points.append(pt)
#         else :
#             pass

# with open("/home/chang/map_merge/orig/map1_t.txt", "r") as f:
#     lines = f.readlines()
#     for i, line in enumerate(lines):
#         cc = line.split()
#         x = float(cc[0])
#         y = float(cc[1])
#         z = float(cc[2])
#         r = int(cc[3])
#         g = int(cc[4])
#         b = int(cc[5])
#         a = 255
#         if r==74 and g==204 and b==254:
#             rgb = struct.unpack('I', struct.pack('BBBB', b, g, r, a))[0]
#             pt = [x, y, z, rgb]
#             points.append(pt)
#         else :
#             pass

# with open("/home/chang/map_merge/Mapping_result/transformed/map6_transformed.txt", "r") as f:
#     lines = f.readlines()
#     for i, line in enumerate(lines):
#         cc = line.split()
#         x = float(cc[0])
#         y = float(cc[1])
#         z = float(cc[2])
#         r = int(cc[3])
#         g = int(cc[4])
#         b = int(cc[5])
#         a = 255
#         rgb = struct.unpack('I', struct.pack('BBBB', b, g, r, a))[0]
#         pt = [x, y, z, rgb]
#         points.append(pt)

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
    rospy.sleep(5.0)
