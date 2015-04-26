# Dockerfile extending the generic Python image
FROM gcr.io/google_appengine/python-compat

# Install via apt-get
RUN apt-get update && apt-get install -y python-shapely

# Install via PIP
ADD requirements.txt /app/
RUN pip install -r requirements.txt

# Include application files
ADD . /app/
