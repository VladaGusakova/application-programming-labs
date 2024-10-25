import csv


class ImageIterator:
    def __init__(self, annotation_path: str) -> None:
        '''
        Constructor. Create class attributes
        :param annotation_path: Path to folder where annotation will be
        '''
        self.annotation_path = annotation_path
        self.paths = self.load_annotation()
        self.limit = len(self.paths)
        self.counter = 0

    def __iter__(self) -> 'ImageIterator':
        return self

    def __next__(self) -> str:
        '''
        Move to next element
        :return: str
        '''
        if self.counter < self.limit:
            next_self = self.paths[self.counter]
            self.counter += 1
            return next_self
        else:
            raise StopIteration

    def load_annotation(self) -> list:
        '''
        Reads the first column from a csv file
        :return: list of realative paths
        '''
        with open(self.annotation_path, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader)
            path_list = list(row[0] for row in reader)
            return path_list