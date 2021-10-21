FROM python:3.9

COPY prosperity /home/prosperity
 
WORKDIR /home/prosperity

RUN pip install -r requirements-prosperity.txt

#EXPOSE 5000

ENTRYPOINT python3 main.py