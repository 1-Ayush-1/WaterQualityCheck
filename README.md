📂 Project Structure: This project contains the following folders:
|
|------Dataset/ – Contains the CSV dataset files.
|
|------Notebook/ – Contains the Jupyter notebooks for analysis and visualization.
|
|------Pdfs/ – Contains project-related PDF files like reports and presentations.



1️⃣ Set Up the Virtual Environment

    To keep your project dependencies isolated, it is recommended to use a virtual environment.

    Run the following commands:

    Create a virtual environment:
    python -m venv ./venv

    Activate the virtual environment:
    For Windows:
    .\venv\Scripts\activate

    For Mac/Linux:
    source venv/bin/activate

2️⃣Install Required Packages
    Install all the necessary Python libraries by running:

    pip install -r requirements.txt

3️⃣ Important: Update Dataset Path
    You need to update the dataset path in the 2nd cell of the Jupyter notebook 
    in Folder "Notebook/Water_Quality_Check".

    Currently, the path is written as:"D:\\Data_Science\\Projects\\WaterQualityCheck\\Dataset\\water_potability.csv"
    Change it to : file_path = "C:/Users/YourUsername/Path/To/Dataset/water_potability.csv"

    You should replace it with your local dataset path.

🔧 Still facing issues while working with the Notebook in VS Code?
    Check out this helpful video tutorial:
    https://www.youtube.com/watch?v=suAkMeWJ1yE&t=3s

📂 Dataset Path Error?
    If you encounter a dataset location error in the 2nd cell, simply go to your project folder, locate the water_potability.csv file, copy its full path, and replace the existing file_path in the 2nd cell with your correct path.