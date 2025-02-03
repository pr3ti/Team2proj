#!/bin/bash

# Step 1: Build the Docker image
docker build -t carapp .

# Step 2: Run tests inside the Docker container
docker run --rm carapp python3 -m pytest tests/

# Step 3: Run the application in the background
docker run -d --name carapp -p 5000:5000 carapp

# Step 4: test website
curl http://localhost:5000

echo "Application is running at: http://localhost:5000"
