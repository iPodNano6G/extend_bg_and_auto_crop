import image_downloader
import mask_processor
import outpainting_processor

import os
import sys
import json

import cv2

with open(sys.argv[1], 'r') as file:
    shoppingmall_data = json.load(file)

ratio = 0
new_folder = shoppingmall_data["seller"]+"/"+shoppingmall_data["brand"]
os.makedirs(new_folder, exist_ok=True)

for data in shoppingmall_data["image_list"]:
    image_url = data["image_url"]
    folder_name = new_folder+"/"+data["product_name"]
    original_image_path = image_downloader.download_image(image_url, folder_name, "original.jpg")
    mask = mask_processor.generate_mask_of(original_image_path)
    transparent_bordered_image = outpainting_processor.make_transparent_border(original_image_path, mask, ratio)
    dallE_image_path = outpainting_processor.outpaint_image_with_DallE(transparent_bordered_image, folder_name)

    outpainting_processor.recover_orignal_image_size(original_image_path, dallE_image_path, transparent_bordered_image, ratio)