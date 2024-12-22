FROM python:3.11.7
WORKDIR /app .
COPY /requirements.txt .

RUN pip install --upgrade pip




RUN apt-get update 
RUN pip install -r  requirements.txt


CMD [ "python3","main.py" ]
