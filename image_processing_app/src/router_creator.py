from controllers.face_controller import face_controller
from controllers.object_controller import object_controller
from controllers.image_controller import image_controller

def create_router(app):
    controllers = [face_controller, object_controller, image_controller]
    for controller in controllers:
        app.register_blueprint(controller)
    return app
