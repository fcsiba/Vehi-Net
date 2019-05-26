# Vehi-Connect
FYP Fall 2018:

This project consists of a simulation of multiple self driving vehicles which are wirelessly interconnected to each other and are continuously sharing their sensor data amongst themselves. Vehicles will use this shared data to make corrective measures in their driving, they will have the ability to detect an accident or problem in their path before they reach the point of the problem, laying the groundwork for a connected, safer future. The Simulation is built on the Robot simulation platform, "WEBOTS". Vehi-Connect scans the vicinity for other vehicles and tracks their positions, directions and speeds, warning other vehicles of potential hazards that might otherwise be invisible. Vehi-Connect holds tremendous potential, as this technology enables the car to acquire and analyse information outside the bounds of the driver’s field of vision.


# How to Run Project:
## 1) Installing Webots
This project runs on webots, an open source robotics simulation software. First thing to do is downnload and install the software. Visit this link to download webots https://cyberbotics.com/download
.Depending on the Operating System of your machine, select the version you want to download. Once download is complete, install the file and restart your system

## 2) Setting up the world in Webots
Once your version of webots is runnig, its time to set up the environment within the software. Go to file, and choose "Import VRML97" and in the file selection menu choose, the "city.wrl" (city world file). The world file contains all the information  regarding the world in webots 

## 3) Creating a controller
### What is a controller?
A controller is a program that defines the behavior of a robot. Webots controllers can be written in the following programming languages: C, C++, Java, Python, MATLAB, ROS, etc. C, C++ and Java controllers need to be compiled before they can be run as robot controllers. Python and MATLAB controllers are interpreted languages so they will run without being compiled. In this tutorial, we are going to use C as a reference language but all the code snippets are also available in C++, Java, Python and MATLAB
