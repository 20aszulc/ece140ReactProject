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

try:
    cursor.execute("""
    create table accel_data(
        id INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY,
        ax float,
        ay float,
        az float,
        created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
    );
  """)
except RuntimeError as err:
    print("runtime error: {0}".format(err))
