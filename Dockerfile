FROM python:3.13.2-slim-bookworm

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install system dependencies
RUN apt-get update \
  && apt-get -y install netcat-traditional gcc postgresql \
  && apt-get clean

RUN pip install --upgrade pip
RUN pip install pipenv

COPY Pipfile Pipfile
COPY Pipfile.lock Pipfile.lock
RUN pipenv install --system --deploy

COPY . . 

# add entrypoint.sh
COPY ./entrypoint.sh .
RUN chmod +x /usr/src/app/entrypoint.sh

# run entrypoint.sh
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]