# Pull base image
FROM nginx:latest

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH="/code:$PYTHONPATH"
ENV VIRTUAL_ENV=/code/.venv
ENV PATH="$VIRTUAL_ENV/"bin":$PATH"
# Create and set work directory called `code`
RUN mkdir -p /code
WORKDIR /code

RUN apt update && apt install -y python3 python3-venv python3-pip gunicorn

# Install dependencies
RUN python3 -m venv $VIRTUAL_ENV
COPY requirements.txt /tmp/requirements.txt

RUN set -ex && \
    pip install --upgrade pip && \
    pip install -r /tmp/requirements.txt && \
    rm -rf /root/.cache/ /code/media/pfps/*

# Copy local project
COPY . /code/

# Expose port 8000
EXPOSE 8000

# Use gunicorn on port 8000
CMD ["gunicorn", "--bind", ":8000", "--workers", "2", "django_project.wsgi"]