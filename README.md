## Parking Scan 
Parking Scan is a Python application built using Tkinter, designed for managing and visualizing data from a parking lot detection system. It offers a user-friendly interface with features including a login screen, real-time parking lot status visualization, and detailed reports. The application leverages vision-based technology for cost-effective parking guidance.

## Features
- **Easy Login:** Simple and secure login and registration process.
- **Real-Time Parking Lot Status Visualization:** View the status of parking lots in real-time.
- **User-Friendly Interface:** Intuitive and easy-to-navigate interface.
- **Vision-Based Parking Slot Detection and Classification:** Detect and classify parking slots using image-based analysis.
- **High Efficiency in Parking Slot Detection:** Accurate detection of parking slots with high efficiency.
- **High Accuracy in Parking Slot Occupancy Classification:** Reliable classification of parking slot occupancy.


## Project Description 
Parking Scan serves as an interface for Parking Guidance Information (PGI) systems, aimed at providing drivers with information about the nearest parking lots and the number of vacant parking slots. Vision-based solutions are employed as a cost-effective alternative to traditional PGI systems that rely on hardware sensors mounted on each parking slot.

Vision-based systems analyze parking occupancy using images captured by cameras monitoring parking lots. Developing these systems poses challenges such as handling various viewpoints, weather conditions, and object occlusions. Additionally, manual labeling of parking slot locations in images is required, which is sensitive to changes in camera angles, replacements, or maintenance.

This project introduces an algorithm for Automatic Parking Slot Detection and Occupancy Classification (APSD-OC) based solely on input images. The approach involves:

1. Detecting vehicles in a series of parking lot images.
2. Applying clustering in a bird's eye view to identify parking slots.
3. Identifying parking slots using either a series of images or hard-coded slot locations.
4. Classifying each detected parking slot as occupied or vacant using YOLOv5 and basic logic.
5. Displaying the output on the screen using Tkinter GUI.
This comprehensive approach is extensively evaluated on publicly available datasets (PKLot and CNRPark+EXT), demonstrating high efficiency in parking slot detection and significant robustness against illegal parking or passing vehicles. The trained YOLOv5 classifier achieves high accuracy in parking slot occupancy classification.

## About Us
Our project is developed by a dedicated team of students under the guidance of experienced mentors. We aim to create innovative solutions for parking lot management using vision-based technologies.

# Mentors

Dr. Sandeep Mandia
Dr. Shishir Maheshwari
Dr. Neeru Jindal
Prof. Kulbir Singh

# Students

Dhwani Goyal
Aditya Pandey 
Vaibhav Baldeva 
Mridula Pal 
Nitika Joshi 

