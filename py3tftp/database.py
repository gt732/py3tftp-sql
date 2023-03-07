import psycopg2
from rich import print
import os
import contextlib

DATABASE_NAME = os.getenv('DATABASE_NAME')
DATABASE_PORT = os.getenv('DATABASE_PORT')
DATABASE_HOSTNAME = os.getenv('DATABASE_HOSTNAME')
DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD')
DATABASE_USERNAME = os.getenv('DATABASE_USERNAME')


class Database:
    def __init__(self, conn):
        self.conn = conn

    def query(self, sql, values=None):
        with self.conn.cursor() as cursor:
            cursor.execute(sql, values)
            return cursor.fetchall()

    def insert_data(self, hostname, config):
        with self.conn.cursor() as cursor:
            sql = "INSERT INTO backups (hostname, config) VALUES (%s, %s)"
            values = (hostname, config)
            cursor.execute(sql, values)
            self.conn.commit()

    def close(self):
        self.conn.close()

@contextlib.contextmanager
def connect_database():
    try:
        conn = psycopg2.connect(
            dbname=DATABASE_NAME, user=DATABASE_USERNAME, password=DATABASE_PASSWORD,
            host=DATABASE_HOSTNAME, port=DATABASE_PORT
        )
        db = Database(conn)
        yield db
    finally:
        conn.close()