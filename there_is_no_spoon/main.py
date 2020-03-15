"""
This code is greatly inspired by Adam Geitgey  and more precisely his following awesome article:
https://algotravelling.com/en/machine-learning-fun-part-8/
"""
import json
import os
import sys
import time

import numpy as np
from PIL import Image
from keras import backend as K
from keras.applications import inception_v3
from keras.preprocessing import image
from tqdm import tqdm

from there_is_no_spoon.utils import get_options

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import tensorflow as tf


def image_formatter(input_path):
    print("Formatting input image...")
    img = image.load_img(input_path, target_size=(299, 299))
    original_image = image.img_to_array(img)
    # Scale the image so all pixel intensities are between [-1, 1] as the model expects
    original_image /= 255.
    original_image -= 0.5
    original_image *= 2.
    # Add a 4th dimension for batch size (as Keras expects)
    original_image = np.expand_dims(original_image, axis=0)
    return original_image


def image_descaler(image_to_descale):
    img_descaled = image_to_descale[0]
    img_descaled /= 2.
    img_descaled += 0.5
    img_descaled *= 255.
    return img_descaled


def there_is_no_spoon(input_path, output_path, target_score, target_class, max_change, learning_rate):
    with open('imagenet_class_index.json') as f:
        imagenet_class_index = json.load(f)

    model = inception_v3.InceptionV3()
    model_input_layer = model.layers[0].input
    model_output_layer = model.layers[-1].output

    # Choose an ImageNet object to fake
    # The list of classes is available here: https://gist.github.com/ageitgey/4e1342c10a71981d0b491e1b8227328b
    object_type_to_fake = target_class

    formatted_image = image_formatter(input_path)
    prediction = model.predict(formatted_image)
    predicted_classes = inception_v3.decode_predictions(prediction, top=1)
    imagenet_id, name, confidence = predicted_classes[0][0]
    print("The input image is classified as {} with {:.4}% confidence.".format(name, confidence * 100))
    # Pre-calculate the maximum change the adversarial image is allowed so it doesn't look funny
    # A larger number produces an image faster but risks more distortion.
    max_change_above = formatted_image + max_change
    max_change_below = formatted_image - max_change

    adversarial_image = np.copy(formatted_image)

    # The 'cost' will be the likelihood that the image is the target class according to the pre-trained model
    cost_function = model_output_layer[0, object_type_to_fake]

    # The gradient based on the input image and the currently predicted class
    gradient_function = K.gradients(cost_function, model_input_layer)[0]

    # Create a Keras function that we can call to calculate the current cost and gradient
    grab_cost_and_gradients_from_model = K.function([model_input_layer, K.learning_phase()],
                                                    [cost_function, gradient_function])

    target_name = imagenet_class_index[str(target_class)][1]
    print(
        "Now let's transform your {} into a {} ! This step can take a while depending on your machine (from minutes "
        "to hours)".format(
            name, target_name), end='\n')
    cost = 0.0
    i = 0
    progress_bar = tqdm(total=target_score * 100)
    while cost < target_score:
        i += 1
        # This loop keeps adjusting the adversarial image slightly so that it tricks the model more and more
        cost, gradients = grab_cost_and_gradients_from_model([adversarial_image, 0])

        # Move the adversarial image one step further towards the target class
        adversarial_image += gradients * learning_rate

        # Ensure that the image doesn't ever change too much to either look funny or to become an invalid image
        adversarial_image = np.clip(adversarial_image, max_change_below, max_change_above)
        adversarial_image = np.clip(adversarial_image, -1.0, 1.0)

        if i % 10 == 0:
            time.sleep(0.1)
            progress_bar.update(cost * 100)
    progress_bar.close()

    descaled_image = image_descaler(adversarial_image[0])

    img = Image.fromarray(descaled_image.astype(np.uint8))
    img.save(output_path)


def main():
    options = get_options(sys.argv[1:])
    there_is_no_spoon(input_path=options.input, output_path=options.output, target_score=options.target_score,
                      target_class=options.target_class, max_change=options.max_change,
                      learning_rate=options.learning_rate)


if __name__ == '__main__':
    main()
