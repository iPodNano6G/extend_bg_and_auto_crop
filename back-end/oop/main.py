import sys
import json

import temp

with open(sys.argv[1], 'r') as file:
    shoppingmall_data = json.load(file)

seller_brand_path = shoppingmall_data["seller"]+"/"+shoppingmall_data["brand"]

imageDownloder = temp.ImageDownloader()
imageFactory = temp.ImageFactory()

imageProcessor = temp.ImageProcessor()

faceDetector = temp.FaceDetector()

clothesDetector = temp.ClothesDetector()

databaseManager = temp.DatabaseManager()

for product in shoppingmall_data["product_list"]:
    save_path = seller_brand_path+"/"+product["name"]
    image_path = imageDownloder.download_image(product["url"], save_path, "original.jpg")
    image = imageFactory.create_image(image_path, None)

    result_image = imageProcessor.process(image)

    faceData = faceDetector.detectFace(image)
    face = faceData.getFace(1)
    
    clothesDataList = clothesDetector.localize_objects(image)
    clothes = clothesDataList.getClothes(product["type_of_clothes"])
    clothes.denormalizeByImageSize(image)

    databaseManager.insertToClothesDataCollection(image, result_image, face, clothes)

