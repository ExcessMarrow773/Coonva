# Pull base image
FROM nginx:latest

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV VIRTUAL_ENV=./.venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
ENV PYTHONPATH=/code:$PYTHONPATH
# Create and set work directory called `code`
RUN mkdir -p /code
WORKDIR /code

RUN apt update && apt install -y python3 python3-venv python3-pip

# Install dependencies
RUN python3 -m venv $VIRTUAL_ENV
COPY requirements.txt /tmp/requirements.txt

RUN set -ex && \
    env

# Copy local project
COPY . /code/

# Expose port 8000
EXPOSE 8000

# Use gunicorn on port 8000
CMD ["gunicorn", "--bind", ":8000", "--workers", "2", "django_project.wsgi"]