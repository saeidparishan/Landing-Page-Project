# Base image
FROM python:3.12-slim

# Environment
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy project
COPY . /app/

# Run server
CMD ["gunicorn", "core.wsgi:application", "--bind", "0.0.0.0:8000"]
