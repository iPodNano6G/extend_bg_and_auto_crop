import os
import json
import subprocess
def cropPanorama_noFace(json_data, name, ratio = 1):
    image_path = json_data["dalle_image"]["file_path"].replace("\\\\", "/")
    clothes_top = json_data["clothes"]["top_line_pixel"]
    clothes_bottom = json_data["clothes"]["bottom_line_pixel"]
    crop_height = (clothes_bottom - clothes_top)
    crop_height = int(ratio * crop_height)
    subprocess.run(
    ["magick",
     "convert", image_path,
     "-crop", ("x" + str(crop_height) + "+" + str(0) + "+" + str(clothes_top)),
     name]
    )

def cropPanorama_withFace(json_data, name, ratio = 1, face_ratio = 1):
    image_path = json_data["dalle_image"]["file_path"].replace("\\\\", "/")

    clothes_top = json_data["clothes"]["top_line_pixel"]
    clothes_bottom = json_data["clothes"]["bottom_line_pixel"]

    face_top = json_data["face"]["top_line_pixel"]

    crop_height = (clothes_bottom - face_top)
    crop_height = int(ratio * crop_height)
    subprocess.run(
    ["magick",
     "convert", image_path,
     "-crop", ("x" + str(crop_height) + "+" + str(0) + "+" + str(face_top)),
     name]
    )


def compare_data(data, key1, value):
    for item in data:
        if key1 in item:
            if item["url"] == value:
                return True

def search_json_files(folder_name):
    json_list =[]
    for root, dirs, files in os.walk(folder_name):
        for file in files:
            if file == "data.json":
                file_path = os.path.join(root, file)
                with open(file_path, encoding='utf-8') as json_file:
                    data = json.load(json_file)
                    # 여기에서 data에 대한 원하는 작업을 수행합니다.
                    json_list.append(data)  # 예시로 데이터를 출력합니다.
    return json_list

json_list = search_json_files("back-end\\source_code\\image_data\\ssfshop\\beanpole")

url = "https://img.ssfshop.com/cmd/LB_750x1000/src/https://img.ssfshop.com/goods/BPBR/23/05/31/GM0023053161909_0_THNAIL_ORGINL_20230602103740739.jpg"
for json_data in json_list:
    original_image = json_data.get("original_image")
    if original_image and original_image.get("url") == url:
        break

cropPanorama_noFace(json_data, "response_panorama_1.0.png")
cropPanorama_noFace(json_data, "response_panorama_1.5.png", 1.5)
cropPanorama_withFace(json_data, "response_panorama_withFace_1.0.png", face_ratio= 1)
cropPanorama_withFace(json_data, "response_panorama_withFace_1.15.png", face_ratio= 1.15)
cropPanorama_withFace(json_data, "response_panorama_withFace_1.3.png", face_ratio= 1.3)








