import requests
from bs4 import BeautifulSoup
import mysql.connector as mysql
import os
from dotenv import load_dotenv

load_dotenv()
db_host = os.environ['MYSQL_HOST']
db_user = os.environ['MYSQL_USER']
db_pass = os.environ['MYSQL_PASSWORD']
db_name = os.environ['MYSQL_DATABASE']

db = mysql.connect(host="sql3.freesqldatabase.com", user="sql3493972", password="CB6YQQVruM",
                   database="sql3493972")
cursor = db.cursor()

url = "http://192.168.188.251/"  # http://192.168.1.212/

try:
    cursor.execute("""TRUNCATE TABLE device0""")
    while True:  # while True:
        r = requests.get(url)
        c = r.content
        soup = BeautifulSoup(c, "html.parser")
        # print(soup.prettify())

        data = []
        for div in soup.find_all("div"):
            for p in div.find_all("p"):
                data.append(float(p.text))

        print(data)

        # time.sleep(0.02)

        query = "INSERT INTO device0 (ax, ay, az, gx, gy, gz, distance) VALUES ({}, {}, {}, {}, {}, {}, {})"\
            .format(data[0], data[1], data[2], data[3], data[4], data[5], data[6])
        print(query)
    
        cursor.execute(query)
        db.commit()

except:
    pass
finally:
    print('close')
