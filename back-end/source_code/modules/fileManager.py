import requests
import os
import json

class ImageDownloader:
    def download_image(self, url, folder_path, file_name):
        response = requests.get(url)
        if response.status_code == 200:
            os.makedirs(folder_path, exist_ok=True)
            image_path = folder_path+"/"+file_name
            with open(image_path, 'wb') as file:
                file.write(response.content)
            return os.path.normpath(os.path.abspath(image_path))

class DocumentManager:
    def save_json_document(self, json_document, file_path):
        abs_path = os.path.abspath(file_path)
        absolute_folder_path = os.path.dirname(abs_path)
        # BSON으로 직렬화된 데이터를 파일에 저장
        json_path = absolute_folder_path+"\\data.json"
        with open(json_path, 'w', encoding='utf-8') as file:
            json.dump(json_document, file, ensure_ascii=False)
        return json_path
class JsonMaker:
    def make_json_for_clothes_data(self, orignalImage, imaga_url, finalImage, face, clothes, no_background_image_path):
        json_document = {
            "original_image": {
                "file_path": orignalImage.filepath,
                "url": imaga_url,
                "width": orignalImage.width,
                "height": orignalImage.height
            },
            "dalle_image": {
                "file_path": finalImage.filepath,
                "dalle_image_width": finalImage.width,
                "dalle_image_height": finalImage.height,
                "x_offset": finalImage.x_offset,
                "y_offset": finalImage.y_offset,
            },
            "face": {
                "left_line_pixel": face.left + finalImage.x_offset,
                "right_line_pixel": face.right + finalImage.x_offset,
                "top_line_pixel": face.top + finalImage.y_offset,
                "bottom_line_pixel": face.bottom + finalImage.y_offset,
            },
            "clothes": {
                "type_of_clothes": clothes.type_of_clothes,
                "left_line_pixel": clothes.left + finalImage.x_offset,
                "right_line_pixel": clothes.right + finalImage.x_offset,
                "top_line_pixel": clothes.top + finalImage.y_offset,
                "bottom_line_pixel": clothes.bottom + finalImage.y_offset,
            },
            "no_background": {
                "file_path": no_background_image_path.replace("\\\\", "\\")
            }
        }
        return json_document