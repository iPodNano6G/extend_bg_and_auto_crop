import onnxruntime
import cv2
import numpy as np

class MaskDetector:
    def detect_mask(self, np_image):
        model = onnxruntime.InferenceSession("../static/model_weight/unet.onnx")
        mask = cv2.resize(np_image, (320, 320))
        mask = mask.transpose((2, 0, 1))  # 채널 순서 변경
        mask = mask.astype(np.float32) / 255.0  # 정규화
        mask = np.expand_dims(mask, axis=0)  # 배치 차원 추가
        # 모델 추론
        input_name = model.get_inputs()[0].name
        output_name = model.get_outputs()[0].name
        mask = model.run([output_name], {input_name: mask})[0]
        # 후처리
        mask = mask[0, 0, :, :]  # 배치와 채널 차원 제거
        mask = cv2.resize(mask, (np_image.shape[1], np_image.shape[0]))  # 원래 크기로 복원. 이 마스크는 확장 영역을 선택할 때 쓰임.
        mask = (mask > 0.5).astype(np.uint8) * 255  # 이진화

        return mask