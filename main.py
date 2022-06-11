#!/usr/bin/env python
"""
This is my program to identify letters of the game: "Scrabble".
Later on I will use this to write an application to give myself help what word to play.
:Author: benni347@github.com
:Tutorial (not mine): https://www.youtube.com/watch?v=ZVKaWPW9oQY
"""
import easyocr
# import cv2
from matplotlib import pyplot as plt


class Main:
    """
    This is the main class for ocr
    """
    def __init__(self):
        self.image_path = None
        self.reader = None

    def get_path(self):
        return self.image_path

    def set_path(self, path):
        self.image_path = path

    def get_reader(self):
        return self.reader

    def set_reader(self, reader):
        self.reader = reader

    def setup(self):
        self.set_path("img/hello.jpg")
        self.set_reader(easyocr.Reader(["en"], gpu=True))

    def run(self):
        self.setup()
        result = self.get_reader().readtext(self.get_path())
        return result




if __name__ == "__main__":
    main = Main()
    print(main.run())

