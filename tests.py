import unittest
import animal_printer
from bs4 import BeautifulSoup



class TestStringMethods(unittest.TestCase):

    def test_download_pic(self):
        self.assertTrue(animal_printer.download_pic("/wiki/Camel",
                                                    "C:/Users/Avi "
                                                    "Fenesh/desktop/python"
                                                    "/TheAnimalPrinter/tmp"
                                                    "/Camel.png"))
        self.assertFalse(animal_printer.download_pic("/wiki/Bird",
                                                     "C:/Users/Avi "
                                                     "Fenesh/desktop/python"
                                                     "/TheAnimalPrinter/tmp"
                                                     "/Bird.png"))

    def test_find_table(self):
        with open("moc.html", "r") as file:
            soup = BeautifulSoup(file, 'html.parser')
            with self.assertRaises(Exception):
                animal_printer.find_table(soup)

    def test_output_animals_and_pic(self):
        with self.assertRaises(Exception):
            animal_printer.output_animals_and_pic(None)

    def test_printer(self):
        with self.assertRaises(Exception):
            animal_printer.printer("https://en.wikipedia.org"
                                   "/wiki/Talk"
                                   ":List_of_animal_names")


if __name__ == '__main__':
    unittest.main()
