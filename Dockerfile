FROM jjanzic/docker-python3-opencv:opencv-4.0.1

RUN apt update
RUN apt -y upgrade

RUN pip3 install -U pip

WORKDIR /home/work

COPY . .
