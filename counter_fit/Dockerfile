FROM python:3.9

COPY requirements-counter_fit.txt .

RUN pip install -r requirements-counter_fit.txt

EXPOSE 5000

ENTRYPOINT python3 -m CounterFit