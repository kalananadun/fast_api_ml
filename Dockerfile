#importing the base image
FROM python:3.10

# specifying the working directory
WORKDIR /api_app

#copying requirement file to the working directory 
COPY requirements.txt  .

# installing the dependencies 
RUN pip install -r requirements.txt

COPY ./app /api_app/

CMD ["python","./app/main.py","--host","0.0.0.0","--port","8080"]
