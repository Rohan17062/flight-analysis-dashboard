# Flight Analysis Dashboard

This is a simple flight data analysis dashboard built using Python,MySQL and Streamlit.  
The goal of this project is to understand how a database can be connected to a Python application and used to build an interactive dashboard.

The application allows users to search flight details and view a few basic analytics using charts.
---

## Features:
1.) Flight Search
- Select source city,destination city,and journey date.
- View available flight details such as airline,route and price.
- Shows a message if no flights are found.

2.) Analytics
- Airline-wise flight distribution (pie chart).
- Busiest airports based on arrivals and departures (bar chart).
- Comparison of average ticket prices across airlines.
---

## Tech Stack:
- Python
- MySQL (local database)
- Streamlit
- Plotly
---

## Project Structure:
flight-analysis-dashboard/
├── app.py # Streamlit application
├── dbhelper.py # Database connection and SQL queries
├── .gitignore
└── README.md
---

## How to Run the Project:
1.)Clone the repository
git clone https://github.com/Rohan17062/flight-analysis-dashboard.git
cd flight-analysis-dashboard

2.)Install required packages
pip install streamlit plotly mysql-connector-python

3.)Database setup
- Create a local MySQL database (for example: `mad`)
- Import flight data into a table named `flights_cleaned`
- Update database credentials in `dbhelper.py` if needed

4.)Run the application
streamlit run app.py
---

## Notes:
-This project uses a local MySQL database,so users need to configure their own database setup.
-The project was created as a learning exercise while studying SQL,Python and Streamlit.
-The focus was on understanding data flow from database → Python → dashboard,not on UI design.
---

## What I learned:
-Connecting MySQL with Python using mysql-connector.
-Writing SQL queries for analytics.
-Building interactive dashboards using Streamlit.
-Visualizing data using Plotly.
-Using Git and GitHub to manage and publish a project.









