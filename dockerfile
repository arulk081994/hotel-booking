# Use a lightweight base image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy requirements file first to leverage Docker caching
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Create database tables after all files are copied
# Consider moving this step to a separate script or entrypoint for better control
RUN python -c "\
    from app import app, db; \
    with app.app_context(): \
        db.create_all()"

# Expose port for the application
EXPOSE 5000

# Use a more robust WSGI server like Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
