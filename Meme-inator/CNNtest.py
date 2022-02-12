# import imp
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
from sklearn import neighbors
import tensorflow as tf
# import copy

import unittest

from tensorflow.keras import datasets, layers, models

# (train_images, train_labels), (test_images, test_labels) = datasets.cifar10.load_data()
# print(train_images.shape)
# print(train_labels.shape)
# print(train_labels[0])
# print(train_labels[1])
# print(train_labels[2])
# Normalize pixel values to be between 0 and 1

nEPOCHS = 5

# nPHOTOS = 25
nPHOTOS = 3
# nVARIATIONSMEMES = 20
nVARIATIONSMEMES = 1

nPHOTOSTotal = nPHOTOS*nVARIATIONSMEMES

train_images = np.array([])
train_results = np.array([])

train_images = np.array([])
train_results = np.array([])
img0Pixels = None


def convertRegImageToRGBMasks(image: np.array):
    #image = 1D[ 2D[RGB[,,], RGB[,,], RGB[,,]...], 2D[], 2D[] ]
    d1Size = image.shape[0]
    d2Size = image.shape[1]
    d3Size = image.shape[2]
    newImage = np.array([])
    for color in range(d3Size):
        colorMask = np.array([])
        for dim1 in image:
            D1colorMask = np.array([])
            for dim2 in dim1:
                D1colorMask = np.append(D1colorMask, dim2[color])
            colorMask = np.append(colorMask, D1colorMask)
        newImage = np.append(newImage, colorMask)
    return newImage.reshape(d3Size,d1Size,d2Size)


def convertRGBMasksToRegImage(rgbImageMasks):
    imD1Size = rgbImageMasks.shape[1]
    imD2Size = rgbImageMasks.shape[2]
    imD3Size = rgbImageMasks.shape[0]

    regImage = np.empty( (imD1Size,imD2Size,imD3Size) )

    for color,colorMask in enumerate(rgbImageMasks):
        for i,colorMaskDim1 in enumerate(colorMask):
            for j,colorValue in enumerate(colorMaskDim1):
                regImage[i][j][color] = colorValue

    return regImage



for i in range(nPHOTOS): #prendre photos train
    # for j in range(nVARIATIONSMEMES):
    
    img = cv.imread(f'RESULTS/E_results{i}-0.jpeg')
    # img = cv.imread(f'RESULTS/results{i}.jpeg')
    imgPixels = np.array([img])
    # imgTemplate = cv.imread('TEMPLATE/200x200.png')
    imgTemplate = cv.imread(f'TEMPLATE_resize/Tem{i}.jpeg')
    imgTemplatePixels = np.array([imgTemplate])
    train_images = np.append(train_images, imgPixels)
    train_results = np.append(train_results, imgTemplatePixels)

test_images = np.array([img0Pixels])
test_results = np.array([imgTemplatePixels])

train_images = np.asarray(train_images).astype(np.float32)
train_results = np.asarray(train_results).astype(np.float32)
test_images = np.asarray(test_images).astype(np.float32)
test_results = np.asarray(test_results).astype(np.float32)


# print("-"*30)
# print("-"*30)
# print(train_images)
# print("-"*30)
# print("-"*30)

train_images, test_images = train_images / 255.0, test_images / 255.0
train_results, test_results = train_results / 255.0, test_results / 255.0

INPUT_DIM = 200*200*3
INPUT_TUPLE_DIM = (200,200,3)
model = models.Sequential()
model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=INPUT_TUPLE_DIM))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), activation='relu'))

model.add(layers.Flatten())
model.add(layers.Dense(64*3, activation='relu'))
model.add(layers.Dense(200*200, activation='relu'))

model.compile(optimizer='adam',
              loss=tf.keras.losses.MeanSquaredError(),
              metrics=['accuracy'])

print("GO")
train_images = np.reshape(train_images, (nPHOTOS,200,200,3))
train_results = np.reshape(train_results, (nPHOTOS,INPUT_DIM))
test_images = np.reshape(train_images, (nPHOTOS,200,200,3))
test_results = np.reshape(train_results, (nPHOTOS,INPUT_DIM))
print("SHAPEEEE : ")
print(train_images.shape)
print(train_results.shape)
# print(train_images.size)

model.summary()

history = model.fit(train_images, train_results, epochs=nEPOCHS
                ,validation_data=(test_images, test_results))

test_loss, test_acc = model.evaluate(test_images,  test_results, verbose=2)

print("-"*30)
print(test_acc)


prediction = model.predict(train_images)
affichagePrediction = np.array([prediction])
print("SHAPE prediction : ")
print(affichagePrediction.shape)
for i in range(nPHOTOS):
    # train_images = tf.keras.utils.normalize(train_images, axis=1)
    originalImage = train_images[i*nPHOTOS]
    plt.imshow(originalImage, cmap=plt.cm.binary)
    plt.show()
    # print(prediction.shape)
    # affichagePrediction = prediction
    imagePrediction = affichagePrediction[i]
    imagePrediction = imagePrediction.reshape((1,200,200,3))
    plt.imshow(imagePrediction, cmap=plt.cm.binary)
    # plt.show()


# prediction = model.predict(img0Pixels)
# plt.imshow(img0Pixels[0], cmap=plt.cm.binary)
# plt.show()
# print(prediction.shape)
# # affichagePrediction = np.array([prediction])
# affichagePrediction = prediction
# print("SHAPE 1:")
# print(affichagePrediction.shape)
# affichagePrediction = affichagePrediction.reshape((1,200,200,3))
# print("SHAPE 2:")
# print(affichagePrediction.shape)
# print(affichagePrediction)
# plt.imshow(affichagePrediction[0], cmap=plt.cm.binary)
# plt.show()

