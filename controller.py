import sys
import re


class Controller(object):

    my_scraper = None
    my_IO = None
    my_cmd = None
    full_dex = []
    local_dex = []
    response = ''
    defaultpath = "F:\CourseMaterial(DO-NOT-DELETE)\Year4\PR301\PythonShit" \
                  "\pokedex\Pokedex"
    defaultName = "test01.txt"

    def __init__(self, the_scraper, the_io):
        self.my_scraper = the_scraper
        self.my_IO = the_io

    def get_scraper(self):
        return self.my_scraper

    def get_io(self):
        return self.my_IO

    def set_full_dex(self, the_dex):
        self.full_dex = the_dex

    def get_full_dex(self):
        return self.full_dex

    def set_local_dex(self, the_dex):
        self.local_dex = the_dex

    def get_local_dex(self):
        return self.local_dex

    def ui_start(self):
        if len(sys.argv) > 1:
            # print(sys.argv)
            for i in sys.argv:
                if re.search('-g', i):
                    gen = self.my_IO.get_user_in("Enter the generation you "
                                                 "want to see")
                    if gen.isdigit():
                        self.start(gen, self.defaultpath, self.defaultName)
        else:
            pass

    def start(self, the_gen, filepath, filename):
        f = self.my_scraper.get_formatter()
        x = self.my_IO
        try:
            self.my_scraper.set_nat_dex(x.load(filepath, filename))
        except FileNotFoundError:
            self.response = self.my_IO.get_user_in(
                "File not found. Would you like to perform a fresh scrape "
                "'Y or N'")
            self.example(0)
        except EOFError:
            self.response = self.my_IO.get_user_in(
                "Error reading file. Would you like to perform a fresh scrape "
                "'Y or N'")
            self.example(0)
        self.full_dex = self.my_scraper.get_nat_dex()
        x.pickler(self.full_dex, filepath, filename)

        self.my_scraper.find_local_dex(the_gen)
        the_dex = self.my_scraper.get_local_dex()
        self.my_IO.printer(int(the_gen), f.readability_formatter(the_dex))

    def check_user_in(self, prompt):
        if str(prompt).capitalize() == 'Y':
            self.example(0)
        elif str(prompt).capitalize() == 'N':
            self.my_cmd.do_load()

    def example(self, the_gen):
        self.my_scraper.set_generation(the_gen)
        self.my_scraper.web_scraper()
