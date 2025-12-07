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

* **Jay Shah - Data Engineer/Database Designer**: SQL & database design, ER modeling,
normalization
* **Tea Adams - Data Analyst/Predictive Modeling Lead**: Programming, analysis, problem solving, and predictive modeling
* **Shriniketh Mukundan - Data Visualization/Reporting Lead**: Data visualization, communication, collaboration

## Tech Stack
* **Languages**: Python, SQL
* **Discussed Tools & Software**: Python(NumPy, SciKit Learn, matplotlib, pandas), SQL(PostgreSQL, SQLAlchemy), Tableau
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
is predicted to be injured or not across both developed models. Furthermore, this web-based dashboard application
is extremely helpful for users to analyze certain player-specific statistics and use the sliders to correspond
to that specific player, and identify the likelihood of injury across both models. With this capability, we hope
to provide a new wave of change for the NBA across teams and fans alike, so that the sport as a whole is only
getting better with time.




