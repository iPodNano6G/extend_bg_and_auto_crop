import temp

imageFactory = temp.ImageFactory()
#faceDetector = temp.FaceDetector()
#boxDrower = temp.BoxDrower()
clothesDetector = temp.ClothesDetector()
imagepath = "/home/sang/automated_image_processing/automated_image_processing/automated_image_processing/back-end/oop/ssfshop/beanpole/남녀공용 베이직 피케 티셔츠 - 블랙/DallE.png"
image = imageFactory.create_image(imagepath, None)

clothesObjectsList = clothesDetector.localize_objects(image)
clothes = clothesObjectsList.getClothes("top")
print(clothes.left, clothes.top, clothes.right, clothes.bottom)
