import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QFileDialog
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from image_iterator import ImageIterator


class MainWindow(QWidget):
    def __init__(self):
        '''
        Create main window
        :return: None
        '''
        super().__init__()

        self.setWindowTitle("Viewing Images")
        self.setGeometry(500, 200, 900, 700)

        self.layout = QVBoxLayout()

        self.select_annotation_button = QPushButton("Select annotation", self)
        self.select_annotation_button.clicked.connect(self.select_annotation)

        self.image_label = QLabel(self)
        self.image_label.setAlignment(Qt.AlignCenter)

        self.next_button = QPushButton("Next image", self)
        self.next_button.clicked.connect(self.show_next_image)
        self.next_button.setEnabled(False)

        self.layout.addWidget(self.select_annotation_button)
        self.layout.addWidget(self.image_label)
        self.layout.addWidget(self.next_button)

        self.setLayout(self.layout)

        self.image_iterator = None

    def select_annotation(self) -> None:
        '''
        Create a window for selecting an annotation file
        :return: None
        '''
        self.image_label.setText("Images")
        annotation_path, _ = QFileDialog.getOpenFileName(self, "Select annotation file", "", "CSV Files (*.csv)")
        if annotation_path:
            self.image_iterator = ImageIterator(annotation_path)
            self.next_button.setEnabled(True)
            self.next_button.click()

    def show_next_image(self) -> None:
        '''
        Finding the path to the image and creating a QPixmap to work with the image
        :return: None
        '''
        if self.image_iterator:
            try:
                image_path = next(self.image_iterator)

                if os.path.exists(image_path):
                    pixmap = QPixmap(image_path)
                    pixmap = pixmap.scaled(800, 600, Qt.KeepAspectRatio)
                    self.image_label.setPixmap(pixmap)
                else:
                    self.image_label.setText("Image not found")

            except StopIteration:
                self.image_label.setText("Images are over")
                self.next_button.setEnabled(False)

def main() -> None:
    '''
    Use all function
    :return: None
    '''
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()