from models.builders.mask_builder import MaskBuilder
from utils.masks.mask_detector import MaskDetector

class MaskGenerationService:
    def detect_mask(self, np_image) -> "Mask":
        np_mask = MaskDetector().detect_mask(np_image)
        mask = MaskBuilder().set_np_image(np_mask).build()
        return mask
