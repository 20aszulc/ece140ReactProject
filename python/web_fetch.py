import requests
from bs4 import BeautifulSoup
import time
import mysql.connector as mysql
import os
from dotenv import load_dotenv

load_dotenv()
db_host = os.environ['MYSQL_HOST']
db_user = os.environ['MYSQL_USER']
db_pass = os.environ['MYSQL_PASSWORD']
db_name = os.environ['MYSQL_DATABASE']

db = mysql.connect(user=db_user, password=db_pass, host=db_host, database=db_name)
cursor = db.cursor()

url = "http://localhost/"

for i in range(3):  # while True:
    r = requests.get(url)
    c = r.content
    soup = BeautifulSoup(c, "html.parser")
    # print(soup.prettify())

    data = []
    for div in soup.find_all("div"):
        for p in div.find_all("p"):
            data.append(float(p.text))

    print(data)

    query = "INSERT INTO accel (ax, ay, az) VALUES ({}, {}, {})".format(data[0], data[1], data[2])
    print(query)

    cursor.execute(query)
    db.commit()

    time.sleep(1)
