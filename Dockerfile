FROM golang:1.8.3-stretch

VOLUME  /go/src/github.com/thewhitetulip/Tasks
WORKDIR /go/src/github.com/thewhitetulip/Tasks

RUN apt-get update && apt-get install -y sqlite3

RUN go get github.com/dgrijalva/jwt-go
RUN go get github.com/gorilla/sessions
RUN go get github.com/mattn/go-sqlite3
RUN go get github.com/shurcooL/github_flavored_markdown

EXPOSE 8081:8081

CMD /bin/bash install.sh
