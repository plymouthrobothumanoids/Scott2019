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

* Open a new termianl tab for running the dynamixel controller/s

First the robot packages need to be sourced. Digit:

```shell
source ~/Scott2019/devel/setup.bash
```

* Use one of the two controller methods for controlling the dynamixels.

1. Method one (single controller method)

This method launches both parts of the controller system at once. This is useful when all dynamixels are known and wanting to be controlled.

Digit:

```shell
roslaunch scott_robot dynamixels.launch
```

2. Method two (dual controller method)

This method uses one launch file to start the controller manager and a seperate launch file generate controllers for each dynamixel. The first launch file can be used on it's own to determine what dynamixels have been detected and what IDs they have assigned to them.

Digit:

```shell
roslaunch scott_robot controller_manager.launch
```
Then open a new tab, source the package, and digit:

```shell
roslaunch scott_robot start_tilt_controller.launch
```

If /dev/ttyUSB0 can't be found then the U2D2 may have mounted to a different port. If this is the case then you will need to change the port in the dynamixel.launch file to the port that the U2D2 is mounted to. If you are denied access to /dev/ttyUSB0 then you will need to run 
```shell
sudo usermod -a -G dialout ${USER}
```
and then restart the computer for the changes to take affect. 

* Run movement script

Two scripts are included, one for setting the robot in a standing position and another for having the robot stand and wave.
New scripts can be created to control the robot in any way that it is physically possible to do so.

Script start example:

```shell
rosrun scott_robot mainStand.py
```

Scripts need to be put in the "scripts" folder to be located by ros and be set to be executable inorder to use rosrun.

This can be done with:

```shell
chmod +x <file_name.type>
```

## Additoanl commands

These are some additonal ros commands that may be useful for mannual control of the servos.

* rostopic list - Lists all of the current ros topics
* rostopic echo <topic_name> - Outputs the current topic data 
* rosnode list - Lists all of the current ros nodes
* rostopic pub -1 /<joint_controller_name>/command std_msgs/Float64 -- <angle> - Sets a servo to a specific angle in radians
* rostopic pub -1 <joint_controller_name>/set_speed <speed> - Sets the speed of a specific servo in radians per second
* rostopic pub -1 <joint_controller_name>/torque_enable - Toggles the torque of a specific servo

The full controller manager ros api can be found here: http://library.isr.ist.utl.pt/docs/roswiki/dynamixel_controllers.html 

