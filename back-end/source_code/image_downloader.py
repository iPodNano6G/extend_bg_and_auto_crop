import requests
import original_image
import os

def download_image(url, folder_path, file_name):
    response = requests.get(url)
    if response.status_code == 200:
        os.makedirs(folder_path, exist_ok=True)
        image_path = folder_path+"/"+file_name
        with open(image_path, 'wb') as file:
            file.write(response.content)
        return image_path