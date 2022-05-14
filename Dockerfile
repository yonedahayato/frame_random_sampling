FROM pachyderm/opencv:1.0

RUN apt update
RUN apt -y upgrade

RUN pip install -U pip

WORKDIR /home/work

COPY . .
