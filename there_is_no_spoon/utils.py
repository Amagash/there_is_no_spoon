import argparse


def get_options(args):
    parser = argparse.ArgumentParser(description="Parses command.")
    parser.add_argument("-i", "--input", help="Your input file.", required=True)
    parser.add_argument("-o", "--output", help="Your destination output file.", default='/data/adversarial_image.png')
    parser.add_argument("-m", "--mode", help="In which mode you would like to run there_is_no_spoon",
                        choices=["predict", "generate"], default="generate")
    parser.add_argument("-tc", "--target_class", type=int, default=910,
                        help="The class number corresponding to the new object you would like to change your image to"
                             "(default is 910 for wooden spoon). The list of classes is available here"
                             ": https://storage.googleapis.com/download.tensorflow.org/data/imagenet_class_index.json")
    parser.add_argument("-ts", "--target_score", type=float, default=0.98,
                        help="The minimum score (should be between 0 and 1) you would like to reach for the new "
                             "classification (default is 0.98)")
    parser.add_argument("-lr", "--learning_rate", type=float, default=0.5,
                        help="The learning rate corresponds to how much to update the adversarial image in each "
                             "iteration (default is 0.5)")
    parser.add_argument("-mc", "--max_change", type=float, default=0.1,
                        help="The maximum change each pixel can support (default is 0.1)"
                             "Larger number produces an image faster but risks more distortion")

    options = parser.parse_args(args)
    return options
