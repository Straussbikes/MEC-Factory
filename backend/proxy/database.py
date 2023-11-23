from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
uri = "mongodb+srv://joao:123@cluster0.ghvmtvr.mongodb.net/?retryWrites=true&w=majority"
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))





def getEmail(etsi):
    client = MongoClient(uri, server_api=ServerApi('1'))
    db=client.test
    collection=db["users"]
    cursor=collection.find({"etsi":etsi})
    #print(cursor)
    for document in cursor:
        email=document.get("email")
        return email
    client.close()
