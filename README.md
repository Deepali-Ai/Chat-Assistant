# Chat-Assistant
This is a FastAPI-powered web application that allows users to query an SQLite database and get formatted responses based on predefined queries. It supports basic SQL queries like listing employees from a department, getting the manager of a department, listing employees hired after a certain date, and more.
The app includes a simple UI where users can type natural language queries, and it returns results in a user-friendly format.

# Project Structure:
  /chat-assistant
  - app.py            # Flask application
  - company.db        # SQLite database
  - requirements.txt  # List of dependencies
  - README.md         # Project documentation

# Features:
* Accepts natural language queries
* Retrieves relevant data from an SQLite database
* Handles errors gracefully

# Installation:
1. Clone the repo:
   git clone https://github.com/Deepali-Ai/Chat-Assistant.git
   cd chatbot
2. Install dependencies:
   pip install -r requirements.txt
3. Run the app:
   sqlite run app.py

# Supported Queries:
Once deployed or running locally, you can interact with the app through the following types of queries:
 1. "Show me all employees in the Sales department."
 2. "Who is the manager of the Engineering department?"
 3. "List all employees hired after 2021-01-01."
 4. "What is the total salary expense for the Marketing department?"
    
The app will return formatted results for these queries, and you can ask more based on the supported types.

# File and Database Structure:
The app is initialized with a sample SQLite database (company.db) containing tables for Employees and Departments.
You can modify the database by adding more employees, departments, or changing existing data.
