#!/usr/bin/env python

import rospy
from project.msg import Nex1
import time
import pandas as pd
import subprocess

def publish_points(excel_data):
    rospy.init_node('test', anonymous=True)
    pub = rospy.Publisher('/Nex1_pub', Nex1, queue_size=10)
    rate = rospy.Rate(20)  # 20hz

    for index in range(len(excel_data)):
        Nex1_msg = Nex1()
        Nex1_msg.header.frame_id = str(excel_data['COUNT'][index])
        Nex1_msg.header.stamp = rospy.Time.now()
        Nex1_msg.distance = excel_data['표적↔기뢰간 거리'][index]
        Nex1_msg.ROLL = excel_data['ROLL'][index]
        Nex1_msg.PITCH = excel_data['PITCH'][index]
        Nex1_msg.YAW = excel_data['YAW'][index]
        Nex1_msg.P = excel_data['P'][index]
        Nex1_msg.Q = excel_data['Q'][index]
        Nex1_msg.R = excel_data['R'][index]
        Nex1_msg.GMX = excel_data['GMX'][index]
        Nex1_msg.GMY = excel_data['GMY'][index]
        Nex1_msg.GMZ = excel_data['GMZ'][index]
        Nex1_msg.GMT = excel_data['GMT'][index]
        Nex1_msg.TMX = excel_data['TMX'][index]
        Nex1_msg.TMY = excel_data['TMY'][index]
        Nex1_msg.TMZ = excel_data['TMZ'][index]
        Nex1_msg.TMT = excel_data['TMT'][index]
        Nex1_msg.ACS1 = excel_data['ACS1'][index]
        Nex1_msg.ACS2_1 = excel_data['ACS2_1'][index]
        Nex1_msg.ACS2_2 = excel_data['ACS2_2'][index]
        Nex1_msg.ACS2_3 = excel_data['ACS2_3'][index]
        Nex1_msg.ACS2_4 = excel_data['ACS2_4'][index]
        pub.publish(Nex1_msg)
        print(Nex1_msg.header.frame_id)
        rate.sleep()
        

if __name__ == '__main__':
    i= 6 + 1
    df = pd.read_excel('/media/chang/jairlab_ssd/1.DATA/nex1/1028_data.xlsx', sheet_name=[i], engine="openpyxl")
    print("data done")
    publish_points(df[i])