import onnxruntime
import cv2
import numpy as np

def generate_mask_of(original_image_cv):

    if type(original_image_cv) is str: #파일 경로를 입력했을 경우 처리
        original_image_cv = cv2.imread(original_image_cv)
    
    model = onnxruntime.InferenceSession('unet.onnx')

    original_height, original_width = original_image_cv.shape[0], original_image_cv.shape[1]

    mask = cv2.resize(original_image_cv, (320, 320))

    mask = mask.transpose((2, 0, 1))  # 채널 순서 변경
    mask = mask.astype(np.float32) / 255.0  # 정규화
    mask = np.expand_dims(mask, axis=0)  # 배치 차원 추가

    # 모델 추론
    input_name = model.get_inputs()[0].name
    output_name = model.get_outputs()[0].name
    mask = model.run([output_name], {input_name: mask})[0]

    # 후처리
    mask = mask[0, 0, :, :]  # 배치와 채널 차원 제거
    mask = cv2.resize(mask, (original_width, original_height))  # 원래 크기로 복원. 이 마스크는 확장 영역을 선택할 때 쓰임.
    mask = (mask > 0.5).astype(np.uint8) * 255  # 이진화
    #cv2.imwrite(folder_path+"/"+'mask.png', mask)

    box_dictionary = get_mask_box(mask)
    mask_dictionary = {
        "mask_image": mask,
        "box_x": box_dictionary["box_x"],
        "box_y": box_dictionary["box_y"],
        "box_w": box_dictionary["box_w"],
        "box_h": box_dictionary["box_h"]
    }
    return mask_dictionary

def get_mask_box(mask):
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # 모든 객체의 윤곽선을 하나의 리스트로 병합
    all_contours = np.concatenate(contours)
    # 윤곽선을 감싸는 최소 사각형 좌표 계산
    box_x, box_y, box_w, box_h = cv2.boundingRect(all_contours)
    # 왼쪽 위를 기준으로 (x,y) 좌표, w(너비)와 h(높이) 형태로 결과 출력
    box_dictionary = {
        "box_x": box_x,
        "box_y": box_y,
        "box_w": box_w,
        "box_h": box_h
    }
    return box_dictionary