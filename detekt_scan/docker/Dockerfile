FROM docker.io/bkci/codecc:latest
RUN mkdir -p /usr/codecc/software
RUN mkdir -p /usr/codecc/tool_scan
COPY sdk /usr/codecc/tool_scan/sdk/
COPY third_rules /usr/codecc/tool_scan/third_rules/
COPY tool /usr/codecc/tool_scan/tool/
RUN chmod -R 755 /usr/codecc/tool_scan
WORKDIR /usr/codecc/tool_scan