FROM golang:1.17

RUN go get github.com/cortesi/devd/cmd/devd

ENTRYPOINT ["devd", "--address=0.0.0.0", "--port=8000"]

EXPOSE 8000/TCP

CMD ["/srv/jekyll/_site"]
