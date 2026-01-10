# Use a tiny Python runtime
FROM python:3.9-slim

# Set the directory in the container
WORKDIR /app

# Copy the script into the container
COPY app.py .

# The script runs on port 8000
EXPOSE 8000

# Run the script
CMD ["python", "app.py"]