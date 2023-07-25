import cv2

class ImageResizer:
    def resize(self, np_image, width, height):
        np_image = cv2.resize(np_image, (width, height))
        return np_image
    def enlarge_according_to_mask(np_image, mask, ratio = 50):
        object_long_side_length = mask.get_long_side_length()

        np_image = cv2.cvtColor(np_image, cv2.COLOR_RGB2RGBA)
        #인물의 객체의 긴 길이가 50%, 1024*1024에서 약 50%(550픽셀)을 차지하도록 설정
        new_width = int(np_image.shape[1]*ratio*10/object_long_side_length)
        new_height =  int(np_image.shape[0]*ratio*10/object_long_side_length)
        np_image = cv2.resize(np_image, (new_width, new_height))
    
        return np_image