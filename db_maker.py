from pymongo import MongoClient
from pymongo.cursor import CursorType
from datetime import datetime
import pprint

host = "localhost"
port = "27017"
mongo = MongoClient(host, int(port))
print(mongo)

def insert_item_one(mongo, email, diary, db_name=None, collection_name=None):
    data = {"email" : email, "time" : datetime.now().strftime('%y년%m월%d일 %H시%M분%S초'), "diary":diary}
    result = mongo[db_name][collection_name].insert_one(data).inserted_id
    return result

def find_item(email):
    db = mongo.diary
    collection = db.diary_list
    posts = db.diary_list
    result = []
    for post in collection.find({"email":email}):
        # pprint.pprint(post)
        result.append(post)
    return result

print(find_item("izero3127@gmail.com"))

# collection = posts['diary_list']
# # insert_item_one(mongo, "izero3127@gmail.com", "오늘 힘드네", "diary", "diarylist")
# # cursor = find_item(mongo, "izero3127@gmail.com", None, "diary", "diarylist")
# pprint.pprint(posts.find_one())


    