FROM python:3.7.10

WORKDIR /core_app
COPY . /core_app
RUN pip install -r requirements.txt



CMD ["python", "run.py"]