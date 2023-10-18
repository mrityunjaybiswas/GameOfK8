# Use the official Python image as the base image
FROM python:3.8-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any necessary dependencies
RUN pip install Flask

# Expose the port that your Flask application will run on
EXPOSE 5000

# Define the command to run your application
CMD ["python", "Api-employeeData.py"]