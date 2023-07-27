from rembg import remove

class ImageBgRemover:
    @staticmethod
    def remove_background(np_image):
        bg_removed_np_image = remove(np_image)
        return bg_removed_np_image

