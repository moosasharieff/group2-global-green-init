# Backend Dockerfile Version-1

# Using official Node.js runtime as a parent image
FROM node:16-alpine

# Set the working directory in the container
WORKDIR /usr/src/app

# Install app dependencies by copying[ Copying the package.json and package-lock.json to the working directory and install dependencies. \n
#This layer caching improves Docker build performance by not reinstalling all dependencies when source code changes.

# package.json and package-lock.json
COPY package*.json ./

# Install dependencies
RUN npm install

# Bundle app source
COPY . .

# Will check with Dev on App binding Ports and update [ Input needed fromDev team needed. Will be updated in new version]
#EXPOSE 3000

# Define the command to run application [ Input needed fromDev team needed. Will be updated in new version]
#CMD ["node", "server.js"]
