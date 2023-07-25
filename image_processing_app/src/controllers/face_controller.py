from flask import Blueprint, request, jsonify

from services.face_detection_service import FaceDetectionService

face_controller = Blueprint('face', __name__)

@face_controller.route('/detectFaceLocation', methods=['POST'])
def detect_face_location():
    if 'image_data' not in request.files:
        return jsonify({'error': 'no image'}), 400
    image_bytes = request.files['image_data'].read()
    face_data_list = FaceDetectionService().detect_faces(image_bytes)
    return jsonify(face_data_list)

