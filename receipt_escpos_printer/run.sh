#!/usr/bin/with-contenv bashio

PRINTER_IP=$(bashio::config 'printer_ip')
PRINTER_PORT=$(bashio::config 'printer_port')
HA_URL=$(bashio::config 'ha_url')
HA_TOKEN=$(bashio::config 'ha_token')

export PRINTER_IP
export PRINTER_PORT
export HA_URL
export HA_TOKEN

python3 /print_list.py
