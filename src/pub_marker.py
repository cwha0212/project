#!/usr/bin/env python

import rospy
from visualization_msgs.msg import Marker, MarkerArray
from geometry_msgs.msg import Point

def publish_markers():
    rospy.init_node('parking_mark', anonymous=True)
    pub = rospy.Publisher('markers', MarkerArray, queue_size=10)
    rate = rospy.Rate(10)  # 10hz
    i = 0
    points = [[[-19.6416,2.11915,-1.1137],[-19.7893,0.905569,-1.12846],[-17.134,0.812966,-1.13689],[-17.1124,2.13017,-1.11651]],
              [[-45.665,12.7599,-1.0393],[-46.3092,13.7718,-1.05568],[-48.4792,12.1176,-1.13046],[-47.9447,11.2403,-1.13046]]]
    markers = MarkerArray()
    for point in points:
        marker = Marker()
        marker.header.frame_id = "map"
        marker.type = marker.LINE_LIST
        marker.action = marker.ADD
        marker.id = i
        i = i+1
        marker.scale.x = 0.2
        marker.scale.y = 0.2
        marker.scale.z = 0.2
        marker.color.a = 1.0
        marker.color.r = 0.0
        marker.color.g = 0.0
        marker.color.b = 1.0
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

    while not rospy.is_shutdown():
        pub.publish(markers)
        rate.sleep()

if __name__ == '__main__':
    try:
        publish_markers()
    except rospy.ROSInterruptException:
        pass
