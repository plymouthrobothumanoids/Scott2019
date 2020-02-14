# Scott Robot Manual

## Installation Guide

* Open a terminal an digit:

```shell
cd ~
git clone https:/github.com/plymouthrobothumanoids/Scott2019.git
```

* Compile the packages using catkin_make

```shell
cd ~/Scott2019
catkin_make
```

## Usage guide

* Open a terminal and start roscore

```shell
roscore
```

*Open a new termianl tab for running the dynamixel controller/s

First the robot packages need to be sourced. Digit:

```shell
source ~/Scott2019/devel/setup.bash
```

There are two controller methods for controlling the dynamixels.

1. Method one (single controller method)

This method launches both parts of the controller system at once. This is useful when all dynamixels are known and wanting to be controlled.

Digit:

```shell
roslaunch scott_robot dynamixels.launch
```

If /dev/ttyUSB0 can't be found then the U2D2 may have mounted to a different port. If this is the case then you will need to change the port in the dynamixel.launch file to the port that the U2D2 is mounted to. If you are denied access to /dev/ttyUSB0 then you will need to run 
```shell
sudo usermod -a -G dialout ${USER}
```
and then restart the computer for the changes to take affect. 


