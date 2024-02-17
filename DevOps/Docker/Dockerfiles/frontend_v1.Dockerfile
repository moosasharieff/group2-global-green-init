# Frontend Dockerfile Version-1

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

# Frontend app build setup, will work on this after checking with Dev. Will be updated in new version
#RUN npm run build

# Will check with Dev on App binding Ports and update [ Dev team need to modify and update]
#EXPOSE 3000

# Serve static files [ Input needed fromDev team needed. Will be updated in new version]
#CMD ["npm", "start"]