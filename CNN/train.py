# import numpy as np
# # 
# import tensorflow as tf

# from keras import layers, models
# import matplotlib.pyplot as plt
# # 

# documents=np.load("dogs.npy")
# labels=np.load("dogs_labels.npy")

# s=np.arange(documents.shape[0])
# np.random.shuffle(s)
# documents=documents[s]
# labels=labels[s]

# # 
# num_classes=len(np.unique(labels))
# data_length=len(documents)
# split_index = int(0.75 * data_length)
# # 
# (x_train,x_test)=documents[:split_index],documents[split_index:]
# x_train = x_train.astype('float32')/255
# x_test = x_test.astype('float32')/255
# train_length=len(x_train)
# test_length=len(x_test)

# # 
# (y_train,y_test)=labels[:split_index],labels[split_index:]

# model = models.Sequential()
# model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(50, 50, 3)))
# model.add(layers.MaxPooling2D((2, 2)))
# model.add(layers.Conv2D(64, (3, 3), activation='relu'))
# model.add(layers.MaxPooling2D((2, 2)))
# model.add(layers.Conv2D(64, (3, 3), activation='relu'))

# model.summary()

# model.add(layers.Flatten())
# model.add(layers.Dense(64, activation='relu'))
# model.add(layers.Dense(10))

# model.summary()

# model.compile(optimizer='adam',
#               loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
#               metrics=['accuracy'])

# history = model.fit(x_train, y_train, epochs=100, 
#                     validation_data=(x_test, y_test))

# plt.plot(history.history['accuracy'], label='accuracy')
# plt.plot(history.history['val_accuracy'], label = 'val_accuracy')
# plt.xlabel('Epoch')
# plt.ylabel('Accuracy')
# plt.ylim([0.5, 1])
# plt.legend(loc='lower right')
# test_loss, test_acc = model.evaluate(x_test,  y_test, verbose=2)
# print(test_acc)
# model.save("dogs_model.keras")





# import os
# import numpy as np
# import tensorflow as tf
# from keras import layers, models
# import matplotlib.pyplot as plt
# from PIL import Image
# import cv2

# class GhanaCardClassifier:
#     def __init__(self, document_path, label_path, input_shape=(50, 50, 3)):
#         self.document_path = document_path
#         self.label_path = label_path
#         self.input_shape = input_shape
#         self.documents = np.load(self.document_path)
#         self.labels = np.load(self.label_path)
#         self.model = None
#         self.history = None
#         self.classnames = ['ghana_card', 'dogs']


#     def load_data(self):
#         print("888888888888888888888888")
#         self.documents = np.load(self.document_path)
#         self.labels = np.load(self.label_path)
#         s = np.arange(self.documents.shape[0])
#         # np.random.shuffle(s)
#         self.documents = self.documents[s]
#         self.labels = self.labels[s]
#         print(self.labels)
#         print(self.documents)

#     def preprocess_data(self, train_ratio=0.75):
#         print("99999999999999999999999999")
#         labels = np.load(self.label_path)
#         # plt.figure()
#         # plt.imshow(self.documents[0])
#         # plt.colorbar()
#         # plt.grid(False)
#         # plt.show()
#         data_length = len(self.documents)
#         print("!!!!!!!!!!!!!!!!!!!!!!!!")
#         print(self.documents)
#         split_index = int(train_ratio * data_length)
#         x_train, x_test = self.documents[:split_index], self.documents[split_index:]
#         y_train, y_test = self.labels[:split_index], self.labels[split_index:]
#         print(x_test.shape)
#         print(x_train.shape)
#         # y_train, y_test = self.labels[:split_index], self.labels[split_index:]
#         x_train = x_train / 255
#         x_test = x_test / 255
#         plt.figure(figsize=(10,10))
#         for i in range(10):
#             plt.subplot(5,5,i+1)
#             plt.xticks([])
#             plt.yticks([])
#             plt.grid(False)
#             plt.imshow(x_train[i], cmap=plt.cm.binary)
#             plt.xlabel(self.classnames[labels[i]])
#             print("333333333333333333333333")
#         plt.show()

