# Use an official Python runtime as a parent image
FROM python:3.9

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install dependencies
RUN python -m pip install -U pip

# Install Python dependencies
RUN pip install -r requirements.txt

# Expose ports
EXPOSE 3000 8000

# Command to run FastAPI and Python HTTP server
CMD ["sh", "-c", "python ./app/app.py --host 0.0.0.0 --port 8000 & python -m http.server 3000 --directory frontend"]