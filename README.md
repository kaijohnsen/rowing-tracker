# Florida Crew Tracker

## Project Overview
This project is a web application built using Flask and a SQLite database that tracks and displays rowing workout data for members of the University of Florida's competitive club rowing team. The application displays individual workout statistics for 12 athletes across a three-month period (January 13, 2025 – March 13, 2025). Each rower's page includes detailed entries such as the workout date, type, meters rowed, rate, split time, calories burned, and heart rate.

The original proposal aimed to include 20 rowers — 10 men and 10 women — but due to data limitations and incomplete logs, the final dataset includes 12 athletes, evenly split between men and women.

## Data Collected 
The data collected for each rower includes their first name and last name, their team and competitive level (such as women's novice or men's varsity), and their pronouns. For each rower, the application records the number of workouts completed during the three-month window. 

For every workout entry, the following data points are collected and stored: the date of the workout, the type of workout completed, the stroke rate, whether the workout took place on land or on water, the number of meters rowed, the split time, the number of calories burned, and the rower's heart rate. The data points vary depending on what data was available for each athlete.

All of this data is stored in a SQLite database and rendered dynamically on the front end using Flask and Jinja templating.

## Process

### 1. Flask Application
The back end of the application is built with Flask and SQLAlchemy. The index route displays all rowers alphabetically, each with a clickable link that leads to their individual detail page. The detail route dynamically loads the selected rower’s data and displays it in a formatted HTML table.

The HTML templates used in the application are `index.html` for the list of rowers and `rowing.html` for the individual rower detail page. The data is sourced from a local SQLite database (`rowing-database.db`) that was created from an original CSV file.

### 2. Rowing Data Structure
The database is structured using a SQLAlchemy model called `Rowing`, which defines the column names and data types. The dataset includes all workouts recorded by each rower during the 60-day period. SQL queries are used to group the data and retrieve workouts based on the rower's first and last name.

### 3. Front-End Features
The front end of the application is styled with fully responsive CSS, including media queries that are optimized for iPhone and other mobile devices. Each athlete’s profile page displays their headshot, team and level information, a link to the official Florida Club Rowing website, and a link to the photo credits for their headshot. All workout data is displayed in a clean and accessible table format.

## Challenges

### Incomplete Dataset
The original goal was to include data for 20 rowers. However, the final dataset includes only 12 athletes due to data availability and logging inconsistencies. Some rowers only recorded water workouts, while others had irregular attendance, which impacted the consistency and completeness of the data.

### SQLite Learning Curve
This was my first experience using SQLite. I had to learn how to structure a relational database, run SQL queries, and merge the database with a Flask application using SQLAlchemy.

### Dynamic Routing in Flask
I developed a more advanced route structure to dynamically handle URLs based on each rower's name. I also included error handling to manage cases where URLs were missing or improperly formatted.

### CSS Responsiveness
The CSS styling was revised and adjusted frequently to ensure that the design remained consistent across different screen sizes. Media queries were specifically refined to improve the layout and readability on small devices like iPhones.

## File Outputs
The `rowing-database.db` file contains all of the structured workout data used in the application. The `requirements.txt` file lists all the Python libraries and modules needed to run the project, including Flask and SQLAlchemy. All HTML templates and static files (CSS, images) are organized into separate folders.

## Final Notes
This project was developed as a final project for JOU4364: Advanced Web Apps with Professor McAdams. 



