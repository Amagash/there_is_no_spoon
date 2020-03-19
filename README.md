
There is no spoon 
===========
There is no spoon is an application to generate adversarial images.

## Quick Start
To use the app:
- *pre-requisite*: You need to have docker installed. You can find the documentation 
here https://docs.docker.com/install/
- put the image you want to change in your current directory
- run the following command and change MY_IMAGE.PNG with the name of your image
```
 sudo docker run -v $(pwd):/data amagash/there_is_no_spoon --input /data/MY_IMAGE.PNG
```
- the output image will be saved in your current directory under the name "adversarial_image.png"

## Advanced features
Several arguments can be passed to the docker to customize your adversarial image generation.

### Synopsis

     sudo docker run -v $(pwd):/data amagash/there_is_no_spoon --input /data/MY_IMAGE.PNG
     [--output=OUTPUT_PATH][--mode=MODE][--target_class=TARGET_CLASS][--target_score=TARGET_SCORE]
     [--learning_rate=LEARNING_RATE][--max_change=MAX_CHANGE]

### Flags
`--input=INPUT_PATH`\
This sets your file input path. By default it's the current directory.

`--output=OUTPUT_PATH`\
This sets your file destination output. By default it is the current directory.

`--mode=MODE`\
You can run the code in 2 modes: "predict" or generate.
- The "predict" mode only takes an image as an input and prints the classification of this image.
- The "generate" mode let's you generate an adversarial image from an input image of your choice.
By default, the mode="generate"

`--target_class=TARGET_CLASS`\
The class index corresponding to the new object you would like to change your image to. For instance
you have a picture of a cat and you want to generate and adversarial image of the cat image 
that will be classified as being a spoon. 
You need to find the corresponding index for the
spoon classification, which you can find here: 
https://storage.googleapis.com/download.tensorflow.org/data/imagenet_class_index.json

By default, the target_class=910, corresponding to the 
classification of a wooden spoon.

`--target_score=TARGET_SCORE`\
The target score is the minimum score (should be between 0 and 1) you would like to reach for 
the new classification. For instance you have a picture of a cat and you
want to generate and adversarial image of the cat image that will be classified as being a spoon
with a confidence of at least your target_score. By default, the target_score = 0.98 to reach
at least 98% confidence for the new classification.

`--learning_rate=LEARNING_RATE`\
The learning rate corresponds to how much to update the adversarial image in each iteration. 
By default learning_rate=0.5.

`--max_change=MAX_CHANGE`\
The maximum change each pixel can support. By default, max_change=0.1.
Larger number produces an image faster but risks more distortion.

