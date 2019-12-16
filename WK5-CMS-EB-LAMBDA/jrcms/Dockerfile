FROM python:3.7-alpine
RUN apk update
WORKDIR /app
COPY app .
RUN pip install -r requirements.txt

EXPOSE 8080
ENTRYPOINT ["python"]
CMD ["app.py"]
