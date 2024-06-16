# import face_recognition
# import cv2
# import matplotlib.pyplot as plt
# import easyocr
# import os


# def load_and_encode_image(image1_path, image2_path):
    
#     # Load the image
#     image = face_recognition.load_image_file(image_path)
    
#     # Detect faces in the image
#     face_locations = face_recognition.face_locations(image)
    
#     if face_locations:
#         # Plot the detected face on the graph
#         for (top, right, bottom, left) in face_locations:
#             # Draw a rectangle around the face
#             cv2.rectangle(image, (left, top), (right, bottom), (0, 0, 255), 2)
        
#         image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
#         # Convert the image to RGB format for plotting
#         plt.imshow(image_rgb)
#         plt.axis('off')
#         plt.show()
#         reader = easyocr.Reader(['en', 'en'])
#         result = reader.readtext(image_rgb)
#         for (bbox, text, prob) in result:
#             print(f'Text: {text}, Probability: {prob}')

#         # Transforming the detected face into an encoded form
#         face_encodings = face_recognition.face_encodings(image_rgb, face_locations)
#         print(f'Face Encodings: {face_encodings}')
#         print(f'Face Encodings: {face_encodings[0]}')
#         return face_encodings[0]
#     else:
#         raise ValueError("No face found in the image.")


# def compare_faces(encoding1, encoding2, tolerance=0.4):
#     # Compare the facial encodings
#     results = face_recognition.compare_faces([encoding1], encoding2, tolerance=tolerance)
#     return results[0]

# # Paths to the ID card image and passport-size picture
# id_card_image_path = f"{os.getcwd()}/CNN/documents/cards/WhatsApp Image 2024-06-02 at 10.31.55 (1).jpeg"
# passport_image_path = f"{os.getcwd()}/CNN/documents/cards/Screenshot 2024-06-05 at 6.53.52 AM.png"

# try:
#     # Encode the faces
#     id_card_face_encoding = load_and_encode_image(id_card_image_path)
#     passport_face_encoding = load_and_encode_image(passport_image_path)

#     # Compare the faces
#     match = compare_faces(id_card_face_encoding, passport_face_encoding)
    
#     if match:
#         print("The faces match.")
#     else:
#         print("The faces do not match.")
# except ValueError as e:
#     print(e)
