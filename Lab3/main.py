import cv2
import numpy
import matplotlib.pyplot as plt
import argparse


def load_image(image_path: str) -> numpy.ndarray:
    '''
    Reads the image
    :param image_path: path to image
    :return:
    '''
    image = cv2.imread(image_path)
    if image is None:
        raise FileNotFoundError(f"Image {image_path} not found.")
    return image


def print_image_parameters(image) -> None:
    '''
    Displays the size and number of channels of an image
    :param image: our image
    :return: None
    '''
    height, width, channels = image.shape
    print(f"Image size: {width}x{height}, number of channels: {channels}")


def plot_histogram(image) -> None:
    '''
    Histogram of image brightness
    :param image: our image
    :return: None
    '''
    grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    plt.figure(figsize=(12, 6))
    plt.hist(grayscale.ravel(), bins=256, color='black')
    plt.title("Image brightness histogram")
    plt.xlabel("Brightness")
    plt.ylabel("Frequency")

    plt.show()


def convert_and_display_images(original, result_path) -> None:
    '''
    Converts image to grayscale, displays both original and grayscale images,
    and saves the grayscale image to the specified path
    :param original: original image
    :param result_path: path to save the grayscale image
    :return: None
    '''
    grayscale = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)

    # BGR to RGB
    original_rgb = cv2.cvtColor(original, cv2.COLOR_BGR2RGB)
    grayscale_rgb = cv2.cvtColor(grayscale, cv2.COLOR_GRAY2RGB)

    plt.figure(figsize=(12, 6))
    plt.subplot(1, 2, 1)
    plt.imshow(original_rgb)
    plt.title("Original Image")
    plt.axis('off')

    plt.subplot(1, 2, 2)
    plt.imshow(grayscale_rgb)
    plt.title("Grayscale Image")
    plt.axis('off')

    plt.tight_layout()
    plt.show()
    cv2.imwrite(result_path, grayscale)


def main() -> None:
    '''
    Use all functions
    :return: None
    '''
    args = create_parse()
    image = load_image(args.images_path)
    print_image_parameters(image)
    plot_histogram(image)
    convert_and_display_images(image, args.new_images_path)


def create_parse () -> argparse.Namespace:
    '''
    Reads args from the terminal
    :return args: args for terminal
    '''
    parser = argparse.ArgumentParser()
    parser.add_argument("images_path", type=str, help="Path to image")
    parser.add_argument("new_images_path", type=str, help="Path to save image")
    args = parser.parse_args()
    return args


if __name__ == "__main__":
    main()