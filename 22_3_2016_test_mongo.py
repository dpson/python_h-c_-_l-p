from pymongo  import MongoClient
URI = "mongodb://c4e3:codethechange@ds015869.mlab.com:15869/c4e3_son_movie"
client = MongoClient(URI)
db = client.get_default_database()
son = db["son"]
son.insert_one(
    {
        "Tuoi" : "22",
        "Name" : "Anh",
        "Bang luong" : "4 do la",
    }
    )
client.close()
