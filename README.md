# Django Band Website

This is my Django capstone project - a website for a band.

## Setup

## Docker Setup

1. **Building the Docker Image**:
   Build the Docker image using the command below. Replace `your_image_name` with a suitable name for your Docker image.
   ```bash
   docker build -t your_image_name .

2. Running the Docker Container:
Once the image is built, run a container from that image. Replace your_image_name with the name you provided in the previous step and your_container_name with a name for your running container.

docker run -d -p 8000:8000 --name your_container_name your_image_name

3. Accessing the App:
After starting the container, open a web browser and navigate to http://localhost:8000 to access the Django application.

4. Stopping the Docker Container:
When you're finished, you can stop the container using the command: docker stop your_container_name