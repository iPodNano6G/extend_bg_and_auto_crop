import cv2
import numpy as np

from utils.image.image_bg_remover import ImageBgRemover

class MaskDetector:
    def detect_mask(self, np_image):
        bg_removed_np_image = ImageBgRemover.remove_background(np_image)
        mask = np.where(bg_removed_np_image[..., 3] == 0, 0, 255).astype(np.uint8)
        
        return mask