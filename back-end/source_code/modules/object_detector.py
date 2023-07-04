import cv2
import os
from modules import image_processor


class Face:
    def __init__(self, left, top, right, bottom) -> None:
        if None in [left, top, right, bottom]:
            self.left = None
            self.top = None
            self.right = None
            self.bottom = None
        else:
            self.left = int(left)
            self.top = int(top)
            self.right = int(right)
            self.bottom = int(bottom)
class FaceDataList:
    def __init__(self, face_dict_data) -> None:
        self.data = face_dict_data
    def getFace(self, face_number):
        if type(self.data) is tuple:
            return Face(None, None, None, None)
        face_location = self.data["face_"+str(face_number)]["facial_area"]
        return Face(face_location[0], face_location[1], face_location[2], face_location[3])
    
class FaceDetector:
    # https://github.com/serengil/retinaface
    def detectFace(self, image):
        from retinaface import RetinaFace
        faceDataList = FaceDataList(RetinaFace.detect_faces(image.cv_image))
        return faceDataList
class BoxDrower:
    def drawBox(self, image, left_top, right_bottom, name):
        print(left_top, right_bottom)
        if left_top == None:
            print("there is no face")
            return
        face_bounding_box = (image.cv_image).copy()
        cv2.rectangle(face_bounding_box, left_top, right_bottom, (0, 255, 0), 2)
        imageSaver = image_processor.ImageSaver()
        imageSaver.saveImage(image.filepath, face_bounding_box, name)

class ClothesDetector:
    def localize_objects(self, image):
        from google.cloud import vision
        client = vision.ImageAnnotatorClient()

        with open(image.filepath, 'rb') as image_file:
            content = image_file.read()
        image = vision.Image(content=content)

        objects = client.object_localization(
            image=image).localized_object_annotations

        return ClothesObjectsList(objects)
    
class Clothes:
    def __init__(self, type_of_clothes, left, top, right, bottom) -> None:
        self.type_of_clothes = type_of_clothes
        self.normalized_left = left
        self.normalized_top = top
        self.normalized_right = right
        self.normalized_bottom = bottom
        self.left = None
        self.top = None
        self.right = None
        self.bottom = None
    def denormalizeByImageSize(self, image):
        self.left = int(self.normalized_left * image.width)
        self.top = int(self.normalized_top * image.height)
        self.right = int(self.normalized_right * image.width)
        self.bottom = int(self.normalized_bottom * image.height)

class ClothesObjectsList:
    def __init__(self, objects) -> None:
        self.objects = objects
    def getClothes(self, type_of_clothes):
        for object_ in self.objects:
            if object_.name.lower() == type_of_clothes.lower():
                break
        clothes_data_normalized_vertices = object_.bounding_poly.normalized_vertices

        normalized_clothes_left = clothes_data_normalized_vertices[0].x
        normalized_clothes_top = clothes_data_normalized_vertices[0].y
        normalized_clothes_right = clothes_data_normalized_vertices[2].x
        normalized_clothes_bottom = clothes_data_normalized_vertices[2].y
        return Clothes(type_of_clothes, normalized_clothes_left,normalized_clothes_top, normalized_clothes_right, normalized_clothes_bottom)