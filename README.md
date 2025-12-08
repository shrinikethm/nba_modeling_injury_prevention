# NBA Injury Prediction Project

Overview: Our group's NBA Injury Predictor Project is aimed at helping NBA teams, coaches, and medical staff
assess their players in terms of how likely a player is to be injured based on several on-court related factors
and statistics including League Tenure, BMI, Average Rest Days, etc. In doing so, organizations will be able
to devise proper strategies to get their players on the right track if they've undergone an injury as well as
mitigate the risk of a player from their team suffering an injury that can hurt the success of the team itself.
Not only is this project applicable for teams and organizations alike to use, but it's also very useful for 
anyone participating on sports betting because with the models that have been developed and tested for this project,
it can be used by these users to make more calculated bets.

## Team Members & Roles

* **Jay Shah - Data Engineer**: Programming, Predictive Analysis, Interactive Web Application Developer
* **Tea Adams - Data Analyst/Predictive Modeling Lead**: Programming, Analysis, Problem Solving, and Predictive Modeling
* **Shriniketh Mukundan - Data Visualization/Reporting Lead**: Data Visualization, Dashboard Application Developer

## Tech Stack
* **Languages**: Python
* **Discussed Tools & Software**: Python(NumPy, SciKit Learn, matplotlib, pandas, Seaborn, joblib, ipywidgets, IPython.display), Tableau
* **Version Control**: GitHub
* **File Management Tools**: Google Drive

## Details

Our project consists of utilizing several key attributes associated with players in order to quantify the 
relationship between selected physical factors and injury risk through the developments of a Logistic Regression
Model and a Random Forest Model which are evaluated across four different performance metrics: Accuracy, Precision,
Recall, and F-1 Score. As a result, our models are not only evaluated and enhanced through the use of prepprocessing 
and feature engineering, but they share incredible insights as to some of the most common contributing factors 
to NBA injuries and what specific features would lead to a higher risk of injury vs features that may 
not be as influential. 

## Dashboard Application

In order to deliver important insights that users can utilize, our group decided to make a dashboard web-based
application with the use of Streamlit, which is an open-source Python framework that enables more streamlined
web application creation. This process was facilitated by creating .joblib files to store objects corresponding 
to the logistic regression model and random forest model we created and inputted into our NBA_Injury_App.py python
file. Under the assumption that all .joblib files and the Python file are within the same directory and the current
directory is that same directory, the linux command: python -m streamlit run NBA_Injury_App.py can be executed, 
which will enable the creation of a web-based dashboard on the user's local browser. With this dashboard, users
can utilize sliders for different features in order to see how those specific values affect whether a player
is predicted to be injured or not across both developed models by using the "Predict Injury Risk" button once all 
sliders are finalized. Furthermore, this web-based dashboard applicationis extremely helpful for users to analyze 
certain player-specific statistics and use the sliders to correspondto that specific player, and identify the 
likelihood of injury across both models. With this capability, we hopeto provide a new wave of change for the 
NBA across teams and fans alike, so that the sport as a whole is only getting better with time.

## Dashboard Application Setup & Steps


<img width="1368" height="311" alt="Screenshot 2025-12-07 at 2 55 41 PM" src="https://github.com/user-attachments/assets/d9aa889a-da43-40b9-b016-01811b503fdf" />

<img width="1512" height="618" alt="Screenshot 2025-12-06 at 6 09 47 PM" src="https://github.com/user-attachments/assets/7aced112-1d6f-431a-a974-2ed47effe4c0" />

# Steps: 
* Change different feature sliders that correspond to the physical and statistical attributes of a specific player
* Press the "Predict Injury Risk" button once all sliders are chosen
* Assess the injury predictions made by both the Logistic Regression Model & Random Forest Model(Injury or No Injury) as well as the likihood each model predicts of an injury occurring


## Requirements & Dependencies for Web-Based Dashboard Application
* **scikit-learn**: Open Source Python Library that helps to build and train the Logistic Regression & Random Forest models
* **joblib files**: Files that are able to reconstruct the Logistic Regression and Random Forest models as object, along with scaler objects
* **streamlit**: Open Source Python Framework that's used for building and enabling web applications
* **pandas**: Python Library utilized for analyzing data
* **numpy**: Python Library used for array manipulation
* **NBA_Injury_Prediction__WithDashboard.ipynb**: Google Colab Python File that contains data preprocessing, training, and evaluation of Logistic Regression & Random Forest Model
* **scikit-learn version**: Proper scikit-learn version that's used in the NBA_Injury_Prediction__WithDashboard.ipynb file: 1.6.1 



