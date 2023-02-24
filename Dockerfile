# start from parent image with python3.8
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

# copy everything in the app directory to the app directory in the new image
COPY ./app /app/app

RUN pip install --no-cache-dir --upgrade -r /app/app/requirements.txt
