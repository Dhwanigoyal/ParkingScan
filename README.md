##Parking Scan

Parking Scan is a Python-based application developed using Tkinter. It is designed to manage and visualize data from a parking lot detection system. The app offers a user-friendly interface with features such as a login screen, real-time visualization of parking lot status, and detailed reports. The application utilizes vision-based technology for cost-effective parking guidance.

##Features

*Simple Login*: Secure and straightforward login and registration process.
*Real-Time Parking Lot Status*: View the current status of parking lots in real-time.
*User-Friendly Interface*: Intuitive and easy-to-navigate design.
*Vision-Based Parking Slot Detection and Classification*: Identify and classify parking slots using image analysis.
*High Efficiency in Parking Slot Detection*: Accurate detection of parking slots with high efficiency.
*High Accuracy in Parking Slot Occupancy Classification*: Reliable classification of parking slot occupancy.

##Project Description

Parking Scan acts as an interface for Parking Guidance Information (PGI) systems, aiming to provide drivers with information about nearby parking lots and the number of available slots. Vision-based solutions are used as a cost-effective alternative to traditional PGI systems that rely on hardware sensors installed in each parking slot.

Vision-based systems analyze parking occupancy using images captured by cameras monitoring parking lots. Developing these systems involves challenges such as dealing with different viewpoints, weather conditions, and object occlusions. Additionally, manual labeling of parking slot locations in images is necessary, which can be sensitive to changes in camera angles, replacements, or maintenance.

This project introduces an algorithm for Automatic Parking Slot Detection and Occupancy Classification (APSD-OC) based solely on input images. The approach involves:

1.Detecting vehicles in a series of parking lot images and applying clustering in a bird's eye view to identify parking slots.
2.Classifying each detected parking slot as occupied or vacant using a specifically trained ResNet34 deep classifier.

The two-step approach is extensively evaluated on publicly available datasets (PKLot and CNRPark+EXT), demonstrating high efficiency in parking slot detection and robustness against illegal parking or passing vehicles. The trained classifier achieves high accuracy in parking slot occupancy classification.

## About Us

Our project is developed by a dedicated team of students under the guidance of experienced mentors. We aim to create innovative solutions for parking lot management using vision-based technologies.

### Mentors

- Prof. Kulbir Singh
- Dr. Neeru Jindal
- Dr. Sandeep Mandia
- Dr. Shishir Maheshwari

### Students
- **Dhwani Goyal** 
- **Aditya Pandey** 
- **Vaibhav Baldeva**
- **Mridula Pal** 
- **Nitika Joshi**


## Getting Started

1. **Clone the Repository:**

   ```bash
   git clone 
   ```

2. **Install Dependencies:**


   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Application:**

   ```bash
   ParkingScan.py
   ```

## Contributing

We welcome contributions to improve the project! To contribute:

1. **Open an Issue:** If you find a bug or have a feature request, please [open an issue]() on GitHub.

2. **Submit a Pull Request:** If you want to propose changes, please fork the repository, make your changes, and submit a [pull request](). Ensure that your code adheres to the project's coding standards and includes appropriate tests.

3. **Code of Conduct:** Please follow our [Code of Conduct](CODE_OF_CONDUCT.md) when participating in this project.

## Contact

For any questions or feedback, please contact [dgoyal_be22@thapar.edu](mailto:dgoyal_be22@thapar.edu).


