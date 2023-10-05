from pymongo import MongoClient

client = MongoClient(
    'mongodb+srv://hdsvidi:AoH8Ab6Jg3NDibr8@cluster0.2u8dits.mongodb.net/?retryWrites=true&w=majority'
)

db = client['semilir']

def get_db_connection():
    return db


# try:
#     client.admin.command('ping')
#     print("Pinged your deployment. You successfully connected to MongoDB!")
# except Exception as e:
#     print(e)
