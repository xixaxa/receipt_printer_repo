#!/usr/bin/with-contenv bashio
export PRINTER_IP=$(bashio::config 'printer_ip')
export PRINTER_PORT=$(bashio::config 'printer_port')

python3 /print_list.py
