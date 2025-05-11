import json
import os
from escpos import printer

printer_ip = os.getenv("PRINTER_IP", "192.168.1.79")
printer_port = int(os.getenv("PRINTER_PORT", "9100"))
shopping_list_path = "/config/.shopping_list.json"

try:
    with open(shopping_list_path, "r") as f:
        items = json.load(f)

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
    print(f"❌ Error printing: {e}")
