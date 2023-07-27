import cv2
import base64

class ImageEncoder:
    @staticmethod
    def encode_np_image_base64(image):
        _, img_encoded = cv2.imencode('.jpg', image)
        img_string = base64.b64encode(img_encoded).decode('utf-8')
        return img_string