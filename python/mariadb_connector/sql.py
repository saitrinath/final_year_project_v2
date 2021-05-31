import mariadb
import sys
try:
    conn = mariadb.connect(
        user="sai",
        password="123",
        host="localhost",
        port=3306,
        database="project"

    )
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)

conn.autocommit = True
# Get Cursor
cur = conn.cursor()

def get_cur():
	return cur

