# Pitch Control Model for Soccer Analysis

## Overview

This repository contains the implementation of a pitch control model designed for soccer analysis. The model uses tracking data to calculate player control over specific areas of the pitch at various timestamps, providing insights into player positioning and decision-making dynamics during matches.

- **Pitch Control Heatmaps**: Below is a heatmap example showing player control zones during a game:
- 
- - **Aggregated Pitch Control Heatmap **: The following image shows pitch control for each team aggregated over the entire game:

  ![Pitch Control Heatmap]()

- **Aggregated Pitch Control Heatmap **: The following image shows pitch control for each team aggregated over the entire game:

  ![Aggregated Pitch Control Heatmap](sample_aggregated_pitch_control.png)
  
## Key Features

- **Training Data**: The model is trained on **30 million rows of tracking data**, which includes player positions, ball positions, and velocities, collected at **3 million timestamps per game**.
- **Pitch Control Calculation**: For each timestamp, the model computes the likelihood of a player controlling a given area of the pitch.
- **Real-World Integration**: Successfully deployed and integrated into the analytics framework of **Nashville SC**.

## Project Structure

- **/data/**: Contains sample tracking data in CSV format.
- **/src/**: Includes the Python scripts for data preprocessing, feature extraction, and the core pitch control model.
  - `data_preprocessing.py`: Cleans and processes raw tracking data.
  - `pitch_control_model.py`: The main script for training the model and calculating control probabilities.
- **/notebooks/**: Jupyter notebooks that demonstrate model training, evaluation, and visualization.
