from retinaface import RetinaFace
from utils.image.image_converter import ImageConverter

class FaceDetectionService:
    # https://github.com/serengil/retinaface
    def detect_faces(self, image_bytes, normalized = True):
        image = ImageConverter().convert_to_np_image(image_bytes)
        
        data = RetinaFace.detect_faces(image)
        
        if normalized is False: # [left, top, right, bottom]
            faceDataList = {face: 
                            {'facial_area': 
                             {"left": int(info['facial_area'][0]),
                              "top": int(info['facial_area'][1]),
                              "right": int(info['facial_area'][2]),
                              "bottom": int(info['facial_area'][3])}}
                              for face, info in data.items()}
        else:
            img_width = image.shape[1]
            img_height = image.shape[0]
            faceDataList = {face: {'facial_area': {
                "left": int(info['facial_area'][0]) / img_width,
                "top": int(info['facial_area'][1]) / img_height,
                "right": int(info['facial_area'][2]) / img_width,
                "bottom": int(info['facial_area'][3]) / img_height}} 
                for face, info in data.items()}
            
        return faceDataList