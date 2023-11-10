FROM ubuntu:latest

WORKDIR /demoapp


COPY  flaskapp/  /demoapp

RUN apt update && \
	apt install python3 pip  -y && \
     	pip3 install -r requirements.txt && \
 	python3 manage.py || \
	date

EXPOSE 5000

CMD ["python3", "routes.py"] 
