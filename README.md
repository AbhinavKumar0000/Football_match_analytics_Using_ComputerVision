# ⚽ Football Match Analytics

This repository contains a Python-based project for analyzing football match footage using computer vision techniques. The project leverages advanced object detection and tracking algorithms to extract meaningful data, including player and ball tracking, team identification, and performance metrics like speed and distance covered. The modular design makes it extensible and suitable for researchers, developers, and sports analysts interested in football analytics.

---

## ✨ Features

* **Player and Ball Tracking:** Employs state-of-the-art object detection (e.g., YOLO) and tracking algorithms to accurately follow players and the football across video frames.
* **Team Assignment:** Automatically classifies players into their respective teams based on visual cues, enabling team-specific analysis.
* **Speed and Distance Estimation:** Calculates individual player speeds and total distance covered during a match, providing insights into player performance.
* **Camera Movement Estimation:** Compensates for camera motion to ensure a stable reference frame, improving the accuracy of tracking and metrics.
* **Jupyter Notebooks:** Includes `player_assigment.ipynb`, a notebook demonstrating the team assignment process with visualizations.
* **Modular Design:** Structured into separate modules for each task, making it easy to modify, extend, or integrate with other systems.

---

## 📂 Project Structure

The repository is organized as follows:

Football_match_analytics/
├── camera_movement_estimator/      # Scripts for analyzing and correcting camera motion

├── player_ball_assigner/           # Core logic for detecting and tracking players and the ball

├── speed_and_distance_estimator/   # Modules for calculating player speed and distance

├── team_assigner/                  # Logic for classifying players into teams

├── trackers/                       # Implementation of tracking algorithms

├── main.py                         # Main script to run the analysis pipeline

├── player_assigment.ipynb          # Jupyter Notebook for team assignment visualization

├── yolo_instance.py                # Custom implementation or wrapper for YOLO model

├── requirements.txt                # List of required Python dependencies

└── README.md                       # Project documentation (this file)


