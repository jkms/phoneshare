FROM alpine
MAINTAINER John Stafford <john@jkms.me>

RUN mkdir /phonebank
COPY . /phonebank

RUN apk update
RUN apk add python3 redis
RUN cd /phonebank \
  && python3 -m venv venv \
  && source venv/bin/activate \
  && pip install --upgrade pip \
  && pip install flask redis phonenumbers \
  && deactivate

ENTRYPOINT ["/phonebank/entrypoint.sh"]