#         return x_train, y_train, x_test, y_test

#     def build_model(self):
#         print("================================")
#         self.model = models.Sequential()
#         self.model.add(layers.Input(shape=(50, 50, 3)))
#         self.model.add(layers.Conv2D(32, (3, 3), activation='relu'))
#         self.model.add(layers.MaxPooling2D((2, 2)))
#         self.model.add(layers.Conv2D(64, (3, 3), activation='relu'))
#         self.model.add(layers.MaxPooling2D((2, 2)))
#         self.model.add(layers.Conv2D(64, (3, 3), activation='relu'))
#         self.model.add(layers.Flatten())
#         self.model.add(layers.Dense(64, activation='relu'))
#         self.model.add(layers.Dense(1, activation='sigmoid'))
#         self.model.summary()
#         # self.model = tf.keras.Sequential([
#         #     tf.keras.layers.Flatten(input_shape=(28, 28)),
#         #     tf.keras.layers.Dense(128, activation='relu'),
#         #     tf.keras.layers.Dense(10)
#         # ])

#         self.model.compile(optimizer='adam',
#               loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
#               metrics=['accuracy'])


#     def train_model(self, x_train, y_train, epochs=10):
#         print("--------------------------------")
#         self.model.fit(x_train, y_train, epochs=epochs)

#     def evaluate_model(self, x_test, y_test):
#         print("//////////////////////////")
#         test_loss, test_acc = self.model.evaluate(x_test, y_test, verbose=2)
#         print(f"Test accuracy: {test_acc}")
#         print(f"Test accuracy2: {test_loss}")
#         return test_acc

#     def save_model(self, filename):
#         print("aaaaaaaaaaaaaaaaaaaaaaaaaaa")
#         self.model.save(filename)

#     def load_model(self, filename):
#         print("xxxxxxxxxxxxxxxxxxxxxxxx")
#         self.model = models.load_model(filename)

#     def predict(self, image_path):
#         print("ccccccccccccccccccccccccc")
#         img = Image.open(image_path)
#         print(img)
#         resize_img = img.resize((50, 50))
#         print("llllllllllllllll")
        
#         probability_model = tf.keras.Sequential([self.model, 
#                                          tf.keras.layers.Softmax()])
#         prediction = probability_model.predict(resize_img)
#         print(prediction)

#         # img_array = np.expand_dims(img_array, axis=0)
#         # prediction = self.model.predict(img_array)
#         if prediction < 0.6:
#             print("The image is a valid Ghana card.")
#         else:
#             print("The image is not a valid Ghana card.")
            
            
#         # imag=cv2.imread(os.getcwd() +'/WhatsApp Image 2024-05-29 at 11.08.25.jpeg')
#         # print(imag)
#         # img_from_ar = Image.fromarray(imag, 'RGB')
#         # resized_image = img_from_ar.resize((50, 50))
#         # test_image =np.expand_dims(resized_image, axis=0) 
#         # model = tf.keras.models.load_model(os.getcwd() + '/ghana_card_model.keras')
#         # result = model.predict(test_image) 

# # Example usage:
# if __name__ == "__main__":
#     classifier = GhanaCardClassifier(document_path="documents.npy", label_path="labels.npy")
#     classifier.load_data()
#     x_train, x_test, y_train, y_test = classifier.preprocess_data()
#     classifier.build_model()
#     classifier.train_model(x_train, x_test, epochs=100)
#     # classifier.plot_accuracy()
#     classifier.evaluate_model(x_test, y_test)
#     classifier.save_model("documents_model.keras")

#     # To load the model and make predictions:
#     classifier.load_model("documents_model.keras")
#     classifier.predict(os.getcwd() +'/istockphoto-1853686056-170667a.webp')
