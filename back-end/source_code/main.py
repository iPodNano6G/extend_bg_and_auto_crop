import json

from modules import image_processor
from modules import database

with open("download.json", 'r') as file:
    shoppingmall_data = json.load(file)

seller_brand_path = shoppingmall_data["seller"]+"/"+shoppingmall_data["brand"]

imageDownloder = image_processor.ImageDownloader()
imageFactory = image_processor.ImageFactory()

imageProcessor = image_processor.ImageProcessor()

faceDetector = image_processor.FaceDetector()
clothesDetector = image_processor.ClothesDetector()

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

