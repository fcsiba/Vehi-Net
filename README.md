# Vehi-Connect
FYP Fall 2018:

This project consists of a simulation of multiple self driving vehicles which are wirelessly interconnected to each other and are continuously sharing their sensor data amongst themselves. Vehicles will use this shared data to make corrective measures in their driving, they will have the ability to detect an accident or problem in their path before they reach the point of the problem, laying the groundwork for a connected, safer future. The Simulation is built on the Robot simulation platform, "WEBOTS". Vehi-Connect scans the vicinity for other vehicles and tracks their positions, directions and speeds, warning other vehicles of potential hazards that might otherwise be invisible. Vehi-Connect holds tremendous potential, as this technology enables the car to acquire and analyse information outside the bounds of the driver’s field of vision.


# How to Run Project:
## 1) Installing Webots
This project runs on webots, an open source robotics simulation software. First thing to do is downnload and install the software. Visit this link to download webots https://cyberbotics.com/download
.Depending on the Operating System of your machine, select the version you want to download. Once download is complete, install the file and restart your system

## 2) Setting up the world in Webots
Start Webots by double-clicking on its icon (or invoking it from a command line in a Terminal). If you are running Webots for the first time on this computer, you may be prompted to select a graphical theme. You may also be invited to follow the Webots guided tour, go ahead and close the guided tour.
Pause the current simulation by clicking on the Pause button of the 3D view. The simulation is paused if the virtual time counter on the main toolbar is stopped. Create a new project from the Wizards menu by selecting the New Project Directory... menu item. Follow the instructions. Name the project directory VehiConnect_simulation instead of the proposed my_project. Name the world file my_first_simulation.wbt instead of the proposed empty.wbt. Go to file, and choose "Import VRML97" and in the file selection menu choose, the "city.wrl" (city world file). The world file contains all the information  regarding the world in webots 

## 3) Creating a controller
### What is a controller?
A controller is a program that defines the behavior of a robot. Webots controllers can be written in the following programming languages: C, C++, Java, Python, MATLAB, ROS, etc. C, C++ and Java controllers need to be compiled before they can be run as robot controllers. Python and MATLAB controllers are interpreted languages so they will run without being compiled. In this tutorial, we are going to use C as a reference language but all the code snippets are also available in C++, Java, Python and MATLAB
### Implementation
Create a new C (or any other language) controller called Auto_driver.c. using the Wizards / New Robot Controller... menu. This will create a new directory in my_first_simulation/controllers. Select the option offering you to open the source file in the text editor. Once you have the ability to open the text editor, copy the contents of file " Auto_driver.c from this repository and save it into the controller file that you have just created. 

## 4) Linking the car to the Controller
By now if you have followed all the step above, you would now see your controller file amongst all other controller files. Now you can link the car connected to the controller. To do this, find the node "BMW X5" on the window in the left side of the software. Double click on it and a drop down menu will appear. In the menu, find "controller". Double Click controller and choose the controller you created in the above step: auto_drive

## 5) Run the Simulation 
You can now run the simulation and see the results.
