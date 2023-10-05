import pytest
from pymongo import MongoClient
import app.database as database 

# Fungsi fixture untuk menginisialisasi koneksi ke database
@pytest.fixture(scope="module")
def db_connection():
    return database.db

# Pengujian koneksi ke database
def test_database_connection(db_connection):
    print('ini', db_connection.client.server_info())
    assert db_connection.client.server_info()