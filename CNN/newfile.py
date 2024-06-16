
# import os
# import numpy as np

# import tensorflow as tf
# from keras import layers, utils, models, losses
# # from tensorflow.python.keras.preprocessing.image import load_img, ImageDataGenerator
# import matplotlib.pyplot as plt
# import streamlit as st


# base_dir = 'CNN/documents'
# img_size = 180
# batch = 32

# train_ds = utils.image_dataset_from_directory( base_dir,
#                                                        seed = 123,
#                                                        validation_split=0.2,
#                                                        subset = 'training',
#                                                        batch_size=batch,
#                                                        image_size=(img_size,img_size))
# val_ds = utils.image_dataset_from_directory( base_dir,
#                                                        seed = 123,
#                                                        validation_split=0.2,
#                                                        subset = 'validation',
#                                                        batch_size=batch,
#                                                        image_size=(img_size,img_size))
# print("----------------------")
# document_name = train_ds.class_names

# AUTOTUNE = tf.data.AUTOTUNE
# train_ds = train_ds.cache().shuffle(1000).prefetch(buffer_size = AUTOTUNE)
# val_ds = val_ds.cache().prefetch(buffer_size = AUTOTUNE)

# # data_augmentation = models.Sequential([
# #     layers.RandomFlip("horizontal", input_shape = (img_size,img_size,3)),
# #     layers.RandomRotation(0.1),
# #     layers.RandomZoom(0.1)
# # ])

# model = models.Sequential([
#     # data_augmentation,
#     layers.Rescaling(1./255),
#     layers.Conv2D(16, 3, padding='same', activation='relu'),
#     layers.MaxPooling2D(),
#     layers.Conv2D(32, 3, padding='same', activation='relu'),
#     layers.MaxPooling2D(),
#     layers.Conv2D(64, 3, padding='same', activation='relu'),
#     layers.MaxPooling2D(),
#     layers.Dropout(0.2),
#     layers.Flatten(),
#     layers.Dense(128, activation='relu'),
#     layers.Dense(5)
# ])
# model.compile(optimizer='adam',
#               loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
#               metrics=['accuracy'])
# model.summary()
# history = model.fit(train_ds, epochs=10, validation_data=val_ds)

# def classify_images(image_path):
#     input_image = tf.keras.utils.load_img(image_path, target_size=(180,180))
#     input_image_array = tf.keras.utils.img_to_array(input_image)
#     input_image_exp_dim = tf.expand_dims(input_image_array,0)

#     predictions = model.predict(input_image_exp_dim)
#     print("///;;;;;;;;;;;;;;;;;;")
#     print(predictions)
#     result = tf.nn.softmax(predictions[0])
#     print(result)
#     print(document_name)
#     print(np.argmax(result))
#     print(np.max(result))
#     outcome = 'The Image is a valid ' + document_name[np.argmax(result)] + ' with an accuracy of '+ str(np.max(result)*100)
#     if (np.max(result)*100) < 100:
#         print("Image Invalid. Upload a new image...")
#     else:
        
#         print(outcome)
#     return outcome

#     predictions = model.predict(input_image_exp_dim)
#     print("///;;;;;;;;;;;;;;;;;;")
#     print(predictions)
#     result = tf.nn.softmax(predictions[0])
#     class_index = np.argmax(result)
#     document_names = train_ds.class_names
#     class_name = document_names[class_index]
#     confidence = result[class_index].numpy()
#     print(f"Predicted label: {class_name} with confidence: {confidence:.2f}")


# classify_images(os.getcwd() +'/gh_card.jpeg')

# # model.save('Documents.keras')
        
        
        
        