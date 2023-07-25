import numpy as np
import cv2

from models.builders.composited_image_builer import CompositedImageBuilder
from utils.image.image_compositer import ImageCompister

class PaddingService:
    """
    mask에 있는 객체를 모두 포함하는 직사각형이 장변이 ratio(%) 만큼
    """
    def add_square_padding_according_to_mask(self, inner_np_image, mask, ratio = 50) -> "CompsitedImage":
        if mask is None:
            if inner_np_image.shape[0] >= inner_np_image.shape[0]:
                long_length = inner_np_image.shape[0]
            else:
                long_length = inner_np_image.shape[1]
        else:
            long_length = mask.get_long_side_length()

        new_length = int(100 * long_length / ratio)


        inner_np_image_width = inner_np_image.shape[1]
        inner_np_image_height = inner_np_image.shape[0]

        x_offset = int((new_length - inner_np_image_width) / 2)
        y_offset = int((new_length - inner_np_image_height) / 2)

        transparent_image = np.zeros((new_length, new_length, 4), dtype=np.uint8)
        inner_np_image = cv2.cvtColor(inner_np_image, cv2.COLOR_RGB2RGBA)
        padded_np_image = ImageCompister().composite(transparent_image, inner_np_image, x_offset, y_offset)

        padded_image = (
            CompositedImageBuilder()
            .set_outer_image(transparent_image)
            .set_inner_image(inner_np_image)
            .set_composited_image(padded_np_image)
            .set_x_offset(x_offset)
            .set_y_offset(y_offset)
            .build())
        return padded_image
    