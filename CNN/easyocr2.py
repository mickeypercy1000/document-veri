# import cv2
# import easyocr
# import matplotlib.pyplot as plt
# import os

# def draw_bounding_boxes(image, detections, threshold=0.25):

#     for bbox, text, score in detections:

#         if score > threshold:

#             cv2.rectangle(image, tuple(map(int, bbox[0])), tuple(map(int, bbox[2])), (0, 255, 0), 5)

#             cv2.putText(image, text, tuple(map(int, bbox[0])), cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.65, (255, 0, 0), 2)

# image_path = f"{os.getcwd()}/CNN/documents/cards/WhatsApp Image 2024-06-02 at 10.31.55 (1).jpeg"
# img = cv2.imread(image_path)

# if img is None:
#     raise ValueError("Error loading the image. Please check the file path.")

# img = cv2.imread(image_path)
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# reader = easyocr.Reader(['en', 'en'])
# result = reader.readtext(gray)
# print(result)
# for (bbox, text, prob) in result:
#     (top_left, top_right, bottom_right, bottom_left) = bbox
#     print(f'Text: {text}, Probability: {prob}')

