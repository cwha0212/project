#!/usr/bin/env python

import rospy
from visualization_msgs.msg import Marker, MarkerArray
from geometry_msgs.msg import Point

def publish_markers():
    rospy.init_node('parking_mark', anonymous=True)
    pub = rospy.Publisher('markers', MarkerArray, queue_size=10)
    rate = rospy.Rate(10)  # 10hz
    i = 0
    points = [[[12.5733,-0.837072,-0.482983],[12.7407,-2.138,-0.667137],[15.3831,-2.05285,-0.549528],[15.2886,-0.593477,-0.574932]]]
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
