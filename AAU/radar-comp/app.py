import csv
import re
from flask import Flask, render_template


app = Flask(__name__)

INPUT_CSV = "mmwave_sensor_modules.csv"
HEADERS = [
    "Image", "Manufacturer", "Model", "Operating Frequency", "Transmit Power",
    "Motion Range", "Presence Range", "Detection Angle", "Operating Voltage",
    "Pins Spacing", "Size(WxH)", "ESPHome Support", "Availability"
]

def slugify(text):
    text = str(text).strip()
    text = re.sub(r'[^\w\s-]', '', text)  # Remove special characters
    text = re.sub(r'[\s\-]+', '-', text)  # Replace spaces/underscores with dash
    return text.lower()

def find_img_path(directory: str, prefix: str) -> str:
    import os
    try:
        image_name = [f for f in os.listdir(directory) if f.startswith(prefix) and os.path.isfile(os.path.join(directory, f))]
        image_path = directory + image_name[0]
        return image_path
    except:
        return ""
def parse_markdown_links(cell):
    pattern = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
    return pattern.findall(cell)

def get_rows():
    with open(INPUT_CSV, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        rows = list(reader)
    processed = []
    for idx, row in enumerate(rows):
        new_row = {}
        # The filename must match how you named it in download_images.py
        model = row.get("Model")
        img_name = f"{slugify(model)}"
        # Try all extensions
        found_img = find_img_path("static/images/", img_name)
        new_row["image"] = found_img
        man = row.get("Manufacturer", "")
        model = row.get("Model", "")
        new_row["manufacturer_model"] = f'{man}<br><b>{model}</b>' if man or model else ""
        for h in HEADERS:
            key = h.lower().replace(" ", "_")
            if h in ["Image", "Manufacturer", "Model"]:
                continue
            elif h in ["ESPHome Support", "Availability"]:
                links = parse_markdown_links(row.get(h, ""))
                new_row[key + "_links"] = links
            else:
                new_row[key] = row.get(h, "")
        processed.append(new_row)
    return processed

@app.route("/")
def table():
    rows = get_rows()
    headers = [
        "#", "Image", "Manufacturer<br>Model", "Operating Frequency",
        "Transmit Power", "Motion Range", "Presence Range", "Detection Angle",
        "Operating Voltage", "Pins Spacing", "Size(WxH)", "ESPHome Support", "Availability"
    ]
    return render_template("table.html", headers=headers, rows=rows)

if __name__ == "__main__":
    app.run(debug=True)