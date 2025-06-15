# About the Project
This project was developed for a competition held at IIT (BHU) Varanasi, where participants were tasked with presenting innovative solutions to real-life problems.

We designed a smart water bottle that helps people quickly check the quality of drinking water, especially in public places like parks, taps, and restaurants. The bottle uses sensors to measure key water parameters and a machine learning model to instantly assess whether the water is safe to drink.

Our goal was to provide a portable, easy-to-use solution to help individuals make safer drinking choices on the go.

## Project Structure: This project contains the following folders:

1. WaterQualityCheck/Dataset/ – Contains the CSV dataset files.

2. WaterQualityCheck/Notebook/ – Contains the Jupyter notebooks for analysis and visualization.

3. WaterQualityCheck/Pdfs/ – Contains project-related PDF files like presentation.

## Project Components:

I have also provided a detailed step-by-step guide within the Notebook (.ipynb file) that walks through each stage of a typical machine learning workflow. The guide covers 8 essential steps, from data overview to model evaluation. I have used models like Random Forest and XGBoost, and evaluated their performance to recommend the most suitable one.

### 8-step guide:
1. Data Overview
2. Data Preprocessing
3. Exploratory Data Analysis (EDA)
4. Feature Engineering
5. Model Selection
6. Model Training
7. Model Evaluation
8. Summary

## How to Get Started with the Project: 

A. Set Up the Virtual Environment:
   
To keep your project dependencies isolated, it is recommended to use a virtual environment.

### Run the following commands:
1. Create a virtual environment:           python -m venv ./venv
2. Activate the virtual environment: For Windows: .\venv\Scripts\activate
3. For Mac/Linux: source venv/bin/activate

B. Install Required Packages

Install all the necessary Python libraries by running: pip install -r requirements.txt

>[!IMPORTANT]
>: Update Dataset Path
    You need to update the dataset path in the 2nd cell of the Jupyter notebook in Folder "Notebook/Water_Quality_Check".

    Currently, the path is written as:"D:\\Data_Science\\Projects\\WaterQualityCheck\\Dataset\\water_potability.csv"
    Change it to : file_path = "C:\\Users\\YourUsername\\Path\\To\\Dataset\\water_potability.csv"

    You should replace it with your local dataset path.

## Potential Issues You Might Encounter:

1. Still facing issues while working with the Notebook in VS Code?
    Check out this helpful video tutorial:
    https://www.youtube.com/watch?v=suAkMeWJ1yE&t=3s

2. Dataset Path Error?
    If you encounter a dataset location error in the 2nd cell, simply go to your project folder, locate the water_potability.csv file, copy its full path, and replace the existing file_path in the 2nd cell with your correct path.