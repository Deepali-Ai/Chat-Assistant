import sqlite3
import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

# configure our api key
genai.configure(api_key="AIzaSyBX0W_YvkzfsChdibv4umSL92HglvOwoXc")

# function to load google gemini model and provide sql query as response
def get_gemini_response(question,prompt):
    model=genai.GenerativeModel('gemini-pro')
    response = model.generate_content([prompt[0],question])
    return response.text

# function to retreive query from sql database

def read_sql_query(sql,db):
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    cursor.execute(sql)
    rows = cursor.fetchall()
    conn.close()
    for row in rows:
        print(row)
    return rows

# define your prompt

prompt=[
    """ 
 You are expert in converting English question to sql query!
 The sql database name is company and has two table - Employees and Departments.Employees table has following columns - ID, Name, Department,Salary,Hire_Date and
 Departments table has following columns - ID ,Name, Manager \n\n For Example,\n example 1 - Show me all employees in the Sales department,
 the sql command will be something like this SELECT * FROM Employees WHERE Department = 'Sales'; \n example 2 - Who is the manager of the Engineering department?,
 the sql command will be something like this SELECT Manager FROM Departments WHERE Name = 'Engineering';
 \n example 3 - List all employees hired after 2021-01-01, the sql command will be something like this SELECT * FROM Employees WHERE Hire_Date > '2021-01-01';
 \n example 4 - What is the total salary expense for the Sales department?,the sql command will be something like this SELECT SUM(Salary) FROM Employees WHERE Department = 'Sales';
 \n example 5 - List all employees hired in the year 2021,the sql command will be something like this SELECT * FROM Employees WHERE strftime('%Y', Hire_Date) = '2021';
 also sql code should not have ``` in begining or end and sql word in output

 """
] 

# Streamlit App Setup
st.set_page_config(page_title = "I can Retreive sql query")
st.header("Chat Assistant")
question = st.text_input("Input:",key="input")
submit = st.button("Get Response")

# if submit is clicked
if submit:
   response = get_gemini_response(question,prompt)
   print(response)
   data = read_sql_query(response,"company.db")

   for row in data:
      print(row)
      st.header(row)
      
else:
    # Handle the case where submit is not triggered
    st.warning("Please submit a valid query to get a response.")
    
    print("Submit not triggered. Please submit a valid question and prompt.")
    
