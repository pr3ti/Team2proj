FROM python:3.9

WORKDIR /app

COPY carapp.py /app/
COPY tests/ /app/tests/
COPY templates/ /app/tests/

RUN pip install flask
RUN pip install pytest

EXPOSE 5000

CMD python3 -m pytest tests/ && python3 carapp.py
