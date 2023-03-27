import rospy
import sensor_msgs.point_cloud2 as pc2
from sensor_msgs.msg import PointCloud2
from visualization_msgs.msg import Marker, MarkerArray
from geometry_msgs.msg import Point, Vector3
from std_msgs.msg import ColorRGBA
import numpy as np

# PointCloud2 메시지를 처리하는 콜백 함수 정의
def pointcloud_callback(msg):
    # 강도 데이터를 저장할 빈 리스트 생성
    intensities = []
    x = []
    y = []
    z = []
    points = np.empty((1,3))
    marker = Marker()
    marker.header.frame_id = '/map'
    marker.ns = "name"
    marker.id = rospy.time.now()
    marker.action = Marker.ADD
    marker.color = ColorRGBA(0,0,1,1)
    marker.type = Marker.POINTS
    marker.scale = Vector3(0.1,0.1,0)
    # PointCloud2 메시지에서 데이터 추출
    for data in pc2.read_points(msg, field_names=("intensity",), skip_nans=True):
      intensities.append(data[0])
    for data in pc2.read_points(msg, field_names=("x",), skip_nans=True):
      x.append(data[0])
    for data in pc2.read_points(msg, field_names=("y",), skip_nans=True):
      y.append(data[0])
    for data in pc2.read_points(msg, field_names=("z",), skip_nans=True):
      z.append(data[0])
    # 강도 데이터를 사용하여 작업 수행
    for i,intensity in enumerate(intensities):
      if intensity>100:
        points = np.append(points,np.array([[x[i],y[i],z[i]]]),axis=0)
        marker.points.append(Point(x[i],y[i],z[i]))
        pub.publish(marker)
        print(points)

rospy.init_node('pointcloud_subscriber')
pub = rospy.Publisher('/point',Marker, queue_size=100)
sub = rospy.Subscriber('/cloud_registered', PointCloud2, pointcloud_callback)
rospy.spin()
