import os
from icrawler.builtin import GoogleImageCrawler


def images_download(images_path: str, keyword: str, num_images: int) -> None:
    '''
    Downloads images according to the selected parameters
    :param images_path: Path to image folder
    :param keyword: Word by which we search for image
    :param num_images: Number of images
    :return None:
    '''
    if not os.path.isdir(images_path):
        os.makedirs(images_path)
    g_crawler = GoogleImageCrawler(storage = {'root_dir': images_path})
    g_crawler.crawl(keyword = keyword, max_num = num_images)