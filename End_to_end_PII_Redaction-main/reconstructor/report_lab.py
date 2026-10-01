import pymongo
client=pymongo.MongoClient("mongodb://localhost:27017/")
db=client['deepak']
collection=db['storage']
a=collection.find()
for i in a:
    print(i)