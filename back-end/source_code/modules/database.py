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
    def insertToClothesDataCollection(self, orignalImage, imaga_url, finalImage, face, clothes):
        db = self.client['fashionImageTest']
        collection = db['clothesData']
        inserted_data = {
            "original_image": {
                "file_path": orignalImage.filepath,
                "url": imaga_url
            },
            "dalle_image_path": finalImage.filepath,
            "dalle_image_width": finalImage.width,
            "dalle_image_height": finalImage.height,
            "x_offset": finalImage.x_offset,
            "y_offset": finalImage.y_offset,
            "face": {
                "left_line_pixel": face.left + finalImage.x_offset,
                "right_line_pixel": face.right + finalImage.x_offset,
                "top_line_pixel": face.top + finalImage.y_offset,
                "bottom_line_pixel": face.bottom + finalImage.y_offset,
            },
            "clothes": {
                "type_of_clothes": clothes.type_of_clothes,
                "left_line_pixel": clothes.left + finalImage.x_offset,
                "right_line_pixel": clothes.right + finalImage.x_offset,
                "top_line_pixel": clothes.top + finalImage.y_offset,
                "bottom_line_pixel": clothes.bottom + finalImage.y_offset,
            }
        }
        print(type(inserted_data["clothes"]["left_line_pixel"]))
        print(inserted_data["clothes"]["left_line_pixel"])
        insert_result = collection.insert_one(inserted_data)
        print(f"Inserted document ID: {insert_result.inserted_id}")