#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import rospy
import cv2
from rospy import Subscriber
from sensor_msgs.msg import Image
from cv_bridge import CvBridge,CvBridgeError

rospy.init_node("view_raw_image_node") # инициализация ноды
bridge=CvBridge() # конвертер из ROS изображения в OpenCv изображения


def callback(data): # функция подписчика 
    global bridge
    try:
        img=bridge.imgmsg_to_cv2(data,"bgr8") # конвертирование картиники ROS в OpenCv
        cv2.imshow("Camera",img) # вывод изображения
        cv2.waitKey(1)
    except CvBridgeError as e:
        rospy.loginfo("cv_bridge error")

sub=Subscriber("/cv_camera/image_raw",Image,callback) # создания подписчика на топик с изобрадениями с камер

while not rospy.is_shutdown(): # обязательное часть иначе нода прирвется после приема одного сообщения 
    pass
