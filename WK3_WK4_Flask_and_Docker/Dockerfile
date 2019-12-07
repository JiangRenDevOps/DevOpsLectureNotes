FROM python:3.7-alpine
#RUN echo http://mirrors.ustc.edu.cn/alpine/v3.7/main > /etc/apk/repositories && \
#    echo http://mirrors.ustc.edu.cn/alpine/v3.7/community >> /etc/apk/repositories
RUN apk update && apk upgrade
#RUN mkdir $HOME/.pip/
#COPY ./pip.conf $HOME/.pip/
RUN pip install flask
RUN mkdir -p /var/www/uploaded_files
COPY templates /var/www/templates
COPY app.py /var/www
WORKDIR /var/www

EXPOSE 5000
ENTRYPOINT ["python"]
CMD ["app.py"]

