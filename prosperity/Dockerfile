FROM python:3.9

COPY components /components
 
WORKDIR /components

RUN pip install -r requirements-prosperity.txt

#EXPOSE 5000

ENTRYPOINT python3 main.py