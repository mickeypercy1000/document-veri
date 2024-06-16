# import os
# import cv2
# import pytesseract
# import numpy as np
# import pandas as pd
# from sklearn.model_selection import train_test_split
# from sklearn.ensemble import RandomForestClassifier
# from sklearn.metrics import classification_report, accuracy_score

# # Path to Tesseract executable
# pytesseract.pytesseract.tesseract_cmd = r'/usr/bin/tesseract'  # Update this path based on your Tesseract installation

# # Function to extract text and features from an image
# def extract_text_features(img_path):
#     img = cv2.imread(img_path)
#     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
#     # Extract text using Tesseract
#     d = pytesseract.image_to_data(gray, output_type=pytesseract.Output.DICT)
    
#     features = []
#     num_boxes = len(d['level'])
#     for i in range(num_boxes):
#         (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
#         text = d['text'][i]
#         conf = int(d['conf'][i])
        
#         if conf > 0:  # Consider only confident text extractions
#             font_size = h
#             features.append({
#                 'text': text,
#                 'x': x,
#                 'y': y,
#                 'w': w,
#                 'h': h,
#                 'font_size': font_size,
#                 'conf': conf
#             })
    
#     return features

# # Function to load dataset and extract features
# def load_data(data_dir, label):
#     data = []
#     labels = []
#     for img_name in os.listdir(data_dir):
#         img_path = os.path.join(data_dir, img_name)
#         features = extract_text_features(img_path)
#         for feature in features:
#             feature['label'] = label
#             data.append(feature)
#             labels.append(label)
#     return pd.DataFrame(data), np.array(labels)

# # Load dataset
# id_card_data_dir = 'path/to/id_card_images'
# non_id_card_data_dir = 'path/to/non_id_card_images'

# id_card_data, id_card_labels = load_data(id_card_data_dir, 1)
# non_id_card_data, non_id_card_labels = load_data(non_id_card_data_dir, 0)

# data = pd.concat([id_card_data, non_id_card_data], ignore_index=True)
# labels = np.concatenate([id_card_labels, non_id_card_labels])


# X = data[['x', 'y', 'w', 'h', 'font_size', 'conf']]
# y = labels

# # Split data into training and test sets
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# # Train a Random Forest Classifier
# clf = RandomForestClassifier(n_estimators=100, random_state=42)
# clf.fit(X_train, y_train)

# # Evaluate the model
# y_pred = clf.predict(X_test)
# print("Accuracy:", accuracy_score(y_test, y_pred))
# print(classification_report(y_test, y_pred))



# # Function to predict whether an image is a valid ID card
# def predict_id_card(model, img_path):
#     features = extract_text_features(img_path)
#     if not features:
#         return "Invalid ID Card"
    
#     feature_df = pd.DataFrame(features)
#     X = feature_df[['x', 'y', 'w', 'h', 'font_size', 'conf']]
#     predictions = model.predict(X)
    
#     if np.mean(predictions) > 0.5:
#         return "Valid ID Card"
#     else:
#         return "Invalid ID Card"

# # Example usage
# img_path = 'path/to/test/id_card_image.jpg'
# print(predict_id_card(clf, img_path))
