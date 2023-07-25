import cv2
class ImageWriter:
    def save_np_image(self, np_image, dir_name = '.' , file_name = "no_named.png"):
        file_dir = dir_name + '/' + file_name
        cv2.imwrite(file_dir, np_image)
        return file_dir