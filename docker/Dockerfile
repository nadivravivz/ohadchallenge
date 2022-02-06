FROM python:3.9-alpine
RUN mkdir /app
WORKDIR /app
COPY . .
RUN pip3 install -r requirements.txt
ENTRYPOINT ["python","./yaml-extract.py"]
CMD ["--help"]
