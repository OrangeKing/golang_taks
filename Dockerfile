FROM golang:1.8.3-stretch

RUN apt-get update && apt-get install -y sqlite3

RUN go get github.com/dgrijalva/jwt-go
RUN go get github.com/gorilla/sessions
RUN go get github.com/mattn/go-sqlite3
RUN go get github.com/shurcooL/github_flavored_markdown

RUN git clone https://github.com/thewhitetulip/Tasks.git src/github.com/thewhitetulip/Tasks
RUN chmod +x src/github.com/thewhitetulip/Tasks/install.sh
EXPOSE 8081:8081

CMD /bin/bash src/github.com/thewhitetulip/Tasks/install.sh
