FROM ubuntu:18.04

#UPDATE PACKAGE LIST
RUN apt-get update

#SET UP PYTHON
RUN apt-get install -y python python-pip
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . /app
WORKDIR /app

#Uncomment for development server
CMD ["python", "run.py"]

#Uncomment for deployment server
#CMD ["gunicorn", "--bind", "0.0.0.0:8080", "run:app"]