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

    clothesDataList = clothesDetector.localize_objects(image)
    clothes = clothesDataList.getClothes(product["type_of_clothes"])
    clothes.denormalizeByImageSize(image)
    boxDrower.drawBox(image, (clothes.left, clothes.top), (clothes.right, clothes.bottom), "clothes")