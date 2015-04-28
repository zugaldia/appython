# Dockerfile extending the generic Python image
FROM gcr.io/google_appengine/python-compat

# Install via apt-get. The package python-dev is important so that Python
# packages can compile their C extensions to enable speedups.
RUN apt-get update && apt-get install -y python-dev python-shapely

# Install via PIP
ADD requirements.txt /app/
RUN pip install -r requirements.txt

# Include application files
ADD . /app/
