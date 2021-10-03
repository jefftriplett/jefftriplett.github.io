# https://github.com/kaaquist/devd-docker/blob/master/Dockerfile
FROM alpine:3.10.2

ENV DEVD_VERSION=0.9

RUN apk add --no-cache ca-certificates \
    openssl \
    curl \
    tar

RUN curl -L https://github.com/cortesi/devd/releases/download/v${DEVD_VERSION}/devd-${DEVD_VERSION}-linux64.tgz | \
    tar -C /usr/local/bin -zxv --strip=1

COPY . .

EXPOSE 8000/TCP

ENTRYPOINT ["/usr/local/bin/devd", "--address=0.0.0.0", "--port=8000"]

CMD ["/srv/jekyll/_site"]
