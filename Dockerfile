# Use an official lightweight Python image as the base
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the file that lists the dependencies into the container
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application's code into the container
COPY . .

# Tell Docker that the container will listen on port 5000
EXPOSE 5000

# Define the command to run your application using Gunicorn
# This command runs when the container starts
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]