from models.image import Image
from abc import ABC, abstractmethod


class ImageBuilder(ABC):
    def __init__(self) -> None:
        self.image = self.create_image()
        
    @abstractmethod
    def create_image(self):
        pass
    def set_np_image(self, np_image):
        self.image.np_image = np_image
        self.image.set_shape()
        return self
    def set_url(self, url):
        self.image.url = url
        return self
    def set_id(self, id):
        self.image.id = id
        return self
    def build(self):
        return self.image