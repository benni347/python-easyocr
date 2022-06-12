#!/usr/bin/env python
"""
This is my program to identify letters of the game: "Scrabble".
Later on I will use this to write an application to give myself help what word to play.
:Author: benni347@github.com
:Tutorial (not mine): https://www.youtube.com/watch?v=ZVKaWPW9oQY
"""
import easyocr
import cv2
from matplotlib import pyplot as plt


class Main:
    """
    This is the main class for ocr
    """

    def __init__(self):
        self.image_path = None
        self.reader = None
        self.result = None

    def get_path(self):
        return self.image_path

    def set_path(self, path):
        self.image_path = path

    def get_reader(self):
        return self.reader

    def set_reader(self, reader):
        self.reader = reader

    def get_result(self):
        return self.result

    def set_result(self, result):
        self.result = result

    def setup(self, file_name: str):
        """
        This function sets up the reader and the path to the image.
        :param file_name: the name of the image + the file_name extension
        """
        self.set_path(str("img/" + file_name))
        self.set_reader(easyocr.Reader(["en"], gpu=False))

    def run(self, file_name: str):
        """
        This function runs the program.
        :TODO: fix the bug that easyocr detects exclamation marks as letters.
        :param file_name: the name of the image + the file_name extension used in the setup function
        :return: the result of the ocr
        """
        self.setup(file_name)
        result = self.get_reader().readtext(self.get_path())
        self.set_result(result)
        self.draw_image()
        return self.get_result()

    def def_image_vars(self):
        """
        This function defines the variables for the image.
        :return: the variables for the image
        """
        top_left = tuple(self.get_result()[0][0][0])
        bottom_right = tuple(self.get_result()[0][0][2])
        text = self.get_result()[0][1]
        font = cv2.FONT_HERSHEY_SIMPLEX
        return top_left, bottom_right, text, font

    def draw_image(self):
        """
        This function draws the image.
        """
        img = cv2.imread(self.get_path())
        for detection in self.get_result():
            top_left = tuple([int(val) for val in detection[0][0]])
            bottom_right = tuple([int(val) for val in detection[0][2]])
            text = detection[1]
            font = cv2.FONT_HERSHEY_SIMPLEX
            img = cv2.rectangle(img, top_left, bottom_right, (0, 0, 255), 5)
            img = cv2.putText(img, text, top_left, font, 5, (255, 0, 0), cv2.LINE_AA)
        plt.figure(figsize=(10, 10))
        plt.imshow(img)
        plt.show()


if __name__ == "__main__":
    main = Main()
    print(main.run("hello.jpg"))
