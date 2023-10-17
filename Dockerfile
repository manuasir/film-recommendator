# Base image
FROM python:3.7-slim-buster

# Set the working directory inside the container to /app
WORKDIR /app

# Copy the .env file from the host to container
COPY .env ./

# Install the required Python packages using pip3
RUN pip3 install pymongo python-dotenv

# Copy the contents from ./src directory from the host to the working directory in the container
COPY ./src/ .

# Run the command "python3 index.py" when the container starts
CMD [ "python3", "index.py"]