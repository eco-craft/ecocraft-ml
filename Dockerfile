# Use the official lightweight Python image.
FROM python:3.9-slim

# Set the working directory in the container to /app.
WORKDIR /app

# Copy the application code into the container
COPY . /app

# Install the required dependencies
RUN pip install -r requirements.txt

# Run the web service using Gunicorn
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 app:app

