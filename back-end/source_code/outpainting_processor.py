import mask_processor
import cv2
import numpy as np
from dotenv import load_dotenv
import os
import openai
import image_downloader

def outpaint_image_with_DallE(bordered_image, folder_name):

    load_dotenv()
    openai.organization = os.getenv("ORG_ID")
    openai.api_key = os.getenv("API_KEY")

    cv2.imwrite("temp.png", bordered_image["transparent_bordered_image"])
    outpainted = openai.Image.create_edit(
    image = open("temp.png", "rb"),
        prompt="photo of person",
        n=1,
        size="1024x1024"
    )
    image_url = outpainted.data[0]['url']
    DallE_image_path = image_downloader.download_image(image_url, folder_name, "DallE.png" )
    return DallE_image_path

def apply_feather(original_image_path):
    if type(original_image_path) is str:
        original = cv2.imread(original_image_path)
    feather = cv2.cvtColor(original, cv2.COLOR_BGR2BGRA)
    original_height = feather.shape[0]
    original_width = feather.shape[1]

    if feather.shape[0] >= original_width:
        border_size = int(0.05 * original_height)
    else: 
        border_size = int(0.05 * original_width)
        
    for i in range(border_size):
        feather[ i,:, 3] = int(255* i/border_size)
        feather[-i,:, 3] = int(255* i/border_size)
        feather[:, i, 3] = int(255* i/border_size)
        feather[:,-i, 3] = int(255* i/border_size)

        feather[:border_size , :border_size, 3] = 0
        feather[:border_size , -border_size:, 3] = 0
        feather[-border_size:, -border_size:, 3] = 0
        feather[-border_size:, :border_size, 3] = 0

    for radius in range(0, border_size):
        for angle in range(0, 90 + 1):
            radian = np.deg2rad(angle)
            x = int(original_width- border_size + radius * np.cos(radian))
            y = int(original_height- border_size + radius * np.sin(radian))
            feather[y, x][3] = int(255 - 255* radius/border_size)

        for angle in range(90, 180 + 1):
            radian = np.deg2rad(angle)
            x = int(border_size + radius * np.cos(radian))
            y = int(original_height- border_size + radius * np.sin(radian))
            feather[y, x][3] = int(255 - 255* radius/border_size)

        for angle in range(180, 270 + 1):
            radian = np.deg2rad(angle)
            x = int(border_size + radius * np.cos(radian))
            y = int(border_size + radius * np.sin(radian))
            feather[y, x][3] = int(255-255* radius/border_size)

        for angle in range(270, 360 + 1):
            radian = np.deg2rad(angle)
            x = int(original_width - border_size + radius * np.cos(radian))
            y = int(border_size + radius * np.sin(radian))
            feather[y, x][3] = int(255 - 255* radius/border_size)

    return feather



def recover_orignal_image_size(original_image_path, dallE_image_path, transparent_bordered_image, ratio):
    feather = apply_feather(original_image_path)
    # 아웃 페인팅 위에 기존 이미지 올리기
    ## 반투명 처리된 이미지 이용

    result = cv2.imread(dallE_image_path)
    new_length = int(1024*longer/ratio)
    result = cv2.resize(result, (new_length, new_length))

    cv2.imwrite(folder_path+"/"+"alpha_compistion.png", result)

    x_offset = int((new_length  - original_width) / 2)
    y_offset = int((new_length  - original_height) / 2)
    subprocess.run(["./magick.appimage","composite", "-geometry", "+" + str(x_offset) + "+" +str(y_offset), folder_path+"/"+"feather.png", folder_path+"/"+"alpha_compistion.png", folder_path+"/"+"alpha_compistion.png"])



def make_transparent_border(original_image_cv, mask, ratio):

    if type(original_image_cv) is str:
        original_image_cv = cv2.imread(original_image_cv)

    transparent_bordered_image = cv2.cvtColor(original_image_cv, cv2.COLOR_RGB2RGBA)

    #객체의 긴 길이 구하기

    box_w, box_h = mask["box_w"], mask["box_h"]
    if box_w > box_h:
        longer = box_w
    else:
        longer = box_h

    #인물의 객체의 긴 길이가 55%, 1024*1024에서 55%(550픽셀)을 차지하도록 설정
    new_width, new_height = int(transparent_bordered_image.shape[1]*ratio*10/longer), int(transparent_bordered_image.shape[0]*ratio*10/longer)
    transparent_bordered_image = cv2.resize(transparent_bordered_image, (new_width, new_height))

    transparent_image = np.zeros((1024, 1024, 4), dtype=np.uint8)
    x_offset = int((transparent_image.shape[1] - transparent_bordered_image.shape[1]) / 2)
    y_offset = int((transparent_image.shape[0] - transparent_bordered_image.shape[0]) / 2)

    transparent_image[y_offset:y_offset + transparent_bordered_image.shape[0], x_offset:x_offset + transparent_bordered_image.shape[1]] = transparent_bordered_image
    transparent_bordered_image = transparent_image

    transparent_bordered_image_dictionary = {
        "transparent_bordered_image": transparent_bordered_image,
        "x_offset": x_offset,
        "y_offset": y_offset
    }
    return transparent_bordered_image_dictionary

