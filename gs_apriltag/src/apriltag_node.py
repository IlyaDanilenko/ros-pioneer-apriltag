#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cv2
import rospy
from rospy import Subscriber,Publisher
from std_msgs.msg import Int32
from sensor_msgs.msg import Image
from cv_bridge import CvBridge,CvBridgeError
from apriltag import Detection,Detector

rospy.init_node("apriltag_node") # обязательный блок инициализации ноды
bridge=CvBridge() # Класс конвертора из картинки форма ROS в формат OpenCv
detector = Detector() # Класс детектора apriltag
pub=Publisher("/geoscan/apriltag_id",Int32,queue_size=10) # объвление Издателя - публикует сообщение в топик в который публикуются id тегов

def callback(data): # функция обработки подписчика
    global bridge
    global detector
    try:
        img=bridge.imgmsg_to_cv2(data,"bgr8") # конвертирование картинки ROS в OpenCv
        img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) # обесцвечивание картинки
        result=detector.detect(img) # детектирование apriltag
        if (len(result)>0):
            pub.publish(result[0].tag_id) # публикует в топик id распознаного apriltag
        else:
            pub.publish(-100) # если детектор не распознал apriltag публикует в топик число соответствующего пустому id

    except CvBridgeError as e:
        rospy.loginfo(str(e))


sub=Subscriber("/cv_camera/image_raw",Image,callback) # подписчик на топик в котором публикуется изображения камеры

while not rospy.is_shutdown(): # обязательное часть иначе нода прирвется после приема одного сообщения
    n=0
