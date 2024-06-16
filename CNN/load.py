# import os
# import cv2
# from PIL import Image
# import numpy as np

# from verify_document.types import IDTypes


# def load_images():

#     data=[]
#     labels=[]

#     # Ghana Card 0
#     ghana_card = os.listdir(os.getcwd() + "/CNN/documents/ghana_card")
#     for card in ghana_card:
#         card_image=cv2.imread(os.getcwd() + "/CNN/documents/ghana_card/" + card)
#         img_from_card = Image.fromarray(card_image, 'RGB')
#         resized_image = img_from_card.resize((50, 50))
#         data.append(np.array(resized_image))
#         labels.append(0)

#     # Dog 1
#     dogs = os.listdir(os.getcwd() + "/CNN/documents/dogs/")
#     for dog in dogs:
#         dog_image=cv2.imread(os.getcwd() + "/CNN/documents/dogs/" + dog)
#         img_from_dog = Image.fromarray(dog_image, 'RGB')
#         resized_image = img_from_dog.resize((50, 50))
#         data.append(np.array(resized_image))
#         labels.append(1)
        
#     # Cats 3
#     cats = os.listdir(os.getcwd() + "/CNN/documents/dogs/")
#     for cat in cats:
#         cat_image=cv2.imread(os.getcwd() + "/CNN/documents/dogs/" + cat)
#         img_from_cat = Image.fromarray(cat_image, 'RGB')
#         resized_image = img_from_cat.resize((50, 50))
#         data.append(np.array(resized_image))
#         labels.append(2)

#     documents=np.array(data)
#     s = np.arange(documents.shape[0])
#     shuffled = np.random.shuffle(s)
#     labels=np.array(labels)
#     #
#     np.save("documents",shuffled)
#     np.save("labels",labels)
    
# load_images()






# # import os
# # import cv2
# # from PIL import Image
# # import numpy as np

# # # from verify_document.types import IDTypes

# # class LoadImages:
# #     def __init__(self):
# #         self.data = []
# #         self.labels = []

# #     def load_ghana_card_images(self):

# #         # data=[]
# #         # labels=[]

# #         ghana_card = os.listdir(os.getcwd() + "/CNN/documents/ghana_card/")
# #         for card in ghana_card:
# #             imag=cv2.imread(os.getcwd() + "/CNN/documents/ghana_card/" + card)
# #             img_from_ar = Image.fromarray(imag, 'RGB')
# #             resized_image = img_from_ar.resize((50, 50))
# #             self.data.append(np.array(resized_image))
# #             self.labels.append(0)
        
# #         documents=np.array(self.data)
# #         labels=np.array(self.labels)
# #         #
# #         np.save("ghana_cards",documents)
# #         np.save("ghana_card_labels",labels)


# #     # Dog 1
# #     def load_dogs(self):
# #         dogs = os.listdir(os.getcwd() + "/CNN/documents/dogs/")
# #         for dog in dogs:
# #             imag=cv2.imread(os.getcwd() + "/CNN/documents/dogs/" + dog)
# #             img_from_ar = Image.fromarray(imag, 'RGB')
# #             resized_image = img_from_ar.resize((50, 50))
# #             self.data.append(np.array(resized_image))
# #             self.labels.append(1)

# #         documents=np.array(self.data)
# #         labels=np.array(self.labels)
# #         #
# #         np.save("dogs",documents)
# #         np.save("dogs_labels",labels)


# # loader = LoadImages()

# # # Load Ghana Card images
# # loader.load_ghana_card_images()

# # # Load Dog images
# # loader.load_dogs()