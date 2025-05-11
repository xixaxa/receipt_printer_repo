import os
import requests
from escpos import printer

printer_ip = os.getenv("PRINTER_IP")
printer_port = int(os.getenv("PRINTER_PORT"))
ha_url = os.getenv("HA_URL").rstrip("/")
ha_token = os.getenv("HA_TOKEN")

headers = {
    "Authorization": f"Bearer {ha_token}",
    "Content-Type": "application/json",
}

try:
    response = requests.get(f"{ha_url}/api/shopping_list", headers=headers)
    response.raise_for_status()
    items = response.json()

    p = printer.Network(printer_ip, port=printer_port)
    p.set(align="left", font="a")
    content = "Home Assistant Shopping List:\n"
    for entry in items:
        if not entry.get("complete", False):
            content += f"[ ] {entry['name']}\n"
    content += "\n"

    p.text(content)
    p.cut()
    p.close()

    print("✅ Printed shopping list.")
except Exception as e:
    print(f"❌ Error: {e}")
