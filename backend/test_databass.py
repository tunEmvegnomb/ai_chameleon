from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.chameleon

selfie = {
    'name_selfie': '2022-05-19:17:30.jpg'
}

db.selfie.insert_one(selfie)
recent_selfie_id = str(db.selfie.find_one(
    {'name_selfie': '2022-05-19:17:30.jpg'})['_id'])

gif = {
    '_id': 'd4f8d964f52s3d45f6sd4f56s',
    'selfie_id': recent_selfie_id,
    'name_gif': 'Chamo0519001.gif'
}

db.gif.insert_one(gif)
