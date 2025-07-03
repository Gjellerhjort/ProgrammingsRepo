import os
import csv
import requests
from pathlib import Path
from urllib.parse import urlparse
import re

INPUT_CSV = "mmwave_sensor_modules.csv"
IMAGE_DIR = Path("static/images")

def slugify(text):
    text = str(text).strip()
    text = re.sub(r'[^\w\s-]', '', text)  # Remove special characters
    text = re.sub(r'[\s\-]+', '-', text)  # Replace spaces/underscores with dash
    return text.lower()

def get_file_extension(url, resp_headers=None):
    ext = os.path.splitext(urlparse(url).path)[-1].lower()
    if ext and ext in ['.jpg', '.jpeg', '.png', '.gif', '.webp']:
        return ext
    if resp_headers:
        ctype = resp_headers.get("Content-Type", "")
        if "image/jpeg" in ctype:
            return ".jpg"
        if "image/png" in ctype:
            return ".png"
        if "image/gif" in ctype:
            return ".gif"
        if "image/webp" in ctype:
            return ".webp"
    return ".jpg"

def download_image(url, model_name):
    print(f"downloading image for {model_name}: {url}")
    if not url or url.strip() in ["/", "-"]:
        print("SKIPPED: empty or placeholder url")
        return None
    IMAGE_DIR.mkdir(exist_ok=True, parents=True)
    try:
        resp = requests.get(url, timeout=15, stream=True)
        if resp.status_code == 200:
            ext = get_file_extension(url, resp.headers)
            model_slug = slugify(model_name)
            if not model_slug:
                model_slug = "unknown-model"
            img_name = f"{model_slug}{ext}"
            img_path = IMAGE_DIR / img_name
            with open(img_path, "wb") as f:
                for chunk in resp.iter_content(4096):
                    f.write(chunk)
            print(f"Saved: {img_path}")
            return img_name
        else:
            print(f"Failed to download (status {resp.status_code}): {url}")
            return None
    except Exception as e:
        print(f"Failed to download {url}: {e}")
        return None

def main():
    with open(INPUT_CSV, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for idx, row in enumerate(reader):
            url = row.get("Image", "")
            model = row.get("Model", "")
            download_image(url, model)

if __name__ == "__main__":
    main()