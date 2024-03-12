# Use a base image with Docker installed
FROM docker:latest AS builder

# Install docker-compose
RUN apk add --no-cache py-pip && \
    pip install --upgrade pip && \
    pip install docker-compose

# Copy the docker-compose.yml file and build the services
WORKDIR /app
COPY docker-compose.yml /app
RUN docker-compose build

# Start the services
CMD ["docker-compose", "up"]
