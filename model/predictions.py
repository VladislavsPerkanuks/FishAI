from keras.models import load_model
from PIL import Image, ImageOps
import numpy as np

model = load_model('model/keras_model.h5', compile=False)
def predict(bilde):
    # Load the model


    # Create the array of the right shape to feed into the keras model
    # The 'length' or number of images you can put into the array is
    # determined by the first position in the shape tuple, in this case 1.
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    # Replace this with the path to your image
    image = Image.open(bilde)
    # resize the image to a 224x224 with the same strategy as in TM2:
    # resizing the image to be at least 224x224 and then cropping from the center
    size = (224, 224)
    image = ImageOps.fit(image, size, Image.ANTIALIAS)

    # turn the image into a numpy array
    image_array = np.asarray(image)
    # Normalize the image
    normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
    # Load the image into the array
    data[0] = normalized_image_array

    # run the inference
    prediction = model.predict(data)
    labels = ['European perch', 'Carp', 'Salmon', 'North Pike', 'European river lamprey', 'Baltic herring',
              'European eel']
    predict_dict = {}

    prediction = [val for sbulist in prediction for val in sbulist]

    for label, predict1 in zip(labels, prediction):
        predict_dict[label] = round(predict1 * 100,1)

    sort_orders = sorted(predict_dict.items(), key=lambda x: x[1], reverse=True)

    return np.array(sort_orders).tolist()
