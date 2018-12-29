FROM python:3.7.1

RUN pip install pipenv

WORKDIR /home/democracy
COPY ./ ./
RUN pipenv install
ENV FLASK_APP /home/democracy/app.py
EXPOSE 5000

ENTRYPOINT [ "pipenv", "run", "flask", "run", "--host", "0.0.0.0" ]