from google.cloud import vision

class ObjectDetectAPI:
    def detect_objects(self, image_bytes):
        client = vision.ImageAnnotatorClient()
        image = vision.Image(content=image_bytes)
        objects = client.object_localization(
            image=image).localized_object_annotations
        return objects