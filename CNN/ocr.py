# import os
# from PIL import Image
# import cv2
# import pytesseract as pt
# from rembg import remove
# import matplotlib.pyplot as plt

# import torch
# import easyocr
# import os


# # image_for_training = f"{os.getcwd()}/CNN/documents/cards/51sfEPwpsYL._AC_UF1000,1000_QL80_.jpg"
# # img = cv2.imread(image_for_training)
# # gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


# # # GRAY IMAGE
# # thresh, image_bw = cv2.threshold(gray_image, 70, 50, cv2.THRESH_BINARY)
# # cv2.imwrite("CNN/documents/cards/gray_image.jpeg", gray_image)
# # print("Loading")
# # ocr_image = pt.image_to_string("CNN/documents/cards/gray_image.jpeg")
# # print(ocr_image)


# # import os
# # from PIL import Image
# # import cv2
# # import pytesseract as pt
# # from rembg import remove
# # import matplotlib.pyplot as plt
# # import numpy as np

# # image_for_training = f"{os.getcwd()}/CNN/documents/cards/WhatsApp Image 2024-05-28 at 12.23.24.jpeg"
# # img = cv2.imread(image_for_training)
# # gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# # thresh, image_bw = cv2.threshold(gray_image, 70, 100, cv2.THRESH_BINARY)
# # plt.imshow(image_bw)
# # plt.show()

# # cv2.imwrite("CNN/documents/cards/gray_image.jpeg", image_bw)
# # print("Loading")
# # ocr_image = pt.image_to_string("CNN/documents/cards/gray_image.jpeg")
# # print(ocr_image)





# # reader = easyocr.Reader(['en', 'en'])
# # img_text = reader.readtext(f"{os.getcwd()}/CNN/documents/cards/text3.jpg")
# # final_text = ""

# # for _, text, __ in img_text: # _ = bounding box, text = text and __ = confident level
# #     final_text += " "
# #     final_text += text
# # print(final_text)




# import cv2
# import easyocr
# import matplotlib.pyplot as plt
# import os

# def draw_bounding_boxes(image, detections, threshold=0.25):
#     for bbox, text, score in detections:
#         if score > threshold:
#             cv2.rectangle(image, tuple(map(int, bbox[0])), tuple(map(int, bbox[2])), (0, 255, 0), 5)
#             cv2.putText(image, text, tuple(map(int, bbox[0])), cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.65, (255, 0, 0), 2)

# def find_id_card(detections, keywords):
#     for bbox, text, score in detections:
#         if any(keyword.lower() in text.lower() for keyword in keywords):
#             return bbox
#     return None

# def crop_and_resize(image, bbox, scale=2.0):
#     x_min = int(min([point[0] for point in bbox]))
#     y_min = int(min([point[1] for point in bbox]))
#     x_max = int(max([point[0] for point in bbox]))
#     y_max = int(max([point[1] for point in bbox]))

#     cropped = image[y_min:y_max, x_min:x_max]
#     resized = cv2.resize(cropped, (0, 0), fx=scale, fy=scale)
#     return resized

# image_path = f"{os.getcwd()}/CNN/documents/cards/WhatsApp Image 2024-06-02 at 10.31.54 (2).jpeg"
# img = cv2.imread(image_path)

# if img is None:
#     raise ValueError("Error loading the image. Please check the file path.")

# reader = easyocr.Reader(['en'])
# text_detections = reader.readtext(img)
# threshold = 0.25

# # Draw bounding boxes on the image
# draw_bounding_boxes(img, text_detections, threshold)

# # Identify the ID card based on keywords
# keywords = ['ECOWAS', 'IDENTITY', 'CARD']
# id_card_bbox = find_id_card(text_detections, keywords)

# if id_card_bbox:
#     # Crop and resize the ID card
#     resized_id_card = crop_and_resize(img, id_card_bbox, scale=2.0)

#     # Display the resized ID card
#     plt.imshow(cv2.cvtColor(resized_id_card, cv2.COLOR_BGR2RGBA))
#     plt.axis('off')
#     plt.show()
# else:
#     print("No ID card found in the image.")

# # Display the original image with bounding boxes
# plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGBA))
# plt.axis('off')
# plt.show()
