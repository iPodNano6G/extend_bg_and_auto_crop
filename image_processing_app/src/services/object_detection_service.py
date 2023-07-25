from services.api.object_detect_api import ObjectDetectAPI

class ObjectDetectionService:
    def detect_objects(self, image_bytes):

        objects = ObjectDetectAPI().detect_objects(image_bytes)
        
        results = {}
        for obj in objects:
            name = obj.name.lower()
            four_normalized_vertices_obj = obj.bounding_poly.normalized_vertices
            left = four_normalized_vertices_obj[0].x
            top = four_normalized_vertices_obj[0].y
            right = four_normalized_vertices_obj[2].x
            bottom = four_normalized_vertices_obj[2].y
            result = {
                "left": left,
                "top": top,
                "right": right,
                "bottom": bottom 
            }
            if name in results:
                results[name].append(result)
            else:
                results[name] = [result]

        return results
    