FROM python:3.9

COPY . /prosperity
 
WORKDIR /prosperity

RUN pip install -r requirements-prosperity.txt

#EXPOSE 5000

ENTRYPOINT python3 main.py