from models.composited_image import CompositedImage
from models.builders.image_builder import ImageBuilder

class CompositedImageBuilder(ImageBuilder):
    def create_image(self):
        return CompositedImage()
    def set_outer_image(self, outer_image):
        self.image.outer_image = outer_image
        return self
    def set_inner_image(self, inner_image):
        self.image.inner_image = inner_image
        return self
    def set_composited_image(self, composited_image):
        self.image.composited_image = composited_image
        return self
    def set_x_offset(self, x_offset):
        self.image.x_offset = x_offset
        return self
    def set_y_offset(self, y_offset):
        self.image.y_offset = y_offset 
        return self
    def build(self):
        return self.image