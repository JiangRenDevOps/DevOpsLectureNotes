FROM python:3.7-alpine
RUN apk update
WORKDIR /app
COPY app .
RUN pip install -r requirements.txt

ENTRYPOINT ["python"]
CMD ["app.py"]
