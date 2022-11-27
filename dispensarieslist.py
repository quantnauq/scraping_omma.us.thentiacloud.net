import requests
import csv


headers = {"accept": "accept: application/json, text/plain, */*"}
response = requests.get("https://omma.us.thentiacloud.net/rest/public/profile/search/?keyword=all&skip=0&take=20&lang=en&type=Dispensary&_=1667643431841",
                        headers=headers)
result = response.json()["result"]
titles = ["Business Name", "Trade Name", "License Type", "License Number", "License Date",
          "County", "City", "Address", "Zip", "Phone", "Email", "Hours of Operation"]
file_name = "growers.csv"
with open(file_name, "a", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(titles)

for record in result:
    business_name = record["legalName"]
    trade_name = record["tradeName"]
    license_type = record["licenseType"]
    license_number = record["licenseNumber"]
    license_date = record["licenseExpiryDate"]
    county = record["county"]
    city = record["city"]
    address = record["streetAddress"]
    zip_value = record["zip"]
    phone = record["phone"]
    email = record["email"]
    hours = record["hours"]
    result = [business_name, trade_name, license_type, license_number, license_date,
              county, city, address, zip_value, phone, email, hours]
    with open(file_name, "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(result)