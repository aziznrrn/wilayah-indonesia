import requests
import re
import csv
import os

def download_sql_file():
    url = "https://raw.githubusercontent.com/cahyadsn/wilayah/master/db/wilayah.sql"
    response = requests.get(url)
    response.raise_for_status()
    return response.text

def extract_region(sql_text):
    insert_pattern = re.compile(r"INSERT INTO wilayah \(kode, nama\)\s+VALUES\s+(.*?);", re.DOTALL)
    matches = insert_pattern.findall(sql_text)

    region = []
    for match in matches:
        rows = re.findall(r"\(([^)]+)\)", match)
        for row in rows:
            row = row.replace("''", "'")
            fields = row.split(",")
            code = fields[0].strip().strip("'")
            name = fields[1].strip().strip("'")
            region.append((code.replace(".", ""), name))

    return region

def write_csv(filename, data, headers):
    os.makedirs("./output", exist_ok=True)
    filepath = os.path.join("./output", filename)
    with open(filepath, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        writer.writerows(data)

def split_region_by_category(region):
    categories = {
        "provinces": [],
        "cities": [],
        "sub_districts": [],
        "villages": []
    }

    for code, name in region:
        length = len(code)
        if length == 2:
            categories["provinces"].append((code, name))
        elif length == 4:
            categories["cities"].append((code, name))
        elif length == 6:
            categories["sub_districts"].append((code, name))
        elif length == 10:
            categories["villages"].append((code, name))

    for category, rows in categories.items():
        filename = f"{category}.csv"
        write_csv(filename, rows, ["code", "name"])

if __name__ == "__main__":
    try:
        sql_text = download_sql_file()

        region = extract_region(sql_text)

        write_csv("wilayah.csv", region, ["code", "name"])

        split_region_by_category(region)

        print("CSV files have been created successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")
