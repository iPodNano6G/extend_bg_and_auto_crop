import numpy as np

class ImageCompister:
    def composite(self, outer_np_image, inner_np_image, x_offset = 0, y_offset = 0):
        '''
        if isinstance(outer_image, CompositedImage):
            outer_image_copy = np.copy(outer_image.outer_image)
            inner_image = outer_image.inner_image
            x_offset = outer_image.x_offset
            y_offset = outer_image.y_offset
        elif isinstance(outer_image, np.ndarray):
            outer_image_copy = np.copy(outer_image)
        '''
        
        outer_np_image_copy = np.copy(outer_np_image)
        outer_np_image_copy[y_offset:y_offset + inner_np_image.shape[0], x_offset:x_offset + inner_np_image.shape[1]] = inner_np_image

        return outer_np_image_copy
    