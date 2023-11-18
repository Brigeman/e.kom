# Forms - FastAPI Application

# This application is designed to work with forms. It uses FastAPI to create an API and MongoDB to store data about form templates.

# Setting Up the Environment

# 1. **Install Docker and Docker Compose:** Make sure you have Docker and Docker Compose installed.
# 2. **Clone the Repository:** Clone the project repository to your computer.
# 3. **Install Dependencies:** Navigate to the project directory and execute the command to install dependencies:
# ```bash
# pip install -r requirements.txt
# ```

# Running the Application

# Launch MongoDB with Docker Compose: Use the command to start MongoDB in a Docker container:
# ```bash
# docker-compose up -d
# ```

# Run the FastAPI Application: Execute the command to start the FastAPI application:
# ```bash
# uvicorn app.main:app --host 0.0.0.0 --port 80
# ```

# Testing the Functionality

# To test the functionality of the application, you can use curl or other tools to send POST requests to the following endpoints:

# Save Form Template:
# ```bash
# curl -X POST "http://localhost/save_form_template" -H "Content-Type: application/json" -d '{"template_name": "MyForm", "fields": {"email": {"field_type": "email"}, "phone": {"field_type": "phone"}, "text_field": {"field_type": "text"}, "date_field": {"field_type": "date"}}}'
# ```

# Get Form Data:
# ```bash
# curl -X POST "http://localhost/get_form" -H "Content-Type: application/json" -d '{"data": {"email": "test@example.com", "phone": "+1234567890", "text_field": "This is a text field", "date_field": "2023-11-19"}}'
# ```

# Code Overview

# Project Structure
# app/: Directory containing the main application code.
# main.py: Main file containing the core application logic and API endpoints.
# models.py: File containing data models used in the application.
# docker-compose.yml: Docker Compose configuration file for running MongoDB.
# requirements.txt: File containing Python dependencies.

# Main Functions and Models
# save_form_template: POST request to save a form template in the MongoDB database.
# get_form_data: POST request to retrieve form data or dynamically type fields.
# FormTemplate: Model for storing form templates.
# FormData: Model for storing form data.
