from utils.image.image_converter import ImageConverter

class ImageChopper:
    @staticmethod
    def chop_left(image, w):
        img = ImageConverter().convert_to_np_image(image)
        chopped_img = img[:, w:]
        return chopped_img
    @staticmethod
    def chop_right(image, w):
        img = ImageConverter().convert_to_np_image(image)
        chopped_img = img[:, :-w]
        return chopped_img
    
    @staticmethod
    def chop_top(image, h):
        img = ImageConverter().convert_to_np_image(image)
        chopped_img = img[h:, :]
        return chopped_img
    @staticmethod
    def chop_bottom(image, h):
        img = ImageConverter().convert_to_np_image(image)
        chopped_img = img[:-h, :]
        return chopped_img
    @staticmethod
    def chop_border(image, w):
        img = ImageConverter().convert_to_np_image(image)
        chopped_img = img[w:-w, w:-w]
        return chopped_img