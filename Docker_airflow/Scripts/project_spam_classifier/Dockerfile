# Use an official Python runtime as a parent image
FROM python:3.11

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container at /usr/src/app
COPY ./requirements.txt /app/requirements.txt

# Install any dependencies in the requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt