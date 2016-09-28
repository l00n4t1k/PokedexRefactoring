import requests
from bs4 import BeautifulSoup


class Scraper(object):

    __max = 0
    __min = 0
    __nat_dex = []
    __local_dex = []
    __generation = 0

    def __init__(self, the_formatter):
        self.__my_formatter = the_formatter

    def gen_decider(self):
        pass

    def set_nat_dex(self, the_dex):
        pass

    def get_nat_dex(self):
        pass

    def set_generation(self, the_gen):
        pass

    def get_generation(self):
        pass

    def get_min(self):
        pass

    def get_max(self):
        pass

    def web_scraper(self):
        pass

    def print(self, the_gen, the_list):
        pass
