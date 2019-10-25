FROM python:3.7-alpine

COPY . /bots
WORKDIR /bots
RUN pip3 install -r requirements.txt
CMD ["python3", "tweet.py"]