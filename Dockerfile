FROM ubuntu:20.04

WORKDIR /core_app
COPY . /core_app
RUN apt-get update && apt-get upgrade -y
RUN apt-get install python3 -y && apt-get install python3-pip -y
RUN sudo apt install -y build-essential libssl-dev libffi-dev python3-dev
RUN pip3 install -r requirements.txt

CMD ["python3", "run.py"]