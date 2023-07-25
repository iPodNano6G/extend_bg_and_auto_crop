from models.image import Image

class CompositedImage(Image):
    def __init__(self) -> None:
        super().__init__()
        self.outer_image = None
        self.inner_image = None
        self.composited_image = None
        self.x_offset = None
        self.y_offset = None