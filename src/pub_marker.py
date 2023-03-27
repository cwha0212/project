#!/usr/bin/env python

import rospy
from visualization_msgs.msg import Marker
from geometry_msgs.msg import Point

def publish_markers():
    rospy.init_node('my_marker_node', anonymous=True)
    pub = rospy.Publisher('markers', Marker, queue_size=10)
    rate = rospy.Rate(10)  # 10hz

    while not rospy.is_shutdown():
        marker = Marker()
        marker.header.frame_id = "map"
        marker.type = marker.LINE_LIST
        marker.action = marker.ADD
        marker.scale.x = 0.2
        marker.scale.y = 0.2
        marker.scale.z = 0.2
        marker.color.a = 1.0
        marker.color.r = 0.0
        marker.color.g = 0.0
        marker.color.b = 1.0

        p1 = Point()
        p1.x = -19.6416
        p1.y = 2.11915
        p1.z = -1.1137

        p2 = Point()
        p2.x = -19.7893
        p2.y = 0.905569
        p2.z = -1.12846

        p3 = Point()
        p3.x = -17.134
        p3.y = 0.812966
        p3.z = -1.13689

        p4 = Point()
        p4.x = -17.1124
        p4.y = 2.13017
        p4.z = -1.11651

        marker.points.append(p1)
        marker.points.append(p2)

        marker.points.append(p2)
        marker.points.append(p3)

        marker.points.append(p3)
        marker.points.append(p4)

        marker.points.append(p4)
        marker.points.append(p1)

        pub.publish(marker)
        rate.sleep()

if __name__ == '__main__':
    try:
        publish_markers()
    except rospy.ROSInterruptException:
        pass
