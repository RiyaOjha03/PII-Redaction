import pymongo

def storage_sender(text_data):

    client=pymongo.MongoClient("mongodb://localhost:27017/")
    # print(client)
    db=client['deepak']
    collection=db['storage']
    collection.insert_one(text_data)