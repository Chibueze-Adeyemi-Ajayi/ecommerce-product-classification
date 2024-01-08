# Base image
FROM python:3.10

# Working directory
WORKDIR /myproject/myapp

# Copy files
COPY dependencies.txt ./
COPY /myproject/myapp ./

# Install dependencies
RUN pip install -r dependencies.txt

# Expose port (replace with your app's port if different)
EXPOSE 8000

# Start command
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
