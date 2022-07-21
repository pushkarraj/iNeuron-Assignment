import pymongo


client = pymongo.MongoClient("mongodb+srv://pushkar:push_94302@cluster0.kr25n79.mongodb.net/?retryWrites=true&w=majority")
db = client.test

d = {
    "name":"Pushkar",
    "email" : "pushkar.raj6@gmail.com",
    "surname" : "raj"
}
db1 = client['connect']
coll = db1['test']
coll.insert_one(d)