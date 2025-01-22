# Use Python base image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy the application code
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 5000
EXPOSE 5000

# Start the application
CMD ["python", "app.py"]
