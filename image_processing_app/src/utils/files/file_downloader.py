import requests
import os

class FileDownloader:
    def download_image(self, url, folder_path = '.', file_name = "downloaded_image.png"):
        response = requests.get(url)
        if response.status_code == 200:
            os.makedirs(folder_path, exist_ok=True)
            image_path = folder_path+"/"+file_name
            with open(image_path, 'wb') as file:
                file.write(response.content)
            return os.path.normpath(os.path.abspath(image_path))
        else:
            print(response.status_code)