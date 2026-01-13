FROM fauria/vsftpd
ENV FTP_USER=user
ENV FTP_PASS=pass
ENV PASV_ADDRESS=127.0.0.1
ENV PASV_MIN_PORT=21100
ENV PASV_MAX_PORT=21110
# The fauria/vsftpd image supports anonymous login via env var ANONYMOUS_ENABLED
ENV ANONYMOUS_ENABLED=YES
RUN mkdir -p /home/vsftpd/anonymous
RUN echo "Welcome to our public FTP server. Please be careful with sensitive files." > /home/vsftpd/anonymous/welcome.txt
RUN echo "Super secret flag: FLAG{ANON_FTP_L0G1N}" > /home/vsftpd/anonymous/flag.txt
