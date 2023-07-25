from services.api.dallE_api import DallEAPI
from utils.image.image_converter import ImageConverter

class OutpaintingService:
    def outpaint_using_dallE(self, image, length):
        """
        이미지의 투명픽셀을 채우는 메서드
        """
        np_image = ImageConverter().convert_to_np_image(image)
        outpainted_np_image = DallEAPI().outpainting(np_image, length)
        
        return outpainted_np_image