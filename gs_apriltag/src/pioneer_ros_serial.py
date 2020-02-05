#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import rospy
from rospy import Subscriber
from std_msgs.msg import Int32
import serial
from time import sleep

ser=serial.Serial("/dev/ttyS0",9600) # объявления UART для сообщения с пионером
sost=b'n' # объявление начального состояние (нулевой id)

def sender(new_sost): # функция отправки сообщения на пионер
    global ser
    global sost
    if(sost!=new_sost): # для того что бы не забивать буфер пионера идет проверка на пофторение id в потоке
        ser.write(new_sost)
        sost=new_sost
        sleep(0.08) # время синхронизации

def callback(data): # функция обработки приема сообщений из топика с id
    dati=data.data 
    if (dati==-100): # интерпритация не распознанных apriltag
        new_sost=b'n'
    else:
        new_sost=bytes(str(dati),'utf-8') # конвертация id apriltag в сообщение для пионера
    sender(new_sost)
    

rospy.init_node("pioneer_ros_serial_node") # инициализация ноды
sub=Subscriber("/geoscan/apriltag_id",Int32,callback) # объявление подписки на топик с id apriltag

while not rospy.is_shutdown():  # обязательное часть иначе нода прирвется после приема одного сообщения 
    pass
