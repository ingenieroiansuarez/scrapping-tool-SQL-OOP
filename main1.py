import time
import requests
import selectorlib
import smtplib, ssl
import os
import sqlite3

# Example SQL queries
"INSERT INTO database VALUES ('tigers', 'tiger city', '2023-10-01')"
"SELECT * FROM database WHERE date='2025.10.05'"

# This script scrapes tour data from a specified URL, extracts relevant information,

URL = "https://programmer100.pythonanywhere.com/tours/"

connection = sqlite3.connect("data1.db")

def scrape(URL):
    """Scrape the tour data from the given URL."""
    response = requests.get(URL)
    source = response.text
    return source

def extract(source):
    # Extract the tour data from the scraped HTML source using selectorlib.
    extractor = selectorlib.Extractor.from_yaml_file("extract.yaml")
    value = extractor.extract(source)["tours"]
    return value

def send_email(message):
    # Send an email notification with the given message.
    host = "smtp.gmail.com"
    port = 465

    username = "ingenieroiansuarez@gmail.com"
    password = "ezkp ydkc zupi uhjx"

    receiver = "ingenieroiansuarez@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)
    print("email sent successfully!")


def store(extracted):
    """Store the extracted data in a file."""
    row = extracted.split(",")
    row = [item.strip() for item in row]
    cursor = connection.cursor()
    cursor.execute("INSERT INTO database VALUES (?, ?, ?)", row)
    connection.commit()
    print("Data stored successfully!")

def read(extracted):
    row = extracted.split(",")
    row = [item.strip() for item in row]
    band, city, date = row
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM database WHERE band=? AND city=? AND date=?",
                   (band, city, date))
    rows = cursor.fetchall()
    print(rows)
    return  rows

if __name__ == "__main__":
    # Scrape the data
    while True:
        scraped = scrape(URL)
        extracted = extract(scraped)
        print(extracted)

        if extracted != "No upcoming tours":
            row = read(extracted)
            if not row:
                store(extracted)
                send_email(message= "new event was found")
        time.sleep(2)


