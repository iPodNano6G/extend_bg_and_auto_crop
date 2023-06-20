import cv2
import numpy as np
import onnxruntime
import os
import subprocess

from modules import fileManager, system

        
class ImageSaver:
    def saveImage(self, file_path, image, name = None):
        if name is None:
            name = "unlabeled.jpg"
            if os.path.isdir(file_path): # 입력 경로가 파일이 아니라 디렉터리일 경우, 
                file_path = os.path.dirname(file_path)
                save_path = os.path.join(file_path, name)
            else:
                file_path = os.path.dirname(file_path)
                save_path = os.path.join(file_path, name)
        else:
            if '.' not in name:
                name = name + ".jpg"
            if os.path.isdir(file_path): # 입력 경로가 파일이 아니라 디렉터리일 경우, 
                file_path = os.path.dirname(file_path)
                save_path = os.path.join(file_path, name)
            else:
                file_path = os.path.dirname(file_path)
                save_path = os.path.join(file_path, name)       
        print(save_path)     
        cv2.imwrite(save_path, image.cv_image)



class Image:
    def __init__(self, filepath, cv_image):
        if filepath is not None:
            self.filepath = os.path.abspath(filepath)
        if cv_image is not None:
            self.cv_image = cv_image
        else:
            img_array = np.fromfile(filepath, np.uint8)
            self.cv_image = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        self.height = self.cv_image.shape[0]
        self.width = self.cv_image.shape[1]
        self.url = None
    def setURL(self, url):
        self.url = url
class ImageFactory:
    def create_image(self,filepath, cv_image):
        image = Image(filepath, cv_image)
        return image

class Mask(Image):
    def __init__(self, filepath, cv_image):
        super().__init__(filepath, cv_image)
        smallest_box = self.calculate_smallest_box(self.cv_image)
        self.smallest_box_x = smallest_box[0]
        self.smallest_box_y = smallest_box[1]
        self.smallest_box_width = smallest_box[2]
        self.smallest_box_height = smallest_box[3]
    def calculate_smallest_box(self, mask):
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        # 모든 객체의 윤곽선을 하나의 리스트로 병합
        all_contours = np.concatenate(contours)
        # 윤곽선을 감싸는 최소 사각형 좌표 계산
        object_x, object_y, object_w, object_h = cv2.boundingRect(all_contours)
        return (object_x, object_y, object_w, object_h)
class MaskGenerator:
    def create_mask(self, image):
        model = onnxruntime.InferenceSession('unet.onnx')
        mask = cv2.resize(image.cv_image, (320, 320))
        mask = mask.transpose((2, 0, 1))  # 채널 순서 변경
        mask = mask.astype(np.float32) / 255.0  # 정규화
        mask = np.expand_dims(mask, axis=0)  # 배치 차원 추가
        # 모델 추론
        input_name = model.get_inputs()[0].name
        output_name = model.get_outputs()[0].name
        mask = model.run([output_name], {input_name: mask})[0]
        # 후처리
        mask = mask[0, 0, :, :]  # 배치와 채널 차원 제거
        mask = cv2.resize(mask, (image.width, image.height))  # 원래 크기로 복원. 이 마스크는 확장 영역을 선택할 때 쓰임.
        mask = (mask > 0.5).astype(np.uint8) * 255  # 이진화
        
        cv2.imwrite('mask.png', mask)
        mask_obj = Mask(None, mask)
        return mask_obj

class PaddedImage(Image):
    def __init__(self, filepath, cv_image, offset, ratio):
        super().__init__(filepath, cv_image)
        self.x_offset = offset[0]
        self.y_offset = offset[1]
        self.ratio = ratio

