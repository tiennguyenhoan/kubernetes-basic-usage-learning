# The base image 
FROM python:3.10.1-alpine

# Install Flask to run this application
RUN pip install --no-cache-dir Flask    

# Create working folder
RUN mkdir /app  

# Set working dir for the docker container
WORKDIR /app

# Copy source code to working folder
COPY app.py ./
COPY templates ./templates

# Just acknowledge this app will be use after
# Start container from this built image
EXPOSE 105

# Command to run the application
CMD [ "python", "./app.py" ]
