import cv2
import numpy as np

class ImageConverter:
    def convert_to_np_image(self, image):
        if isinstance(image, bytes):
            npimg = np.fromstring(image, np.uint8)
            img = cv2.imdecode(npimg, cv2.IMREAD_COLOR)
        elif isinstance(image, np.ndarray):
            img = image
        elif isinstance(image, str):
            img = cv2.imread(image)

        return img