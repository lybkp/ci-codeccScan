FROM docker.io/bkci/codecc:latest
RUN mkdir -p /usr/codecc/software
COPY software/go1.15.2.linux-amd64.tar.gz /usr/codecc/software
WORKDIR /usr/codecc/software
RUN tar zxvf go1.15.2.linux-amd64.tar.gz
RUN rm -rf go1.15.2.linux-amd64.tar.gz
RUN chmod -R 755 /usr/codecc/software/go
ENV GOROOT=/usr/codecc/software/go
COPY tool/gometalinter /usr/codecc/software/gometalinter
RUN chmod -R 755 /usr/codecc/software/gometalinter
ENV GOML_PATH=/usr/codecc/software/gometalinter/bin
ENV PATH="${GOML_PATH}:${GOROOT}/bin:${PATH}"
RUN mkdir -p /usr/codecc/tool_scan
COPY sdk /usr/codecc/tool_scan/sdk/
RUN chmod -R 755 /usr/codecc/tool_scan
WORKDIR /usr/codecc/tool_scan