class PaddedImageFactory:
    def create_padded_image(self, image, mask, ratio):
        #객체의 긴 길이 구하기
        if mask.smallest_box_width > mask.smallest_box_height:
            longer = mask.smallest_box_width
        else:
            longer = mask.smallest_box_height

        transparent_bordered_image = cv2.cvtColor(image.cv_image, cv2.COLOR_RGB2RGBA)

        #인물의 객체의 긴 길이가 55%, 1024*1024에서 약 55%(550픽셀)을 차지하도록 설정
        new_width, new_height = int(image.width*ratio*10/longer), int(image.height*ratio*10/longer)
        transparent_bordered_image = cv2.resize(transparent_bordered_image, (new_width, new_height))

        transparent_image = np.zeros((1024, 1024, 4), dtype=np.uint8)
        x_offset = int((transparent_image.shape[1] - transparent_bordered_image.shape[1]) / 2)
        y_offset = int((transparent_image.shape[0] - transparent_bordered_image.shape[0]) / 2)

        transparent_image[y_offset:y_offset + transparent_bordered_image.shape[0], x_offset:x_offset + transparent_bordered_image.shape[1]] = transparent_bordered_image
        transparent_bordered_image = transparent_image

        padded_image = PaddedImage(None, transparent_bordered_image, (x_offset, y_offset), ratio)
        return padded_image
    
class DallEImage(PaddedImage):
    def __init__(self, filepath, cv_image, offset, ratio):
        super().__init__(filepath, cv_image, offset, ratio)
class Outpainter:
    def outpaintUsingDallE(self, imageDownloader, padded_image, image_path):
        if not isinstance(padded_image, PaddedImage):
            raise ValueError("Invalid input. Only objects of class PaddedImage are allowed.")
        
        from dotenv import load_dotenv
        import openai

        load_dotenv()
        openai.organization = os.getenv("ORG_ID")
        openai.api_key = os.getenv("API_KEY")

        cv2.imwrite("temp.png", padded_image.cv_image)
        outpainted = openai.Image.create_edit(
        image = open("temp.png", "rb"),
            prompt="photo of person",
            n=1,
            size="1024x1024"
        )
        image_url = outpainted.data[0]['url']

        folder_path = os.path.dirname(image_path)
        dallE_image_path = imageDownloader.download_image(image_url, folder_path, "DallE.png" )

        dallE_obj = DallEImage(dallE_image_path, None, (padded_image.x_offset,padded_image.y_offset), padded_image.ratio)

        return dallE_obj

class FeatheredImage(Image):
    def __init__(self, filepath, cv_image):
        super().__init__(filepath, cv_image)

class FeatheredImageFactory():
    def applyFeather(self, image):
        feather = cv2.cvtColor(image.cv_image, cv2.COLOR_BGR2BGRA)
        if image.height >= image.width:
            border_size = int(0.05 * image.height)
        else: 
            border_size = int(0.05 * image.width)
            
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
                x = int(image.width- border_size + radius * np.cos(radian))
                y = int(image.height - border_size + radius * np.sin(radian))
                feather[y, x][3] = int(255 - 255* radius/border_size)

            for angle in range(90, 180 + 1):
                radian = np.deg2rad(angle)
                x = int(border_size + radius * np.cos(radian))
                y = int(image.height- border_size + radius * np.sin(radian))
                feather[y, x][3] = int(255 - 255* radius/border_size)

            for angle in range(180, 270 + 1):
                radian = np.deg2rad(angle)
                x = int(border_size + radius * np.cos(radian))
                y = int(border_size + radius * np.sin(radian))
                feather[y, x][3] = int(255-255* radius/border_size)

            for angle in range(270, 360 + 1):
                radian = np.deg2rad(angle)
                x = int(image.width - border_size + radius * np.cos(radian))
                y = int(border_size + radius * np.sin(radian))
                feather[y, x][3] = int(255 - 255* radius/border_size)
        
        feathered_image_obj = FeatheredImage(None, feather)
        return feathered_image_obj

