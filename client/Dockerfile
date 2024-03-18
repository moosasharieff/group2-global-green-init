# Use the official Node.js image as a base
FROM node:latest AS builder
# Set the working directory in the container
WORKDIR /app
# Copy package.json and package-lock.json to the working directory
COPY package.json package-lock.json ./
# Install dependencies
RUN npm install
# Copy the rest of the application code
COPY . .
# Build the application using Vite
RUN npm run build
# Use a lightweight Nginx image to serve the application
FROM nginx:alpine
# Copy the built application from the builder stage to the Nginx server directory
COPY --from=builder /app/dist /usr/share/nginx/html
# Expose port 80
EXPOSE 80
# Command to start Nginx when the container starts
CMD ["nginx", "-g", "daemon off;"]
