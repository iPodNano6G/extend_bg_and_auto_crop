from abc import ABC, abstractmethod

class Image(ABC):
    def __init__(self):
        self.np_image = None
        self.height = None
        self.width = None
        self.url = None
        self.id = None
    def set_shape(self):
        self.height, self.width = self.np_image.shape[:2]
