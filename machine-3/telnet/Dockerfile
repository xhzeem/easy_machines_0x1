FROM alpine:latest
RUN apk add --no-cache busybox-extras
RUN adduser -D admin && echo "admin:admin" | chpasswd
EXPOSE 23
CMD ["telnetd", "-F", "-p", "23"]
