from services.padding_service import PaddingService
from services.mask_generantion_service import MaskGenerationService
from services.outpainting_service import OutpaintingService
from services.image_chopping_service import ImageChoppingService

from utils.image.image_resizer import ImageResizer
from utils.image.image_compositer import ImageCompister
from utils.image.image_chopper import ImageChopper

class ImageProcessingService:
    def process(self, np_image, ratio = 50, recover_size = True, chop_image = True, outpainting_size = 1024, removed_border_pixel = 2):
        if removed_border_pixel > 0:
            np_image = ImageChopper().chop_border(np_image, removed_border_pixel)

        mask = MaskGenerationService().detect_mask(np_image)
        compsited_image = PaddingService().add_square_padding_according_to_mask(np_image, mask, ratio = ratio)
        
        pre_outpainted_image = compsited_image.composited_image
        outpainted_image = OutpaintingService().outpaint_using_dallE(pre_outpainted_image, outpainting_size)
        #############################################################
        if recover_size is True:
            outer_width = compsited_image.outer_image.shape[1]
            outer_height = compsited_image.outer_image.shape[0]
            outpainted_image = ImageResizer().resize(outpainted_image, outer_width, outer_height)
            reduction_ratio = 1
            x_offset = compsited_image.x_offset
            y_offset = compsited_image.y_offset
            outpainted_image = ImageCompister().composite(outpainted_image, np_image, x_offset, y_offset)
        else:
            reduction_ratio = outpainting_size / compsited_image.outer_image.shape[0]
            x_offset = int(compsited_image.x_offset * reduction_ratio)
            y_offset = int(compsited_image.y_offset * reduction_ratio)
        #############################################################
        if chop_image is True:
            chopped_image, x_offset, y_offset = ImageChoppingService().chop_according_to_mask(outpainted_image, mask, x_offset, y_offset)
        
        mask.relocate_smallest_box(reduction_ratio, x_offset, y_offset)
        
        result = {
            "result_image": {
                "image_data": chopped_image,
                "width": chopped_image.shape[1],
                "height": chopped_image.shape[0]
            },
            "original_x_offset": x_offset / chopped_image.shape[1],
            "original_y_offset": y_offset / chopped_image.shape[0],
            "mask": {
                "smallest_box_x": mask.smallest_box_x / chopped_image.shape[1],
                "smallest_box_y": mask.smallest_box_y / chopped_image.shape[0],
                "smallest_box_width": mask.smallest_box_width / chopped_image.shape[1],
                "smallest_box_height": mask.smallest_box_height / chopped_image.shape[0]
            }
        }

        return result
    