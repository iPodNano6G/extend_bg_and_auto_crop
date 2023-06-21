import subprocess
from modules import photoshop
photoshop_path = "C:/Program Files/Adobe/Adobe Photoshop 2023/Photoshop.exe"
script_path = "C:\\SDP\\automated_image_processing\\back-end\\source_code\\modules\\remove_background.jsx"
file_path = "C:\\SDP\\automated_image_processing\\back-end\\source_code\\image_data\\ssfshop\\beanpole\\남녀공용 베이직 피케 티셔츠 - 블랙\\original.jpg"
photoshop = photoshop.Photoshop(photoshop_path)
photoshop.remove_background(file_path)
