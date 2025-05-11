ARG BUILD_FROM=ghcr.io/home-assistant/amd64-base:latest
FROM $BUILD_FROM

ENV LANG C.UTF-8

# Install system dependencies
RUN apk add --no-cache \
    python3 \
    py3-pip \
    build-base \
    libffi-dev \
    libusb-dev \
    cups-dev \
    py3-setuptools \
    py3-wheel \
    linux-headers

# Add Python requirements
COPY requirements.txt /requirements.txt
RUN pip3 install --break-system-packages --no-cache-dir -r /requirements.txt

# Copy runtime files
COPY run.sh /run.sh
COPY print_list.py /print_list.py
RUN chmod a+x /run.sh

CMD [ "/run.sh" ]
