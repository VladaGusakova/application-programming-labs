from image_iterator import ImageIterator
from annotation import create_annotation
from download import images_download
import argparse


def create_parse () -> argparse.Namespace:
    '''
    Reads args from the terminal
    :return args: args for terminal
    '''
    parser = argparse.ArgumentParser()
    parser.add_argument('keyword', type = str, help = 'Keyword to search', default = 'hedgehog')
    parser.add_argument('num_images', type = int, help = 'Number of images you want to download', default = 50)
    parser.add_argument('images_path', type = str, help = 'Path to images folder', default = './images')
    parser.add_argument('annotation_path', type=str, help='Path to annotation folder', default = 'annotation.csv')
    args = parser.parse_args()
    return args


def main() -> None:
    args = create_parse()
    images_download(args.images_path, args.keyword, args.num_images)
    create_annotation(args.images_path, args.annotation_path)
    image_iterator = ImageIterator(args.annotation_path)
    for i in image_iterator:
        print(i)


if __name__ == '__main__':
    main()