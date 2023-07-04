from pymongo import MongoClient

class DatabaseManager:
    def __init__(self):
        self.client = MongoClient('mongodb://localhost:27017/')
        
    def is_mongodb_running(self):
        try:
            self.client.server_info()  # 서버 정보 요청
            return True  # 실행 중인 경우 True 반환
        except:
            return False
    def insertToClothesDataCollection(self, bson_document):
        db = self.client['fashionImageTest']
        collection = db['clothesData']
        insert_result = collection.insert_one(bson_document)
        print(f"Inserted document ID: {insert_result.inserted_id}")