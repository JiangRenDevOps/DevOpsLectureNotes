FROM ubuntu

RUN apt-get update && apt-get install -y curl && apt-get autoclean

COPY app/main.sh .

ENTRYPOINT ["/bin/bash"]

CMD ["main.sh"] 
