FROM ubuntu:latest
COPY src /app
WORKDIR /app
RUN apt update
RUN apt install tree python3 python3-pip -y
RUN tree
RUN pip install -r requirements.txt
EXPOSE 80:80
CMD python3 -m waitress --port 80 main:app
