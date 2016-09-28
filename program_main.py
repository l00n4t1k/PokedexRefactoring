from controller import Controller
from pokemon_scraper import PokemonScraper
from formatter import Formatter
from IO import IO
from command import Command


class Main(object):

    def __init__(self):
        self.my_controller = None
        self.my_scraper = None
        self.my_cmd = None

    def go(self):
        self.my_scraper = PokemonScraper(Formatter)
        self.my_controller = Controller(self.my_scraper, IO)
        self.my_cmd = Command(self.my_controller)
        self.my_controller.ui_start()
        self.my_cmd.cmdloop()

    def go_test(self):
        self.my_scraper = PokemonScraper(Formatter)
        self.my_controller = Controller(self.my_scraper, IO)
        self.my_cmd = Command(self.my_controller)


if __name__ == "__main__":
    m = Main()
    m.go()
