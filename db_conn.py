import db_info
import psycopg2


url = db_info.DATABASE_URL
connection = psycopg2.connect(url)


