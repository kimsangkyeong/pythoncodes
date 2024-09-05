import cv2
import numpy as np

# 원본 이미지 불러오기
original_image = cv2.imread("origin.jpg")
# full_path = 'D:\\origin.jpg'
# img_array = np.fromfile(full_path, np.uint8) # 컴퓨터가 읽을수 있게 이로 변환
# original_image = cv2.imdecode(img_array,  cv2.IMREAD_COLOR) #이미지를 읽어옴

# 이미지가 제대로 불러와졌는지 확인
if original_image is None:
    print("이미지를 불러오는데 실패했습니다. 경로를 확인하세요.")
else:
    # 이미지 크기 확인
    height, width = original_image.shape[:2]

    # 분할된 이미지 저장 경로
    output_paths = [
        "origin_part1.jpg",
        "origin_part2.jpg",
        "origin_part3.jpg",
        "origin_part4.jpg"
    ]

    # output_paths = [
    #     "origin_part1.jpg",
    #     "origin_part2.jpg",
    #     "origin_part3.jpg"
    # ]

    # # 이미지 3분할
    # images = [
    #     original_image[:height//3, :],  # 좌상단
    #     original_image[height//3:height//3 *2, :],  # 우상단
    #     original_image[height//3 *2:, :],  # 좌하단
    # ]
    # print("이미지 3분할 및 저장이 완료되었습니다.")

    # 이미지 4분할
    images = [
        original_image[:(height*4)//7, :(width*3)//5],  # 좌상단
        original_image[:(height*4)//7:, (width*2)//5:],  # 우상단
        original_image[(height*3)//7:, :(width*3)//5],  # 좌하단
        original_image[(height*3)//7:, (width*2)//5:]   # 우하단
    ]

    # 각 분할된 이미지 저장
    for idx, img in enumerate(images):
        cv2.imwrite(output_paths[idx], img)

    print("이미지 4분할 및 저장이 완료되었습니다.")