class AlphaCompositer:
    def alphaCompositingWithResizing(self, image, dallE_image):
        inner_width = dallE_image.width - 2 * dallE_image.x_offset
        inner_height = dallE_image.height - 2 * dallE_image.y_offset

        cv2.imwrite("temp_fearthered.png", image.cv_image)
        new_length = int(image.width / inner_width * dallE_image.width)
        result = cv2.resize(dallE_image.cv_image, (new_length, new_length))

        cv2.imwrite("temp_alpha.png", result)

        x_offset = int((new_length - image.width) / 2)
        y_offset = int((new_length - image.height) / 2)
        print(x_offset, y_offset)

        import platform
        system = platform.system()
        if system == 'Linux':
            magick_command = "./magick.appimage"
        elif system == 'Windows':
            magick_command = "magick"
        subprocess.run([magick_command,"composite", "-geometry", "+" + str(x_offset) + "+" +str(y_offset), "temp_fearthered.png", "temp_alpha.png",  "temp_alpha.png"])

        AlphaComposited_obj = PaddedImage("temp_alpha.png", None, (x_offset, y_offset), dallE_image.ratio)

        return AlphaComposited_obj
    



class ImageChopper:
    def chopInvadingBorderUsingMask(self, paddedImage, mask, image_path):
        print(paddedImage.x_offset,paddedImage.y_offset, mask.smallest_box_x, mask.smallest_box_y, mask.smallest_box_width, mask.smallest_box_height)
        object_move_x = paddedImage.x_offset
        object_move_y = paddedImage.y_offset


        magick_command = system.SystemChecker().returnMagickCommand()

        if mask.smallest_box_x == 0:
            subprocess.run([magick_command,"convert", "temp_alpha.png", "-gravity", "west", "-chop", (str(paddedImage.x_offset)+"x"+"0"), "temp_alpha.png"])
            object_move_x = 0
        if mask.smallest_box_y == 0:
            subprocess.run([magick_command,"convert", "temp_alpha.png", "-gravity", "north", "-chop", ("0"+"x"+str(paddedImage.y_offset)), "temp_alpha.png"])
            object_move_y = 0
        if mask.smallest_box_x + mask.smallest_box_width + 10 >= mask.width:
            subprocess.run([magick_command,"convert", "temp_alpha.png", "-gravity", "east", "-chop", (str(paddedImage.x_offset)+"x"+"0"), "temp_alpha.png"])
        if mask.smallest_box_y + mask.smallest_box_height + 10 >= mask.height:
            print(magick_command,"convert", "temp_alpha.png", "-gravity", "south", "-chop", ("0"+"x"+str(paddedImage.y_offset)), "temp_alpha.png")
            subprocess.run([magick_command,"convert", "temp_alpha.png", "-gravity", "south", "-chop", ("0"+"x"+str(paddedImage.y_offset)), "temp_alpha.png"])        
        '''
        folder_path = os.path.abspath(image_path)
        file_path = folder_path + "/result.png"
        os.remove(file_path)
        os.rename("temp_alpha.png", file_path)
        '''
        result = PaddedImage("temp_alpha.png", None, (object_move_x, object_move_y), None)

        return result
    

class ImageProcessor:
    def __init__(self):
        self.maskGenerator = MaskGenerator()
        self.paddedImageFactory = PaddedImageFactory()
        self.outpainter= Outpainter()
        self.featheredImageFactory = FeatheredImageFactory()
        self.alphaCompositer = AlphaCompositer()
        self.imageChopper = ImageChopper()
        self.imageDownloder = fileManager.ImageDownloader()
    def process(self, image):
        mask = self.maskGenerator.create_mask(image)
        padded_image = self.paddedImageFactory.create_padded_image(image, mask, 55)
        dallE_image = self.outpainter.outpaintUsingDallE(self.imageDownloder, padded_image, image.filepath)
        feathered_image = self.featheredImageFactory.applyFeather(image)
        resized_outpainted_image = self.alphaCompositer.alphaCompositingWithResizing(feathered_image, dallE_image)
        result_image = self.imageChopper.chopInvadingBorderUsingMask(resized_outpainted_image, mask, image.filepath)
        ImageSaver().saveImage(image.filepath, result_image, "result")
        return result_image
