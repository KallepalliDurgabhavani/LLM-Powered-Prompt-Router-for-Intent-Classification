# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Create an empty log file to ensure it exists
RUN touch route_log.jsonl

# Define environment variables (can be overridden by docker-compose)
ENV PYTHONUNBUFFERED=1

# Run main.py when the container launches
# Use -m to run as a module to correctly resolve relative imports
CMD ["python", "-m", "src.main", "how do i sort a list of objects in python?"]
