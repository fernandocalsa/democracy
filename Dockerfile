FROM neo4j:2.3
MAINTAINER Fernando Calvo <fernando.calvo.sanz@gmail.com>

RUN apt-get update && \
    apt-get install -y python3 && \
    apt-get install -y python3-pip && \
    mkdir /home/democracy && \
    pip3 install pipenv

WORKDIR /home/democracy
COPY ./ ./
RUN pipenv install --system
ENV FLASK_APP /home/democracy/app.py
ENV NEO4J_AUTH none
EXPOSE 5000

WORKDIR /var/lib/neo4j

ENTRYPOINT flask run --host 0.0.0.0 & /docker-entrypoint.sh neo4j