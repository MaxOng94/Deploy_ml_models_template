# start from parent image with python3.8
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

COPY ./requirements.txt /app/requirements.txt

# the newly created image has the requirments.txt file under the /app/ path
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

# copy everything in the app directory to the app directory in the new image
COPY ./app /app/app
