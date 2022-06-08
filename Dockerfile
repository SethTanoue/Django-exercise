#Dockerfile
FROM python:3.9.13

WORKDIR /usr/src/app/

COPY requirements.txt /usr/src/app/
RUN pip install -r requirements.txt
COPY requirements.txt /usr/src/app/
RUN scripts/install_dependencies.sh

COPY . /usr/src/app/
# scripts/install_dependencies.sh
#!/bin/bash

pip install -r requirements.txt