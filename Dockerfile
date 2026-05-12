# Use a lightweight Python image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container
COPY . .

# Install the "Mulla" engine dependencies (Flask is the critical one here)
RUN pip install --no-cache-dir flask dataclasses

# Expose the port Hugging Face is looking for
EXPOSE 7860

# Run the Sovereign Heartbeat
CMD ["python", "app.py"]
