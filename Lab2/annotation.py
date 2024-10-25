import os
import csv


def create_annotation(images_path: str, annotation_path: str) -> None:
    '''
    Creates (if necessary) a csv file and writes rows with image path data
    :param images_path:
    :param annotation_path:
    :return: None
    '''
    with open(annotation_path, 'w', newline = '', encoding = 'utf-8') as annotation:
        writer = csv.writer(annotation)
        writer.writerow(["relative path","absolute path"])
        for file in os.listdir(images_path):
            real_path = os.path.relpath(os.path.join(images_path, file), start='./')
            abs_path = os.path.abspath(os.path.join(images_path, file))
            writer.writerow([real_path, abs_path])