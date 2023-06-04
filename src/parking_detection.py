import rospy
import struct
import sensor_msgs.point_cloud2 as pc2
from sensor_msgs.msg import PointCloud2, PointField
from std_msgs.msg import Header
from project.msg import Point_Array
from nav_msgs.msg import Odometry
import numpy as np

rospy.init_node('parking_detection')
pub1 = rospy.Publisher('/legal',PointCloud2, queue_size=100)
pub2 = rospy.Publisher('/illegal',PointCloud2, queue_size=100)
points_of_parking_lots = [[[0,0],[10,0],[10,10],[0,10]]]
parking_lots_is = 0
R = [[1,0,0,0],
     [0,1,0,0],
     [0,0,1,0],
     [0,0,0,1]]

fields = [PointField('x', 0, PointField.FLOAT32, 1),
          PointField('y', 8, PointField.FLOAT32, 1),
          PointField('z', 16, PointField.FLOAT32, 1),
          # PointField('rgb', 12, PointField.UINT32, 1),
          PointField('rgba', 24, PointField.UINT32, 1),
          ]

def inside_or_outside(polygon, point):
    N = len(polygon)-1
    counter = 0
    p1 = polygon[0]
    for i in range(1, N+1):
        p2 = polygon[i%N]
        if point[1] > min(p1[1], p2[1]) and point[1] <= max(p1[1], p2[1]) and point[0] <= max(p1[0], p2[0]) and p1[1] != p2[1]:
            xinters = (point[1]-p1[1])*(p2[0]-p1[0])/(p2[1]-p1[1]) + p1[0]
            if(p1[0]==p2[0] or point[0]<=xinters):
                counter += 1
        p1 = p2 
    if counter % 2 == 0:
        res = False
    else:
        res = True
    return res

def point_array_callback(msg):
    global parking_lots_is
    i = 0
    _p_array = []
    if parking_lots_is == 0:
      for point in msg.points:
          _p = []
          _p.append(point.x)
          _p.append(point.y)
          _p.append(point.z)
          _p_array.append(_p)
          i += 1
          if i == 4 :
              _p_array.append(_p_array[0])
              points_of_parking_lots.append(_p_array)
              _p_array = []
              i = 0
      parking_lots_is = 1

def pointcloud_callback(msg):
    xyz = []
    _xyz = []
    legal_boards = []
    illegal_boards = []
    fields = [PointField('x', 0, PointField.FLOAT32, 1),
          PointField('y', 8, PointField.FLOAT32, 1),
          PointField('z', 16, PointField.FLOAT32, 1),
          # PointField('rgb', 12, PointField.UINT32, 1),
          PointField('rgba', 24, PointField.UINT32, 1),
          ]
    for data in pc2.read_points(msg, field_names=("x","y","z"), skip_nans=True):
      xyz.append([data[0], data[1], data[2], 1])
    xyz = np.array(xyz)
    print(R)
    _xyz = np.dot(R, xyz.T)
    _xyz = np.delete(_xyz.T, 3, axis = 1)
    for polygon in points_of_parking_lots:
        for i,_point in enumerate(_xyz):
          cloud_x = _xyz[i][0]
          cloud_y = _xyz[i][1]
          cloud_z = _xyz[i][2]
          a = 255
          if inside_or_outside(polygon, _point):
            cloud_r = 100
            cloud_g = 255
            cloud_b = 0
            rgb = struct.unpack('I', struct.pack('BBBB', cloud_b, cloud_g, cloud_r, a))[0]
            pt = [cloud_x, cloud_y, cloud_z, rgb]
            legal_boards.append(pt)
          else :
            cloud_r = 255
            cloud_g = 0
            cloud_b = 0
            rgb = struct.unpack('I', struct.pack('BBBB', cloud_b, cloud_g, cloud_r, a))[0]
            pt = [cloud_x, cloud_y, cloud_z, rgb]
            illegal_boards.append(pt)
    header = Header()
    header.frame_id = "map"
    legal = pc2.create_cloud(header, fields, legal_boards)
    illegal = pc2.create_cloud(header, fields, illegal_boards)
    pub1.publish(legal)
    pub2.publish(illegal)

def Odometry_callback(msg):
    global R
    x = msg.pose.pose.position.x
    y = msg.pose.pose.position.y
    z = msg.pose.pose.position.z
    q_w = msg.pose.pose.orientation.w
    q_x = msg.pose.pose.orientation.x
    q_y = msg.pose.pose.orientation.y
    q_z = msg.pose.pose.orientation.z
    r00 = 2 * (q_w * q_w + q_x * q_x) - 1
    r01 = 2 * (q_x * q_y - q_w * q_z)
    r02 = 2 * (q_x * q_z + q_w * q_y)
    r03 = x

    r10 = 2 * (q_x * q_y + q_w * q_z)
    r11 = 2 * (q_w * q_w + q_y * q_y) - 1
    r12 = 2 * (q_y * q_z - q_w * q_x)
    r13 = y

    r20 = 2 * (q_x * q_z - q_w * q_y)
    r21 = 2 * (q_y * q_z + q_w * q_x)
    r22 = 2 * (q_w * q_w + q_z * q_z) - 1
    r23 = z
    R = np.array([[r00, r01, r02, r03],
                  [r10, r11, r12, r13],
                  [r20, r21, r22, r23],
                  [0, 0, 0, 1]])

sub1 = rospy.Subscriber('/parking_lots_points',Point_Array, point_array_callback)
sub2 = rospy.Subscriber('/ouster/points', PointCloud2, pointcloud_callback)
sub3 = rospy.Subscriber('/odom', Odometry, Odometry_callback)
rospy.spin()
