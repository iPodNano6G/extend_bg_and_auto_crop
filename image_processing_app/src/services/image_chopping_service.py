from utils.image.image_chopper import ImageChopper

class ImageChoppingService:
    def __init__(self) -> None:
        self.image_chopper = ImageChopper()

    def chop_according_to_mask(self, image, mask, x_offset, y_offset):
        new_x_offset = x_offset
        new_y_offset = y_offset
        if mask.touch_border_left is True:
            image = self.image_chopper.chop_left(image, x_offset)
            new_x_offset = 0
        if mask.touch_border_right is True:
            image = self.image_chopper.chop_right(image, x_offset)
        if mask.touch_border_top is True:
            image = self.image_chopper.chop_top(image, y_offset)
            new_y_offset = 0
        if mask.touch_border_bottom is True:
            image = self.image_chopper.chop_bottom(image, y_offset)
        return image, new_x_offset, new_y_offset
    