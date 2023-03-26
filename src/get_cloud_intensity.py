import rospy
import sensor_msgs.point_cloud2 as pc2
from sensor_msgs.msg import PointCloud2
import numpy as np

# PointCloud2 메시지를 처리하는 콜백 함수 정의
def pointcloud_callback(msg):
    # 강도 데이터를 저장할 빈 리스트 생성
    intensities = []
    x = []
    y = []
    z = []
    points = np.empty((1,3))
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
        print(points)

rospy.init_node('pointcloud_subscriber')
sub = rospy.Subscriber('/cloud_registered', PointCloud2, pointcloud_callback)
rospy.spin()
