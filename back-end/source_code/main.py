import json
import sys

from modules import image_processor
from modules import fileManager
from modules import object_detector
from modules import database
from modules import photoshop

with open(sys.argv[1], 'r', encoding='UTF8') as file:
    shoppingmall_data = json.load(file)


boxDrower = object_detector.BoxDrower()

seller_brand_path = shoppingmall_data["seller"]+"/"+shoppingmall_data["brand"]

imageDownloder = fileManager.ImageDownloader()
imageFactory = image_processor.ImageFactory()

imageProcessor = image_processor.ImageProcessor()

faceDetector = object_detector.FaceDetector()
clothesDetector = object_detector.ClothesDetector()


jsonMaker = fileManager.JsonMaker()
DocumentManager = fileManager.DocumentManager()

photoshop_ = photoshop.Photoshop("C:/Program Files/Adobe/Adobe Photoshop 2023/Photoshop.exe")

for product in shoppingmall_data["product_list"]:
    save_path = "image_data/"+seller_brand_path+"/"+product["name"]
    image_url = product["url"]
    image_path = imageDownloder.download_image(image_url, save_path, "original.jpg")
    image = imageFactory.create_image(image_path, None, image_url)


    result_image = imageProcessor.process(image)
    boxDrower.drawBox(result_image, (result_image.x_offset, result_image.y_offset), (result_image.x_offset + image.width, result_image.y_offset + image.height), "box_result_box")
    print((result_image.x_offset, result_image.y_offset), (result_image.x_offset + image.width, result_image.y_offset + image.height))

    faceData = faceDetector.detectFace(image)
    face = faceData.getFace(1)
    print((face.left, face.top), (face.right, face.bottom))
    boxDrower.drawBox(image, (face.left, face.top), (face.right, face.bottom), "box_face")
    

    clothesDataList = clothesDetector.localize_objects(image)
    clothes = clothesDataList.getClothes(product["type_of_clothes"])
    clothes.denormalizeByImageSize(image)
    boxDrower.drawBox(image, (clothes.left, clothes.top), (clothes.right, clothes.bottom), "box_clothes")

    no_background_image_path = photoshop_.remove_background(image_path)

    json_document = jsonMaker.make_json_for_clothes_data(image, image_url, result_image, face, clothes, no_background_image_path)
    json_path = DocumentManager.save_json_document(json_document, image_path)

    #databaseManager.insertToClothesDataCollection(image, image_url, result_image, face, clothes)