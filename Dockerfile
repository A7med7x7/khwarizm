# Use an official Python runtime as a parent image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Install the package in editable mode
RUN pip install --no-cache-dir -e .

# Command to run the application (optional, depending on your use case)
# CMD ["python", "your_package_name/main.py"]