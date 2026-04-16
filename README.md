<div align="center">
  <img width="390" height="390" alt="Image" src="https://github.com/user-attachments/assets/af10757b-967a-4f0d-9f11-68e7829afd85" />
  
  # Strava Activity Visualizer 🏃‍♂️🚴‍♀️🗺️

  **A modern Python toolkit to analyze and beautifully visualize your Strava activity data.**
  
  [![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
  [![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)](#)
  [![Matplotlib](https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black)](#)
  [![License: MIT](https://img.shields.io/badge/License-MIT-success.svg?style=for-the-badge)](#)
</div>

---

## 📖 Overview

**Strava Activity Visualizer** is a collection of Python scripts designed to take your raw Strava bulk data export (specifically `activities.csv` and `.gpx` files) and transform it into stunning visual insights. Whether you want to see an interactive heatmap of your routes, a calendar of your consistency, or beautiful geographic facets, this tool suite has you covered.

## ✨ Features & Visualizations

This repository contains several dedicated visualization scripts:

### 🗺️ 1. Maps & Geography
* **`activity_map.py`**: Generates a fully interactive HTML map plotting all of your GPX route traces. 
* **`pace_map.py`**: Analyzes GPX data to generate high-resolution images of individual routes color-coded by pace (gradient maps).
* **`make_plots.py` & `stravavis activities.py`**: Generates beautiful global maps, geographic facets, and landscape joyplots.

### 📅 2. Time & Consistency Tracking
* **`make_plots.py`**: Generates GitHub-style activity calendars and time-of-day dumbbell plots to visualize when and how often you work out.
* **`ridge_plot.py`**: Utilizes `joypy` to draw ridgeline plots of your activities distributed across the 365 days of the year.

### 🫧 3. Advanced Grouping Charts
* **`packed_circles.py` & `advanced_packed_circles.py`**: Creates visually striking packed circle charts representing total distance grouped by Activity Type and Year.

### 🛠️ 4. Utilities
* **`check_files.py`**: A helper script to quickly audit your `activities/` directory and ensure GPX/gzip files are correctly formatted.

---

## 🖼️ Visualization Gallery

Below are examples of the visualizations.

-- ACTIVITIES BY MONTH
<img width="3003" height="1666" alt="Image" src="https://github.com/user-attachments/assets/586a845a-ff20-4298-9ff8-6d401309e7ef" />

-- ACTIVITIES BY WEEK
<img width="3700" height="1668" alt="Image" src="https://github.com/user-attachments/assets/42ba3ca7-2ea2-4bfb-9f19-1a95c7b31db1" />

-- ACTIVITIES BY YEAR
<img width="2538" height="1665" alt="Image" src="https://github.com/user-attachments/assets/5a61e770-f89b-4c24-8016-2c6aba0e337f" />

-- ACTIVITIES BY YEAR RIDGES
<img width="3570" height="2366" alt="Image" src="https://github.com/user-attachments/assets/cd4db27f-9415-487a-ae33-48bd75c33597" />

-- DISTANCE AND SPEED
<img width="2497" height="1560" alt="Image" src="https://github.com/user-attachments/assets/280fa22d-0570-4b72-8034-1b8e912bb032" />

-- STRAVA ACTIVITY FOOTPRINTS
<img width="3315" height="3588" alt="Image" src="https://github.com/user-attachments/assets/bc92b151-dd53-4aa8-8c52-5df588028b46" />

-- STRAVA INVERACTIVE MAP
<img width="1829" height="890" alt="Image" src="https://github.com/user-attachments/assets/6f9e176f-ab55-4777-a0f7-1651baa86956" />

-- STRAVA CALENDAR
<img width="5400" height="9000" alt="Image" src="https://github.com/user-attachments/assets/60ca9e6b-7f28-45f5-b052-9a87d4d29517" />

-- STRAVA DUMBBELL PLOTS
<img width="8031" height="8031" alt="Image" src="https://github.com/user-attachments/assets/1694201f-e4bf-4c99-a002-c5e3c6978958" />

-- STRAVA ELEVATIONS
<img width="2400" height="2100" alt="Image" src="https://github.com/user-attachments/assets/7561856d-8456-493e-a3c9-6e358a1f5890" />

-- STRAVA FACETS
<img width="2400" height="2100" alt="Image" src="https://github.com/user-attachments/assets/550a0bed-11a5-4082-a422-9018ac7f21f7" />

-- STRAVA LANDSCAPE
<img width="3840" height="2880" alt="Image" src="https://github.com/user-attachments/assets/86ea817a-f4f2-453a-98d6-ce0314c1dc1d" />

-- STRAVA OVERLAP MAP
<img width="2949" height="5664" alt="Image" src="https://github.com/user-attachments/assets/4e258686-aebb-4298-9035-c8727ae16b56" />


-- INDIVIDUAL PACE

<img width="2531" height="2440" alt="Image" src="https://github.com/user-attachments/assets/021aa365-c99c-4241-bc12-a58653d6fbf0" />
<img width="2531" height="2440" alt="Image" src="https://github.com/user-attachments/assets/6d5d0e9f-d063-4b8d-bb39-c8bacc51e606" />
<img width="2531" height="2440" alt="Image" src="https://github.com/user-attachments/assets/674f8623-0570-4224-a076-52ee105e52c9" />





---

## 🚀 Getting Started

### Prerequisites
Make sure you have Python 3.8+ installed. It is recommended to use a virtual environment.

```bash
# Clone the repository
git clone [https://github.com/dean-sabroso/strava-activity-visualizer.git](https://github.com/dean-sabroso/strava-activity-visualizer.git)
cd strava-activity-visualizer

# Create a virtual environment
python -m venv venv

Installation
Install the required visualization and data manipulation libraries:

Bash
pip install pandas matplotlib folium gpxpy circlify joypy contextily stravavis numpy


📁 Data Setup
Request your bulk data export from Strava.

Unzip the export.

Place your activities.csv file and your activities/ folder (containing all your .gpx and .gpx.gz files) into your working directory.
(Note: Edit the activities_dir variable in the scripts to match your local file paths if necessary).

💻 Usage
Run any of the standalone scripts from your terminal. For example, to generate the calendar and map plots:

Bash
python make_plots.py
To generate individual route pace maps:

Bash
python pace_map.py
To generate the interactive heatmap:

Bash
python activity_map.py
📂 Project Structure
Plaintext
📦strava-activity-visualizer
 ┣ 📂activities/               # Place your Strava .gpx files here
 ┣ 📂images/                   # Output folder for generated plots
 ┣ 📜activities.csv            # Your Strava metadata export
 ┣ 📜activity_map.py           # Generates Folium HTML map
 ┣ 📜advanced_packed_circles.py # High-res grouped distance visualization
 ┣ 📜check_files.py            # Utility to count/verify files
 ┣ 📜make_plots.py             # Calendar, map, and dumbbell plots
 ┣ 📜pace_map.py               # Geographic map colored by speed
 ┣ 📜packed_circles.py         # Basic grouped distance visualization
 ┣ 📜ridge_plot.py             # Yearly joyplot generator
 ┗ 📜stravavis activities.py   # Alternative stravavis wrapper
🤝 Contributing
Contributions, issues, and feature requests are welcome! Feel free to check the issues page if you want to contribute.

📝 License
This project is open-source and available under the MIT License.

<div align="center">


<i>Built with ❤️ using Python, Pandas, Matplotlib, and Stravavis.</i>
</div>

source venv/bin/activate  # On Windows use `venv\Scripts\activate`
