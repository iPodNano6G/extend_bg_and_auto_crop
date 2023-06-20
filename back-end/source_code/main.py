import json
import sys

from modules import image_processor
from modules import fileManager
from modules import object_detector
from modules import database


with open(sys.argv[1], 'r', encoding='UTF8') as file:
    shoppingmall_data = json.load(file)

seller_brand_path = shoppingmall_data["seller"]+"/"+shoppingmall_data["brand"]

imageDownloder = fileManager.ImageDownloader()
imageFactory = image_processor.ImageFactory()

imageProcessor = image_processor.ImageProcessor()

faceDetector = object_detector.FaceDetector()
clothesDetector = object_detector.ClothesDetector()

databaseManager = database.DatabaseManager()

for product in shoppingmall_data["product_list"]:
    save_path = "image_data/"+seller_brand_path+"/"+product["name"]
    image_url = product["url"]
    image_path = imageDownloder.download_image(image_url, save_path, "original.jpg")
    image = imageFactory.create_image(image_path, None)

    result_image = imageProcessor.process(image)

    faceData = faceDetector.detectFace(image)
    face = faceData.getFace(1)
    
    clothesDataList = clothesDetector.localize_objects(image)
    clothes = clothesDataList.getClothes(product["type_of_clothes"])
    clothes.denormalizeByImageSize(image)

    

    databaseManager.insertToClothesDataCollection(image, image_url, result_image, face, clothes)