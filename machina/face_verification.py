from io import BytesIO
import cv2
# from deepface import DeepFace
from pprint import pprint
import requests
from rest_framework.response import Response
from PIL import Image
import numpy as np
from passporteye import read_mrz
import easyocr
import matplotlib.pyplot as plt
import face_recognition

def get_face_encoding(image):
    # Detect face in the image
    face_locations = face_recognition.face_locations(image)
    if not face_locations:
        raise ValueError("No face detected in the image")

    # Get the face encoding for the first detected face
    face_encoding = face_recognition.face_encodings(image, known_face_locations=face_locations)[0]
    return face_encoding


class VerificationsAndValidations:
        
    @staticmethod
    def compare_images(image1_path, image2_path):
        if not image1_path and image2_path:
            return Response({"status": False, "message": "Ensure both images for verification are present"})
        try:
            if image1_path.startswith('http') or image2_path.startswith('http'):         
                image1 = requests.get(image1_path)
                image2 = requests.get(image2_path)

                if image1.status_code == 200 and image2.status_code == 200:
                    image1_response = Image.open(BytesIO(image1.content))
                    image2_response = Image.open(BytesIO(image2.content))
                    image1_cv = cv2.cvtColor(np.array(image1_response), cv2.COLOR_RGB2BGR)
                    image2_cv = cv2.cvtColor(np.array(image2_response), cv2.COLOR_RGB2BGR)
                else:
                    print("Failed to retrieve the image from the URL.")
                    return "Failed to retrieve the image from the URL."
            else:
                image1_cv = cv2.imread(image1)
                image2_cv = cv2.imread(image2)
                
            # Get face encodings
            encoding1 = get_face_encoding(image1_cv)
            encoding2 = get_face_encoding(image2_cv)
            result = face_recognition.compare_faces([encoding1], encoding2, tolerance=0.7)
            # result = DeepFace.verify(image1_cv, image2_cv)
            print(result[0])
            return result[0]
        except Exception as e:
            print({"message": str(e)})
            return str(e)
    
    @staticmethod  
    def extract_text(ghana_card_back):
        print("extracting...........")
        print(ghana_card_back)
        try:
            # if ghana_card_back.startswith('http'):         
            #     print("yessssss")            
            #     image1 = requests.get(ghana_card_back)
            #     if image1.status_code == 200:
            #         image1_response = Image.open(BytesIO(image1.content))
            #         image1_cv = cv2.cvtColor(np.array(image1_response), cv2.COLOR_RGB2BGR)
            #         print("mmmmmmmmm")
            #         print(image1_cv)
            #     else:
            #         print("Failed to retrieve the image from the URL.")
            #         return "Failed to retrieve the image from the URL."
            # gray = cv2.cvtColor(ghana_card_back, cv2.COLOR_BGR2GRAY)
            # print("=========================")
            # reader = easyocr.Reader(['en', 'en'])
            # result = reader.readtext(gray)
            # print(":::::::::::::::::::::::::::::")
            # for (bbox, text, prob) in result:
            #     print(f'Text: {text}, Probability: {prob}')
            mrz = read_mrz(ghana_card_back)
            if mrz is None:
                print("Upload a clear picture of the back of the Ghana Card.")
                return None
            mrz_data = mrz.to_dict()

            return mrz_data
        except Exception as e:
            print(f"An error occurred: {e}")
            return None

