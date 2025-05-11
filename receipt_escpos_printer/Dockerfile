ARG BUILD_FROM
FROM $BUILD_FROM

# Install system dependencies for python-escpos
RUN apk add --no-cache \
    python3 \
    py3-pip \
    build-base \
    libffi-dev \
    libusb-dev \
    cups-dev \
    py3-setuptools

COPY requirements.txt /requirements.txt
RUN pip3 install --no-cache-dir -r /requirements.txt

COPY run.sh /
COPY print_list.py /
RUN chmod +x /run.sh

CMD ["/run.sh"]
