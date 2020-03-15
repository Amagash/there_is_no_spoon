import argparse


def get_options(args):
    parser = argparse.ArgumentParser(description="Parses command.")
    parser.add_argument("-i", "--input", help="Your input file.", required=True)
    parser.add_argument("-o", "--output", help="Your destination output file.", required=True)
    parser.add_argument("-s", "--target_score", type=float, default=0.98,
                        help="The minimum score (should be between 0 and 1) you would like to reach for the new "
                             "classification (default is 0.98)")
    parser.add_argument("-c", "--target_class", default=910,
                        help="The class number corresponding to the new object you would like to change your image to"
                             "(default is 910 for wooden spoon). The list of classes is available here"
                             ": https://gist.github.com/ageitgey/4e1342c10a71981d0b491e1b8227328b")
    parser.add_argument("-m", "--max_change", type=float, default=0.1,
                        help="The maximum change each pixel can support (default is 0.1)"
                             "Larger number produces an image faster but risks more distortion")
    parser.add_argument("-l", "--learning_rate", type=float, default=0.5,
                        help="The learning rate corresponds to how much to update the adversarial image in each "
                             "iteration (default is 0.5)")
    options = parser.parse_args(args)
    return options
