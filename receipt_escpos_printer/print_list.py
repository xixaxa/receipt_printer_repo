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
    # Fetch state of the todo.shopping_list entity
    response = requests.get(f"{ha_url}/api/states/todo.shopping_list", headers=headers)
    response.raise_for_status()
    data = response.json()

    # Extract items
    items = data["attributes"].get("items", [])

    p = printer.Network(printer_ip, port=printer_port)
    p.set(align="left", font="a")
    content = "🛒 Home Assistant To-Do List:\\n"
    for entry in items:
        if not entry.get("completed", False):
            content += f"[ ] {entry['summary']}\\n"
    content += "\\n"

    p.text(content)
    p.cut()
    p.close()

    print("✅ Printed from todo.shopping_list.")
except Exception as e:
    print(f"❌ Error printing: {e}")
