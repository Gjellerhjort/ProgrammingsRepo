import requests
from bs4 import BeautifulSoup
import pandas as pd

# Target URL
url = "https://smarthomescene.com/blog/the-ultimate-list-of-mmwave-radar-sensor-modules/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Find the radar sensor table
table = soup.find("table")
if not table:
    raise Exception("Could not find table")

# Original headers
headers = [th.get_text(strip=True) for th in table.find("thead").find_all("th")]

# Insert "Image" as second column
headers.insert(1, "Image")

rows = []

# Process rows
for tr in table.find("tbody").find_all("tr"):
    row_data = []
    image_url = ""

    tds = tr.find_all("td")

    for i, td in enumerate(tds):
        text = td.get_text(strip=True)

        # Extract image URL (once per row)
        if not image_url:
            for img in td.find_all("img"):
                src = img.get("src")
                if src and src.startswith("http"):
                    image_url = src
                    break

        # Format ESPHomeSupport as Markdown link(s)
        if headers[i + 1] == "ESPHomeSupport":
            links = td.find_all("a", href=True)
            if links:
                md_links = [f"[{a.get_text(strip=True)}]({a['href']})" for a in links if a["href"].startswith("http")]
                text = ", ".join(md_links)

        # Format Availability as Markdown link(s)
        elif headers[i + 1] == "Availability":
            links = td.find_all("a", href=True)
            if links:
                md_links = [f"[{a.get_text(strip=True)}]({a['href']})" for a in links if a["href"].startswith("http")]
                text = ", ".join(md_links)

        row_data.append(text)

    # Insert image_url after the first column
    row_data.insert(1, image_url)
    rows.append(row_data)

# Create and save the final DataFrame
df = pd.DataFrame(rows, columns=headers)
df.to_csv("mmwave_sensor_modules_cleaned.csv", index=False)

print("✅ Done! Image is now in the 2nd column, and links are cleaned.")
