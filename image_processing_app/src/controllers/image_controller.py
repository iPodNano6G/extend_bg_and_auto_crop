from flask import Blueprint, request, jsonify

from services.aggregated_services.image_processing_service import ImageProcessingService
from utils.image.image_converter import ImageConverter

image_controller  = Blueprint('image', __name__)

@image_controller.route('/ProcessImage', methods=['POST'])
def process_image():
    ratio = int(request.args.get('ratio', 50))  # ratio 파라미터가 없으면 기본값 50 사용
    recover_size = request.args.get('recover_size', 'True').lower() == 'true'
    chop_image = request.args.get('chop_image', 'True').lower() == 'true'
    outpainting_size = int(request.args.get('outpainting_size', 1024))
    removed_border_pixel = int(request.args.get('removed_border_pixel', 2))
    image_bytes = request.files['image_data'].read()
    np_image = ImageConverter().convert_to_np_image(image_bytes)
    processed_np_image, x_offset, y_offset = ImageProcessingService().process(np_image, ratio, recover_size, chop_image, outpainting_size, removed_border_pixel)