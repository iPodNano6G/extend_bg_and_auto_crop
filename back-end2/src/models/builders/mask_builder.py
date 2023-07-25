from models.mask import Mask
from models.builders.image_builder import ImageBuilder

class MaskBuilder(ImageBuilder):
    def create_image(self):
        return Mask()
    def set_np_image(self, np_image):
        super().set_np_image(np_image)
        self.image.set_smallest_box()
        self.image.check_touching_border()
        '''
        상태를 가질 책임은 본인에게 있다. 하지만 그 상태를 확인하기 위해 많은 자원이 필요하기에, 매번 확인하기 부담스럽다면
        언제 그 상태를 확인하도록 해야하는가?
        '''
        return self
