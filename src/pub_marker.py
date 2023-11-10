#!/usr/bin/env python

import rospy
from visualization_msgs.msg import Marker, MarkerArray
from geometry_msgs.msg import Point

def publish_markers():
    data = [[-1.24396, -19.2675, -3.28597], [-0.965169, -0.454852, -1.14931], [-9.35781, -0.536103, -1.14858], [-10.6162, -21.1506, -1.16918]]
    pub = rospy.Publisher('parking_lots', MarkerArray, queue_size=10)
    i = 0
    points=[]
    _p_array = []
    for point in data:
        _p = []
        _p.append(point[0])
        _p.append(point[1])
        _p.append(point[2])
        _p_array.append(_p)
        i += 1
        if i == 4 :
            points.append(_p_array)
            _p_array = []
            i = 0
    markers = MarkerArray()
    i = 0
    for point in points:
        marker = Marker()
        marker.header.frame_id = "world"
        marker.type = marker.LINE_LIST
        marker.action = marker.ADD
        marker.id = i
        i = i+1
        marker.scale.x = 0.5
        marker.scale.y = 0.5
        marker.scale.z = 0.5
        marker.color.a = 1.0
        marker.color.r = 0.0
        marker.color.g = 1.0
        marker.color.b = 0.0
        p_list = []
        for p in point:
            _p = Point()
            _p.x = p[0]
            _p.y = p[1]
            _p.z = p[2]
            p_list.append(_p)
        marker.points.append(p_list[0])
        marker.points.append(p_list[1])
        marker.points.append(p_list[1])
        marker.points.append(p_list[2])
        marker.points.append(p_list[2])
        marker.points.append(p_list[3])
        marker.points.append(p_list[3])
        marker.points.append(p_list[0])
        markers.markers.append(marker)
        pub.publish(markers)

rospy.init_node('parking_lots', anonymous=True)

while True:
    publish_markers()
    rospy.sleep(1.0)