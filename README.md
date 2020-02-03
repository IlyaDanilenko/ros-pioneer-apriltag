# ros-pioneer-apriltag
Robot Operating System with GEOSCAN Pioneer
Используется [ROS Melodic Morenia](http://wiki.ros.org/melodic)

### Описание
Структура ROS основа на нодах, каждая нода отвечает за свою часть сообщение между ними происходит с помощью топиков.
Данную задачу я разделил на три части:
* [Анализ картинки](https://github.com/IlyaDanilenko/ros-pioneer-apriltag/blob/master/gs_apriltag/src/apriltag_node.py)
* [Вывод изобрадения с камер для наглядности](https://github.com/IlyaDanilenko/ros-pioneer-apriltag/blob/master/gs_apriltag/src/view_raw_image_node.py)
* [Отправка id тэгов в Pioneer](https://github.com/IlyaDanilenko/ros-pioneer-apriltag/tree/master/gs_apriltag/src)

Одельной задачей можно считать запуск [сценария](https://github.com/IlyaDanilenko/ros-pioneer-apriltag/blob/master/launch/geoscan.launch). Сценарий упрощает запуск нод, а так же запускает ноды в нужном для корректной работы порядке. В сценарии, по мимо описанных выше нод, используется запуск потока с камеры.

### Описание репозитория

В состав репозитория входят:
* Пакет [gs_apriltag](https://github.com/IlyaDanilenko/ros-pioneer-apriltag/tree/master/gs_apriltag)
* [Файл](https://github.com/IlyaDanilenko/ros-pioneer-apriltag/blob/master/config_catkin.txt) конфигурации сборщика для Python 3
* [Папка](https://github.com/IlyaDanilenko/ros-pioneer-apriltag/tree/master/launch) со сценарием
* [Lua скрипты](https://github.com/IlyaDanilenko/ros-pioneer-apriltag/tree/master/Lua)

### Видео работы

* [Видео с комментариями](https://1drv.ms/v/s!Ao6apD9z3iUVgrB6GAzxQURUjpIHCQ)
* [Видео безмолвной работы](https://1drv.ms/v/s!Ao6apD9z3iUVgrB520DtpR7aiocuoA?e=dnCEOx)

### Коментарии автора
На выполенение самой работы времени понадобилось не очень много, но для настройки Raspberry Pi с нуля очень много. 
Все ноды рабочие, но проверить передачу данных на Pioneer мне не удалось по причине не работающего UART на плате.

### Зависимости

В пакете [gs_apriltag](https://github.com/IlyaDanilenko/ros-pioneer-apriltag/tree/master/gs_apriltag) используются некоторые пакеты ROS и Python

Пакеты ROS
* [cv_bridge](http://wiki.ros.org/cv_bridge) 
* [cv_camera](http://wiki.ros.org/cv_camera)

Пакеты Python
* OpenCv
* apriltag