from flask import Blueprint, request, jsonify

from services.object_detection_service import ObjectDetectionService

object_controller = Blueprint('object', __name__)

@object_controller.route('/detectObjectLocation', methods=['POST'])
def detect_object_location():
    if 'image_data' not in request.files:
        return jsonify({'error': 'no image'}), 400
    
    image_bytes = request.files['image_data'].read()

    object_data_list = ObjectDetectionService().detect_objects(image_bytes)
    return jsonify(object_data_list)