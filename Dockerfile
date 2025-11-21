# Use an official Python runtime as a base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80

# Create a non-root user to run the application
RUN useradd --create-home --shell /bin/bash app
USER app

# Run gunicorn when the container launches
CMD ["gunicorn", "--bind", "0.0.0.0:80", "service:app"]
